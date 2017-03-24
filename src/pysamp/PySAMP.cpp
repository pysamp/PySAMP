#include "PySAMP.h"

PyGamemode* PySAMP::gamemode = 0;


void PySAMP::load()
{
	PySAMP::gamemode = new PyGamemode(PYTHON_PATH);
}

void PySAMP::unload()
{
	delete PySAMP::gamemode;
}

bool PySAMP::callback(char * name, PyObject * pArgs)
{
	//if gamemode exists forward to callback
	if(PySAMP::gamemode != NULL)
		return PySAMP::gamemode->callback(name, pArgs);
	return 0;
}
