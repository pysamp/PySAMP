#include <stdio.h>
#include <string.h>
#include "sampgdk.h"
#include "pySAMP/pySAMP.h"
#include "bindings/callbacks.h"

#define DEBUG


PLUGIN_EXPORT unsigned int PLUGIN_CALL Supports() {
  return sampgdk::Supports() | SUPPORTS_PROCESS_TICK;
}

PLUGIN_EXPORT bool PLUGIN_CALL Load(void **ppData) {

	try {
		PySAMP::load();
	} catch (std::exception) {
		return false;
	}
	
	return sampgdk::Load(ppData);
}

PLUGIN_EXPORT void PLUGIN_CALL Unload() {
  sampgdk::Unload();
}

PLUGIN_EXPORT void PLUGIN_CALL ProcessTick() {
  sampgdk::ProcessTick();
}