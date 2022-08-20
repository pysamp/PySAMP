#include "callbacks.h"


const std::string* CallbacksManager::getFormat(const std::string& name) const
{
	auto itr = this->formats.find(name);

	if(itr == this->formats.end())
		return nullptr;

	return &itr->second;
}

int CallbacksManager::getBadret(const std::string& name) const
{
	static int const notFound = -1;
	auto itr = this->badrets.find(name);

	if(itr == this->badrets.end())
		return notFound;

	return itr->second;
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
	{"OnPlayerText", "is"},
	{"OnPlayerCommandText", "is"},
	{"OnPlayerRequestClass", "ii"},
	{"OnPlayerEnterVehicle", "iib"},
	{"OnPlayerExitVehicle", "ii"},
	{"OnPlayerStateChange", "iii"},
	{"OnPlayerEnterCheckpoint", "i"},
	{"OnPlayerLeaveCheckpoint", "i"},
	{"OnPlayerEnterRaceCheckpoint", "i"},
	{"OnPlayerLeaveRaceCheckpoint", "i"},
	{"OnRconCommand", "s"},
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
	{"OnRconLoginAttempt", "ssb"},
	{"OnPlayerUpdate", "i"},
	{"OnPlayerStreamIn", "ii"},
	{"OnPlayerStreamOut", "ii"},
	{"OnVehicleStreamIn", "ii"},
	{"OnVehicleStreamOut", "ii"},
	{"OnActorStreamIn", "ii"},
	{"OnActorStreamOut", "ii"},
	{"OnDialogResponse", "iiiis"},
	{"OnPlayerTakeDamage", "iifii"},
	{"OnPlayerGiveDamage", "iifii"},
	{"OnPlayerGiveDamageActor", "iifii"},
	{"OnPlayerClickMap", "ifff"},
	{"OnPlayerClickTextDraw", "ii"},
	{"OnPlayerClickPlayerTextDraw", "ii"},
	{"OnIncomingConnection", "isi"},
	{"OnTrailerUpdate", "ii"},
	{"OnVehicleSirenStateChange", "iii"},
	{"OnPlayerClickPlayer", "iii"},
	{"OnPlayerEditObject", "ibiiffffff"},
	{"OnPlayerEditAttachedObject", "iiiiifffffffff"},
	{"OnPlayerSelectObject", "iiiifff"},
	{"OnPlayerWeaponShot", "iiiifff"}
};

const std::unordered_map<std::string, bool> CallbacksManager::badrets = {
	{"OnDialogResponse", true},
	{"OnIncomingConnection", true},
	{"OnPlayerClickMap", true},
	{"OnPlayerClickPlayer", true},
	{"OnPlayerClickPlayerTextDraw", true},
	{"OnPlayerClickTextDraw", true},
	{"OnPlayerCommandText", true},
	{"OnPlayerConnect", false},
	{"OnPlayerDeath", false},
	{"OnPlayerDisconnect", false},
	{"OnPlayerEditAttachedObject", true},
	{"OnPlayerEditObject", true},
	{"OnPlayerGiveDamage", true},
	{"OnPlayerGiveDamageActor", true},
	{"OnPlayerRequestSpawn", false},
	{"OnPlayerSelectObject", true},
	{"OnPlayerSpawn", false},
	{"OnPlayerTakeDamage", true},
	{"OnPlayerText", false},
	{"OnPlayerUpdate", false},
	{"OnPlayerWeaponShot", false},
	{"OnRconCommand", true},
	{"OnTrailerUpdate", false},
	{"OnUnoccupiedVehicleUpdate", false},
	{"OnVehicleDamageStatusUpdate", true},
	{"OnVehicleMod", false},
	{"OnVehiclePaintjob", false},
	{"OnVehicleRespray", false},
	{"OnVehicleSpawn", false}
};
