#ifndef PYSAMP_H
#define PYSAMP_H

#ifdef TEST
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
	static void unload();
	static bool callback(const char* name, PyObject * pArgs);
};



#endif // PYSAMP_H
