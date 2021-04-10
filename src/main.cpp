#include "main.h"

std::thread threading;
bool threadingInitialized = false;

extern void *pAMXFunctions;

static Logger logger = Logger("main");

PLUGIN_EXPORT unsigned int PLUGIN_CALL Supports()
{
	return sampgdk::Supports() | SUPPORTS_AMX_NATIVES  | SUPPORTS_PROCESS_TICK;
}

PLUGIN_EXPORT bool PLUGIN_CALL Load(void **ppData) 
{
	pAMXFunctions = ppData[PLUGIN_DATA_AMX_EXPORTS];
	sampgdk::logprintf("PySAMP %s for python%s", PYSAMP_VERSION, PYTHON_VERSION);
	
	initializeDefaultCallbacks();

#if PY_TRACE == 1
	Logger::setGlobalLevel(LogLevel::TRACE);
#endif
#ifndef WIN32
	//load libpython to support numpy and other libraries
	dlopen(PYTHON_LIBRARY, RTLD_GLOBAL);
#endif
	return sampgdk::Load(ppData);
}

void startThreading()
{
	if (PySAMP::hasCallback("OnThreadingInit"))
	{
		threading = std::thread([] {
			logger.debug("Initializing Threading");
			PySAMP::callback("OnThreadingInit", NULL);
			logger.debug("Initialized Threading");
		});
		threadingInitialized = true;
	}
}

void stopThreading()
{
	logger.debug("Stopping PYSAMP-Threading");
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
	/*
	int numNatives = 0;
	AMX_NATIVE native = sampgdk_FindNative("FCNPC_SetWeapon23");
	if (native != NULL)
		sampgdk::logprintf("Found FCNPC_SetWeapon23!");
	*/
	logger.debug("Loading PYSAMP");
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
	//TODO make this configurable!
	bool skipLog = strcmp(name, "OnPlayerTick") == 0 || strcmp(name, "OnPlayerUpdate") == 0 || strcmp(name, "OnUpdate") == 0 || strcmp(name, "FCNPC_OnUpdate") == 0;
	if (!skipLog)
		logger.trace("Begin OnPublicCall2 for %s", name);
	
	if (Py_IsInitialized() == 0)
	{
		return false;
	}

	if (strcmp(name, "OnGameModeInit") == 0 || strcmp(name, "OnGameModeExit") == 0 || strcmp(name, "OnPlayerCommandText") == 0) {
		return false;
	}

	if (callback_format.count(name) == 0) {
		logger.error("Callback %s not found", name);
		return false;
	}

	if (!PySAMP::hasCallback(name)) {
		if (!skipLog)
			logger.trace("Skipping callback because python gamemode has no callback: %s", name);
		return false;
	}

	bool hasReturnValue = callback_return_configuration.count(name) > 0;

	if (!skipLog)
		logger.trace("Calling python callback for %s with param format %s", name, callback_format.at(name).c_str());

	bool result = PySAMP::callback(name, createParameterObject(amx, name, params));

	if (!skipLog)
		logger.trace("Python callback for %s returned %d", name, result);

	if (hasReturnValue)
	{
		if (!skipLog)
			logger.trace("Check if callback propagation should stop for %s", name);
		bool stopOnReturnValue = callback_return_configuration.at(name);
		if (result == stopOnReturnValue)
		{
			if (!skipLog)
				logger.trace("Stop callback propagation for %s", name);
			*stop = true;
		}
		*retval = result;
	}
	if (!skipLog)
		logger.trace("End OnPublicCall2 for %s", name);
	return result;
}


PLUGIN_EXPORT bool PLUGIN_CALL OnRconCommand(const char * cmd) {
	logger.trace("rcon command: %s", cmd);
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
	bool ret = PySAMP::callback("OnPlayerCommandText", Py_BuildValue("(iy)", playerid, cmd));
	delete[] cmd;
	return ret;
}
