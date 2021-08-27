#include "logprintf.h"


std::string logprintf_buffer;

PyObject* logprintf_write(PyObject *self, PyObject *args)
{
	const char *text = NULL;

	if(!PyArg_ParseTuple(args, "s", &text))
		return NULL;

	std::stringstream text_stream(logprintf_buffer + text);
	std::string line, text_stream_string = text_stream.str();
	unsigned int num_lines = std::count(
		text_stream_string.begin(),
		text_stream_string.end(),
		'\n'
	), printed_len = 0;

	for(
		unsigned int current_line = 0;
		current_line < num_lines
		&& std::getline(text_stream, line);
		++current_line
	)
	{
		sampgdk::logprintf(line.c_str());
		printed_len += line.length();
	}

	std::getline(text_stream, logprintf_buffer);

	return PyLong_FromUnsignedLong(printed_len);
}

PyObject* logprintf_flush(PyObject *self, PyObject *args)
{
	if(logprintf_buffer.length())
	{
		sampgdk::logprintf(logprintf_buffer.c_str());
		logprintf_buffer.clear();
	}
	Py_RETURN_NONE;
}

PyMethodDef LogPrintfMethods[] = {
	{ "write", logprintf_write, METH_VARARGS, "Writes to server_log.txt - assigned to sys.std{out,err}.write at startup." },
	{ "flush", logprintf_flush, METH_VARARGS, "Flushes server_log.txt writes - empties internal line buffer into server_log.txt." },
	{ NULL, NULL, 0, NULL },
};

PyModuleDef LogPrintfModule = {
	PyModuleDef_HEAD_INIT,
	"logprintf",
	"Standard output to logprintf adapter",
	-1,
	LogPrintfMethods,
};
