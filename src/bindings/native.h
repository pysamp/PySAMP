#ifndef py_native_h
#define py_native_h

#include <Python.h>
#include "sampgdk.h"
#include "callbacks.h"

struct PY_NATIVE_INFO {
	AMX_NATIVE amx_native;
	const char* name;
	const char* parameters;
	char return_type;
};

static std::map<const char*, PY_NATIVE_INFO> natives;


static bool findNative(const char* name, const char* param_format, const char* return_type)
{
	if (natives.count(name) > 0)
		return true;

	AMX_NATIVE native = sampgdk::FindNative(name);

	if (native == nullptr)
		return false;

	natives[name] = {
		native,
		name,
		param_format,
		return_type[0]
	};
	return true;
}

static PyObject* PyNative_findNative(PyObject* self, PyObject* args) {
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

static PyObject* PyNative_registerCallback(PyObject* self, PyObject* args) {
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


static void* parseArgument(PyObject* value, char out_argument_type)
{
	void* out_argument_value = nullptr;
	long vali;
	bool valb;
	double valf;
	char* vals;
	switch (out_argument_type)
	{
	case 'i':
	case 'd':
		vali = PyLong_AsLong(value);
		sampgdk::logprintf("d=%d", vali);
		out_argument_value = &vali;
		break;
	case 'b':
		valb = PyBool_Check(value);
		out_argument_value = &valb;
		break;
	case 'f':
		valf = PyFloat_AsDouble(value);
		sampgdk::logprintf("f=%.2f", valf);
		out_argument_value = &valf;
		break;
	case 's':
		vals = PyBytes_AsString(value);
		out_argument_value = vals;
		break;
	}
	return out_argument_value;
}

static void parseArguments(PyObject* call_arguments, const char* out_argument_format, void** out_argument_array)
{
	int number_of_arguments = PyTuple_Size(call_arguments);
	for (int i = 0; i < number_of_arguments; i++)
	{
		char type = out_argument_format[i];
		out_argument_array[i] = parseArgument(PyTuple_GetItem(call_arguments, i), out_argument_format[i]);
	}
}

static PyObject* PyNative_invokeNative(PyObject* self, PyObject* args)
{
	// TODO: raise err if not found or args not enough, check if strlen and call_arguments match (not null if >0)
	const char* name;
	PyObject* call_arguments;
	sampgdk::logprintf("[DEBUG-1]PyNative_invokeNative");
	if (!PyArg_ParseTuple(args, "yO!", &name, &PyTuple_Type, &call_arguments))
	{
		PyErr_Print();
		return NULL;
	}
	sampgdk::logprintf("[DEBUG-2]PyNative_invokeNative, name=%s, tuple_size=%d", name, PyTuple_Size(call_arguments));
	PY_NATIVE_INFO &info = natives[name];
	sampgdk::logprintf("[DEBUG-3]PyNative_invokeNative");
	sampgdk::logprintf("name=%s, param_format=%s, return_type=%c", name, info.parameters, info.return_type);
	int param_len = strlen(info.parameters);
	if (param_len > 0)
	{
		sampgdk::logprintf("[DEBUG-4]PyNative_invokeNative");
		void** out_argument_array = new void* [param_len];
		//sampgdk::InvokeNativeArray()
		parseArguments(call_arguments, info.parameters, out_argument_array);
		sampgdk::InvokeNativeArray(info.amx_native, info.parameters, out_argument_array);
		//TODO interpret return value(s)
		sampgdk::logprintf("[DEBUG-6]PyNative_invokeNative");
		delete[] out_argument_array;
	} else {
		sampgdk::InvokeNative(info.amx_native, "");
	}
	sampgdk::logprintf("[DEBUG-7]PyNative_invokeNative");
	return Py_None;
}

static PyMethodDef PyNative_methods[] = {
   { "find_native", PyNative_findNative, METH_VARARGS, NULL },
   { "invoke_native", PyNative_invokeNative, METH_VARARGS, NULL },
   {"register_callback", PyNative_registerCallback, METH_VARARGS, NULL},
   { NULL, NULL, 0, NULL }
};

static PyModuleDef PyNative_module = {
	PyModuleDef_HEAD_INIT, "pynative", "AMX natives interface", -1, PyNative_methods,
	NULL, NULL, NULL, NULL
};

static PyObject* PyNative_createModule()
{
	return PyModule_Create(&PyNative_module);
};

#endif
