#ifndef CALLBACKS_H
#define CALLBACKS_H

#include "sampgdk.h"
#include "pysamp/PySAMP.h"

char* fromConst(const char * str) {
	const size_t len = strlen(str);
	char * cstr = new char[len + 1];
	strncpy(cstr, str, len);
	cstr[len] = '\0'; 
	return cstr;
}

PLUGIN_EXPORT bool PLUGIN_CALL OnGameModeInit() {
	sampgdk::logprintf("OnGameModeInit");
	PySAMP::callback("OnGameModeInit", NULL);
	return true;
}

PLUGIN_EXPORT bool PLUGIN_CALL OnGameModeExit() {
	sampgdk::logprintf("OnGameModeExit");
	PySAMP::callback("OnGameModeExit", NULL);
	return true;
}

PLUGIN_EXPORT bool PLUGIN_CALL OnPlayerConnect(int playerid) {
	sampgdk::logprintf("OnPlayerConnect");
	PySAMP::callback("OnPlayerConnect", Py_BuildValue("(i)", playerid));
	return true;
}

PLUGIN_EXPORT bool PLUGIN_CALL OnPlayerRequestClass(int playerid,
	int classid) {
	sampgdk::logprintf("OnPlayerRequestClass");
	PySAMP::callback("OnPlayerRequestClass", Py_BuildValue("(ii)", playerid, classid));
	return true;
}

PLUGIN_EXPORT bool PLUGIN_CALL OnPlayerCommandText(int playerid,
	const char *cmdtext) {
	sampgdk::logprintf("OnPlayerCommandText");
	char* cmd = fromConst(cmdtext);
	PySAMP::callback("OnPlayerCommandText", Py_BuildValue("(is)", playerid, cmd));
	delete[] cmd;
	return false;
}


#endif