#include "PySAMP.h"

PyGamemode* PySAMP::gamemode = 0;


void PySAMP::load() 
{
	PySAMP::gamemode = new PyGamemode(PYTHON_PATH);
}

void PySAMP::callback(char * name, PyObject * pArgs)
{
	PySAMP::gamemode->callback(name, pArgs);
}
