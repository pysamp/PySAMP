#include "native.h"


static Logger logger = Logger("native");

std::map<const char*, PY_NATIVE_INFO> natives;

bool findNative(const char* name, const char* param_format, const char* return_type, int number_of_arguments, int number_of_reference_arguments)
{
	if (natives.count(name) > 0)
		return true;

	char* parameters = (char*)malloc(strlen(param_format) + 1);
	strcpy(parameters, param_format);

	AMX_NATIVE native = sampgdk::FindNative(name);

	if (native == nullptr)
		return false;

	char char_return_type = 'n';

	if (strlen(return_type) > 0)
		char_return_type = return_type[0];

	logger.trace("return_type is %s, extracted char is %c", return_type, char_return_type);

	char* sampgdk_param_format = new char[number_of_arguments + 1]{};

	// todo: to support arrays another mechanism for iterating is needed as not all argument descriptors consist of only one char
	for (int i = 0; i < number_of_arguments; i++)
	{
		char type = parameters[i];
		switch (type)
		{
		case 'i':
			sampgdk_param_format[i] = 'i';
			break;
		case 'd':
			sampgdk_param_format[i] = 'd';
			break;
		case 'b':
			sampgdk_param_format[i] = 'b';
			break;
		case 'f':
			sampgdk_param_format[i] = 'f';
			break;
		case 's':
			sampgdk_param_format[i] = 's';
			break;
		case 'I':
		case 'D':
		case 'B':
		case 'F':
			sampgdk_param_format[i] = 'R';
			break;
		case 'S':
		case 'A':
		default:
			//TODO arrays and variadic functions
			logger.error("Unsupported native argument type %s", type);
			return false;
		}
	}

	logger.debug("New native registered %s with arguments %s resp. %s return_type %c", name, parameters, sampgdk_param_format, char_return_type);

	PY_NATIVE_INFO info = {
		native,
		name,
		parameters,
		sampgdk_param_format,
		char_return_type,
		number_of_arguments,
		number_of_reference_arguments
	};

	natives.insert({name, info});
	
	logger.trace("Arguments: %s", natives.at(name).parameters);

	return true;
}

PyObject* PyNative_findNative(PyObject* self, PyObject* args) {
	const char* name;
	const char* param_format;
	const char* return_type;
	int number_of_arguments;
	int number_of_reference_arguments;

	if (!PyArg_ParseTuple(args, "yyyii:find_native", &name, &param_format, &return_type, &number_of_arguments, &number_of_reference_arguments))
	{
		PyErr_Print();
		return NULL;
	}

	if (findNative(name, param_format, return_type, number_of_arguments, number_of_reference_arguments))
		Py_RETURN_TRUE;

	Py_RETURN_FALSE;
}

PyObject* PyNative_registerCallback(PyObject* self, PyObject* args) {
	const char* name;
	const char* param_format;

	if (!PyArg_ParseTuple(args, "yy:register_callback", &name, &param_format))
	{
		PyErr_Print();
		return NULL;
	}
	logger.debug("Number of callbacks=%d", callback_format.size());
	logger.debug("Register new callback: name=%s, params=%s", name, param_format);
	std::string name_str = name;
	std::string param_format_str = param_format;

	callback_format[name_str] = param_format_str;
	if (callback_format.count(name) == 0)
	{
		logger.error("Could not register callback: name=%s, params=%s", name, param_format);
	}
	else {
		logger.debug("New callback registered: name=%s", name);
	}
	Py_RETURN_NONE;
}


void* parseArgument(PyObject* value, char out_argument_type)
{
	void* out_argument_value = nullptr;
	long vali;
	bool valb;
	float valf;
	char* vals;
	switch (out_argument_type)
	{
	case 'i':
	case 'd':
	case 'I':
	case 'D':
		out_argument_value = new long[1];
		vali = PyLong_AsLong(value);
		*((long*)out_argument_value) = vali;
		break;
	case 'b':
	case 'B':
		out_argument_value = new bool[1];
		valb = PyBool_Check(value);
		*((bool*)out_argument_value) = valb;
		break;
	case 'f':
	case 'F':
		out_argument_value = new float[1];
		valf = (float) PyFloat_AsDouble(value);
		*((float*)out_argument_value) = valf;
		break;
	case 's':
		vals = PyBytes_AsString(value);
		out_argument_value = new char[strlen(vals)+1];
		out_argument_value = vals;
		break;
	case 'S':
	case 'A':
		break;
	}
	return out_argument_value;
}

void parseArguments(PyObject* call_arguments, const char* out_argument_format, void** out_argument_array)
{
	int number_of_arguments = PyTuple_Size(call_arguments);
	for (int i = 0; i < number_of_arguments; i++)
	{
		char type = out_argument_format[i];
		out_argument_array[i] = parseArgument(PyTuple_GetItem(call_arguments, i), out_argument_format[i]);
	}
}
PyObject* parseCellValue(const char type, cell value)
{
	PyObject* returnValue = Py_None;
	switch (type)
	{
	case 'i':
	case 'd':
	case 'I':
	case 'D':
		returnValue = PyLong_FromLong(value);
		break;
	case 'b':
	case 'B':
		returnValue = PyBool_FromLong(value);
		break;
	case 'n':
		// void
		break;
	case 'f':
	case 'F':
		returnValue = PyFloat_FromDouble((float)amx_ctof(value));
	default:
		logger.warn("Type %c unsupported. Returning none", type);
		break;
	}
	return returnValue;
}

PyObject* parseReturnValues(PY_NATIVE_INFO& info, void** arguments, cell invocationReturnValue)
{
	// TODO: extract "return" values from argument references
	PyObject* returnValue = parseCellValue(info.return_type, invocationReturnValue);

	if (info.number_of_reference_arguments > 0)
	{
		PyObject* returnTuple = PyTuple_New((returnValue != Py_None) ? info.number_of_reference_arguments + 1 : info.number_of_reference_arguments);
		int tupleIdx = 0;
		if (returnValue != Py_None)
		{
			PyTuple_SetItem(returnTuple, tupleIdx++, returnValue);
		}
		for (int argIdx = 0; argIdx < info.number_of_arguments; argIdx++)
		{
			char type = info.parameters[argIdx];
			if (isupper(type))
			{
				// todo support arrays here too?
				PyTuple_SetItem(returnTuple, tupleIdx++, parseCellValue(type, (cell)&arguments[argIdx]));
			}
		}
		returnValue = returnTuple;
	}

	return returnValue;
}

PyObject* PyNative_invokeNative(PyObject* self, PyObject* args)
{
	// TODO: raise err if not found or args not enough, check if strlen and call_arguments match (not null if >0)
	const char* name;
	PyObject* call_arguments;
	// TODO: make tuple
	PyObject* returnValue = Py_None;
	logger.trace("PyNative_invokeNative");
	if (!PyArg_ParseTuple(args, "yO!", &name, &PyTuple_Type, &call_arguments))
	{
		PyErr_Print();
		return Py_None;
	}

	if (natives.count(name) == 0)
	{
		PyErr_Format(PyExc_RuntimeError, "Could not invoke native: native %s was not registered.", name);
		return Py_None;
	}

	PY_NATIVE_INFO& info = natives.at(name);
	logger.trace("PyNative_invokeNative %s with arguments %s resp. %s return_type %c", info.name, info.parameters, info.sampgdk_param_format, info.return_type);
	int param_len = strlen(info.parameters);
	if (param_len > 0)
	{
		void** out_argument_array = new void* [param_len];
		
		parseArguments(call_arguments, info.parameters, out_argument_array);
		cell retval = sampgdk::InvokeNativeArray(info.amx_native, info.sampgdk_param_format, out_argument_array);
		//TODO interpret reference values
		returnValue = parseReturnValues(info, out_argument_array, retval);
		delete[] out_argument_array;
	}
	else {
		sampgdk::InvokeNative(info.amx_native, "");
	}
	return returnValue;
}

PyMethodDef PyNative_methods[] = {
   { "find_native", PyNative_findNative, METH_VARARGS, NULL },
   { "invoke_native", PyNative_invokeNative, METH_VARARGS, NULL },
   { "register_callback", PyNative_registerCallback, METH_VARARGS, NULL},
   { NULL, NULL, 0, NULL }
};

PyModuleDef PyNative_module = {
	PyModuleDef_HEAD_INIT, "pynative", "AMX natives interface", -1, PyNative_methods,
	NULL, NULL, NULL, NULL
};

PyObject* PyNative_createModule()
{
	return PyModule_Create(&PyNative_module);
};