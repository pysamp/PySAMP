#include "param_converter.h"


cell* ParamConverter::from_tuple(PyObject* tuple, bool asReference)
{
	Py_ssize_t len_tuple = PyTuple_Size(tuple);
	int offset = (asReference ? 2 : 1);  // 2 - argc, format
	cell *amx_params = new cell[
		len_tuple
		+ offset
	];
	PyObject *current_argument = NULL;
	std::string _format;

	amx_params[0] = (
		len_tuple
		+ (offset - 1)
	) * sizeof(cell);

	if(asReference)
	{
		// XXX: I know this is all a bit static, but we only ever need it once...
		// I'd rather have this bit of the code be complex than the actual native
		PyObject *function_name = PyTuple_GetItem(tuple, 0);

		if(!PyUnicode_Check(function_name))
		{
			PyErr_Format(
				PyExc_ValueError,
				"from_tuple(asReference=true) function argument (pos 1) must be str, not %s",
				Py_TYPE(function_name)->tp_name
			);
			return NULL;
		}

		const char *value = PyUnicode_AsUTF8(function_name);
		sampgdk_fakeamx_push_string(value, NULL, &amx_params[1]);
	}

	for(
		Py_ssize_t i = (asReference ? 1 : 0);  // We just consumed function name above
		i < len_tuple;
		i++
	)
	{
		current_argument = PyTuple_GetItem(tuple, i);

		if(PyBool_Check(current_argument))
		{
			bool value = PyObject_IsTrue(current_argument);

			if(!asReference)
				amx_params[i + offset] = value;
			else
				sampgdk_fakeamx_push_cell(value, &amx_params[i + offset]);

			_format += "b";
		}
		else if(PyLong_Check(current_argument))
		{
			int value = PyLong_AsLong(current_argument);

			if(!asReference)
				amx_params[i + offset] = value;
			else
				sampgdk_fakeamx_push_cell(value, &amx_params[i + offset]);

			_format += "d";
		}
		else if(PyFloat_Check(current_argument))
		{
			float value = PyFloat_AsDouble(current_argument);

			if(!asReference)
				amx_params[i + offset] = amx_ftoc(value);
			else
				sampgdk_fakeamx_push_float(value, &amx_params[i + offset]);

			_format += "f";
		}
		else if(PyUnicode_Check(current_argument))
		{
			const char* value = PyUnicode_AsUTF8(current_argument);
			sampgdk_fakeamx_push_string(value, NULL, &amx_params[i + offset]);

			_format += "s";
		}
		else
		{
			char *repr;
			size_t size;
			FILE *bytes_io = open_memstream(&repr, &size);
			PyObject_Print(current_argument, bytes_io, 0);
			fclose(bytes_io);
			PyErr_Format(
				PyExc_TypeError,
				"CallNativeFunction() could not convert argument %s in position %d",
				repr,
				i + 1
			);
			free(repr);
			return NULL;
		}
	}

	if(asReference)
		sampgdk_fakeamx_push_string(_format.c_str(), NULL, &amx_params[2]);  // First param being function name

	return amx_params;
}

PyObject* ParamConverter::to_tuple(cell* params, const std::string format, AMX* amx)
{
	int number_of_arguments = format.length();

	if(number_of_arguments != params[0] / sizeof(cell))
	{
		PyErr_Format(
			PyExc_ValueError,
			"Invalid argument count for callback: expected %d, got %d",
			params[0] / sizeof(cell),
			number_of_arguments
		);
		return NULL;
	}

	PyObject *arguments = PyTuple_New(number_of_arguments);

	for(int i = 0; i < number_of_arguments; ++i)
	{
		const char type = format.at(i);
		cell param = params[i + 1];
		PyObject *argument;

		switch(type)
		{
			case 'i':
				argument = PyLong_FromLong((int) param);
				break;
			case 'O':
				argument = param ? Py_True : Py_False;
				break;
			case 'f':
				argument = PyFloat_FromDouble((double) amx_ctof(param));
				break;
			case 'y':
			{
				int length = -1;
				char *string_value = NULL;
				cell *phys_addr = NULL;

				if(amx_GetAddr(amx, param, &phys_addr) != AMX_ERR_NONE)
				{
					argument = Py_None;
					break;
				}

				amx_StrLen(phys_addr, &length);

				if(length == -1)
				{
					argument = Py_None;
					break;
				}

				string_value = (char *)malloc((length + 1) * sizeof(char));

				if(
					amx_GetString(
						string_value,
						phys_addr,
						0,
						length + 1
					) != AMX_ERR_NONE
					|| string_value == NULL
				)
				{
					free(string_value);
					argument = Py_None;
					break;
				}

				argument = PyUnicode_Decode(
					string_value,
					length,
					PySAMP::getEncoding().c_str(),
					"strict"
				);
				free(string_value);
				break;
			}
		}

		PyTuple_SetItem(arguments, i, argument);
	}

	return arguments;
}
