#ifndef PARAMCONVERTER_H
#define PARAMCONVERTER_H

#include <string>

#include "sampgdk.h"
#include "amx/amx.h"

#include "limited_api_python.h"  // IWYU pragma: keep


namespace ParamConverter
{
	std::string get_format(PyObject *tuple);
	void amx_pop_params(cell *params, PyObject *tuple);
	cell* from_tuple(PyObject *tuple);
	PyObject* to_tuple(cell *params, const std::string format, AMX *amx);
};

#endif
