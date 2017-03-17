#include "SDK\amx\amx.h"
#include "SDK\plugincommon.h"


typedef void(*logprintf_t)(char* format, ...);


logprintf_t logprintf;


cell AMX_NATIVE_CALL Main(AMX* amx, cell* params)
{
	logprintf("pySAMP 1.0a");
	return 1;
}

PLUGIN_EXPORT unsigned int PLUGIN_CALL Supports()
{
	return SUPPORTS_VERSION | SUPPORTS_AMX_NATIVES;
}

PLUGIN_EXPORT bool PLUGIN_CALL Load(void **ppData)
{
	logprintf("LOADED pySAMP");
	return true;
}

PLUGIN_EXPORT void PLUGIN_CALL Unload()
{
	logprintf(" * Test plugin was unloaded.");
}