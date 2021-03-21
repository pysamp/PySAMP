#pragma once

#include "sampgdk.h"

#include <stdio.h>
#include <stdarg.h>
#include <map>
#include <string>
#include <Python.h>

#include "logging/logger.h"

extern std::map<std::string, std::string> callback_format;
extern std::map<std::string, bool> callback_return_configuration;

void initializeDefaultCallbacks();

char* fromConst(const char* str);
PyObject* createParameterObject(AMX* amx, const char* callback_name, cell* parameters);
