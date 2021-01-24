#include "pysamp.h"

PyGamemode* PySAMP::gamemode = nullptr;


void PySAMP::load()
{
	sampgdk::logprintf("Loading PySAMP gamemode");
	PySAMP::gamemode = new PyGamemode(PYTHON_PATH);

	if (!PyEval_ThreadsInitialized()) 
	{
		PyEval_InitThreads();
	}

	gamemode->load();
}

void PySAMP::reload()
{
	sampgdk::logprintf("Reloading PySAMP gamemode");
	if (PySAMP::isLoaded())
		PySAMP::gamemode->reload();
}

void PySAMP::disable()
{
	if (PySAMP::isLoaded())
		PySAMP::gamemode->disable();
}

void PySAMP::unload()
{
	sampgdk::logprintf("Unloading PySAMP gamemode");
	delete PySAMP::gamemode;
	PySAMP::gamemode = nullptr;
}

bool PySAMP::callback(const char * name, PyObject * pArgs)
{
	return PySAMP::callback(name, pArgs, true);
}

bool PySAMP::callback(const char * name, PyObject * pArgs, bool obtainLock)
{
	if(PySAMP::gamemode && PySAMP::gamemode->isLoaded())
		return PySAMP::gamemode->callback(name, pArgs, obtainLock);
	return 0;
}

bool PySAMP::isInitialized()
{
	return !!PySAMP::gamemode;
}

bool PySAMP::isLoaded()
{
	return PySAMP::isInitialized() && PySAMP::gamemode->isLoaded();
}

bool PySAMP::isEnabled()
{
	return PySAMP::isLoaded() && PySAMP::gamemode->isEnabled();
}
