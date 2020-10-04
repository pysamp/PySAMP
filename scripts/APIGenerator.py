import re
import os
import traceback 
import glob
import json


class NoMethodException(Exception):
    pass

#todo: delete chars

PARAMETER_REGEX = '(\[out\] )?([A-z]+) ([A-z]+)'
METHODEXTRACTOR = re.compile('^(\[native\]) ([A-z]+) ([A-z]+)\((.*)\)\;$')
PARAMETERSEXTRACTOR = re.compile(r'([ ]*(?P<out>\[out\])?[ ]*?(?P<type>[a-zA-Z]+) (?P<name>[a-zA-Z0-9_]+)[ ]*(?:=[ ]*(?P<default>[a-zA-Z0-9\"\'\.\-\_]*))?)')
PARAMETEREXTRACTOR = re.compile('^{0}$'.format(PARAMETER_REGEX))
OUTPUT_PYTHONFILE = '../gamemodes/empty/samp.py'
INPUT_DIRECTORY = '/Users/yannickhabecker/git/private/sampgdk/lib/sampgdk/*.idl'

CONST_NAME_REGEX = re.compile(r'^[A-Z][A-Z0-9_x]*$')

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
        self.name = result.group('name')
        self.isOut = result.group('out') == '[out]'
        self.default = result.group('default')

        if self.default == 'false':
            self.default = 'False'
        elif self.default == 'true':
            self.default = 'True'

    def toDeclaration(self, nextParamName):
        st = ('const ' if constTypes[self.type] and not(self.isOut) else '')+cppTypes[self.type]+' '+self.name
        if self.default != None:
            st += ' = ' + self.default;  
        elif self.type == 'string' and self.isOut:
            st += ' = new char['+ nextParamName + ']' #da next Param die Laenge enthaelt
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
            raise NoMethodException()
        self.native = result.group(1) == '[native]'
        self.returns = result.group(2)
        self.name = result.group(3)
        self.initParams(result.group(4))
        self.line = line
        
    
    def initParams(self, string):
        for res in PARAMETERSEXTRACTOR.finditer(string):
            self.params.append(Parameter(res, len(self.params)))


    def toAPIMethod(self):
        _params = filter(lambda p: not p.isOut, self.params)
        _out = filter(lambda p: p.isOut, self.params)

        
        method_params = [p.name if not p.default else (p.name + ' = Const(\'%s\')' % p.default if CONST_NAME_REGEX.match(p.default) else p.name + ' = %s' % p.default) for p in _params]
        call_params = ['encode(%s)' % p.name if p.type == 'string' else p.name for p in _params]
        
        _method = 'def %s(%s):\n' % (self.name, ', '.join(method_params))
        
        if len(_out) == 1:
            _out = _out[0]
            if _out.type == 'string':
                _method += '    return decode(pysamp.%s(%s))\n' % (self.name, ', '.join(call_params))
            else:
                _method += '    return pysamp.%s(%s)\n' % (self.name, ', '.join(call_params))
        elif len(_out) > 1:
            _method += '    (%s) = pysamp.%s(%s)\n' % (', '.join([o.name for o in _out]), self.name, ', '.join(call_params))
            _method += '    return (%s)\n' % ', '.join(['decode(%s)' % o.name if o.type == 'string' else o.name for o in _out])
        else:
            _method += '    return pysamp.%s(%s)\n' % (self.name, ', '.join(call_params))
            
        return _method + '\n'

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

methods = []

for path in glob.glob(INPUT_DIRECTORY):
    with open(path, 'r') as f:
        for line in f:
            try:
                m = Method(line)
                methods.append(m)
            except Exception as e:
                if e.__class__ != NoMethodException:
                    traceback.print_exc()

header = [
    'import pysamp\n',
    '\n',
    'def encode(value):\n',
    '    if type(value) != \'bytes\':\n',
    '        return value.encode(\'iso-8859-1\')\n',
    '    return value\n',
    '\n',
    'def decode(value):\n',
    '    if value is None:\n',
    '        return None\n',
    '    if type(value) == str:\n',
    '        return value\n',
    '    return value.decode(\'iso-8859-1\')\n',
    '\n',
    'def Const(name):\n',
    '    return pysamp.Const(name)\n',
    '\n'
]

with open(OUTPUT_PYTHONFILE, 'w') as f:
    f.writelines(header)
    f.writelines([m.toAPIMethod() for m in methods])

# try:
#     os.remove('functions.h')
# except OSError:
#     pass

# with open("functions/functions.txt") as f:
#     with open("functions.h", 'a+') as g:
#         methods = []
#         for line in f:
#             try:
#                 m = Method(line)
#                 methods.append(m)
#             except Exception as e:
#                 traceback.print_exc()
#         output = '#ifndef samp_h\n#define samp_h\n#include <Python.h>\n#include "sampgdk.h"\n#include "const.h"\n\n'
#         for method in methods:
#             output += method.toCpp()

#         output += 'static PyMethodDef PySAMPMethods[] = {\n'
#         for method in methods:           
#             output += '    { "' + method.name + '", pysamp_'+method.name.lower()+', METH_VARARGS, NULL },\n'
#         output += '    { "Const", pysamp_const, METH_VARARGS, NULL },\n'
#         output += '    { NULL, NULL, 0, NULL }\n};\n\n'
#         output += 'static PyModuleDef PySAMPModule = {\n'
#         output += '    PyModuleDef_HEAD_INIT, "pysamp", "SAMP functions", -1, PySAMPMethods,\n'
#         output += '    NULL, NULL, NULL, NULL\n'
#         output += '};\n\n'
#         output += 'static PyObject* PyInit_samp()\n{\n    return PyModule_Create(&PySAMPModule);\n}\n'
#         output += '#endif // !samp_h'



#         g.write(output)