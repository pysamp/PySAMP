#ifndef PYSAMP_H
#define PYSAMP_H
#ifdef WIN32
#define PYTHON_PATH "\\python"
#else
#define PYTHON_PATH "/python"
#endif

#include "PyGamemode.h"



class PySAMP
{
private:
	static PyGamemode* gamemode;
public:
	static void load();
	static void unload();
	static bool callback(char* name, PyObject * pArgs);
};



#endif // PYSAMP_H