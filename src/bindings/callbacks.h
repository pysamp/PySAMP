#ifndef CALLBACKS_H
#define CALLBACKS_H

#include "sampgdk.h"
#include "pysamp/pysamp.h"
#include "test/callbackstest.h"

char* fromConst(const char * str) {
	const size_t len = strlen(str);
	char * cstr = new char[len + 1];
	strncpy(cstr, str, len);
	cstr[len] = '\0'; 
	return cstr;
}

PLUGIN_EXPORT bool PLUGIN_CALL OnGameModeInit() {
#if PY_TEST
	CallbacksTest::runAll();
#endif // TEST

	return PySAMP::callback("OnGameModeInit", NULL);
}

PLUGIN_EXPORT bool PLUGIN_CALL OnGameModeExit() {
	return PySAMP::callback("OnGameModeExit", NULL);
}

PLUGIN_EXPORT bool PLUGIN_CALL OnPlayerConnect(int playerid) {
	return PySAMP::callback("OnPlayerConnect", Py_BuildValue("(i)", playerid));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnPlayerDisconnect(int playerid, int reason) {
	return PySAMP::callback("OnPlayerDisconnect", Py_BuildValue("(ii)", playerid, reason));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnPlayerRequestClass(int playerid,
	int classid) {
	return PySAMP::callback("OnPlayerRequestClass", Py_BuildValue("(ii)", playerid, classid));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnPlayerCommandText(int playerid,
	const char *cmdtext) {
	char* cmd = fromConst(cmdtext);
	sampgdk::logprintf(cmd);
	bool ret = PySAMP::callback("OnPlayerCommandText", Py_BuildValue("(is)", playerid, cmd));
	delete[] cmd;
	return ret;
}

PLUGIN_EXPORT bool PLUGIN_CALL OnPlayerSpawn(int playerid) {
	return PySAMP::callback("OnPlayerSpawn", Py_BuildValue("(i)", playerid));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnPlayerDeath(int playerid, int killerid, int reason) {
	return PySAMP::callback("OnPlayerDeath", Py_BuildValue("(i)", playerid));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnVehicleSpawn(int vehicleid) {
	return PySAMP::callback("OnVehicleSpawn", Py_BuildValue("(i)", vehicleid));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnVehicleDeath(int vehicleid, int killerid) {
	return PySAMP::callback("OnVehicleDeath", Py_BuildValue("(ii)", vehicleid, killerid));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnPlayerText(int playerid, const char * text) {
	char* txt = fromConst(text);
	bool ret = PySAMP::callback("OnPlayerCommandText", Py_BuildValue("(is)", playerid, txt));
	delete[] txt;
	return ret;
}

PLUGIN_EXPORT bool PLUGIN_CALL OnPlayerEnterVehicle(int playerid, int vehicleid, bool ispassenger) {
	return PySAMP::callback("OnPlayerEnterVehicle", Py_BuildValue("(iiO)", playerid, vehicleid, (ispassenger?Py_True:Py_False)));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnPlayerExitVehicle(int playerid, int vehicleid) {
	return PySAMP::callback("OnPlayerExitVehicle", Py_BuildValue("(ii)", playerid, vehicleid));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnPlayerStateChange(int playerid, int newstate, int oldstate) {
	return PySAMP::callback("OnPlayerStateChange", Py_BuildValue("(iii)", playerid, newstate, oldstate));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnPlayerEnterCheckpoint(int playerid) {
	return PySAMP::callback("OnPlayerEnterCheckpoint", Py_BuildValue("(i)", playerid));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnPlayerLeaveCheckpoint(int playerid) {
	return PySAMP::callback("OnPlayerLeaveCheckpoint", Py_BuildValue("(i)", playerid));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnPlayerEnterRaceCheckpoint(int playerid) {
	return PySAMP::callback("OnPlayerEnterRaceCheckpoint", Py_BuildValue("(i)", playerid));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnPlayerLeaveRaceCheckpoint(int playerid) {
	return PySAMP::callback("OnPlayerLeaveRaceCheckpoint", Py_BuildValue("(i)", playerid));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnRconCommand(const char * cmd) {
	char* str = fromConst(cmd);
	bool ret = PySAMP::callback("OnPlayerCommandText", Py_BuildValue("(is)", str));
	delete[] str;
	return ret;
}

PLUGIN_EXPORT bool PLUGIN_CALL OnPlayerRequestSpawn(int playerid) {
	return PySAMP::callback("OnPlayerRequestSpawn", Py_BuildValue("(i)", playerid));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnObjectMoved(int objectid) {
	return PySAMP::callback("OnObjectMoved", Py_BuildValue("(i)", objectid));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnPlayerObjectMoved(int playerid, int objectid) {
	return PySAMP::callback("OnPlayerObjectMoved", Py_BuildValue("(ii)", playerid, objectid));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnPlayerPickUpPickup(int playerid, int pickupid) {
	return PySAMP::callback("OnPlayerPickUpPickup", Py_BuildValue("(ii)", playerid, pickupid));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnVehicleMod(int playerid, int vehicleid, int componentid) {
	return PySAMP::callback("OnVehicleMod", Py_BuildValue("(iii)", playerid, vehicleid, componentid));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnEnterExitModShop(int playerid, int enterexit, int interiorid) {
	return PySAMP::callback("OnEnterExitModShop", Py_BuildValue("(iii)", playerid, enterexit, interiorid));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnVehiclePaintjob(int playerid, int vehicleid, int paintjobid) {
	return PySAMP::callback("OnVehiclePaintjob", Py_BuildValue("(iii)", playerid, vehicleid, paintjobid));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnVehicleRespray(int playerid, int vehicleid, int color1, int color2) {
	return PySAMP::callback("OnVehicleRespray", Py_BuildValue("(iiii)", playerid, vehicleid, color1, color2));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnVehicleDamageStatusUpdate(int vehicleid, int playerid) {
	return PySAMP::callback("OnVehicleDamageStatusUpdate", Py_BuildValue("(ii)", playerid, vehicleid));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnUnoccupiedVehicleUpdate(int vehicleid, int playerid, int passenger_seat, float new_x, float new_y, float new_z, float vel_x, float vel_y, float vel_z) {
	return PySAMP::callback("OnUnoccupiedVehicleUpdate", Py_BuildValue("(iiiffffff)", playerid, vehicleid, passenger_seat, new_x, new_y, new_z, vel_x, vel_y, vel_z));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnPlayerSelectedMenuRow(int playerid, int row) {
	return PySAMP::callback("OnPlayerSelectedMenuRow", Py_BuildValue("(ii)", playerid, row));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnPlayerExitedMenu(int playerid) {
	return PySAMP::callback("OnPlayerExitedMenu", Py_BuildValue("(i)", playerid));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnPlayerInteriorChange(int playerid, int newinteriorid, int oldinteriorid) {
	return PySAMP::callback("OnPlayerInteriorChange", Py_BuildValue("(iii)", playerid, newinteriorid, oldinteriorid));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnPlayerKeyStateChange(int playerid, int newkeys, int oldkeys) {
	return PySAMP::callback("OnPlayerKeyStateChange", Py_BuildValue("(iii)", playerid, newkeys, oldkeys));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnRconLoginAttempt(const char * ip, const char * password, bool success) {
	char* ipStr = fromConst(ip);
	char* passwordStr = fromConst(password);
	bool ret = PySAMP::callback("OnRconLoginAttempt", Py_BuildValue("(ssO)", ipStr, passwordStr, (success ? Py_True : Py_False)));
	delete[] ipStr, passwordStr;
	return ret;
}

PLUGIN_EXPORT bool PLUGIN_CALL OnPlayerUpdate(int playerid) {
	return PySAMP::callback("OnPlayerUpdate", Py_BuildValue("(i)", playerid));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnPlayerStreamIn(int playerid, int forplayerid) {
	return PySAMP::callback("OnPlayerStreamIn", Py_BuildValue("(ii)", playerid, forplayerid));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnPlayerStreamOut(int playerid, int forplayerid) {
	return PySAMP::callback("OnPlayerStreamOut", Py_BuildValue("(ii)", playerid, forplayerid));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnVehicleStreamIn(int vehicleid, int forplayerid) {
	return PySAMP::callback("OnVehicleStreamIn", Py_BuildValue("(ii)", vehicleid, forplayerid));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnVehicleStreamOut(int vehicleid, int forplayerid) {
	return PySAMP::callback("OnVehicleStreamOut", Py_BuildValue("(ii)", vehicleid, forplayerid));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnActorStreamIn(int actorid, int forplayerid) {
	return PySAMP::callback("OnActorStreamIn", Py_BuildValue("(ii)", actorid, forplayerid));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnActorStreamOut(int actorid, int forplayerid) {
	return PySAMP::callback("OnActorStreamOut", Py_BuildValue("(ii)", actorid, forplayerid));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnDialogResponse(int playerid, int dialogid, int response, int listitem, const char * inputtext) {
	char* inputtextStr = fromConst(inputtext);
	bool ret = PySAMP::callback("OnDialogResponse", Py_BuildValue("(iiiis)", playerid, dialogid, response, listitem, inputtextStr));
	delete[] inputtextStr;
	return ret;
}

PLUGIN_EXPORT bool PLUGIN_CALL OnPlayerTakeDamage(int playerid, int issuerid, float amount, int weaponid, int bodypart) {
	return PySAMP::callback("OnPlayerTakeDamage", Py_BuildValue("(iifii)", playerid, issuerid, amount, weaponid, bodypart));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnPlayerGiveDamage(int playerid, int damagedid, float amount, int weaponid, int bodypart) {
	return PySAMP::callback("OnPlayerGiveDamage", Py_BuildValue("(iifii)", playerid, damagedid, amount, weaponid, bodypart));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnPlayerGiveDamageActor(int playerid, int damaged_actorid, float amount, int weaponid, int bodypart) {
	return PySAMP::callback("OnPlayerGiveDamageActor", Py_BuildValue("(iifii)", playerid, damaged_actorid, amount, weaponid, bodypart));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnPlayerClickMap(int playerid, float fX, float fY, float fZ) {
	return PySAMP::callback("OnPlayerClickMap", Py_BuildValue("(ifff)", playerid, fX, fY, fZ));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnPlayerClickTextDraw(int playerid, int clickedid) {
	return PySAMP::callback("OnPlayerClickTextDraw", Py_BuildValue("(ii)", playerid, clickedid));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnPlayerClickPlayerTextDraw(int playerid, int playertextid) {
	return PySAMP::callback("OnPlayerClickPlayerTextDraw", Py_BuildValue("(ii)", playerid, playertextid));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnIncomingConnection(int playerid, const char * ip_address, int port) {
	sampgdk::logprintf("OnIncomingConnection");
	char * ipStr = fromConst(ip_address);
	bool ret = PySAMP::callback("OnIncomingConnection", Py_BuildValue("(isi)", playerid, ipStr, port));
	delete[] ipStr;
	return ret;
}

PLUGIN_EXPORT bool PLUGIN_CALL OnTrailerUpdate(int playerid, int vehicleid) {
	return PySAMP::callback("OnTrailerUpdate", Py_BuildValue("(ii)", playerid, vehicleid));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnVehicleSirenStateChange(int playerid, int vehicleid, int newstate) {
	return PySAMP::callback("OnVehicleSirenStateChange", Py_BuildValue("(iii)", playerid, vehicleid, newstate));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnPlayerClickPlayer(int playerid, int clickedplayerid, int source) {
	return PySAMP::callback("OnPlayerClickPlayer", Py_BuildValue("(iii)", playerid, clickedplayerid, source));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnPlayerEditObject(int playerid, bool playerobject, int objectid, int response, float fX, float fY, float fZ, float fRotX, float fRotY, float fRotZ) {
	return PySAMP::callback("OnPlayerEditObject", Py_BuildValue("(iOiiffffff)", playerid, (playerobject ? Py_True : Py_False), objectid, response, fX, fY, fZ, fRotX, fRotY, fRotZ));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnPlayerEditAttachedObject(int playerid, int response, int index, int modelid, int boneid, float fOffsetX, float fOffsetY, float fOffsetZ, float fRotX, float fRotY, float fRotZ, float fScaleX, float fScaleY, float fScaleZ) {
	return PySAMP::callback("OnPlayerEditAttachedObject", Py_BuildValue("(iiiiifffffffff)", playerid, response, index, modelid, boneid, fOffsetX, fOffsetY, fOffsetZ, fRotX, fRotY, fRotZ, fScaleX, fScaleY, fScaleZ));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnPlayerSelectObject(int playerid, int type, int objectid, int modelid, float fX, float fY, float fZ) {
	return PySAMP::callback("OnPlayerSelectObject", Py_BuildValue("(iiiifff)", playerid, type, objectid, modelid, fX, fY, fZ));
}

PLUGIN_EXPORT bool PLUGIN_CALL OnPlayerWeaponShot(int playerid, int weaponid, int hittype, int hitid, float fX, float fY, float fZ) {
	return PySAMP::callback("OnPlayerWeaponShot", Py_BuildValue("(iiiifff)", playerid, weaponid, hittype, hitid, fX, fY, fZ));
}

#endif
