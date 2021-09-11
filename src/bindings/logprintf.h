#ifndef LOGPRINTF_H
#define LOGPRINTF_H

#include <algorithm>
#include <string>
#include <sstream>
#include <iostream>
#include <Python.h>
#include "sampgdk.h"


extern struct PyModuleDef LogPrintfModule;

static PyObject* logprintf_write(PyObject *self, PyObject *args);
static PyObject* logprintf_flush(PyObject *self, PyObject *args);
#endif
