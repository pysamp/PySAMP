#ifndef CALLBACKS_H
#define CALLBACKS_H

#include "sampgdk.h"
#include "pysamp/pysamp.h"

#include <stdio.h>
#include <stdarg.h>

std::map<std::string, std::string> _createCallbackFormatMap()
{
    std::map<std::string, std::string> callback_format;
    callback_format["OnPlayerConnect"] = "i";
    callback_format["OnPlayerDisconnect"] = "ii";
    callback_format["OnPlayerSpawn"] = "i";
    callback_format["OnPlayerDeath"] = "iii";
    callback_format["OnVehicleSpawn"] = "i";
    callback_format["OnVehicleDeath"] = "ii";
    callback_format["OnPlayerText"] = "iy";
    callback_format["OnPlayerCommandText"] = "iy";
    callback_format["OnPlayerRequestClass"] = "ii";
    callback_format["OnPlayerEnterVehicle"] = "iiO";
    callback_format["OnPlayerExitVehicle"] = "ii";
    callback_format["OnPlayerStateChange"] = "iii";
    callback_format["OnPlayerEnterCheckpoint"] = "i";
    callback_format["OnPlayerLeaveCheckpoint"] = "i";
    callback_format["OnPlayerEnterRaceCheckpoint"] = "i";
    callback_format["OnPlayerLeaveRaceCheckpoint"] = "i";
    callback_format["OnRconCommand"] = "y";
    callback_format["OnPlayerRequestSpawn"] = "i";
    callback_format["OnObjectMoved"] = "i";
    callback_format["OnPlayerObjectMoved"] = "ii";
    callback_format["OnPlayerPickUpPickup"] = "ii";
    callback_format["OnVehicleMod"] = "iii";
    callback_format["OnEnterExitModShop"] = "iii";
    callback_format["OnVehiclePaintjob"] = "iii"; //
    callback_format["OnVehicleRespray"] = "iiii";
    callback_format["OnVehicleDamageStatusUpdate"] = "ii";
    callback_format["OnUnoccupiedVehicleUpdate"] = "iiiffffff";
    callback_format["OnPlayerSelectedMenuRow"] = "ii";
    callback_format["OnPlayerExitedMenu"] = "i";
    callback_format["OnPlayerInteriorChange"] = "iii";
    callback_format["OnPlayerKeyStateChange"] = "iii";
    callback_format["OnRconLoginAttempt"] = "yyO";
    callback_format["OnPlayerUpdate"] = "i";
    callback_format["OnPlayerStreamIn"] = "ii";
    callback_format["OnPlayerStreamOut"] = "ii";
    callback_format["OnVehicleStreamIn"] = "ii";
    callback_format["OnVehicleStreamOut"] = "ii";
    callback_format["OnActorStreamIn"] = "ii";
    callback_format["OnActorStreamOut"] = "ii";
    callback_format["OnDialogResponse"] = "iiiiy";
    callback_format["OnPlayerTakeDamage"] = "iifii";
    callback_format["OnPlayerGiveDamage"] = "iifii";
    callback_format["OnPlayerGiveDamageActor"] = "iifii";
    callback_format["OnPlayerClickMap"] = "ifff";
    callback_format["OnPlayerClickTextDraw"] = "ii";
    callback_format["OnPlayerClickPlayerTextDraw"] = "ii";
    callback_format["OnIncomingConnection"] = "iyi";
    callback_format["OnTrailerUpdate"] = "ii";
    callback_format["OnVehicleSirenStateChange"] = "iii";
    callback_format["OnPlayerClickPlayer"] = "iii";
    callback_format["OnPlayerEditObject"] = "iOiiffffff";
    callback_format["OnPlayerEditAttachedObject"] = "iiiiifffffffff";
    callback_format["OnPlayerSelectObject"] = "iiiifff";
    callback_format["OnPlayerWeaponShot"] = "iiiifff";
    return callback_format;
}

/* creates map of all callbacks which can prohibit further callback propagation to other filterscripts / gamemodes / plugins */
std::map<std::string, bool> _createCallbackReturnConfiguration()
{
    std::map<std::string, bool> map;
    map["OnDialogResponse"] = 0;
    map["OnGameModeExit"] = 0;
    map["OnGameModeInit"] = 0;
    map["OnIncomingConnection"] = 1;
    map["OnPlayerClickMap"] = 1;
    map["OnPlayerClickPlayer"] = 1;
    map["OnPlayerClickPlayerTextDraw"] = 1;
    map["OnPlayerClickTextDraw"] = 1;
    map["OnPlayerCommandText"] = 1;
    map["OnPlayerConnect"] = 0;
    map["OnPlayerDeath"] = 0;
    map["OnPlayerDisconnect"] = 0;
    map["OnPlayerEditAttachedObject"] = 1;
    map["OnPlayerEditObject"] = 1;
    map["OnPlayerGiveDamage"] = 1;
    map["OnPlayerGiveDamageActor"] = 1;
    map["OnPlayerRequestSpawn"] = 0;
    map["OnPlayerSelectObject"] = 1;
    map["OnPlayerSpawn"] = 0;
    map["OnPlayerTakeDamage"] = 1;
    map["OnPlayerText"] = 0;
    map["OnPlayerWeaponShot"] = 0;
    map["OnRconCommand"] = 1;
    map["OnUnoccupiedVehicleUpdate"] = 0;
    map["OnVehicleDamageStatusUpdate"] = 1;
    map["OnVehicleMod"] = 0;
    map["OnVehiclePaintjob"] = 0;
    map["OnVehicleRespray"] = 0;
    map["OnVehicleSirenStateChange"] = 1;
    map["OnVehicleSpawn"] = 0;
    return map;
}

std::map<std::string, std::string> callback_format = _createCallbackFormatMap();

std::map<std::string, bool> callback_return_configuration = _createCallbackReturnConfiguration();

PyObject * createParameterObject(AMX *amx, const char *callback_name, cell *parameters)
{
    if (callback_format.count(callback_name) == 0)
        return nullptr;
    std::string format = callback_format.at(callback_name);
    int number_of_arguments = format.length();

    PyObject *arguments = PyTuple_New(number_of_arguments);

    for (int i = 0; i < number_of_arguments; i++) {
        const char type = format.at(i);
        cell param = parameters[i+1];
        PyObject *argument;
        switch (type)
        {
            case 'i':
                argument = PyLong_FromLong((int) param);
                break;
            case 'y':
                int length;
                char *string_value;
                cell *phys_addr;
                if (amx_GetAddr(amx, param, &phys_addr) != AMX_ERR_NONE) { //param == 0 || 
                    argument = Py_None;
                    break;
                }
                amx_StrLen(phys_addr, &length);
                string_value = (char *)malloc((length + 1) * sizeof(char));
                if (amx_GetString(string_value, phys_addr, 0, length + 1) != AMX_ERR_NONE) {
                    free(string_value);
                    argument = Py_None;
                    break;
                }
                assert(string_value != NULL);
                argument = PyBytes_FromString(string_value);
                free(string_value);
                break;
            case 'O':
                if (!param) {
                    argument = Py_False;
                } else {
                    argument = Py_True;
                }
                break;
            case 'f':
                argument = PyFloat_FromDouble((double) amx_ctof(param));
                break;
        }
        PyTuple_SET_ITEM(arguments, i, argument);
    }
    return arguments;
}

char* fromConst(const char * str) {
    const size_t len = strlen(str);
    char * cstr = new char[len + 1];
    strncpy(cstr, str, len);
    cstr[len] = '\0'; 
    return cstr;
}


#endif
