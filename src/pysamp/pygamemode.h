#ifndef PYGAMEMODE_H
#define PYGAMEMODE_H

#include <Python.h>
#include "sampgdk.h"
#include <stdexcept>
#include "samp.h"

#ifdef DEBUG
#define PY_DEBUG
#endif // DEBUG


#ifdef WIN32
#include <algorithm>
#include <string>
#include <direct.h>
#define GetCurrentDir _getcwd
#else
#include <dlfcn.h>
#include <unistd.h>
#define GetCurrentDir getcwd
#endif

class PyGamemode
{
private:	
	PyObject *pName = nullptr, *pModule = nullptr;
	bool initialized = false;
	bool loaded = false;
	bool disabled = false;
	const char* path;
public:
	PyGamemode(const char* apath);
	~PyGamemode();
	bool callback(const char* name , PyObject* pArgs, bool obtainLock);
	void load();
	void reload();
	void unload();
	bool isLoaded();
	void disable();
	bool isEnabled();
};

#endif
