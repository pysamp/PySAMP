#ifndef PYGAMEMODE_H
#define PYGAMEMODE_H

#include <Python.h>
#include "sampgdk.h"
#include <stdexcept>


#ifdef WIN32
#include <algorithm>
#include <string>
#include <direct.h>
#define GetCurrentDir _getcwd
#else
#include <unistd.h>
#define GetCurrentDir getcwd
#endif

class PyGamemode
{
private:	
	PyObject *pName, *pModule, *pDict;
	bool initialized = false;
public:
	PyGamemode(const char* path);
	~PyGamemode();
	bool callback(const char* name , PyObject* pArgs);
};

#endif