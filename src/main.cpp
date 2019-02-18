#define VERSION "1.1.0-100"

#include <stdio.h>
#include <string.h>
#include "main.h"
#include "sampgdk.h"
#include "pysamp/pysamp.h"
#include "bindings/callbacks.h"
#include "test/callbackstest.h"
#include <thread>

std::thread threading;
bool threadingInitialized = false;

PLUGIN_EXPORT unsigned int PLUGIN_CALL Supports()
{
	return sampgdk::Supports() | SUPPORTS_PROCESS_TICK;
}

PLUGIN_EXPORT bool PLUGIN_CALL Load(void **ppData) 
{
	std::cout << "Loading PYSAMP" << std::endl;
	try {
		PySAMP::load();
	} catch (std::exception) {
		return false;
	}
	
	bool sgdk = sampgdk::Load(ppData);
	if (sgdk) 
	{
		sampgdk::logprintf("PySAMP %s", VERSION);

		threadingInitialized = true;
		threading = std::thread([] { 
			PyGILState_STATE state = PyGILState_Ensure();
			PySAMP::callback("OnThreadingInit", NULL);
			PyGILState_Release(state);
		});

		
	}
	return sgdk;
}

PLUGIN_EXPORT void PLUGIN_CALL Unload()
{
	sampgdk::Unload();
}

PLUGIN_EXPORT void PLUGIN_CALL ProcessTick()
{
	sampgdk::ProcessTick();
	PySAMP::callback("OnProcessTick", NULL);
}


PLUGIN_EXPORT bool PLUGIN_CALL OnGameModeExit() {
	if(threadingInitialized)
	{
		PySAMP::callback("OnThreadingStopSignal", NULL);
		threading.join();
	}
	return PySAMP::callback("OnGameModeExit", NULL);
}
