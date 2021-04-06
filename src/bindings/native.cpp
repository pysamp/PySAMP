#include "native.h"


static Logger logger = Logger("native");

std::map<const char*, PY_NATIVE_INFO> natives;

bool findNative(const char* name, const char* param_format, const char* return_type)
{
	if (natives.count(name) > 0)
		return true;

	AMX_NATIVE native = sampgdk::FindNative(name);

	if (native == nullptr)
		return false;

	char char_return_type = 'n';

	if (strlen(return_type) > 0)
		char_return_type = return_type[0];

	char* sampgdk_param_format = new char[strlen(param_format)];
	int number_of_arguments = strlen(param_format);

	for (int i = 0; i < number_of_arguments; i++)
	{
		char type = param_format[i];
		switch (type)
		{
		case 'i':
		case 'd':
		case 'b':
		case 'f':
		case 's':
			sampgdk_param_format[i] = type;
			break;
		case 'I':
			sampgdk_param_format[i] = 'i';
			break;
		case 'D':
			sampgdk_param_format[i] = 'd';
			break;
		case 'B':
			sampgdk_param_format[i] = 'b';
			break;
		case 'F':
			sampgdk_param_format[i] = 'f';
			break;
		case 'S':
		case 'A':
		default:
			//TODO arrays and variadic functions
			logger.error("Unsupported native argument type %s", type);
			break;
		}
	}

	natives[name] = {
		native,
		name,
		param_format,
		sampgdk_param_format,
		char_return_type
	};
	return true;
}

PyObject* PyNative_findNative(PyObject* self, PyObject* args) {
	const char* name;
	const char* param_format;
	const char* return_type;

	if (!PyArg_ParseTuple(args, "yyy:find_native", &name, &param_format, &return_type))
	{
		PyErr_Print();
		return NULL;
	}

	if (findNative(name, param_format, return_type))
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
	sampgdk::logprintf("Number of callbacks=%d", callback_format.size());
	sampgdk::logprintf("Register new callback: name=%s, params=%s", name, param_format);
	std::string name_str = name;
	std::string param_format_str = param_format;

	callback_format[name_str] = param_format_str;
	if (callback_format.count(name) == 0)
	{
		sampgdk::logprintf("Could not register callback: name=%s, params=%s", name, param_format);
	}
	else {
		sampgdk::logprintf("New callback registered: name=%s", name);
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
		out_argument_value = new long[1];
		vali = PyLong_AsLong(value);
		*((long*)out_argument_value) = vali;
		break;
	case 'I':
	case 'D':
		out_argument_value = new long[1];
	case 'b':
		out_argument_value = new bool[1];
		valb = PyBool_Check(value);
		*((bool*)out_argument_value) = valb;
		break;
	case 'B':
		out_argument_value = new bool[1];
		break;
	case 'f':
		out_argument_value = new float[1];
		valf = (float) PyFloat_AsDouble(value);
		*((float*)out_argument_value) = valf;
		break;
	case 'F':
		out_argument_value = new float[1];
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
	for (int i = 0; i < number_of_arguments; i++)
	{
		char type = out_argument_format[i];
		if (type == 'i' || type == 'd')
			logger.trace("arg%d=%d", i, *((long*)out_argument_array[i]));
	}
}

PyObject* parseCellValue(PY_NATIVE_INFO& info, void** arguments, cell value)
{
	// TODO: extract "return" values from argument references
	switch (info.return_type)
	{
	case 'i':
	case 'd':
		return PyLong_FromLong(value);
		break;
	case 'b':
		return PyBool_FromLong(value);
		break;
	case 'n':
		// void
		break;
	case 'f':
		return PyFloat_FromDouble((float)amx_ctof(value));
	default:
		logger.warn("return type %s for function %s is unsupported. Returning none", info.return_type, info.name);
		break;
	}
	return Py_None;
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
		return NULL;
	}
	PY_NATIVE_INFO& info = natives[name];
	int param_len = strlen(info.parameters);
	if (param_len > 0)
	{
		void** out_argument_array = new void* [param_len];
		
		parseArguments(call_arguments, info.parameters, out_argument_array);
		cell retval = sampgdk::InvokeNativeArray(info.amx_native, info.sampgdk_param_format, out_argument_array);
		//TODO interpret reference values
		returnValue = parseCellValue(info, out_argument_array, retval);
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