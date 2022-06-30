#include "callbacks.h"

const std::string* CallbacksManager::getFormat(const std::string& name) const
{
	auto itr = this->formats.find(name);

	if (itr == this->formats.end())
		return nullptr;

	return &itr->second;
}

const int* CallbacksManager::getBadret(const std::string& name) const
{
	static auto not_found = -1;
	auto itr = this->badrets.find(name);

	if (itr == this->badrets.end())
		return &not_found;

	return &itr->second;
}

void CallbacksManager::addFormat(const std::string& name, const std::string& format)
{
	this->formats[name] = format;
}

std::unordered_map<std::string, std::string> CallbacksManager::formats = {
	{"OnPlayerConnect", "i"},
	{"OnPlayerDisconnect", "ii"},
	{"OnPlayerSpawn", "i"},
	{"OnPlayerDeath", "iii"},
	{"OnVehicleSpawn", "i"},
	{"OnVehicleDeath", "ii"},
	{"OnPlayerText", "iy"},
	{"OnPlayerCommandText", "iy"},
	{"OnPlayerRequestClass", "ii"},
	{"OnPlayerEnterVehicle", "iiO"},
	{"OnPlayerExitVehicle", "ii"},
	{"OnPlayerStateChange", "iii"},
	{"OnPlayerEnterCheckpoint", "i"},
	{"OnPlayerLeaveCheckpoint", "i"},
	{"OnPlayerEnterRaceCheckpoint", "i"},
	{"OnPlayerLeaveRaceCheckpoint", "i"},
	{"OnRconCommand", "y"},
	{"OnPlayerRequestSpawn", "i"},
	{"OnObjectMoved", "i"},
	{"OnPlayerObjectMoved", "ii"},
	{"OnPlayerPickUpPickup", "ii"},
	{"OnVehicleMod", "iii"},
	{"OnEnterExitModShop", "iii"},
	{"OnVehiclePaintjob", "iii"},
	{"OnVehicleRespray", "iiii"},
	{"OnVehicleDamageStatusUpdate", "ii"},
	{"OnUnoccupiedVehicleUpdate", "iiiffffff"},
	{"OnPlayerSelectedMenuRow", "ii"},
	{"OnPlayerExitedMenu", "i"},
	{"OnPlayerInteriorChange", "iii"},
	{"OnPlayerKeyStateChange", "iii"},
	{"OnRconLoginAttempt", "yyO"},
	{"OnPlayerUpdate", "i"},
	{"OnPlayerStreamIn", "ii"},
	{"OnPlayerStreamOut", "ii"},
	{"OnVehicleStreamIn", "ii"},
	{"OnVehicleStreamOut", "ii"},
	{"OnActorStreamIn", "ii"},
	{"OnActorStreamOut", "ii"},
	{"OnDialogResponse", "iiiiy"},
	{"OnPlayerTakeDamage", "iifii"},
	{"OnPlayerGiveDamage", "iifii"},
	{"OnPlayerGiveDamageActor", "iifii"},
	{"OnPlayerClickMap", "ifff"},
	{"OnPlayerClickTextDraw", "ii"},
	{"OnPlayerClickPlayerTextDraw", "ii"},
	{"OnIncomingConnection", "iyi"},
	{"OnTrailerUpdate", "ii"},
	{"OnVehicleSirenStateChange", "iii"},
	{"OnPlayerClickPlayer", "iii"},
	{"OnPlayerEditObject", "iOiiffffff"},
	{"OnPlayerEditAttachedObject", "iiiiifffffffff"},
	{"OnPlayerSelectObject", "iiiifff"},
	{"OnPlayerWeaponShot", "iiiifff"}
};

const std::unordered_map<std::string, int> CallbacksManager::badrets = {
	{"OnDialogResponse", 1},
	{"OnIncomingConnection", 1},
	{"OnPlayerClickMap", 1},
	{"OnPlayerClickPlayer", 1},
	{"OnPlayerClickPlayerTextDraw", 1},
	{"OnPlayerClickTextDraw", 1},
	{"OnPlayerCommandText", 1},
	{"OnPlayerConnect", 0},
	{"OnPlayerDeath", 0},
	{"OnPlayerDisconnect", 0},
	{"OnPlayerEditAttachedObject", 1},
	{"OnPlayerEditObject", 1},
	{"OnPlayerGiveDamage", 1},
	{"OnPlayerGiveDamageActor", 1},
	{"OnPlayerRequestSpawn", 0},
	{"OnPlayerSelectObject", 1},
	{"OnPlayerSpawn", 0},
	{"OnPlayerTakeDamage", 1},
	{"OnPlayerText", 0},
	{"OnPlayerUpdate", 0},
	{"OnPlayerWeaponShot", 0},
	{"OnRconCommand", 1},
	{"OnTrailerUpdate", 0},
	{"OnUnoccupiedVehicleUpdate", 0},
	{"OnVehicleDamageStatusUpdate", 1},
	{"OnVehicleMod", 0},
	{"OnVehiclePaintjob", 0},
	{"OnVehicleRespray", 0},
	{"OnVehicleSpawn", 0}
};
