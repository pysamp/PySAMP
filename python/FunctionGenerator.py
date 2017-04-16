import re
import os
import traceback 

#todo: delete chars

PARAMETER_REGEX = '(\[out\] )?([A-z]+) ([A-z]+)'
METHODEXTRACTOR = re.compile('^(\[native\]) ([A-z]+) ([A-z]+)\((.*)\)\;$')
PARAMETERSEXTRACTOR = re.compile('([ ]*(?P<out>\[out\])?[ ]*?(?P<type>[A-z]+) (?P<name>[A-z]+)[ ]*(?:=[ ]*(?P<default>[A-z0-9\"\'\.\-]*))?)')
PARAMETEREXTRACTOR = re.compile('^{0}$'.format(PARAMETER_REGEX))
OUTPUTFILE = 'cpp/vehicles.cpp'

formatTypes = {
    'int':'i',
    'bool':'p',
    'string':'s',
    'float':'f'
}

cppTypes = {
    'int':'int',
    'bool':'bool',
    'string':'char*',
    'float':'float'
}

deleteTypes = {
    'int':False,
    'bool':False,
    'string':True,
    'float':False,
}

constTypes = {
    'int':False,
    'bool':False,
    'string':True,
    'float':False
}

initValues = {
    'int':'-1',
    'bool':'false',
    'string':'""',
    'float':'-1.0f'
}

class Parameter:
    type = None
    name = None
    isOut = None
    default = None

    def __init__(self, result, num):
        self.type = result.group('type')
        self.name = 'arg'+str(num)
        self.isOut = result.group('out') == '[out]'
        self.default = result.group('default')

    def toString(self):
        return '{type:\'%s\'\n name:\'%s\'\n isOut:\'%s\'\n default:\'%s\'}' % (self.type, self.name, self.isOut, self.default)

    def toDeclaration(self, nextParamName):
        st = ('const ' if constTypes[self.type] and not(self.isOut) else '')+cppTypes[self.type]+' '+self.name
        if self.default != None:
            st += ' = ' + self.default;  
        elif self.type == 'string' and self.isOut:
            st += ' = new char['+ nextParamName + ']' #da next Param die Länge enthält
        else:
            st += ' = ' + initValues[self.type]
        return st + ';'

class Method:

    def __init__(self, line):
        
        self.native = 0
        self.returns = ''
        self.name = ''
        self.params = []
        result = METHODEXTRACTOR.match(line)
        if result == None:
            raise Exception('NoMethod')
        self.native = result.group(1) == '[native]'
        self.returns = result.group(2)
        self.name = result.group(3)
        self.initParams(result.group(4))
        with open('json/'+self.name+'.txt', 'a+') as f:
            f.write(self.toString())
        
    
    def initParams(self, string):
        for res in PARAMETERSEXTRACTOR.finditer(string):
            self.params.append(Parameter(res, len(self.params)))


    def toString(self):
        ps = '['
        for param in self.params:
            ps = ps + param.toString()
        ps = ps + ']'
        return '{native:\'%s\'\n returns:\'%s\'\n name:\'%s\'\n parameters:\'%s\'}' % (self.native, self.returns, self.name, ps)

    def toFormatString(self):
        fs = ''
        optional_began = False
        for param in self.params:
            if not(param.isOut):
                if not(optional_began) and param.default != None:
                    optional_began = True
                    fs += '|'
                fs += formatTypes[param.type]
        return fs
    
    def hasOutputParam(self):
        for param in self.params:
            if param.isOut:
                return True
        return False
    
    def getOutputParamFormatString(self):
        ret = ''
        for param in self.params:
            if param.isOut:
                ret += formatTypes[param.type]
        return ret

    def getReturnString(self):
        ret = 'PyObject* out =  '
        if self.hasOutputParam():
            ret += 'Py_BuildValue("'+self.getOutputParamFormatString()+'"'
            for param in self.params:
                if param.isOut:
                    ret += ', ' + param.name 
            ret += ');\n'
            for param in self.params:
                if param.type == 'string':
                    ret += '    delete[] ' + param.name + ';\n'
        else:
            if self.returns == 'bool':
                ret += '(ret)?Py_True:Py_False;\n'
            else:
                ret += 'Py_BuildValue("('+formatTypes[self.returns]+')", ret);\n'
            for param in self.params:
                if param.type == 'string':
                    ret += '    delete[] ' + param.name + ';\n'
        ret += '    return out;'
        return ret
    
    def toCpp(self):
        lines = 'static PyObject* pysamp_'+self.name.lower()+'(PyObject *self, PyObject *args)\n{\n'
        pars = self.params.copy()
        pars.reverse()

        i = len(self.params)
        for param in pars:
            if not(param.isOut and param.type == 'string'):
                lines += '    '+param.toDeclaration('arg'+str(i))+'\n'
            i -= 1
        lines += '    if (!PyArg_ParseTuple(args, "'+self.toFormatString()+':'+self.name+'"'
        for param in self.params:
            if not(param.isOut):
                lines += ', &'
                lines += param.name
        lines += '))\n'
        lines += '    {\n'
        lines += '        PyErr_Print();\n'
        lines += '        return NULL;\n'
        lines += '    }\n'
        
        i = len(self.params)
        for param in pars:
            if (param.isOut and param.type == 'string'):
                lines += '    '+param.toDeclaration('arg'+str(i))+'\n'
            i -= 1

        lines += '    ' + self.returns + ' ret = ' + self.name + '('
        fl = True
        for param in self.params:
            if(fl):
                fl = False
            else:
                lines += ', '
            if param.isOut and not(param.type == 'string'):
                lines += '&'
            lines += param.name
        lines += ');\n'  
        

        lines += '    '+self.getReturnString() + '\n';
        lines += '}\n\n'
        return lines

try:
    os.remove('functions.h')
except OSError:
    pass

with open("functions/functions.txt") as f:
    with open("functions.h", 'a+') as g:
        methods = []
        for line in f:
            try:
                m = Method(line)
                methods.append(m)
            except Exception as e:
                traceback.print_exc()
        output = '#ifndef samp_h\n#define samp_h\n#include <Python.h>\n#include "sampgdk.h"\n#include "const.h"\n\n'
        for method in methods:
            output += method.toCpp()

        output += 'static PyMethodDef PySAMPMethods[] = {\n'
        for method in methods:           
            output += '    { "' + method.name + '", pysamp_'+method.name.lower()+', METH_VARARGS, NULL },\n'
        output += '    { "Const", pysamp_const, METH_VARARGS, NULL },\n'
        output += '    { NULL, NULL, 0, NULL }\n};\n\n'
        output += 'static PyModuleDef PySAMPModule = {\n'
        output += '    PyModuleDef_HEAD_INIT, "pysamp", "SAMP functions", -1, PySAMPMethods,\n'
        output += '    NULL, NULL, NULL, NULL\n'
        output += '};\n\n'
        output += 'static PyObject* PyInit_samp()\n{\n    return PyModule_Create(&PySAMPModule);\n}\n'
        output += '#endif // !samp_h'



        g.write(output)