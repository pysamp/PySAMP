#ifndef PYSAMP_H
#define PYSAMP_H

#if PY_TEST == 0
	#ifdef WIN32
	#define PYTHON_PATH "\\python"
	#else
	#define PYTHON_PATH "/python"
	#endif
#else
	#ifdef WIN32
	#define PYTHON_PATH "\\python\\test"
	#else
	#define PYTHON_PATH "/python/test"
	#endif
#endif // DEBUG


#include "pygamemode.h"



class PySAMP
{
private:
	static PyGamemode* gamemode;
public:
	static void load();
	static void reload();
	static void unload();
	static void disable();
	static bool callback(const char* name, PyObject * pArgs);
	static bool callback(const char* name, PyObject * pArgs, bool obtainLock);
	static bool isInitialized();
	static bool isLoaded();
	static bool isEnabled();
};



#endif // PYSAMP_H
