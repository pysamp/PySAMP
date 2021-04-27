#define VERSION "1.1.0-300"

#include <stdio.h>
#include <string.h>
#include "config.h"
#include "main.h"
#include "sampgdk.h"
#include "pysamp/pysamp.h"
#include "bindings/callbacks.h"
#include "test/callbackstest.h"

extern void *pAMXFunctions;

PLUGIN_EXPORT unsigned int PLUGIN_CALL Supports()
{
	return sampgdk::Supports() | SUPPORTS_PROCESS_TICK;
}

PLUGIN_EXPORT bool PLUGIN_CALL Load(void **ppData) 
{
	pAMXFunctions = ppData[PLUGIN_DATA_AMX_EXPORTS];
	sampgdk::logprintf("PySAMP %s for python%s", PYSAMP_VERSION, PYTHON_VERSION);

#ifndef WIN32
	//load libpython to support numpy and other libraries
	dlopen(PYTHON_LIBRARY, RTLD_GLOBAL);
#endif
	
	return sampgdk::Load(ppData);
}

PLUGIN_EXPORT void PLUGIN_CALL Unload()
{
	PySAMP::disable();
	// if (PySAMP::isInitialized())
    //		sampgdk::Unload();
}

PLUGIN_EXPORT void PLUGIN_CALL ProcessTick()
{
	if (PySAMP::isLoaded()) {
		PySAMP::callback("OnProcessTick", NULL);
	}
	Py_BEGIN_ALLOW_THREADS
	sampgdk::ProcessTick();
	Py_END_ALLOW_THREADS
}

PLUGIN_EXPORT bool PLUGIN_CALL OnGameModeExit()
{
	PySAMP::disable();

	bool result = PySAMP::callback("OnGameModeExit", NULL);
	return result;
}

PLUGIN_EXPORT bool PLUGIN_CALL OnGameModeInit()
{
	sampgdk::logprintf("Loading PYSAMP");
	try {
		if (PySAMP::isLoaded())
			PySAMP::reload();
		else
			PySAMP::load();
	} catch (std::exception) {
		return false;
	}
	bool result = PySAMP::callback("OnGameModeInit", NULL);
	return result;
}


PLUGIN_EXPORT bool PLUGIN_CALL OnPublicCall2(AMX *amx, const char *name,
    cell *params, cell *retval, bool* stop)
{
	if (Py_IsInitialized() == 0)
	{
		return false;
	}

	if (strcmp(name, "OnGameModeInit") == 0 || strcmp(name, "OnGameModeExit") == 0 || strcmp(name, "OnPlayerCommandText") == 0) {
		return false;
	}

	bool doesStop = callback_return_configuration.count(name) > 0;
	bool result = PySAMP::callback(name, createParameterObject(amx, name, params));

	if (doesStop)
	{
		bool stopOnReturnValue = callback_return_configuration.at(name);
		if (result == stopOnReturnValue)
		{
			*stop = true;
		}
	}

	if (retval != NULL)
	{
		*retval = result;
	}

	return result;
}


PLUGIN_EXPORT bool PLUGIN_CALL OnRconCommand(const char * cmd) {
	if (strcmp(cmd, "pyreload") == 0)
	{
		PySAMP::callback("OnPyUnload", NULL);
		PySAMP::disable();
		PySAMP::reload();
		PySAMP::callback("OnPyReload", NULL);
		return true;
	}

	return false;
}


PLUGIN_EXPORT bool PLUGIN_CALL OnPlayerCommandText(int playerid,
	const char *cmdtext) {
	bool ret = PySAMP::callback(
		"OnPlayerCommandText",
		Py_BuildValue("(iN)", playerid, PyUnicode_Decode(cmdtext, strlen(cmdtext), "cp1252", "strict"))
	);
	return ret;
}
