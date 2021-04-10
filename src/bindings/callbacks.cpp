#include "callbacks.h"

static Logger logger = Logger("callbacks");

std::map<std::string, std::string> callback_format;
std::map<std::string, bool> callback_return_configuration;

void initializeDefaultCallbacks()
{
    callback_format.insert({ "OnPlayerConnect", "i" });
    callback_format.insert({ "OnPlayerDisconnect", "ii" });
    callback_format.insert({ "OnPlayerSpawn", "i" });
    callback_format.insert({ "OnPlayerDeath", "iii" });
    callback_format.insert({ "OnVehicleSpawn", "i" });
    callback_format.insert({ "OnVehicleDeath", "ii" });
    callback_format.insert({ "OnPlayerText", "iy" });
    callback_format.insert({ "OnPlayerCommandText", "iy" });
    callback_format.insert({ "OnPlayerRequestClass", "ii" });
    callback_format.insert({ "OnPlayerEnterVehicle", "iiO" });
    callback_format.insert({ "OnPlayerExitVehicle", "ii" });
    callback_format.insert({ "OnPlayerStateChange", "iii" });
    callback_format.insert({ "OnPlayerEnterCheckpoint", "i" });
    callback_format.insert({ "OnPlayerLeaveCheckpoint", "i" });
    callback_format.insert({ "OnPlayerEnterRaceCheckpoint", "i" });
    callback_format.insert({ "OnPlayerLeaveRaceCheckpoint", "i" });
    callback_format.insert({ "OnRconCommand", "y" });
    callback_format.insert({ "OnPlayerRequestSpawn", "i" });
    callback_format.insert({ "OnObjectMoved", "i" });
    callback_format.insert({ "OnPlayerObjectMoved", "ii" });
    callback_format.insert({ "OnPlayerPickUpPickup", "ii" });
    callback_format.insert({ "OnVehicleMod", "iii" });
    callback_format.insert({ "OnEnterExitModShop", "iii" });
    callback_format.insert({ "OnVehiclePaintjob", "iii" }); //
    callback_format.insert({ "OnVehicleRespray", "iiii" });
    callback_format.insert({ "OnVehicleDamageStatusUpdate", "ii" });
    callback_format.insert({ "OnUnoccupiedVehicleUpdate", "iiiffffff" });
    callback_format.insert({ "OnPlayerSelectedMenuRow", "ii" });
    callback_format.insert({ "OnPlayerExitedMenu", "i" });
    callback_format.insert({ "OnPlayerInteriorChange", "iii" });
    callback_format.insert({ "OnPlayerKeyStateChange", "iii" });
    callback_format.insert({ "OnRconLoginAttempt", "yyO" });
    callback_format.insert({ "OnPlayerUpdate", "i" });
    callback_format.insert({ "OnPlayerStreamIn", "ii" });
    callback_format.insert({ "OnPlayerStreamOut", "ii" });
    callback_format.insert({ "OnVehicleStreamIn", "ii" });
    callback_format.insert({ "OnVehicleStreamOut", "ii" });
    callback_format.insert({ "OnActorStreamIn", "ii" });
    callback_format.insert({ "OnActorStreamOut", "ii" });
    callback_format.insert({ "OnDialogResponse", "iiiiy" });
    callback_format.insert({ "OnPlayerTakeDamage", "iifii" });
    callback_format.insert({ "OnPlayerGiveDamage", "iifii" });
    callback_format.insert({ "OnPlayerGiveDamageActor", "iifii" });
    callback_format.insert({ "OnPlayerClickMap", "ifff" });
    callback_format.insert({ "OnPlayerClickTextDraw", "ii" });
    callback_format.insert({ "OnPlayerClickPlayerTextDraw", "ii" });
    callback_format.insert({ "OnIncomingConnection", "iyi" });
    callback_format.insert({ "OnTrailerUpdate", "ii" });
    callback_format.insert({ "OnVehicleSirenStateChange", "iii" });
    callback_format.insert({ "OnPlayerClickPlayer", "iii" });
    callback_format.insert({ "OnPlayerEditObject", "iOiiffffff" });
    callback_format.insert({ "OnPlayerEditAttachedObject", "iiiiifffffffff" });
    callback_format.insert({ "OnPlayerSelectObject", "iiiifff" });
    callback_format.insert({ "OnPlayerWeaponShot", "iiiifff" });

    callback_return_configuration.insert({ "OnDialogResponse", 1 });
    callback_return_configuration.insert({ "OnGameModeExit", 0 });
    callback_return_configuration.insert({ "OnGameModeInit", 0 });
    callback_return_configuration.insert({ "OnIncomingConnection", 1 });
    callback_return_configuration.insert({ "OnPlayerClickMap", 1 });
    callback_return_configuration.insert({ "OnPlayerClickPlayer", 1 });
    callback_return_configuration.insert({ "OnPlayerClickPlayerTextDraw", 1 });
    callback_return_configuration.insert({ "OnPlayerClickTextDraw", 1 });
    callback_return_configuration.insert({ "OnPlayerCommandText", 1 });
    callback_return_configuration.insert({ "OnPlayerConnect", 0 });
    callback_return_configuration.insert({ "OnPlayerDeath", 0 });
    callback_return_configuration.insert({ "OnPlayerDisconnect", 0 });
    callback_return_configuration.insert({ "OnPlayerEditAttachedObject", 1 });
    callback_return_configuration.insert({ "OnPlayerEditObject", 1 });
    callback_return_configuration.insert({ "OnPlayerGiveDamage", 1 });
    callback_return_configuration.insert({ "OnPlayerGiveDamageActor", 1 });
    callback_return_configuration.insert({ "OnPlayerRequestSpawn", 0 });
    callback_return_configuration.insert({ "OnPlayerSelectObject", 1 });
    callback_return_configuration.insert({ "OnPlayerSpawn", 0 });
    callback_return_configuration.insert({ "OnPlayerTakeDamage", 1 });
    callback_return_configuration.insert({ "OnPlayerText", 0 });
    callback_return_configuration.insert({ "OnPlayerWeaponShot", 0 });
    callback_return_configuration.insert({ "OnRconCommand", 1 });
    callback_return_configuration.insert({ "OnUnoccupiedVehicleUpdate", 0 });
    callback_return_configuration.insert({ "OnVehicleDamageStatusUpdate", 1 });
    callback_return_configuration.insert({ "OnVehicleMod", 0 });
    callback_return_configuration.insert({ "OnVehiclePaintjob", 0 });
    callback_return_configuration.insert({ "OnVehicleRespray", 0 });
    callback_return_configuration.insert({ "OnVehicleSirenStateChange", 1 });
    callback_return_configuration.insert({ "OnVehicleSpawn", 0 });
}

PyObject* createParameterObject(AMX* amx, const char* callback_name, cell* parameters)
{
    if (callback_format.count(callback_name) == 0)
        return nullptr;
    std::string format = callback_format.at(callback_name);
    int number_of_arguments = format.length();

    PyObject* arguments = PyTuple_New(number_of_arguments);

    for (int i = 0; i < number_of_arguments; i++) {
        const char type = format.at(i);
        cell param = parameters[i + 1];
        PyObject* argument;
        switch (type)
        {
        case 'i':
            argument = PyLong_FromLong((int)param);
            break;
        case 'y':
            int length;
            char* string_value;
            cell* phys_addr;
            if (amx_GetAddr(amx, param, &phys_addr) != AMX_ERR_NONE) { //param == 0 || 
                argument = Py_None;
                break;
            }
            amx_StrLen(phys_addr, &length);
            string_value = (char*)malloc((length + 1) * sizeof(char));
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
            }
            else {
                argument = Py_True;
            }
            break;
        case 'f':
            argument = PyFloat_FromDouble((double)amx_ctof(param));
            break;
        }
        PyTuple_SET_ITEM(arguments, i, argument);
    }
    return arguments;
}

char* fromConst(const char* str) {
    const size_t len = strlen(str);
    char* cstr = new char[len + 1];
    strncpy(cstr, str, len);
    cstr[len] = '\0';
    return cstr;
}
