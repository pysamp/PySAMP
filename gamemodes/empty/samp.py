import pysamp

def encode(value):
    if type(value) != 'bytes':
        return value.encode('iso-8859-1')
    return value

def decode(value):
    if value is None:
        return None
    if type(value) == str:
        return value
    return value.decode('iso-8859-1')

def Const(name):
    return pysamp.Const(name)

def SetSpawnInfo(playerid, team, skin, x, y, z, rotation, weapon1, weapon1_ammo, weapon2, weapon2_ammo, weapon3, weapon3_ammo):
    return pysamp.SetSpawnInfo(playerid, team, skin, x, y, z, rotation, weapon1, weapon1_ammo, weapon2, weapon2_ammo, weapon3, weapon3_ammo)

def SpawnPlayer(playerid):
    return pysamp.SpawnPlayer(playerid)

def SetPlayerPos(playerid, x, y, z):
    return pysamp.SetPlayerPos(playerid, x, y, z)

def SetPlayerPosFindZ(playerid, x, y, z):
    return pysamp.SetPlayerPosFindZ(playerid, x, y, z)

def GetPlayerPos(playerid):
    (x, y, z) = pysamp.GetPlayerPos(playerid)
    return (x, y, z)

def SetPlayerFacingAngle(playerid, angle):
    return pysamp.SetPlayerFacingAngle(playerid, angle)

def GetPlayerFacingAngle(playerid):
    return pysamp.GetPlayerFacingAngle(playerid)

def IsPlayerInRangeOfPoint(playerid, range, x, y, z):
    return pysamp.IsPlayerInRangeOfPoint(playerid, range, x, y, z)

def GetPlayerDistanceFromPoint(playerid, x, y, z):
    return pysamp.GetPlayerDistanceFromPoint(playerid, x, y, z)

def IsPlayerStreamedIn(playerid, forplayerid):
    return pysamp.IsPlayerStreamedIn(playerid, forplayerid)

def SetPlayerInterior(playerid, interiorid):
    return pysamp.SetPlayerInterior(playerid, interiorid)

def GetPlayerInterior(playerid):
    return pysamp.GetPlayerInterior(playerid)

def SetPlayerHealth(playerid, health):
    return pysamp.SetPlayerHealth(playerid, health)

def GetPlayerHealth(playerid):
    return pysamp.GetPlayerHealth(playerid)

def SetPlayerArmour(playerid, armour):
    return pysamp.SetPlayerArmour(playerid, armour)

def GetPlayerArmour(playerid):
    return pysamp.GetPlayerArmour(playerid)

def SetPlayerAmmo(playerid, weaponid, ammo):
    return pysamp.SetPlayerAmmo(playerid, weaponid, ammo)

def GetPlayerAmmo(playerid):
    return pysamp.GetPlayerAmmo(playerid)

def GetPlayerWeaponState(playerid):
    return pysamp.GetPlayerWeaponState(playerid)

def GetPlayerTargetPlayer(playerid):
    return pysamp.GetPlayerTargetPlayer(playerid)

def GetPlayerTargetActor(playerid):
    return pysamp.GetPlayerTargetActor(playerid)

def SetPlayerTeam(playerid, teamid):
    return pysamp.SetPlayerTeam(playerid, teamid)

def GetPlayerTeam(playerid):
    return pysamp.GetPlayerTeam(playerid)

def SetPlayerScore(playerid, score):
    return pysamp.SetPlayerScore(playerid, score)

def GetPlayerScore(playerid):
    return pysamp.GetPlayerScore(playerid)

def GetPlayerDrunkLevel(playerid):
    return pysamp.GetPlayerDrunkLevel(playerid)

def SetPlayerDrunkLevel(playerid, level):
    return pysamp.SetPlayerDrunkLevel(playerid, level)

def SetPlayerColor(playerid, color):
    return pysamp.SetPlayerColor(playerid, color)

def GetPlayerColor(playerid):
    return pysamp.GetPlayerColor(playerid)

def SetPlayerSkin(playerid, skinid):
    return pysamp.SetPlayerSkin(playerid, skinid)

def GetPlayerSkin(playerid):
    return pysamp.GetPlayerSkin(playerid)

def GivePlayerWeapon(playerid, weaponid, ammo):
    return pysamp.GivePlayerWeapon(playerid, weaponid, ammo)

def ResetPlayerWeapons(playerid):
    return pysamp.ResetPlayerWeapons(playerid)

def SetPlayerArmedWeapon(playerid, weaponid):
    return pysamp.SetPlayerArmedWeapon(playerid, weaponid)

def GetPlayerWeaponData(playerid, slot):
    (weapon, ammo) = pysamp.GetPlayerWeaponData(playerid, slot)
    return (weapon, ammo)

def GivePlayerMoney(playerid, money):
    return pysamp.GivePlayerMoney(playerid, money)

def ResetPlayerMoney(playerid):
    return pysamp.ResetPlayerMoney(playerid)

def SetPlayerName(playerid, name):
    return pysamp.SetPlayerName(playerid, encode(name))

def GetPlayerMoney(playerid):
    return pysamp.GetPlayerMoney(playerid)

def GetPlayerState(playerid):
    return pysamp.GetPlayerState(playerid)

def GetPlayerIp(playerid, size):
    return decode(pysamp.GetPlayerIp(playerid, size))

def GetPlayerPing(playerid):
    return pysamp.GetPlayerPing(playerid)

def GetPlayerWeapon(playerid):
    return pysamp.GetPlayerWeapon(playerid)

def GetPlayerKeys(playerid):
    (keys, updown, leftright) = pysamp.GetPlayerKeys(playerid)
    return (keys, updown, leftright)

def GetPlayerName(playerid, size):
    return decode(pysamp.GetPlayerName(playerid, size))

def SetPlayerTime(playerid, hour, minute):
    return pysamp.SetPlayerTime(playerid, hour, minute)

def GetPlayerTime(playerid):
    (hour, minute) = pysamp.GetPlayerTime(playerid)
    return (hour, minute)

def TogglePlayerClock(playerid, toggle):
    return pysamp.TogglePlayerClock(playerid, toggle)

def SetPlayerWeather(playerid, weather):
    return pysamp.SetPlayerWeather(playerid, weather)

def ForceClassSelection(playerid):
    return pysamp.ForceClassSelection(playerid)

def SetPlayerWantedLevel(playerid, level):
    return pysamp.SetPlayerWantedLevel(playerid, level)

def GetPlayerWantedLevel(playerid):
    return pysamp.GetPlayerWantedLevel(playerid)

def SetPlayerFightingStyle(playerid, style):
    return pysamp.SetPlayerFightingStyle(playerid, style)

def GetPlayerFightingStyle(playerid):
    return pysamp.GetPlayerFightingStyle(playerid)

def SetPlayerVelocity(playerid, x, y, z):
    return pysamp.SetPlayerVelocity(playerid, x, y, z)

def GetPlayerVelocity(playerid):
    (x, y, z) = pysamp.GetPlayerVelocity(playerid)
    return (x, y, z)

def PlayCrimeReportForPlayer(playerid, suspectid, crime):
    return pysamp.PlayCrimeReportForPlayer(playerid, suspectid, crime)

def PlayAudioStreamForPlayer(playerid, url, posX = 0.0, posY = 0.0, posZ = 0.0, distance = 50.0, usepos = False):
    return pysamp.PlayAudioStreamForPlayer(playerid, encode(url), posX, posY, posZ, distance, usepos)

def StopAudioStreamForPlayer(playerid):
    return pysamp.StopAudioStreamForPlayer(playerid)

def SetPlayerShopName(playerid, shopname):
    return pysamp.SetPlayerShopName(playerid, encode(shopname))

def SetPlayerSkillLevel(playerid, skill, level):
    return pysamp.SetPlayerSkillLevel(playerid, skill, level)

def GetPlayerSurfingVehicleID(playerid):
    return pysamp.GetPlayerSurfingVehicleID(playerid)

def GetPlayerSurfingObjectID(playerid):
    return pysamp.GetPlayerSurfingObjectID(playerid)

def RemoveBuildingForPlayer(playerid, modelid, fX, fY, fZ, fRadius):
    return pysamp.RemoveBuildingForPlayer(playerid, modelid, fX, fY, fZ, fRadius)

def GetPlayerLastShotVectors(playerid):
    (fOriginX, fOriginY, fOriginZ, fHitPosX, fHitPosY, fHitPosZ) = pysamp.GetPlayerLastShotVectors(playerid)
    return (fOriginX, fOriginY, fOriginZ, fHitPosX, fHitPosY, fHitPosZ)

def SetPlayerAttachedObject(playerid, index, modelid, bone, fOffsetX = 0.0, fOffsetY = 0.0, fOffsetZ = 0.0, fRotX = 0.0, fRotY = 0.0, fRotZ = 0.0, fScaleX = 1.0, fScaleY = 1.0, fScaleZ = 1.0, materialcolor1 = 0, materialcolor2 = 0):
    return pysamp.SetPlayerAttachedObject(playerid, index, modelid, bone, fOffsetX, fOffsetY, fOffsetZ, fRotX, fRotY, fRotZ, fScaleX, fScaleY, fScaleZ, materialcolor1, materialcolor2)

def RemovePlayerAttachedObject(playerid, index):
    return pysamp.RemovePlayerAttachedObject(playerid, index)

def IsPlayerAttachedObjectSlotUsed(playerid, index):
    return pysamp.IsPlayerAttachedObjectSlotUsed(playerid, index)

def EditAttachedObject(playerid, index):
    return pysamp.EditAttachedObject(playerid, index)

def CreatePlayerTextDraw(playerid, x, y, text):
    return pysamp.CreatePlayerTextDraw(playerid, x, y, encode(text))

def PlayerTextDrawDestroy(playerid, text):
    return pysamp.PlayerTextDrawDestroy(playerid, text)

def PlayerTextDrawLetterSize(playerid, text, x, y):
    return pysamp.PlayerTextDrawLetterSize(playerid, text, x, y)

def PlayerTextDrawTextSize(playerid, text, x, y):
    return pysamp.PlayerTextDrawTextSize(playerid, text, x, y)

def PlayerTextDrawAlignment(playerid, text, alignment):
    return pysamp.PlayerTextDrawAlignment(playerid, text, alignment)

def PlayerTextDrawColor(playerid, text, color):
    return pysamp.PlayerTextDrawColor(playerid, text, color)

def PlayerTextDrawUseBox(playerid, text, use):
    return pysamp.PlayerTextDrawUseBox(playerid, text, use)

def PlayerTextDrawBoxColor(playerid, text, color):
    return pysamp.PlayerTextDrawBoxColor(playerid, text, color)

def PlayerTextDrawSetShadow(playerid, text, size):
    return pysamp.PlayerTextDrawSetShadow(playerid, text, size)

def PlayerTextDrawSetOutline(playerid, text, size):
    return pysamp.PlayerTextDrawSetOutline(playerid, text, size)

def PlayerTextDrawBackgroundColor(playerid, text, color):
    return pysamp.PlayerTextDrawBackgroundColor(playerid, text, color)

def PlayerTextDrawFont(playerid, text, font):
    return pysamp.PlayerTextDrawFont(playerid, text, font)

def PlayerTextDrawSetProportional(playerid, text, set):
    return pysamp.PlayerTextDrawSetProportional(playerid, text, set)

def PlayerTextDrawSetSelectable(playerid, text, set):
    return pysamp.PlayerTextDrawSetSelectable(playerid, text, set)

def PlayerTextDrawShow(playerid, text):
    return pysamp.PlayerTextDrawShow(playerid, text)

def PlayerTextDrawHide(playerid, text):
    return pysamp.PlayerTextDrawHide(playerid, text)

def PlayerTextDrawSetString(playerid, text, string):
    return pysamp.PlayerTextDrawSetString(playerid, text, encode(string))

def PlayerTextDrawSetPreviewModel(playerid, text, modelindex):
    return pysamp.PlayerTextDrawSetPreviewModel(playerid, text, modelindex)

def PlayerTextDrawSetPreviewRot(playerid, text, fRotX, fRotY, fRotZ, fZoom = 1.0):
    return pysamp.PlayerTextDrawSetPreviewRot(playerid, text, fRotX, fRotY, fRotZ, fZoom)

def PlayerTextDrawSetPreviewVehCol(playerid, text, color1, color2):
    return pysamp.PlayerTextDrawSetPreviewVehCol(playerid, text, color1, color2)

def SetPVarInt(playerid, varname, value):
    return pysamp.SetPVarInt(playerid, encode(varname), value)

def GetPVarInt(playerid, varname):
    return pysamp.GetPVarInt(playerid, encode(varname))

def SetPVarString(playerid, varname, value):
    return pysamp.SetPVarString(playerid, encode(varname), encode(value))

def GetPVarString(playerid, varname, size):
    return decode(pysamp.GetPVarString(playerid, encode(varname), size))

def SetPVarFloat(playerid, varname, value):
    return pysamp.SetPVarFloat(playerid, encode(varname), value)

def GetPVarFloat(playerid, varname):
    return pysamp.GetPVarFloat(playerid, encode(varname))

def DeletePVar(playerid, varname):
    return pysamp.DeletePVar(playerid, encode(varname))

def GetPVarsUpperIndex(playerid):
    return pysamp.GetPVarsUpperIndex(playerid)

def GetPVarNameAtIndex(playerid, index, size):
    return decode(pysamp.GetPVarNameAtIndex(playerid, index, size))

def GetPVarType(playerid, varname):
    return pysamp.GetPVarType(playerid, encode(varname))

def SetPlayerChatBubble(playerid, text, color, drawdistance, expiretime):
    return pysamp.SetPlayerChatBubble(playerid, encode(text), color, drawdistance, expiretime)

def PutPlayerInVehicle(playerid, vehicleid, seatid):
    return pysamp.PutPlayerInVehicle(playerid, vehicleid, seatid)

def GetPlayerVehicleID(playerid):
    return pysamp.GetPlayerVehicleID(playerid)

def GetPlayerVehicleSeat(playerid):
    return pysamp.GetPlayerVehicleSeat(playerid)

def RemovePlayerFromVehicle(playerid):
    return pysamp.RemovePlayerFromVehicle(playerid)

def TogglePlayerControllable(playerid, toggle):
    return pysamp.TogglePlayerControllable(playerid, toggle)

def PlayerPlaySound(playerid, soundid, x, y, z):
    return pysamp.PlayerPlaySound(playerid, soundid, x, y, z)

def ApplyAnimation(playerid, animlib, animname, fDelta, loop, lockx, locky, freeze, time, forcesync = False):
    return pysamp.ApplyAnimation(playerid, encode(animlib), encode(animname), fDelta, loop, lockx, locky, freeze, time, forcesync)

def ClearAnimations(playerid, forcesync = False):
    return pysamp.ClearAnimations(playerid, forcesync)

def GetPlayerAnimationIndex(playerid):
    return pysamp.GetPlayerAnimationIndex(playerid)

def GetAnimationName(index, animlib_size, animname_size):
    (animlib, animname) = pysamp.GetAnimationName(index, animlib_size, animname_size)
    return (decode(animlib), decode(animname))

def GetPlayerSpecialAction(playerid):
    return pysamp.GetPlayerSpecialAction(playerid)

def SetPlayerSpecialAction(playerid, actionid):
    return pysamp.SetPlayerSpecialAction(playerid, actionid)

def DisableRemoteVehicleCollisions(playerid, disable):
    return pysamp.DisableRemoteVehicleCollisions(playerid, disable)

def SetPlayerCheckpoint(playerid, x, y, z, size):
    return pysamp.SetPlayerCheckpoint(playerid, x, y, z, size)

def DisablePlayerCheckpoint(playerid):
    return pysamp.DisablePlayerCheckpoint(playerid)

def SetPlayerRaceCheckpoint(playerid, type, x, y, z, nextx, nexty, nextz, size):
    return pysamp.SetPlayerRaceCheckpoint(playerid, type, x, y, z, nextx, nexty, nextz, size)

def DisablePlayerRaceCheckpoint(playerid):
    return pysamp.DisablePlayerRaceCheckpoint(playerid)

def SetPlayerWorldBounds(playerid, x_max, x_min, y_max, y_min):
    return pysamp.SetPlayerWorldBounds(playerid, x_max, x_min, y_max, y_min)

def SetPlayerMarkerForPlayer(playerid, showplayerid, color):
    return pysamp.SetPlayerMarkerForPlayer(playerid, showplayerid, color)

def ShowPlayerNameTagForPlayer(playerid, showplayerid, show):
    return pysamp.ShowPlayerNameTagForPlayer(playerid, showplayerid, show)

def SetPlayerMapIcon(playerid, iconid, x, y, z, markertype, color, style = Const('MAPICON_LOCAL')):
    return pysamp.SetPlayerMapIcon(playerid, iconid, x, y, z, markertype, color, style)

def RemovePlayerMapIcon(playerid, iconid):
    return pysamp.RemovePlayerMapIcon(playerid, iconid)

def AllowPlayerTeleport(playerid, allow):
    return pysamp.AllowPlayerTeleport(playerid, allow)

def SetPlayerCameraPos(playerid, x, y, z):
    return pysamp.SetPlayerCameraPos(playerid, x, y, z)

def SetPlayerCameraLookAt(playerid, x, y, z, cut = Const('CAMERA_CUT')):
    return pysamp.SetPlayerCameraLookAt(playerid, x, y, z, cut)

def SetCameraBehindPlayer(playerid):
    return pysamp.SetCameraBehindPlayer(playerid)

def GetPlayerCameraPos(playerid):
    (x, y, z) = pysamp.GetPlayerCameraPos(playerid)
    return (x, y, z)

def GetPlayerCameraFrontVector(playerid):
    (x, y, z) = pysamp.GetPlayerCameraFrontVector(playerid)
    return (x, y, z)

def GetPlayerCameraMode(playerid):
    return pysamp.GetPlayerCameraMode(playerid)

def EnablePlayerCameraTarget(playerid, enable):
    return pysamp.EnablePlayerCameraTarget(playerid, enable)

def GetPlayerCameraTargetObject(playerid):
    return pysamp.GetPlayerCameraTargetObject(playerid)

def GetPlayerCameraTargetVehicle(playerid):
    return pysamp.GetPlayerCameraTargetVehicle(playerid)

def GetPlayerCameraTargetPlayer(playerid):
    return pysamp.GetPlayerCameraTargetPlayer(playerid)

def GetPlayerCameraTargetActor(playerid):
    return pysamp.GetPlayerCameraTargetActor(playerid)

def GetPlayerCameraAspectRatio(playerid):
    return pysamp.GetPlayerCameraAspectRatio(playerid)

def GetPlayerCameraZoom(playerid):
    return pysamp.GetPlayerCameraZoom(playerid)

def AttachCameraToObject(playerid, objectid):
    return pysamp.AttachCameraToObject(playerid, objectid)

def AttachCameraToPlayerObject(playerid, playerobjectid):
    return pysamp.AttachCameraToPlayerObject(playerid, playerobjectid)

def InterpolateCameraPos(playerid, FromX, FromY, FromZ, ToX, ToY, ToZ, time, cut = Const('CAMERA_CUT')):
    return pysamp.InterpolateCameraPos(playerid, FromX, FromY, FromZ, ToX, ToY, ToZ, time, cut)

def InterpolateCameraLookAt(playerid, FromX, FromY, FromZ, ToX, ToY, ToZ, time, cut = Const('CAMERA_CUT')):
    return pysamp.InterpolateCameraLookAt(playerid, FromX, FromY, FromZ, ToX, ToY, ToZ, time, cut)

def IsPlayerConnected(playerid):
    return pysamp.IsPlayerConnected(playerid)

def IsPlayerInVehicle(playerid, vehicleid):
    return pysamp.IsPlayerInVehicle(playerid, vehicleid)

def IsPlayerInAnyVehicle(playerid):
    return pysamp.IsPlayerInAnyVehicle(playerid)

def IsPlayerInCheckpoint(playerid):
    return pysamp.IsPlayerInCheckpoint(playerid)

def IsPlayerInRaceCheckpoint(playerid):
    return pysamp.IsPlayerInRaceCheckpoint(playerid)

def SetPlayerVirtualWorld(playerid, worldid):
    return pysamp.SetPlayerVirtualWorld(playerid, worldid)

def GetPlayerVirtualWorld(playerid):
    return pysamp.GetPlayerVirtualWorld(playerid)

def EnableStuntBonusForPlayer(playerid, enable):
    return pysamp.EnableStuntBonusForPlayer(playerid, enable)

def EnableStuntBonusForAll(enable):
    return pysamp.EnableStuntBonusForAll(enable)

def TogglePlayerSpectating(playerid, toggle):
    return pysamp.TogglePlayerSpectating(playerid, toggle)

def PlayerSpectatePlayer(playerid, targetplayerid, mode = Const('SPECTATE_MODE_NORMAL')):
    return pysamp.PlayerSpectatePlayer(playerid, targetplayerid, mode)

def PlayerSpectateVehicle(playerid, targetvehicleid, mode = Const('SPECTATE_MODE_NORMAL')):
    return pysamp.PlayerSpectateVehicle(playerid, targetvehicleid, mode)

def StartRecordingPlayerData(playerid, recordtype, recordname):
    return pysamp.StartRecordingPlayerData(playerid, recordtype, encode(recordname))

def StopRecordingPlayerData(playerid):
    return pysamp.StopRecordingPlayerData(playerid)

def CreateExplosionForPlayer(playerid, X, Y, Z, type, Radius):
    return pysamp.CreateExplosionForPlayer(playerid, X, Y, Z, type, Radius)

def CreateObject(modelid, x, y, z, rX, rY, rZ, DrawDistance = 0.0):
    return pysamp.CreateObject(modelid, x, y, z, rX, rY, rZ, DrawDistance)

def AttachObjectToVehicle(objectid, vehicleid, fOffsetX, fOffsetY, fOffsetZ, fRotX, fRotY, fRotZ):
    return pysamp.AttachObjectToVehicle(objectid, vehicleid, fOffsetX, fOffsetY, fOffsetZ, fRotX, fRotY, fRotZ)

def AttachObjectToObject(objectid, attachtoid, fOffsetX, fOffsetY, fOffsetZ, fRotX, fRotY, fRotZ, SyncRotation = False):
    return pysamp.AttachObjectToObject(objectid, attachtoid, fOffsetX, fOffsetY, fOffsetZ, fRotX, fRotY, fRotZ, SyncRotation)

def AttachObjectToPlayer(objectid, playerid, fOffsetX, fOffsetY, fOffsetZ, fRotX, fRotY, fRotZ):
    return pysamp.AttachObjectToPlayer(objectid, playerid, fOffsetX, fOffsetY, fOffsetZ, fRotX, fRotY, fRotZ)

def SetObjectPos(objectid, x, y, z):
    return pysamp.SetObjectPos(objectid, x, y, z)

def GetObjectPos(objectid):
    (x, y, z) = pysamp.GetObjectPos(objectid)
    return (x, y, z)

def SetObjectRot(objectid, rotX, rotY, rotZ):
    return pysamp.SetObjectRot(objectid, rotX, rotY, rotZ)

def GetObjectRot(objectid):
    (rotX, rotY, rotZ) = pysamp.GetObjectRot(objectid)
    return (rotX, rotY, rotZ)

def GetObjectModel(objectid):
    return pysamp.GetObjectModel(objectid)

def SetObjectNoCameraCol(objectid):
    return pysamp.SetObjectNoCameraCol(objectid)

def IsValidObject(objectid):
    return pysamp.IsValidObject(objectid)

def DestroyObject(objectid):
    return pysamp.DestroyObject(objectid)

def MoveObject(objectid, X, Y, Z, Speed, RotX = -1000.0, RotY = -1000.0, RotZ = -1000.0):
    return pysamp.MoveObject(objectid, X, Y, Z, Speed, RotX, RotY, RotZ)

def StopObject(objectid):
    return pysamp.StopObject(objectid)

def IsObjectMoving(objectid):
    return pysamp.IsObjectMoving(objectid)

def EditObject(playerid, objectid):
    return pysamp.EditObject(playerid, objectid)

def EditPlayerObject(playerid, objectid):
    return pysamp.EditPlayerObject(playerid, objectid)

def SelectObject(playerid):
    return pysamp.SelectObject(playerid)

def CancelEdit(playerid):
    return pysamp.CancelEdit(playerid)

def CreatePlayerObject(playerid, modelid, x, y, z, rX, rY, rZ, DrawDistance = 0.0):
    return pysamp.CreatePlayerObject(playerid, modelid, x, y, z, rX, rY, rZ, DrawDistance)

def AttachPlayerObjectToPlayer(objectplayer, objectid, attachplayer, OffsetX, OffsetY, OffsetZ, rX, rY, rZ):
    return pysamp.AttachPlayerObjectToPlayer(objectplayer, objectid, attachplayer, OffsetX, OffsetY, OffsetZ, rX, rY, rZ)

def AttachPlayerObjectToVehicle(playerid, objectid, vehicleid, fOffsetX, fOffsetY, fOffsetZ, fRotX, fRotY, RotZ):
    return pysamp.AttachPlayerObjectToVehicle(playerid, objectid, vehicleid, fOffsetX, fOffsetY, fOffsetZ, fRotX, fRotY, RotZ)

def SetPlayerObjectPos(playerid, objectid, x, y, z):
    return pysamp.SetPlayerObjectPos(playerid, objectid, x, y, z)

def GetPlayerObjectPos(playerid, objectid):
    (x, y, z) = pysamp.GetPlayerObjectPos(playerid, objectid)
    return (x, y, z)

def SetPlayerObjectRot(playerid, objectid, rotX, rotY, rotZ):
    return pysamp.SetPlayerObjectRot(playerid, objectid, rotX, rotY, rotZ)

def GetPlayerObjectRot(playerid, objectid):
    (rotX, rotY, rotZ) = pysamp.GetPlayerObjectRot(playerid, objectid)
    return (rotX, rotY, rotZ)

def GetPlayerObjectModel(playerid, objectid):
    return pysamp.GetPlayerObjectModel(playerid, objectid)

def SetPlayerObjectNoCameraCol(playerid, objectid):
    return pysamp.SetPlayerObjectNoCameraCol(playerid, objectid)

def IsValidPlayerObject(playerid, objectid):
    return pysamp.IsValidPlayerObject(playerid, objectid)

def DestroyPlayerObject(playerid, objectid):
    return pysamp.DestroyPlayerObject(playerid, objectid)

def MovePlayerObject(playerid, objectid, x, y, z, Speed, RotX = -1000.0, RotY = -1000.0, RotZ = -1000.0):
    return pysamp.MovePlayerObject(playerid, objectid, x, y, z, Speed, RotX, RotY, RotZ)

def StopPlayerObject(playerid, objectid):
    return pysamp.StopPlayerObject(playerid, objectid)

def IsPlayerObjectMoving(playerid, objectid):
    return pysamp.IsPlayerObjectMoving(playerid, objectid)

def SetObjectMaterial(objectid, materialindex, modelid, txdname, texturename, materialcolor = 0):
    return pysamp.SetObjectMaterial(objectid, materialindex, modelid, encode(txdname), encode(texturename), materialcolor)

def SetPlayerObjectMaterial(playerid, objectid, materialindex, modelid, txdname, texturename, materialcolor = 0):
    return pysamp.SetPlayerObjectMaterial(playerid, objectid, materialindex, modelid, encode(txdname), encode(texturename), materialcolor)

def SetObjectMaterialText(objectid, text, materialindex = 0, materialsize = Const('OBJECT_MATERIAL_SIZE_256x128'), fontface = "Arial", fontsize = 24, bold = True, fontcolor = 0xFFFFFFFF, backcolor = 0, textalignment = 0):
    return pysamp.SetObjectMaterialText(objectid, encode(text), materialindex, materialsize, encode(fontface), fontsize, bold, fontcolor, backcolor, textalignment)

def SetPlayerObjectMaterialText(playerid, objectid, text, materialindex = 0, materialsize = Const('OBJECT_MATERIAL_SIZE_256x128'), fontface = "Arial", fontsize = 24, bold = True, fontcolor = 0xFFFFFFFF, backcolor = 0, textalignment = 0):
    return pysamp.SetPlayerObjectMaterialText(playerid, objectid, encode(text), materialindex, materialsize, encode(fontface), fontsize, bold, fontcolor, backcolor, textalignment)

def SetObjectsDefaultCameraCol(disable):
    return pysamp.SetObjectsDefaultCameraCol(disable)

def SendClientMessage(playerid, color, message):
    return pysamp.SendClientMessage(playerid, color, encode(message))

def SendClientMessageToAll(color, message):
    return pysamp.SendClientMessageToAll(color, encode(message))

def SendPlayerMessageToPlayer(playerid, senderid, message):
    return pysamp.SendPlayerMessageToPlayer(playerid, senderid, encode(message))

def SendPlayerMessageToAll(senderid, message):
    return pysamp.SendPlayerMessageToAll(senderid, encode(message))

def SendDeathMessage(killer, killee, weapon):
    return pysamp.SendDeathMessage(killer, killee, weapon)

def SendDeathMessageToPlayer(playerid, killer, killee, weapon):
    return pysamp.SendDeathMessageToPlayer(playerid, killer, killee, weapon)

def GameTextForAll(text, time, style):
    return pysamp.GameTextForAll(encode(text), time, style)

def GameTextForPlayer(playerid, text, time, style):
    return pysamp.GameTextForPlayer(playerid, encode(text), time, style)

def GetTickCount():
    return pysamp.GetTickCount()

def GetMaxPlayers():
    return pysamp.GetMaxPlayers()

def VectorSize(x, y, z):
    return pysamp.VectorSize(x, y, z)

def GetPlayerPoolSize():
    return pysamp.GetPlayerPoolSize()

def GetVehiclePoolSize():
    return pysamp.GetVehiclePoolSize()

def GetActorPoolSize():
    return pysamp.GetActorPoolSize()

def SetSVarInt(varname, int_value):
    return pysamp.SetSVarInt(encode(varname), int_value)

def GetSVarInt(varname):
    return pysamp.GetSVarInt(encode(varname))

def SetSVarString(varname, string_value):
    return pysamp.SetSVarString(encode(varname), encode(string_value))

def GetSVarString(varname, len):
    return decode(pysamp.GetSVarString(encode(varname), len))

def SetSVarFloat(varname, float_value):
    return pysamp.SetSVarFloat(encode(varname), float_value)

def GetSVarFloat(varname):
    return pysamp.GetSVarFloat(encode(varname))

def DeleteSVar(varname):
    return pysamp.DeleteSVar(encode(varname))

def GetSVarsUpperIndex():
    return pysamp.GetSVarsUpperIndex()

def GetSVarNameAtIndex(index, ret_len):
    return decode(pysamp.GetSVarNameAtIndex(index, ret_len))

def GetSVarType(varname):
    return pysamp.GetSVarType(encode(varname))

def SetGameModeText(text):
    return pysamp.SetGameModeText(encode(text))

def SetTeamCount(count):
    return pysamp.SetTeamCount(count)

def AddPlayerClass(modelid, spawn_x, spawn_y, spawn_z, z_angle, weapon1, weapon1_ammo, weapon2, weapon2_ammo, weapon3, weapon3_ammo):
    return pysamp.AddPlayerClass(modelid, spawn_x, spawn_y, spawn_z, z_angle, weapon1, weapon1_ammo, weapon2, weapon2_ammo, weapon3, weapon3_ammo)

def AddPlayerClassEx(teamid, modelid, spawn_x, spawn_y, spawn_z, z_angle, weapon1, weapon1_ammo, weapon2, weapon2_ammo, weapon3, weapon3_ammo):
    return pysamp.AddPlayerClassEx(teamid, modelid, spawn_x, spawn_y, spawn_z, z_angle, weapon1, weapon1_ammo, weapon2, weapon2_ammo, weapon3, weapon3_ammo)

def AddStaticVehicle(modelid, spawn_x, spawn_y, spawn_z, z_angle, color1, color2):
    return pysamp.AddStaticVehicle(modelid, spawn_x, spawn_y, spawn_z, z_angle, color1, color2)

def AddStaticVehicleEx(modelid, spawn_x, spawn_y, spawn_z, z_angle, color1, color2, respawn_delay, addsiren = False):
    return pysamp.AddStaticVehicleEx(modelid, spawn_x, spawn_y, spawn_z, z_angle, color1, color2, respawn_delay, addsiren)

def AddStaticPickup(model, type, x, y, z, virtualworld = 0):
    return pysamp.AddStaticPickup(model, type, x, y, z, virtualworld)

def CreatePickup(model, type, x, y, z, virtualworld = 0):
    return pysamp.CreatePickup(model, type, x, y, z, virtualworld)

def DestroyPickup(pickup):
    return pysamp.DestroyPickup(pickup)

def ShowNameTags(show):
    return pysamp.ShowNameTags(show)

def ShowPlayerMarkers(mode):
    return pysamp.ShowPlayerMarkers(mode)

def GameModeExit():
    return pysamp.GameModeExit()

def SetWorldTime(hour):
    return pysamp.SetWorldTime(hour)

def GetWeaponName(weaponid, size):
    return decode(pysamp.GetWeaponName(weaponid, size))

def EnableTirePopping(enable):
    return pysamp.EnableTirePopping(enable)

def EnableVehicleFriendlyFire():
    return pysamp.EnableVehicleFriendlyFire()

def AllowInteriorWeapons(allow):
    return pysamp.AllowInteriorWeapons(allow)

def SetWeather(weatherid):
    return pysamp.SetWeather(weatherid)

def SetGravity(gravity):
    return pysamp.SetGravity(gravity)

def GetGravity():
    return pysamp.GetGravity()

def AllowAdminTeleport(allow):
    return pysamp.AllowAdminTeleport(allow)

def SetDeathDropAmount(amount):
    return pysamp.SetDeathDropAmount(amount)

def CreateExplosion(x, y, z, type, radius):
    return pysamp.CreateExplosion(x, y, z, type, radius)

def EnableZoneNames(enable):
    return pysamp.EnableZoneNames(enable)

def UsePlayerPedAnims():
    return pysamp.UsePlayerPedAnims()

def DisableInteriorEnterExits():
    return pysamp.DisableInteriorEnterExits()

def SetNameTagDrawDistance(distance):
    return pysamp.SetNameTagDrawDistance(distance)

def DisableNameTagLOS():
    return pysamp.DisableNameTagLOS()

def LimitGlobalChatRadius(chat_radius):
    return pysamp.LimitGlobalChatRadius(chat_radius)

def LimitPlayerMarkerRadius(marker_radius):
    return pysamp.LimitPlayerMarkerRadius(marker_radius)

def ConnectNPC(name, script):
    return pysamp.ConnectNPC(encode(name), encode(script))

def IsPlayerNPC(playerid):
    return pysamp.IsPlayerNPC(playerid)

def IsPlayerAdmin(playerid):
    return pysamp.IsPlayerAdmin(playerid)

def Kick(playerid):
    return pysamp.Kick(playerid)

def Ban(playerid):
    return pysamp.Ban(playerid)

def BanEx(playerid, reason):
    return pysamp.BanEx(playerid, encode(reason))

def SendRconCommand(command):
    return pysamp.SendRconCommand(encode(command))

def GetPlayerNetworkStats(playerid, size):
    return decode(pysamp.GetPlayerNetworkStats(playerid, size))

def GetNetworkStats(size):
    return decode(pysamp.GetNetworkStats(size))

def GetPlayerVersion(playerid, len):
    return decode(pysamp.GetPlayerVersion(playerid, len))

def BlockIpAddress(ip_address, timems):
    return pysamp.BlockIpAddress(encode(ip_address), timems)

def UnBlockIpAddress(ip_address):
    return pysamp.UnBlockIpAddress(encode(ip_address))

def GetServerVarAsString(varname, size):
    return decode(pysamp.GetServerVarAsString(encode(varname), size))

def GetServerVarAsInt(varname):
    return pysamp.GetServerVarAsInt(encode(varname))

def GetServerVarAsBool(varname):
    return pysamp.GetServerVarAsBool(encode(varname))

def GetConsoleVarAsString(varname, len):
    return decode(pysamp.GetConsoleVarAsString(encode(varname), len))

def GetConsoleVarAsInt(varname):
    return pysamp.GetConsoleVarAsInt(encode(varname))

def GetConsoleVarAsBool(varname):
    return pysamp.GetConsoleVarAsBool(encode(varname))

def GetServerTickRate():
    return pysamp.GetServerTickRate()

def NetStats_GetConnectedTime(playerid):
    return pysamp.NetStats_GetConnectedTime(playerid)

def NetStats_MessagesReceived(playerid):
    return pysamp.NetStats_MessagesReceived(playerid)

def NetStats_BytesReceived(playerid):
    return pysamp.NetStats_BytesReceived(playerid)

def NetStats_MessagesSent(playerid):
    return pysamp.NetStats_MessagesSent(playerid)

def NetStats_BytesSent(playerid):
    return pysamp.NetStats_BytesSent(playerid)

def NetStats_MessagesRecvPerSecond(playerid):
    return pysamp.NetStats_MessagesRecvPerSecond(playerid)

def NetStats_PacketLossPercent(playerid):
    return pysamp.NetStats_PacketLossPercent(playerid)

def NetStats_ConnectionStatus(playerid):
    return pysamp.NetStats_ConnectionStatus(playerid)

def NetStats_GetIpPort(playerid, ip_port_len):
    return decode(pysamp.NetStats_GetIpPort(playerid, ip_port_len))

def CreateMenu(title, columns, x, y, col1width, col2width = 0.0):
    return pysamp.CreateMenu(encode(title), columns, x, y, col1width, col2width)

def DestroyMenu(menuid):
    return pysamp.DestroyMenu(menuid)

def AddMenuItem(menuid, column, menutext):
    return pysamp.AddMenuItem(menuid, column, encode(menutext))

def SetMenuColumnHeader(menuid, column, columnheader):
    return pysamp.SetMenuColumnHeader(menuid, column, encode(columnheader))

def ShowMenuForPlayer(menuid, playerid):
    return pysamp.ShowMenuForPlayer(menuid, playerid)

def HideMenuForPlayer(menuid, playerid):
    return pysamp.HideMenuForPlayer(menuid, playerid)

def IsValidMenu(menuid):
    return pysamp.IsValidMenu(menuid)

def DisableMenu(menuid):
    return pysamp.DisableMenu(menuid)

def DisableMenuRow(menuid, row):
    return pysamp.DisableMenuRow(menuid, row)

def GetPlayerMenu(playerid):
    return pysamp.GetPlayerMenu(playerid)

def TextDrawCreate(x, y, text):
    return pysamp.TextDrawCreate(x, y, encode(text))

def TextDrawDestroy(text):
    return pysamp.TextDrawDestroy(text)

def TextDrawLetterSize(text, x, y):
    return pysamp.TextDrawLetterSize(text, x, y)

def TextDrawTextSize(text, x, y):
    return pysamp.TextDrawTextSize(text, x, y)

def TextDrawAlignment(text, alignment):
    return pysamp.TextDrawAlignment(text, alignment)

def TextDrawColor(text, color):
    return pysamp.TextDrawColor(text, color)

def TextDrawUseBox(text, use):
    return pysamp.TextDrawUseBox(text, use)

def TextDrawBoxColor(text, color):
    return pysamp.TextDrawBoxColor(text, color)

def TextDrawSetShadow(text, size):
    return pysamp.TextDrawSetShadow(text, size)

def TextDrawSetOutline(text, size):
    return pysamp.TextDrawSetOutline(text, size)

def TextDrawBackgroundColor(text, color):
    return pysamp.TextDrawBackgroundColor(text, color)

def TextDrawFont(text, font):
    return pysamp.TextDrawFont(text, font)

def TextDrawSetProportional(text, set):
    return pysamp.TextDrawSetProportional(text, set)

def TextDrawSetSelectable(text, set):
    return pysamp.TextDrawSetSelectable(text, set)

def TextDrawShowForPlayer(playerid, text):
    return pysamp.TextDrawShowForPlayer(playerid, text)

def TextDrawHideForPlayer(playerid, text):
    return pysamp.TextDrawHideForPlayer(playerid, text)

def TextDrawShowForAll(text):
    return pysamp.TextDrawShowForAll(text)

def TextDrawHideForAll(text):
    return pysamp.TextDrawHideForAll(text)

def TextDrawSetString(text, string):
    return pysamp.TextDrawSetString(text, encode(string))

def TextDrawSetPreviewModel(text, modelindex):
    return pysamp.TextDrawSetPreviewModel(text, modelindex)

def TextDrawSetPreviewRot(text, fRotX, fRotY, fRotZ, fZoom = 1.0):
    return pysamp.TextDrawSetPreviewRot(text, fRotX, fRotY, fRotZ, fZoom)

def TextDrawSetPreviewVehCol(text, color1, color2):
    return pysamp.TextDrawSetPreviewVehCol(text, color1, color2)

def SelectTextDraw(playerid, hovercolor):
    return pysamp.SelectTextDraw(playerid, hovercolor)

def CancelSelectTextDraw(playerid):
    return pysamp.CancelSelectTextDraw(playerid)

def GangZoneCreate(minx, miny, maxx, maxy):
    return pysamp.GangZoneCreate(minx, miny, maxx, maxy)

def GangZoneDestroy(zone):
    return pysamp.GangZoneDestroy(zone)

def GangZoneShowForPlayer(playerid, zone, color):
    return pysamp.GangZoneShowForPlayer(playerid, zone, color)

def GangZoneShowForAll(zone, color):
    return pysamp.GangZoneShowForAll(zone, color)

def GangZoneHideForPlayer(playerid, zone):
    return pysamp.GangZoneHideForPlayer(playerid, zone)

def GangZoneHideForAll(zone):
    return pysamp.GangZoneHideForAll(zone)

def GangZoneFlashForPlayer(playerid, zone, flashcolor):
    return pysamp.GangZoneFlashForPlayer(playerid, zone, flashcolor)

def GangZoneFlashForAll(zone, flashcolor):
    return pysamp.GangZoneFlashForAll(zone, flashcolor)

def GangZoneStopFlashForPlayer(playerid, zone):
    return pysamp.GangZoneStopFlashForPlayer(playerid, zone)

def GangZoneStopFlashForAll(zone):
    return pysamp.GangZoneStopFlashForAll(zone)

def ShowPlayerDialog(playerid, dialogid, style, caption, info, button1, button2):
    return pysamp.ShowPlayerDialog(playerid, dialogid, style, encode(caption), encode(info), encode(button1), encode(button2))

def gpci(playerid, size):
    return decode(pysamp.gpci(playerid, size))

def AddCharModel(baseid, newid, dffname, txdname):
    return pysamp.AddCharModel(baseid, newid, encode(dffname), encode(txdname))

def AddSimpleModel(virtualworld, baseid, newid, dffname, txdname):
    return pysamp.AddSimpleModel(virtualworld, baseid, newid, encode(dffname), encode(txdname))

def AddSimpleModelTimed(virtualworld, baseid, newid, dffname, txdname, timeon, timeoff):
    return pysamp.AddSimpleModelTimed(virtualworld, baseid, newid, encode(dffname), encode(txdname), timeon, timeoff)

def FindModelFileNameFromCRC(crc, model_str_len):
    return decode(pysamp.FindModelFileNameFromCRC(crc, model_str_len))

def FindTextureFileNameFromCRC(crc, texture_str_len):
    return decode(pysamp.FindTextureFileNameFromCRC(crc, texture_str_len))

def RedirectDownload(playerid, url):
    return pysamp.RedirectDownload(playerid, encode(url))

def IsValidVehicle(vehicleid):
    return pysamp.IsValidVehicle(vehicleid)

def GetVehicleDistanceFromPoint(vehicleid, x, y, z):
    return pysamp.GetVehicleDistanceFromPoint(vehicleid, x, y, z)

def CreateVehicle(vehicletype, x, y, z, rotation, color1, color2, respawn_delay, addsiren = False):
    return pysamp.CreateVehicle(vehicletype, x, y, z, rotation, color1, color2, respawn_delay, addsiren)

def DestroyVehicle(vehicleid):
    return pysamp.DestroyVehicle(vehicleid)

def IsVehicleStreamedIn(vehicleid, forplayerid):
    return pysamp.IsVehicleStreamedIn(vehicleid, forplayerid)

def GetVehiclePos(vehicleid):
    (x, y, z) = pysamp.GetVehiclePos(vehicleid)
    return (x, y, z)

def SetVehiclePos(vehicleid, x, y, z):
    return pysamp.SetVehiclePos(vehicleid, x, y, z)

def GetVehicleZAngle(vehicleid):
    return pysamp.GetVehicleZAngle(vehicleid)

def GetVehicleRotationQuat(vehicleid):
    (w, x, y, z) = pysamp.GetVehicleRotationQuat(vehicleid)
    return (w, x, y, z)

def SetVehicleZAngle(vehicleid, z_angle):
    return pysamp.SetVehicleZAngle(vehicleid, z_angle)

def SetVehicleParamsForPlayer(vehicleid, playerid, objective, doorslocked):
    return pysamp.SetVehicleParamsForPlayer(vehicleid, playerid, objective, doorslocked)

def ManualVehicleEngineAndLights():
    return pysamp.ManualVehicleEngineAndLights()

def SetVehicleParamsEx(vehicleid, engine, lights, alarm, doors, bonnet, boot, objective):
    return pysamp.SetVehicleParamsEx(vehicleid, engine, lights, alarm, doors, bonnet, boot, objective)

def GetVehicleParamsEx(vehicleid):
    (engine, lights, alarm, doors, bonnet, boot, objective) = pysamp.GetVehicleParamsEx(vehicleid)
    return (engine, lights, alarm, doors, bonnet, boot, objective)

def GetVehicleParamsSirenState(vehicleid):
    return pysamp.GetVehicleParamsSirenState(vehicleid)

def SetVehicleParamsCarDoors(vehicleid, driver, passenger, backleft, backright):
    return pysamp.SetVehicleParamsCarDoors(vehicleid, driver, passenger, backleft, backright)

def GetVehicleParamsCarDoors(vehicleid):
    (driver, passenger, backleft, backright) = pysamp.GetVehicleParamsCarDoors(vehicleid)
    return (driver, passenger, backleft, backright)

def SetVehicleParamsCarWindows(vehicleid, driver, passenger, backleft, backright):
    return pysamp.SetVehicleParamsCarWindows(vehicleid, driver, passenger, backleft, backright)

def GetVehicleParamsCarWindows(vehicleid):
    (driver, passenger, backleft, backright) = pysamp.GetVehicleParamsCarWindows(vehicleid)
    return (driver, passenger, backleft, backright)

def SetVehicleToRespawn(vehicleid):
    return pysamp.SetVehicleToRespawn(vehicleid)

def LinkVehicleToInterior(vehicleid, interiorid):
    return pysamp.LinkVehicleToInterior(vehicleid, interiorid)

def AddVehicleComponent(vehicleid, componentid):
    return pysamp.AddVehicleComponent(vehicleid, componentid)

def RemoveVehicleComponent(vehicleid, componentid):
    return pysamp.RemoveVehicleComponent(vehicleid, componentid)

def ChangeVehicleColor(vehicleid, color1, color2):
    return pysamp.ChangeVehicleColor(vehicleid, color1, color2)

def ChangeVehiclePaintjob(vehicleid, paintjobid):
    return pysamp.ChangeVehiclePaintjob(vehicleid, paintjobid)

def SetVehicleHealth(vehicleid, health):
    return pysamp.SetVehicleHealth(vehicleid, health)

def GetVehicleHealth(vehicleid):
    return pysamp.GetVehicleHealth(vehicleid)

def AttachTrailerToVehicle(trailerid, vehicleid):
    return pysamp.AttachTrailerToVehicle(trailerid, vehicleid)

def DetachTrailerFromVehicle(vehicleid):
    return pysamp.DetachTrailerFromVehicle(vehicleid)

def IsTrailerAttachedToVehicle(vehicleid):
    return pysamp.IsTrailerAttachedToVehicle(vehicleid)

def GetVehicleTrailer(vehicleid):
    return pysamp.GetVehicleTrailer(vehicleid)

def SetVehicleNumberPlate(vehicleid, numberplate):
    return pysamp.SetVehicleNumberPlate(vehicleid, encode(numberplate))

def GetVehicleModel(vehicleid):
    return pysamp.GetVehicleModel(vehicleid)

def GetVehicleComponentInSlot(vehicleid, slot):
    return pysamp.GetVehicleComponentInSlot(vehicleid, slot)

def GetVehicleComponentType(component):
    return pysamp.GetVehicleComponentType(component)

def RepairVehicle(vehicleid):
    return pysamp.RepairVehicle(vehicleid)

def GetVehicleVelocity(vehicleid):
    (X, Y, Z) = pysamp.GetVehicleVelocity(vehicleid)
    return (X, Y, Z)

def SetVehicleVelocity(vehicleid, X, Y, Z):
    return pysamp.SetVehicleVelocity(vehicleid, X, Y, Z)

def SetVehicleAngularVelocity(vehicleid, X, Y, Z):
    return pysamp.SetVehicleAngularVelocity(vehicleid, X, Y, Z)

def GetVehicleDamageStatus(vehicleid):
    (panels, doors, lights, tires) = pysamp.GetVehicleDamageStatus(vehicleid)
    return (panels, doors, lights, tires)

def UpdateVehicleDamageStatus(vehicleid, panels, doors, lights, tires):
    return pysamp.UpdateVehicleDamageStatus(vehicleid, panels, doors, lights, tires)

def SetVehicleVirtualWorld(vehicleid, worldid):
    return pysamp.SetVehicleVirtualWorld(vehicleid, worldid)

def GetVehicleVirtualWorld(vehicleid):
    return pysamp.GetVehicleVirtualWorld(vehicleid)

def GetVehicleModelInfo(model, infotype):
    (X, Y, Z) = pysamp.GetVehicleModelInfo(model, infotype)
    return (X, Y, Z)

def CreateActor(modelid, x, y, z, rotation):
    return pysamp.CreateActor(modelid, x, y, z, rotation)

def DestroyActor(actorid):
    return pysamp.DestroyActor(actorid)

def IsActorStreamedIn(actorid, forplayerid):
    return pysamp.IsActorStreamedIn(actorid, forplayerid)

def SetActorVirtualWorld(actorid, vworld):
    return pysamp.SetActorVirtualWorld(actorid, vworld)

def GetActorVirtualWorld(actorid):
    return pysamp.GetActorVirtualWorld(actorid)

def ApplyActorAnimation(actorid, animlib, animname, fDelta, loop, lockx, locky, freeze, time):
    return pysamp.ApplyActorAnimation(actorid, encode(animlib), encode(animname), fDelta, loop, lockx, locky, freeze, time)

def ClearActorAnimations(actorid):
    return pysamp.ClearActorAnimations(actorid)

def SetActorPos(actorid, x, y, z):
    return pysamp.SetActorPos(actorid, x, y, z)

def GetActorPos(actorid):
    (x, y, z) = pysamp.GetActorPos(actorid)
    return (x, y, z)

def SetActorFacingAngle(actorid, angle):
    return pysamp.SetActorFacingAngle(actorid, angle)

def GetActorFacingAngle(actorid):
    return pysamp.GetActorFacingAngle(actorid)

def SetActorHealth(actorid, health):
    return pysamp.SetActorHealth(actorid, health)

def GetActorHealth(actorid):
    return pysamp.GetActorHealth(actorid)

def SetActorInvulnerable(actorid, invulnerable = True):
    return pysamp.SetActorInvulnerable(actorid, invulnerable)

def IsActorInvulnerable(actorid):
    return pysamp.IsActorInvulnerable(actorid)

def IsValidActor(actorid):
    return pysamp.IsValidActor(actorid)

def HTTP(index, type, url, data, callback):
    return pysamp.HTTP(index, type, encode(url), encode(data), encode(callback))

