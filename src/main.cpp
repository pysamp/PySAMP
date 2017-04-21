
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
	try {
		PySAMP::load();
	} catch (std::exception) {
		return false;
	}
	
	bool sgdk = sampgdk::Load(ppData);
	if (sgdk) {
		PySAMP::callback("OnThreadingInit", NULL);
		threading = std::thread([] { PySAMP::callback("OnThreadingInit", NULL); });

	}
	return false;
}

PLUGIN_EXPORT void PLUGIN_CALL Unload()
{
  sampgdk::Unload();
}

PLUGIN_EXPORT void PLUGIN_CALL ProcessTick()
{
	PySAMP::callback("OnThreadingStopSignal", NULL);
	threading.join();
	sampgdk::ProcessTick();
	PySAMP::callback("OnProcessTick", NULL);
}
