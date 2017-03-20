#include "PySAMP.h"

PyGamemode* PySAMP::gamemode = 0;


void PySAMP::load() 
{
	PySAMP::gamemode = new PyGamemode(PYTHON_PATH);
}

bool PySAMP::callback(char * name, PyObject * pArgs)
{
	return PySAMP::gamemode->callback(name, pArgs);
}
