#ifndef PARAMCONVERTER_H
#define PARAMCONVERTER_H

#include <string>
#include <Python.h>
#include "sampgdk.h"
#include "pysamp.h"


// From sampgdk
extern "C"
{
	int sampgdk_fakeamx_push_cell(cell value, cell *address);
	int sampgdk_fakeamx_push_float(float value, cell *address);
	int sampgdk_fakeamx_push_string(const char *src, int *size, cell *address);
}

class ParamConverter
{
public:
	cell* from_tuple(PyObject* tuple, bool asReference = false);
	PyObject* to_tuple(cell* params, const std::string format, AMX* amx);
};

#endif
