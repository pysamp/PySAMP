#pragma once

#include <Python.h>
#include "sampgdk.h"
#include "callbacks.h"
#include <map>

struct PY_NATIVE_INFO {
	AMX_NATIVE amx_native;
	const char* name;
	const char* parameters;
	const char* sampgdk_param_format;
	char return_type;
};

extern std::map<const char*, PY_NATIVE_INFO> natives;
extern PyMethodDef PyNative_methods[];
extern PyModuleDef PyNative_module;

bool findNative(const char* name, const char* param_format, const char* return_type);
PyObject* PyNative_findNative(PyObject* self, PyObject* args);
PyObject* PyNative_registerCallback(PyObject* self, PyObject* args);
void* parseArgument(PyObject* value, char out_argument_type);
void parseArguments(PyObject* call_arguments, const char* out_argument_format, void** out_argument_array);
PyObject* parseCellValue(PY_NATIVE_INFO& info, void** arguments, cell value);
PyObject* PyNative_invokeNative(PyObject* self, PyObject* args);
PyObject* PyNative_createModule();