#define VERSION "1.1.0-300"

#include <stdio.h>
#include <string.h>
#include "config.h"
#include "main.h"
#include "sampgdk.h"
#include "pysamp/pysamp.h"
#include "bindings/callbacks.h"
#include "test/callbackstest.h"
#include <thread>

std::thread threading;
bool threadingInitialized = false;

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

void startThreading()
{
	threadingInitialized = true;
	threading = std::thread([] { 
		sampgdk::logprintf("Initializing Threading");
		PySAMP::callback("OnThreadingInit", NULL);
		sampgdk::logprintf("Initialized Threading");
	});
}

void stopThreading()
{
	sampgdk::logprintf("Stopping PYSAMP-Threading");
	if(threadingInitialized)
	{
		PySAMP::callback("OnThreadingStopSignal", NULL);
		threading.join();
	}
}

PLUGIN_EXPORT void PLUGIN_CALL Unload()
{
	stopThreading();
	PySAMP::disable();
	// if (PySAMP::isInitialized())
    //		sampgdk::Unload();
}

PLUGIN_EXPORT void PLUGIN_CALL ProcessTick()
{
	if (PySAMP::isLoaded()) {
		PySAMP::callback("OnProcessTick", NULL);
	}
	sampgdk::ProcessTick();
}

PLUGIN_EXPORT bool PLUGIN_CALL OnGameModeExit()
{
	stopThreading();
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
	startThreading();
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

	*retval = result;
	return result;
}


PLUGIN_EXPORT bool PLUGIN_CALL OnRconCommand(const char * cmd) {
	sampgdk::logprintf("rcon command: %s", cmd);
	if (strcmp(cmd, "pyreload") == 0)
	{
		PySAMP::callback("OnPyUnload", NULL);
		stopThreading();
		PySAMP::disable();
		PySAMP::reload();
		startThreading();
		PySAMP::callback("OnPyReload", NULL);
		return true;
	}

	return false;
}


PLUGIN_EXPORT bool PLUGIN_CALL OnPlayerCommandText(int playerid,
	const char *cmdtext) {
	char* cmd = fromConst(cmdtext);
	sampgdk::logprintf(cmd);
	bool ret = PySAMP::callback("OnPlayerCommandText", Py_BuildValue("(iy)", playerid, cmd));
	delete[] cmd;
	return ret;
}
