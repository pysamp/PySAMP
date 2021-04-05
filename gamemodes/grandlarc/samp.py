import pysamp
from const import *

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

def PlayAudioStreamForPlayer(playerid, url, posX=0.0, posY=0.0, posZ=0.0, distance=50.0, usepos=False):
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
    (fOriginX, fOriginY, fOriginZ, fHitPosX, fHitPosY,
     fHitPosZ) = pysamp.GetPlayerLastShotVectors(playerid)
    return (fOriginX, fOriginY, fOriginZ, fHitPosX, fHitPosY, fHitPosZ)

def SetPlayerAttachedObject(playerid, index, modelid, bone, fOffsetX=0.0, fOffsetY=0.0, fOffsetZ=0.0, fRotX=0.0, fRotY=0.0, fRotZ=0.0, fScaleX=1.0, fScaleY=1.0, fScaleZ=1.0, materialcolor1=0, materialcolor2=0):
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

def PlayerTextDrawSetPreviewRot(playerid, text, fRotX, fRotY, fRotZ, fZoom=1.0):
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

def ApplyAnimation(playerid, animlib, animname, fDelta, loop, lockx, locky, freeze, time, forcesync=False):
    return pysamp.ApplyAnimation(playerid, encode(animlib), encode(animname), fDelta, loop, lockx, locky, freeze, time, forcesync)

def ClearAnimations(playerid, forcesync=False):
    return pysamp.ClearAnimations(playerid, forcesync)

def GetPlayerAnimationIndex(playerid):
    return pysamp.GetPlayerAnimationIndex(playerid)

def GetAnimationName(index, animlib_size, animname_size):
    (animlib, animname) = pysamp.GetAnimationName(
        index, animlib_size, animname_size)
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

def SetPlayerMapIcon(playerid, iconid, x, y, z, markertype, color, style=MAPICON_LOCAL.get()):
    return pysamp.SetPlayerMapIcon(playerid, iconid, x, y, z, markertype, color, style)

def RemovePlayerMapIcon(playerid, iconid):
    return pysamp.RemovePlayerMapIcon(playerid, iconid)

def AllowPlayerTeleport(playerid, allow):
    return pysamp.AllowPlayerTeleport(playerid, allow)

def SetPlayerCameraPos(playerid, x, y, z):
    return pysamp.SetPlayerCameraPos(playerid, x, y, z)

def SetPlayerCameraLookAt(playerid, x, y, z, cut=CAMERA_CUT.get()):
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

def InterpolateCameraPos(playerid, FromX, FromY, FromZ, ToX, ToY, ToZ, time, cut=CAMERA_CUT.get()):
    return pysamp.InterpolateCameraPos(playerid, FromX, FromY, FromZ, ToX, ToY, ToZ, time, cut)

def InterpolateCameraLookAt(playerid, FromX, FromY, FromZ, ToX, ToY, ToZ, time, cut=CAMERA_CUT.get()):
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

def PlayerSpectatePlayer(playerid, targetplayerid, mode=SPECTATE_MODE_NORMAL.get()):
    return pysamp.PlayerSpectatePlayer(playerid, targetplayerid, mode)

def PlayerSpectateVehicle(playerid, targetvehicleid, mode=SPECTATE_MODE_NORMAL.get()):
    return pysamp.PlayerSpectateVehicle(playerid, targetvehicleid, mode)

def StartRecordingPlayerData(playerid, recordtype, recordname):
    return pysamp.StartRecordingPlayerData(playerid, recordtype, encode(recordname))

def StopRecordingPlayerData(playerid):
    return pysamp.StopRecordingPlayerData(playerid)

def CreateExplosionForPlayer(playerid, X, Y, Z, type, Radius):
    return pysamp.CreateExplosionForPlayer(playerid, X, Y, Z, type, Radius)

def CreateObject(modelid, x, y, z, rX, rY, rZ, DrawDistance=0.0):
    return pysamp.CreateObject(modelid, x, y, z, rX, rY, rZ, DrawDistance)

def AttachObjectToVehicle(objectid, vehicleid, fOffsetX, fOffsetY, fOffsetZ, fRotX, fRotY, fRotZ):
    return pysamp.AttachObjectToVehicle(objectid, vehicleid, fOffsetX, fOffsetY, fOffsetZ, fRotX, fRotY, fRotZ)

def AttachObjectToObject(objectid, attachtoid, fOffsetX, fOffsetY, fOffsetZ, fRotX, fRotY, fRotZ, SyncRotation=False):
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

def MoveObject(objectid, X, Y, Z, Speed, RotX=-1000.0, RotY=-1000.0, RotZ=-1000.0):
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

def CreatePlayerObject(playerid, modelid, x, y, z, rX, rY, rZ, DrawDistance=0.0):
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

def MovePlayerObject(playerid, objectid, x, y, z, Speed, RotX=-1000.0, RotY=-1000.0, RotZ=-1000.0):
    return pysamp.MovePlayerObject(playerid, objectid, x, y, z, Speed, RotX, RotY, RotZ)

def StopPlayerObject(playerid, objectid):
    return pysamp.StopPlayerObject(playerid, objectid)

def IsPlayerObjectMoving(playerid, objectid):
    return pysamp.IsPlayerObjectMoving(playerid, objectid)

def SetObjectMaterial(objectid, materialindex, modelid, txdname, texturename, materialcolor=0):
    return pysamp.SetObjectMaterial(objectid, materialindex, modelid, encode(txdname), encode(texturename), materialcolor)

def SetPlayerObjectMaterial(playerid, objectid, materialindex, modelid, txdname, texturename, materialcolor=0):
    return pysamp.SetPlayerObjectMaterial(playerid, objectid, materialindex, modelid, encode(txdname), encode(texturename), materialcolor)

def SetObjectMaterialText(objectid, text, materialindex=0, materialsize=Const('OBJECT_MATERIAL_SIZE_256x128'), fontface="Arial", fontsize=24, bold=True, fontcolor=0xFFFFFFFF, backcolor=0, textalignment=0):
    return pysamp.SetObjectMaterialText(objectid, encode(text), materialindex, materialsize, encode(fontface), fontsize, bold, fontcolor, backcolor, textalignment)

def SetPlayerObjectMaterialText(playerid, objectid, text, materialindex=0, materialsize=Const('OBJECT_MATERIAL_SIZE_256x128'), fontface="Arial", fontsize=24, bold=True, fontcolor=0xFFFFFFFF, backcolor=0, textalignment=0):
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

def AddStaticVehicleEx(modelid, spawn_x, spawn_y, spawn_z, z_angle, color1, color2, respawn_delay, addsiren=False):
    return pysamp.AddStaticVehicleEx(modelid, spawn_x, spawn_y, spawn_z, z_angle, color1, color2, respawn_delay, addsiren)

def AddStaticPickup(model, type, x, y, z, virtualworld=0):
    return pysamp.AddStaticPickup(model, type, x, y, z, virtualworld)

def CreatePickup(model, type, x, y, z, virtualworld=0):
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

def CreateMenu(title, columns, x, y, col1width, col2width=0.0):
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

def TextDrawSetPreviewRot(text, fRotX, fRotY, fRotZ, fZoom=1.0):
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

def CreateVehicle(vehicletype, x, y, z, rotation, color1, color2, respawn_delay, addsiren=False):
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
    (engine, lights, alarm, doors, bonnet, boot,
     objective) = pysamp.GetVehicleParamsEx(vehicleid)
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
    (driver, passenger, backleft,
     backright) = pysamp.GetVehicleParamsCarWindows(vehicleid)
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

def SetActorInvulnerable(actorid, invulnerable=True):
    return pysamp.SetActorInvulnerable(actorid, invulnerable)

def IsActorInvulnerable(actorid):
    return pysamp.IsActorInvulnerable(actorid)

def IsValidActor(actorid):
    return pysamp.IsValidActor(actorid)

def HTTP(index, type, url, data, callback):
    return pysamp.HTTP(index, type, encode(url), encode(data), encode(callback))

def Create3DTextLabel(text, color, x, y, z, drawDistance, virtualworld, testLOS=False):
    return pysamp.Create3DTextLabel(encode(text), color, x, y, z, drawDistance, virtualworld, testLOS)

def Delete3DTextLabel(id):
    return pysamp.Delete3DTextLabel(id)

def Attach3DTextLabelToPlayer(id, playerid, offsetX, offsetY, offsetZ):
    return pysamp.Attach3DTextLabelToPlayer(id, playerid, offsetX, offsetY, offsetZ)

def Attach3DTextLabelToVehicle(id, vehicleid, offsetX, offsetY, offsetZ):
    return pysamp.Attach3DTextLabelToVehicle(id, vehicleid, offsetX, offsetY, offsetZ)

def Update3DTextLabelText(id, color, text):
    return pysamp.Update3DTextLabelText(id, color, encode(text))

def CreatePlayer3DTextLabel(playerid, text, color, x, y, z, drawDistance, attachedplayer=INVALID_PLAYER_ID.get(), attachedvehicle=INVALID_VEHICLE_ID.get(), testLOS=False):
    return pysamp.CreatePlayer3DTextLabel(playerid, encode(text), color, x, y, z, drawDistance, attachedplayer, attachedvehicle, testLOS)

def DeletePlayer3DTextLabel(playerid, id):
    return pysamp.DeletePlayer3DTextLabel(playerid, id)

def UpdatePlayer3DTextLabelText(playerid, id, color, text):
    return pysamp.UpdatePlayer3DTextLabelText(playerid, id, color, encode(text))
########################
# SNAKE CASE WRAPPERS FOR PEP8 COMPATIBILITY
########################
def const(name):
	return Const(name)

def set_spawn_info(playerid, team, skin, x, y, z, rotation, weapon1, weapon1_ammo, weapon2, weapon2_ammo, weapon3, weapon3_ammo):
	return SetSpawnInfo(playerid, team, skin, x, y, z, rotation, weapon1, weapon1_ammo, weapon2, weapon2_ammo, weapon3, weapon3_ammo)

def spawn_player(playerid):
	return SpawnPlayer(playerid)

def set_player_pos(playerid, x, y, z):
	return SetPlayerPos(playerid, x, y, z)

def set_player_pos_find_z(playerid, x, y, z):
	return SetPlayerPosFindZ(playerid, x, y, z)

def get_player_pos(playerid):
	return GetPlayerPos(playerid)

def set_player_facing_angle(playerid, angle):
	return SetPlayerFacingAngle(playerid, angle)

def get_player_facing_angle(playerid):
	return GetPlayerFacingAngle(playerid)

def is_player_in_range_of_point(playerid, range, x, y, z):
	return IsPlayerInRangeOfPoint(playerid, range, x, y, z)

def get_player_distance_from_point(playerid, x, y, z):
	return GetPlayerDistanceFromPoint(playerid, x, y, z)

def is_player_streamed_in(playerid, forplayerid):
	return IsPlayerStreamedIn(playerid, forplayerid)

def set_player_interior(playerid, interiorid):
	return SetPlayerInterior(playerid, interiorid)

def get_player_interior(playerid):
	return GetPlayerInterior(playerid)

def set_player_health(playerid, health):
	return SetPlayerHealth(playerid, health)

def get_player_health(playerid):
	return GetPlayerHealth(playerid)

def set_player_armour(playerid, armour):
	return SetPlayerArmour(playerid, armour)

def get_player_armour(playerid):
	return GetPlayerArmour(playerid)

def set_player_ammo(playerid, weaponid, ammo):
	return SetPlayerAmmo(playerid, weaponid, ammo)

def get_player_ammo(playerid):
	return GetPlayerAmmo(playerid)

def get_player_weapon_state(playerid):
	return GetPlayerWeaponState(playerid)

def get_player_target_player(playerid):
	return GetPlayerTargetPlayer(playerid)

def get_player_target_actor(playerid):
	return GetPlayerTargetActor(playerid)

def set_player_team(playerid, teamid):
	return SetPlayerTeam(playerid, teamid)

def get_player_team(playerid):
	return GetPlayerTeam(playerid)

def set_player_score(playerid, score):
	return SetPlayerScore(playerid, score)

def get_player_score(playerid):
	return GetPlayerScore(playerid)

def get_player_drunk_level(playerid):
	return GetPlayerDrunkLevel(playerid)

def set_player_drunk_level(playerid, level):
	return SetPlayerDrunkLevel(playerid, level)

def set_player_color(playerid, color):
	return SetPlayerColor(playerid, color)

def get_player_color(playerid):
	return GetPlayerColor(playerid)

def set_player_skin(playerid, skinid):
	return SetPlayerSkin(playerid, skinid)

def get_player_skin(playerid):
	return GetPlayerSkin(playerid)

def give_player_weapon(playerid, weaponid, ammo):
	return GivePlayerWeapon(playerid, weaponid, ammo)

def reset_player_weapons(playerid):
	return ResetPlayerWeapons(playerid)

def set_player_armed_weapon(playerid, weaponid):
	return SetPlayerArmedWeapon(playerid, weaponid)

def get_player_weapon_data(playerid, slot):
	return GetPlayerWeaponData(playerid, slot)

def give_player_money(playerid, money):
	return GivePlayerMoney(playerid, money)

def reset_player_money(playerid):
	return ResetPlayerMoney(playerid)

def set_player_name(playerid, name):
	return SetPlayerName(playerid, name)

def get_player_money(playerid):
	return GetPlayerMoney(playerid)

def get_player_state(playerid):
	return GetPlayerState(playerid)

def get_player_ip(playerid, size):
	return GetPlayerIp(playerid, size)

def get_player_ping(playerid):
	return GetPlayerPing(playerid)

def get_player_weapon(playerid):
	return GetPlayerWeapon(playerid)

def get_player_keys(playerid):
	return GetPlayerKeys(playerid)

def get_player_name(playerid, size):
	return GetPlayerName(playerid, size)

def set_player_time(playerid, hour, minute):
	return SetPlayerTime(playerid, hour, minute)

def get_player_time(playerid):
	return GetPlayerTime(playerid)

def toggle_player_clock(playerid, toggle):
	return TogglePlayerClock(playerid, toggle)

def set_player_weather(playerid, weather):
	return SetPlayerWeather(playerid, weather)

def force_class_selection(playerid):
	return ForceClassSelection(playerid)

def set_player_wanted_level(playerid, level):
	return SetPlayerWantedLevel(playerid, level)

def get_player_wanted_level(playerid):
	return GetPlayerWantedLevel(playerid)

def set_player_fighting_style(playerid, style):
	return SetPlayerFightingStyle(playerid, style)

def get_player_fighting_style(playerid):
	return GetPlayerFightingStyle(playerid)

def set_player_velocity(playerid, x, y, z):
	return SetPlayerVelocity(playerid, x, y, z)

def get_player_velocity(playerid):
	return GetPlayerVelocity(playerid)

def play_crime_report_for_player(playerid, suspectid, crime):
	return PlayCrimeReportForPlayer(playerid, suspectid, crime)

def play_audio_stream_for_player(playerid, url, posX=0.0, posY=0.0, posZ=0.0, distance=50.0, usepos=False):
	return PlayAudioStreamForPlayer(playerid, url, posX, posY, posZ, distance, usepos)

def stop_audio_stream_for_player(playerid):
	return StopAudioStreamForPlayer(playerid)

def set_player_shop_name(playerid, shopname):
	return SetPlayerShopName(playerid, shopname)

def set_player_skill_level(playerid, skill, level):
	return SetPlayerSkillLevel(playerid, skill, level)

def get_player_surfing_vehicle_id(playerid):
	return GetPlayerSurfingVehicleID(playerid)

def get_player_surfing_object_id(playerid):
	return GetPlayerSurfingObjectID(playerid)

def remove_building_for_player(playerid, modelid, fX, fY, fZ, fRadius):
	return RemoveBuildingForPlayer(playerid, modelid, fX, fY, fZ, fRadius)

def get_player_last_shot_vectors(playerid):
	return GetPlayerLastShotVectors(playerid)

def set_player_attached_object(playerid, index, modelid, bone, fOffsetX=0.0, fOffsetY=0.0, fOffsetZ=0.0, fRotX=0.0, fRotY=0.0, fRotZ=0.0, fScaleX=1.0, fScaleY=1.0, fScaleZ=1.0, materialcolor1=0, materialcolor2=0):
	return SetPlayerAttachedObject(playerid, index, modelid, bone, fOffsetX, fOffsetY, fOffsetZ, fRotX, fRotY, fRotZ, fScaleX, fScaleY, fScaleZ, materialcolor1, materialcolor2)

def remove_player_attached_object(playerid, index):
	return RemovePlayerAttachedObject(playerid, index)

def is_player_attached_object_slot_used(playerid, index):
	return IsPlayerAttachedObjectSlotUsed(playerid, index)

def edit_attached_object(playerid, index):
	return EditAttachedObject(playerid, index)

def create_player_text_draw(playerid, x, y, text):
	return CreatePlayerTextDraw(playerid, x, y, text)

def player_text_draw_destroy(playerid, text):
	return PlayerTextDrawDestroy(playerid, text)

def player_text_draw_letter_size(playerid, text, x, y):
	return PlayerTextDrawLetterSize(playerid, text, x, y)

def player_text_draw_text_size(playerid, text, x, y):
	return PlayerTextDrawTextSize(playerid, text, x, y)

def player_text_draw_alignment(playerid, text, alignment):
	return PlayerTextDrawAlignment(playerid, text, alignment)

def player_text_draw_color(playerid, text, color):
	return PlayerTextDrawColor(playerid, text, color)

def player_text_draw_use_box(playerid, text, use):
	return PlayerTextDrawUseBox(playerid, text, use)

def player_text_draw_box_color(playerid, text, color):
	return PlayerTextDrawBoxColor(playerid, text, color)

def player_text_draw_set_shadow(playerid, text, size):
	return PlayerTextDrawSetShadow(playerid, text, size)

def player_text_draw_set_outline(playerid, text, size):
	return PlayerTextDrawSetOutline(playerid, text, size)

def player_text_draw_background_color(playerid, text, color):
	return PlayerTextDrawBackgroundColor(playerid, text, color)

def player_text_draw_font(playerid, text, font):
	return PlayerTextDrawFont(playerid, text, font)

def player_text_draw_set_proportional(playerid, text, set):
	return PlayerTextDrawSetProportional(playerid, text, set)

def player_text_draw_set_selectable(playerid, text, set):
	return PlayerTextDrawSetSelectable(playerid, text, set)

def player_text_draw_show(playerid, text):
	return PlayerTextDrawShow(playerid, text)

def player_text_draw_hide(playerid, text):
	return PlayerTextDrawHide(playerid, text)

def player_text_draw_set_string(playerid, text, string):
	return PlayerTextDrawSetString(playerid, text, string)

def player_text_draw_set_preview_model(playerid, text, modelindex):
	return PlayerTextDrawSetPreviewModel(playerid, text, modelindex)

def player_text_draw_set_preview_rot(playerid, text, fRotX, fRotY, fRotZ, fZoom=1.0):
	return PlayerTextDrawSetPreviewRot(playerid, text, fRotX, fRotY, fRotZ, fZoom)

def player_text_draw_set_preview_veh_col(playerid, text, color1, color2):
	return PlayerTextDrawSetPreviewVehCol(playerid, text, color1, color2)

def set_pvar_int(playerid, varname, value):
	return SetPVarInt(playerid, varname, value)

def get_pvar_int(playerid, varname):
	return GetPVarInt(playerid, varname)

def set_pvar_string(playerid, varname, value):
	return SetPVarString(playerid, varname, value)

def get_pvar_string(playerid, varname, size):
	return GetPVarString(playerid, varname, size)

def set_pvar_float(playerid, varname, value):
	return SetPVarFloat(playerid, varname, value)

def get_pvar_float(playerid, varname):
	return GetPVarFloat(playerid, varname)

def delete_pvar(playerid, varname):
	return DeletePVar(playerid, varname)

def get_pvars_upper_index(playerid):
	return GetPVarsUpperIndex(playerid)

def get_pvar_name_at_index(playerid, index, size):
	return GetPVarNameAtIndex(playerid, index, size)

def get_pvar_type(playerid, varname):
	return GetPVarType(playerid, varname)

def set_player_chat_bubble(playerid, text, color, drawdistance, expiretime):
	return SetPlayerChatBubble(playerid, text, color, drawdistance, expiretime)

def put_player_in_vehicle(playerid, vehicleid, seatid):
	return PutPlayerInVehicle(playerid, vehicleid, seatid)

def get_player_vehicle_id(playerid):
	return GetPlayerVehicleID(playerid)

def get_player_vehicle_seat(playerid):
	return GetPlayerVehicleSeat(playerid)

def remove_player_from_vehicle(playerid):
	return RemovePlayerFromVehicle(playerid)

def toggle_player_controllable(playerid, toggle):
	return TogglePlayerControllable(playerid, toggle)

def player_play_sound(playerid, soundid, x, y, z):
	return PlayerPlaySound(playerid, soundid, x, y, z)

def apply_animation(playerid, animlib, animname, fDelta, loop, lockx, locky, freeze, time, forcesync=False):
	return ApplyAnimation(playerid, animlib, animname, fDelta, loop, lockx, locky, freeze, time, forcesync)

def clear_animations(playerid, forcesync=False):
	return ClearAnimations(playerid, forcesync)

def get_player_animation_index(playerid):
	return GetPlayerAnimationIndex(playerid)

def get_animation_name(index, animlib_size, animname_size):
	return GetAnimationName(index, animlib_size, animname_size)

def get_player_special_action(playerid):
	return GetPlayerSpecialAction(playerid)

def set_player_special_action(playerid, actionid):
	return SetPlayerSpecialAction(playerid, actionid)

def disable_remote_vehicle_collisions(playerid, disable):
	return DisableRemoteVehicleCollisions(playerid, disable)

def set_player_checkpoint(playerid, x, y, z, size):
	return SetPlayerCheckpoint(playerid, x, y, z, size)

def disable_player_checkpoint(playerid):
	return DisablePlayerCheckpoint(playerid)

def set_player_race_checkpoint(playerid, type, x, y, z, nextx, nexty, nextz, size):
	return SetPlayerRaceCheckpoint(playerid, type, x, y, z, nextx, nexty, nextz, size)

def disable_player_race_checkpoint(playerid):
	return DisablePlayerRaceCheckpoint(playerid)

def set_player_world_bounds(playerid, x_max, x_min, y_max, y_min):
	return SetPlayerWorldBounds(playerid, x_max, x_min, y_max, y_min)

def set_player_marker_for_player(playerid, showplayerid, color):
	return SetPlayerMarkerForPlayer(playerid, showplayerid, color)

def show_player_name_tag_for_player(playerid, showplayerid, show):
	return ShowPlayerNameTagForPlayer(playerid, showplayerid, show)

def set_player_map_icon(playerid, iconid, x, y, z, markertype, color, style=MAPICON_LOCAL.get()):
	return SetPlayerMapIcon(playerid, iconid, x, y, z, markertype, color, style)

def remove_player_map_icon(playerid, iconid):
	return RemovePlayerMapIcon(playerid, iconid)

def allow_player_teleport(playerid, allow):
	return AllowPlayerTeleport(playerid, allow)

def set_player_camera_pos(playerid, x, y, z):
	return SetPlayerCameraPos(playerid, x, y, z)

def set_player_camera_look_at(playerid, x, y, z, cut=CAMERA_CUT.get()):
	return SetPlayerCameraLookAt(playerid, x, y, z, cut)

def set_camera_behind_player(playerid):
	return SetCameraBehindPlayer(playerid)

def get_player_camera_pos(playerid):
	return GetPlayerCameraPos(playerid)

def get_player_camera_front_vector(playerid):
	return GetPlayerCameraFrontVector(playerid)

def get_player_camera_mode(playerid):
	return GetPlayerCameraMode(playerid)

def enable_player_camera_target(playerid, enable):
	return EnablePlayerCameraTarget(playerid, enable)

def get_player_camera_target_object(playerid):
	return GetPlayerCameraTargetObject(playerid)

def get_player_camera_target_vehicle(playerid):
	return GetPlayerCameraTargetVehicle(playerid)

def get_player_camera_target_player(playerid):
	return GetPlayerCameraTargetPlayer(playerid)

def get_player_camera_target_actor(playerid):
	return GetPlayerCameraTargetActor(playerid)

def get_player_camera_aspect_ratio(playerid):
	return GetPlayerCameraAspectRatio(playerid)

def get_player_camera_zoom(playerid):
	return GetPlayerCameraZoom(playerid)

def attach_camera_to_object(playerid, objectid):
	return AttachCameraToObject(playerid, objectid)

def attach_camera_to_player_object(playerid, playerobjectid):
	return AttachCameraToPlayerObject(playerid, playerobjectid)

def interpolate_camera_pos(playerid, FromX, FromY, FromZ, ToX, ToY, ToZ, time, cut=CAMERA_CUT.get()):
	return InterpolateCameraPos(playerid, FromX, FromY, FromZ, ToX, ToY, ToZ, time, cut)

def interpolate_camera_look_at(playerid, FromX, FromY, FromZ, ToX, ToY, ToZ, time, cut=CAMERA_CUT.get()):
	return InterpolateCameraLookAt(playerid, FromX, FromY, FromZ, ToX, ToY, ToZ, time, cut)

def is_player_connected(playerid):
	return IsPlayerConnected(playerid)

def is_player_in_vehicle(playerid, vehicleid):
	return IsPlayerInVehicle(playerid, vehicleid)

def is_player_in_any_vehicle(playerid):
	return IsPlayerInAnyVehicle(playerid)

def is_player_in_checkpoint(playerid):
	return IsPlayerInCheckpoint(playerid)

def is_player_in_race_checkpoint(playerid):
	return IsPlayerInRaceCheckpoint(playerid)

def set_player_virtual_world(playerid, worldid):
	return SetPlayerVirtualWorld(playerid, worldid)

def get_player_virtual_world(playerid):
	return GetPlayerVirtualWorld(playerid)

def enable_stunt_bonus_for_player(playerid, enable):
	return EnableStuntBonusForPlayer(playerid, enable)

def enable_stunt_bonus_for_all(enable):
	return EnableStuntBonusForAll(enable)

def toggle_player_spectating(playerid, toggle):
	return TogglePlayerSpectating(playerid, toggle)

def player_spectate_player(playerid, targetplayerid, mode=SPECTATE_MODE_NORMAL.get()):
	return PlayerSpectatePlayer(playerid, targetplayerid, mode)

def player_spectate_vehicle(playerid, targetvehicleid, mode=SPECTATE_MODE_NORMAL.get()):
	return PlayerSpectateVehicle(playerid, targetvehicleid, mode)

def start_recording_player_data(playerid, recordtype, recordname):
	return StartRecordingPlayerData(playerid, recordtype, recordname)

def stop_recording_player_data(playerid):
	return StopRecordingPlayerData(playerid)

def create_explosion_for_player(playerid, X, Y, Z, type, Radius):
	return CreateExplosionForPlayer(playerid, X, Y, Z, type, Radius)

def create_object(modelid, x, y, z, rX, rY, rZ, DrawDistance=0.0):
	return CreateObject(modelid, x, y, z, rX, rY, rZ, DrawDistance)

def attach_object_to_vehicle(objectid, vehicleid, fOffsetX, fOffsetY, fOffsetZ, fRotX, fRotY, fRotZ):
	return AttachObjectToVehicle(objectid, vehicleid, fOffsetX, fOffsetY, fOffsetZ, fRotX, fRotY, fRotZ)

def attach_object_to_object(objectid, attachtoid, fOffsetX, fOffsetY, fOffsetZ, fRotX, fRotY, fRotZ, SyncRotation=False):
	return AttachObjectToObject(objectid, attachtoid, fOffsetX, fOffsetY, fOffsetZ, fRotX, fRotY, fRotZ, SyncRotation)

def attach_object_to_player(objectid, playerid, fOffsetX, fOffsetY, fOffsetZ, fRotX, fRotY, fRotZ):
	return AttachObjectToPlayer(objectid, playerid, fOffsetX, fOffsetY, fOffsetZ, fRotX, fRotY, fRotZ)

def set_object_pos(objectid, x, y, z):
	return SetObjectPos(objectid, x, y, z)

def get_object_pos(objectid):
	return GetObjectPos(objectid)

def set_object_rot(objectid, rotX, rotY, rotZ):
	return SetObjectRot(objectid, rotX, rotY, rotZ)

def get_object_rot(objectid):
	return GetObjectRot(objectid)

def get_object_model(objectid):
	return GetObjectModel(objectid)

def set_object_no_camera_col(objectid):
	return SetObjectNoCameraCol(objectid)

def is_valid_object(objectid):
	return IsValidObject(objectid)

def destroy_object(objectid):
	return DestroyObject(objectid)

def move_object(objectid, X, Y, Z, Speed, RotX=-1000.0, RotY=-1000.0, RotZ=-1000.0):
	return MoveObject(objectid, X, Y, Z, Speed, RotX, RotY, RotZ)

def stop_object(objectid):
	return StopObject(objectid)

def is_object_moving(objectid):
	return IsObjectMoving(objectid)

def edit_object(playerid, objectid):
	return EditObject(playerid, objectid)

def edit_player_object(playerid, objectid):
	return EditPlayerObject(playerid, objectid)

def select_object(playerid):
	return SelectObject(playerid)

def cancel_edit(playerid):
	return CancelEdit(playerid)

def create_player_object(playerid, modelid, x, y, z, rX, rY, rZ, DrawDistance=0.0):
	return CreatePlayerObject(playerid, modelid, x, y, z, rX, rY, rZ, DrawDistance)

def attach_player_object_to_player(objectplayer, objectid, attachplayer, OffsetX, OffsetY, OffsetZ, rX, rY, rZ):
	return AttachPlayerObjectToPlayer(objectplayer, objectid, attachplayer, OffsetX, OffsetY, OffsetZ, rX, rY, rZ)

def attach_player_object_to_vehicle(playerid, objectid, vehicleid, fOffsetX, fOffsetY, fOffsetZ, fRotX, fRotY, RotZ):
	return AttachPlayerObjectToVehicle(playerid, objectid, vehicleid, fOffsetX, fOffsetY, fOffsetZ, fRotX, fRotY, RotZ)

def set_player_object_pos(playerid, objectid, x, y, z):
	return SetPlayerObjectPos(playerid, objectid, x, y, z)

def get_player_object_pos(playerid, objectid):
	return GetPlayerObjectPos(playerid, objectid)

def set_player_object_rot(playerid, objectid, rotX, rotY, rotZ):
	return SetPlayerObjectRot(playerid, objectid, rotX, rotY, rotZ)

def get_player_object_rot(playerid, objectid):
	return GetPlayerObjectRot(playerid, objectid)

def get_player_object_model(playerid, objectid):
	return GetPlayerObjectModel(playerid, objectid)

def set_player_object_no_camera_col(playerid, objectid):
	return SetPlayerObjectNoCameraCol(playerid, objectid)

def is_valid_player_object(playerid, objectid):
	return IsValidPlayerObject(playerid, objectid)

def destroy_player_object(playerid, objectid):
	return DestroyPlayerObject(playerid, objectid)

def move_player_object(playerid, objectid, x, y, z, Speed, RotX=-1000.0, RotY=-1000.0, RotZ=-1000.0):
	return MovePlayerObject(playerid, objectid, x, y, z, Speed, RotX, RotY, RotZ)

def stop_player_object(playerid, objectid):
	return StopPlayerObject(playerid, objectid)

def is_player_object_moving(playerid, objectid):
	return IsPlayerObjectMoving(playerid, objectid)

def set_object_material(objectid, materialindex, modelid, txdname, texturename, materialcolor=0):
	return SetObjectMaterial(objectid, materialindex, modelid, txdname, texturename, materialcolor)

def set_player_object_material(playerid, objectid, materialindex, modelid, txdname, texturename, materialcolor=0):
	return SetPlayerObjectMaterial(playerid, objectid, materialindex, modelid, txdname, texturename, materialcolor)

def set_object_material_text(objectid, text, materialindex=0, materialsize=OBJECT_MATERIAL_SIZE_256x128.get(),  fontface="Arial", fontsize=24, bold=True, fontcolor=0xFFFFFFFF, backcolor=0, textalignment=0):
	return SetObjectMaterialText(objectid, text, materialindex, materialsize, fontface, fontsize, bold, fontcolor, backcolor, textalignment)

def set_player_object_material_text(playerid, objectid, text, materialindex=0, materialsize=OBJECT_MATERIAL_SIZE_256x128.get(),  fontface="Arial", fontsize=24, bold=True, fontcolor=0xFFFFFFFF, backcolor=0, textalignment=0):
	return SetPlayerObjectMaterialText(playerid, objectid, text, materialindex, materialsize, fontface, fontsize, bold, fontcolor, backcolor, textalignment)

def set_objects_default_camera_col(disable):
	return SetObjectsDefaultCameraCol(disable)

def send_client_message(playerid, color, message):
	return SendClientMessage(playerid, color, message)

def send_client_message_to_all(color, message):
	return SendClientMessageToAll(color, message)

def send_player_message_to_player(playerid, senderid, message):
	return SendPlayerMessageToPlayer(playerid, senderid, message)

def send_player_message_to_all(senderid, message):
	return SendPlayerMessageToAll(senderid, message)

def send_death_message(killer, killee, weapon):
	return SendDeathMessage(killer, killee, weapon)

def send_death_message_to_player(playerid, killer, killee, weapon):
	return SendDeathMessageToPlayer(playerid, killer, killee, weapon)

def game_text_for_all(text, time, style):
	return GameTextForAll(text, time, style)

def game_text_for_player(playerid, text, time, style):
	return GameTextForPlayer(playerid, text, time, style)

def get_tick_count():
	return GetTickCount()

def get_max_players():
	return GetMaxPlayers()

def vector_size(x, y, z):
	return VectorSize(x, y, z)

def get_player_pool_size():
	return GetPlayerPoolSize()

def get_vehicle_pool_size():
	return GetVehiclePoolSize()

def get_actor_pool_size():
	return GetActorPoolSize()

def set_svar_int(varname, int_value):
	return SetSVarInt(varname, int_value)

def get_svar_int(varname):
	return GetSVarInt(varname)

def set_svar_string(varname, string_value):
	return SetSVarString(varname, string_value)

def get_svar_string(varname, len):
	return GetSVarString(varname, len)

def set_svar_float(varname, float_value):
	return SetSVarFloat(varname, float_value)

def get_svar_float(varname):
	return GetSVarFloat(varname)

def delete_svar(varname):
	return DeleteSVar(varname)

def get_svars_upper_index():
	return GetSVarsUpperIndex()

def get_svar_name_at_index(index, ret_len):
	return GetSVarNameAtIndex(index, ret_len)

def get_svar_type(varname):
	return GetSVarType(varname)

def set_game_mode_text(text):
	return SetGameModeText(text)

def set_team_count(count):
	return SetTeamCount(count)

def add_player_class(modelid, spawn_x, spawn_y, spawn_z, z_angle, weapon1, weapon1_ammo, weapon2, weapon2_ammo, weapon3, weapon3_ammo):
	return AddPlayerClass(modelid, spawn_x, spawn_y, spawn_z, z_angle, weapon1, weapon1_ammo, weapon2, weapon2_ammo, weapon3, weapon3_ammo)

def add_player_class_ex(teamid, modelid, spawn_x, spawn_y, spawn_z, z_angle, weapon1, weapon1_ammo, weapon2, weapon2_ammo, weapon3, weapon3_ammo):
	return AddPlayerClassEx(teamid, modelid, spawn_x, spawn_y, spawn_z, z_angle, weapon1, weapon1_ammo, weapon2, weapon2_ammo, weapon3, weapon3_ammo)

def add_static_vehicle(modelid, spawn_x, spawn_y, spawn_z, z_angle, color1, color2):
	return AddStaticVehicle(modelid, spawn_x, spawn_y, spawn_z, z_angle, color1, color2)

def add_static_vehicle_ex(modelid, spawn_x, spawn_y, spawn_z, z_angle, color1, color2, respawn_delay, addsiren=False):
	return AddStaticVehicleEx(modelid, spawn_x, spawn_y, spawn_z, z_angle, color1, color2, respawn_delay, addsiren)

def add_static_pickup(model, type, x, y, z, virtualworld=0):
	return AddStaticPickup(model, type, x, y, z, virtualworld)

def create_pickup(model, type, x, y, z, virtualworld=0):
	return CreatePickup(model, type, x, y, z, virtualworld)

def destroy_pickup(pickup):
	return DestroyPickup(pickup)

def show_name_tags(show):
	return ShowNameTags(show)

def show_player_markers(mode):
	return ShowPlayerMarkers(mode)

def game_mode_exit():
	return GameModeExit()

def set_world_time(hour):
	return SetWorldTime(hour)

def get_weapon_name(weaponid, size):
	return GetWeaponName(weaponid, size)

def enable_tire_popping(enable):
	return EnableTirePopping(enable)

def enable_vehicle_friendly_fire():
	return EnableVehicleFriendlyFire()

def allow_interior_weapons(allow):
	return AllowInteriorWeapons(allow)

def set_weather(weatherid):
	return SetWeather(weatherid)

def set_gravity(gravity):
	return SetGravity(gravity)

def get_gravity():
	return GetGravity()

def allow_admin_teleport(allow):
	return AllowAdminTeleport(allow)

def set_death_drop_amount(amount):
	return SetDeathDropAmount(amount)

def create_explosion(x, y, z, type, radius):
	return CreateExplosion(x, y, z, type, radius)

def enable_zone_names(enable):
	return EnableZoneNames(enable)

def use_player_ped_anims():
	return UsePlayerPedAnims()

def disable_interior_enter_exits():
	return DisableInteriorEnterExits()

def set_name_tag_draw_distance(distance):
	return SetNameTagDrawDistance(distance)

def disable_name_tag_los():
	return DisableNameTagLOS()

def limit_global_chat_radius(chat_radius):
	return LimitGlobalChatRadius(chat_radius)

def limit_player_marker_radius(marker_radius):
	return LimitPlayerMarkerRadius(marker_radius)

def connect_npc(name, script):
	return ConnectNPC(name, script)

def is_player_npc(playerid):
	return IsPlayerNPC(playerid)

def is_player_admin(playerid):
	return IsPlayerAdmin(playerid)

def kick(playerid):
	return Kick(playerid)

def ban(playerid):
	return Ban(playerid)

def ban_ex(playerid, reason):
	return BanEx(playerid, reason)

def send_rcon_command(command):
	return SendRconCommand(command)

def get_player_network_stats(playerid, size):
	return GetPlayerNetworkStats(playerid, size)

def get_network_stats(size):
	return GetNetworkStats(size)

def get_player_version(playerid, len):
	return GetPlayerVersion(playerid, len)

def block_ip_address(ip_address, timems):
	return BlockIpAddress(ip_address, timems)

def un_block_ip_address(ip_address):
	return UnBlockIpAddress(ip_address)

def get_server_var_as_string(varname, size):
	return GetServerVarAsString(varname, size)

def get_server_var_as_int(varname):
	return GetServerVarAsInt(varname)

def get_server_var_as_bool(varname):
	return GetServerVarAsBool(varname)

def get_console_var_as_string(varname, len):
	return GetConsoleVarAsString(varname, len)

def get_console_var_as_int(varname):
	return GetConsoleVarAsInt(varname)

def get_console_var_as_bool(varname):
	return GetConsoleVarAsBool(varname)

def get_server_tick_rate():
	return GetServerTickRate()

def net_stats_get_connected_time(playerid):
	return NetStats_GetConnectedTime(playerid)

def net_stats_messages_received(playerid):
	return NetStats_MessagesReceived(playerid)

def net_stats_bytes_received(playerid):
	return NetStats_BytesReceived(playerid)

def net_stats_messages_sent(playerid):
	return NetStats_MessagesSent(playerid)

def net_stats_bytes_sent(playerid):
	return NetStats_BytesSent(playerid)

def net_stats_messages_recv_per_second(playerid):
	return NetStats_MessagesRecvPerSecond(playerid)

def net_stats_packet_loss_percent(playerid):
	return NetStats_PacketLossPercent(playerid)

def net_stats_connection_status(playerid):
	return NetStats_ConnectionStatus(playerid)

def net_stats_get_ip_port(playerid, ip_port_len):
	return NetStats_GetIpPort(playerid, ip_port_len)

def create_menu(title, columns, x, y, col1width, col2width=0.0):
	return CreateMenu(title, columns, x, y, col1width, col2width)

def destroy_menu(menuid):
	return DestroyMenu(menuid)

def add_menu_item(menuid, column, menutext):
	return AddMenuItem(menuid, column, menutext)

def set_menu_column_header(menuid, column, columnheader):
	return SetMenuColumnHeader(menuid, column, columnheader)

def show_menu_for_player(menuid, playerid):
	return ShowMenuForPlayer(menuid, playerid)

def hide_menu_for_player(menuid, playerid):
	return HideMenuForPlayer(menuid, playerid)

def is_valid_menu(menuid):
	return IsValidMenu(menuid)

def disable_menu(menuid):
	return DisableMenu(menuid)

def disable_menu_row(menuid, row):
	return DisableMenuRow(menuid, row)

def get_player_menu(playerid):
	return GetPlayerMenu(playerid)

def text_draw_create(x, y, text):
	return TextDrawCreate(x, y, text)

def text_draw_destroy(text):
	return TextDrawDestroy(text)

def text_draw_letter_size(text, x, y):
	return TextDrawLetterSize(text, x, y)

def text_draw_text_size(text, x, y):
	return TextDrawTextSize(text, x, y)

def text_draw_alignment(text, alignment):
	return TextDrawAlignment(text, alignment)

def text_draw_color(text, color):
	return TextDrawColor(text, color)

def text_draw_use_box(text, use):
	return TextDrawUseBox(text, use)

def text_draw_box_color(text, color):
	return TextDrawBoxColor(text, color)

def text_draw_set_shadow(text, size):
	return TextDrawSetShadow(text, size)

def text_draw_set_outline(text, size):
	return TextDrawSetOutline(text, size)

def text_draw_background_color(text, color):
	return TextDrawBackgroundColor(text, color)

def text_draw_font(text, font):
	return TextDrawFont(text, font)

def text_draw_set_proportional(text, set):
	return TextDrawSetProportional(text, set)

def text_draw_set_selectable(text, set):
	return TextDrawSetSelectable(text, set)

def text_draw_show_for_player(playerid, text):
	return TextDrawShowForPlayer(playerid, text)

def text_draw_hide_for_player(playerid, text):
	return TextDrawHideForPlayer(playerid, text)

def text_draw_show_for_all(text):
	return TextDrawShowForAll(text)

def text_draw_hide_for_all(text):
	return TextDrawHideForAll(text)

def text_draw_set_string(text, string):
	return TextDrawSetString(text, string)

def text_draw_set_preview_model(text, modelindex):
	return TextDrawSetPreviewModel(text, modelindex)

def text_draw_set_preview_rot(text, fRotX, fRotY, fRotZ, fZoom=1.0):
	return TextDrawSetPreviewRot(text, fRotX, fRotY, fRotZ, fZoom)

def text_draw_set_preview_veh_col(text, color1, color2):
	return TextDrawSetPreviewVehCol(text, color1, color2)

def select_text_draw(playerid, hovercolor):
	return SelectTextDraw(playerid, hovercolor)

def cancel_select_text_draw(playerid):
	return CancelSelectTextDraw(playerid)

def gang_zone_create(minx, miny, maxx, maxy):
	return GangZoneCreate(minx, miny, maxx, maxy)

def gang_zone_destroy(zone):
	return GangZoneDestroy(zone)

def gang_zone_show_for_player(playerid, zone, color):
	return GangZoneShowForPlayer(playerid, zone, color)

def gang_zone_show_for_all(zone, color):
	return GangZoneShowForAll(zone, color)

def gang_zone_hide_for_player(playerid, zone):
	return GangZoneHideForPlayer(playerid, zone)

def gang_zone_hide_for_all(zone):
	return GangZoneHideForAll(zone)

def gang_zone_flash_for_player(playerid, zone, flashcolor):
	return GangZoneFlashForPlayer(playerid, zone, flashcolor)

def gang_zone_flash_for_all(zone, flashcolor):
	return GangZoneFlashForAll(zone, flashcolor)

def gang_zone_stop_flash_for_player(playerid, zone):
	return GangZoneStopFlashForPlayer(playerid, zone)

def gang_zone_stop_flash_for_all(zone):
	return GangZoneStopFlashForAll(zone)

def show_player_dialog(playerid, dialogid, style, caption, info, button1, button2):
	return ShowPlayerDialog(playerid, dialogid, style, caption, info, button1, button2)

def add_char_model(baseid, newid, dffname, txdname):
	return AddCharModel(baseid, newid, dffname, txdname)

def add_simple_model(virtualworld, baseid, newid, dffname, txdname):
	return AddSimpleModel(virtualworld, baseid, newid, dffname, txdname)

def add_simple_model_timed(virtualworld, baseid, newid, dffname, txdname, timeon, timeoff):
	return AddSimpleModelTimed(virtualworld, baseid, newid, dffname, txdname, timeon, timeoff)

def find_model_file_name_from_crc(crc, model_str_len):
	return FindModelFileNameFromCRC(crc, model_str_len)

def find_texture_file_name_from_crc(crc, texture_str_len):
	return FindTextureFileNameFromCRC(crc, texture_str_len)

def redirect_download(playerid, url):
	return RedirectDownload(playerid, url)

def is_valid_vehicle(vehicleid):
	return IsValidVehicle(vehicleid)

def get_vehicle_distance_from_point(vehicleid, x, y, z):
	return GetVehicleDistanceFromPoint(vehicleid, x, y, z)

def create_vehicle(vehicletype, x, y, z, rotation, color1, color2, respawn_delay, addsiren=False):
	return CreateVehicle(vehicletype, x, y, z, rotation, color1, color2, respawn_delay, addsiren)

def destroy_vehicle(vehicleid):
	return DestroyVehicle(vehicleid)

def is_vehicle_streamed_in(vehicleid, forplayerid):
	return IsVehicleStreamedIn(vehicleid, forplayerid)

def get_vehicle_pos(vehicleid):
	return GetVehiclePos(vehicleid)

def set_vehicle_pos(vehicleid, x, y, z):
	return SetVehiclePos(vehicleid, x, y, z)

def get_vehicle_z_angle(vehicleid):
	return GetVehicleZAngle(vehicleid)

def get_vehicle_rotation_quat(vehicleid):
	return GetVehicleRotationQuat(vehicleid)

def set_vehicle_z_angle(vehicleid, z_angle):
	return SetVehicleZAngle(vehicleid, z_angle)

def set_vehicle_params_for_player(vehicleid, playerid, objective, doorslocked):
	return SetVehicleParamsForPlayer(vehicleid, playerid, objective, doorslocked)

def manual_vehicle_engine_and_lights():
	return ManualVehicleEngineAndLights()

def set_vehicle_params_ex(vehicleid, engine, lights, alarm, doors, bonnet, boot, objective):
	return SetVehicleParamsEx(vehicleid, engine, lights, alarm, doors, bonnet, boot, objective)

def get_vehicle_params_ex(vehicleid):
	return GetVehicleParamsEx(vehicleid)

def get_vehicle_params_siren_state(vehicleid):
	return GetVehicleParamsSirenState(vehicleid)

def set_vehicle_params_car_doors(vehicleid, driver, passenger, backleft, backright):
	return SetVehicleParamsCarDoors(vehicleid, driver, passenger, backleft, backright)

def get_vehicle_params_car_doors(vehicleid):
	return GetVehicleParamsCarDoors(vehicleid)

def set_vehicle_params_car_windows(vehicleid, driver, passenger, backleft, backright):
	return SetVehicleParamsCarWindows(vehicleid, driver, passenger, backleft, backright)

def get_vehicle_params_car_windows(vehicleid):
	return GetVehicleParamsCarWindows(vehicleid)

def set_vehicle_to_respawn(vehicleid):
	return SetVehicleToRespawn(vehicleid)

def link_vehicle_to_interior(vehicleid, interiorid):
	return LinkVehicleToInterior(vehicleid, interiorid)

def add_vehicle_component(vehicleid, componentid):
	return AddVehicleComponent(vehicleid, componentid)

def remove_vehicle_component(vehicleid, componentid):
	return RemoveVehicleComponent(vehicleid, componentid)

def change_vehicle_color(vehicleid, color1, color2):
	return ChangeVehicleColor(vehicleid, color1, color2)

def change_vehicle_paintjob(vehicleid, paintjobid):
	return ChangeVehiclePaintjob(vehicleid, paintjobid)

def set_vehicle_health(vehicleid, health):
	return SetVehicleHealth(vehicleid, health)

def get_vehicle_health(vehicleid):
	return GetVehicleHealth(vehicleid)

def attach_trailer_to_vehicle(trailerid, vehicleid):
	return AttachTrailerToVehicle(trailerid, vehicleid)

def detach_trailer_from_vehicle(vehicleid):
	return DetachTrailerFromVehicle(vehicleid)

def is_trailer_attached_to_vehicle(vehicleid):
	return IsTrailerAttachedToVehicle(vehicleid)

def get_vehicle_trailer(vehicleid):
	return GetVehicleTrailer(vehicleid)

def set_vehicle_number_plate(vehicleid, numberplate):
	return SetVehicleNumberPlate(vehicleid, numberplate)

def get_vehicle_model(vehicleid):
	return GetVehicleModel(vehicleid)

def get_vehicle_component_in_slot(vehicleid, slot):
	return GetVehicleComponentInSlot(vehicleid, slot)

def get_vehicle_component_type(component):
	return GetVehicleComponentType(component)

def repair_vehicle(vehicleid):
	return RepairVehicle(vehicleid)

def get_vehicle_velocity(vehicleid):
	return GetVehicleVelocity(vehicleid)

def set_vehicle_velocity(vehicleid, X, Y, Z):
	return SetVehicleVelocity(vehicleid, X, Y, Z)

def set_vehicle_angular_velocity(vehicleid, X, Y, Z):
	return SetVehicleAngularVelocity(vehicleid, X, Y, Z)

def get_vehicle_damage_status(vehicleid):
	return GetVehicleDamageStatus(vehicleid)

def update_vehicle_damage_status(vehicleid, panels, doors, lights, tires):
	return UpdateVehicleDamageStatus(vehicleid, panels, doors, lights, tires)

def set_vehicle_virtual_world(vehicleid, worldid):
	return SetVehicleVirtualWorld(vehicleid, worldid)

def get_vehicle_virtual_world(vehicleid):
	return GetVehicleVirtualWorld(vehicleid)

def get_vehicle_model_info(model, infotype):
	return GetVehicleModelInfo(model, infotype)

def create_actor(modelid, x, y, z, rotation):
	return CreateActor(modelid, x, y, z, rotation)

def destroy_actor(actorid):
	return DestroyActor(actorid)

def is_actor_streamed_in(actorid, forplayerid):
	return IsActorStreamedIn(actorid, forplayerid)

def set_actor_virtual_world(actorid, vworld):
	return SetActorVirtualWorld(actorid, vworld)

def get_actor_virtual_world(actorid):
	return GetActorVirtualWorld(actorid)

def apply_actor_animation(actorid, animlib, animname, fDelta, loop, lockx, locky, freeze, time):
	return ApplyActorAnimation(actorid, animlib, animname, fDelta, loop, lockx, locky, freeze, time)

def clear_actor_animations(actorid):
	return ClearActorAnimations(actorid)

def set_actor_pos(actorid, x, y, z):
	return SetActorPos(actorid, x, y, z)

def get_actor_pos(actorid):
	return GetActorPos(actorid)

def set_actor_facing_angle(actorid, angle):
	return SetActorFacingAngle(actorid, angle)

def get_actor_facing_angle(actorid):
	return GetActorFacingAngle(actorid)

def set_actor_health(actorid, health):
	return SetActorHealth(actorid, health)

def get_actor_health(actorid):
	return GetActorHealth(actorid)

def set_actor_invulnerable(actorid, invulnerable=True):
	return SetActorInvulnerable(actorid, invulnerable)

def is_actor_invulnerable(actorid):
	return IsActorInvulnerable(actorid)

def is_valid_actor(actorid):
	return IsValidActor(actorid)

def http(index, type, url, data, callback):
	return HTTP(index, type, url, data, callback)

def create_3d_text_label(text, color, x, y, z, drawDistance, virtualworld, testLOS=False):
	return Create3DTextLabel(text, color, x, y, z, drawDistance, virtualworld, testLOS)

def delete_3d_text_label(id):
	return Delete3DTextLabel(id)

def attach_3d_text_label_to_player(id, playerid, offsetX, offsetY, offsetZ):
	return Attach3DTextLabelToPlayer(id, playerid, offsetX, offsetY, offsetZ)

def attach_3d_text_label_to_vehicle(id, vehicleid, offsetX, offsetY, offsetZ):
	return Attach3DTextLabelToVehicle(id, vehicleid, offsetX, offsetY, offsetZ)

def update_3d_text_label_text(id, color, text):
	return Update3DTextLabelText(id, color, text)

def create_player_3d_text_label(playerid, text, color, x, y, z, drawDistance, attachedplayer=INVALID_PLAYER_ID.get(), attachedvehicle=INVALID_VEHICLE_ID.get(), testLOS=False):
	return CreatePlayer3DTextLabel(playerid, text, color, x, y, z, drawDistance, attachedplayer, attachedvehicle, testLOS)

def delete_player_3d_text_label(playerid, id):
	return DeletePlayer3DTextLabel(playerid, id)

def update_player_3d_text_label_text(playerid, id, color, text):
	return UpdatePlayer3DTextLabelText(playerid, id, color, text)

class Actor(object):
    """
    Read more about actors here: https://open.mp/docs/scripting/functions/CreateActor
    -----------------
    """
    def __init__(self, modelid, x, y, z, rot):
        self.id = CreateActor(modelid, x, y, z, rot)

    def destroy(self):
        return DestroyActor(self.id)
        
    def streamed_in(self, forplayerid):
        return IsActorStreamedIn(self.id, forplayerid)
        
    @property
    def virtual_world(self):
        return GetActorVirtualWorld(self.id)
        
    @virtual_world.setter
    def virtual_world(self, vworld):
        return SetActorVirtualWorld(self.id, vworld)
        
    def apply_animation(self, animlib, animname, fDelta, loop, lockx, locky, freeze, time):
        return ApplyActorAnimation(self.id, animlib, animname, fDelta, loop, lockx, locky, freeze, time)
        
    def clear_animations(self):
        return ClearActorAnimations(self.id)
        
    @property
    def pos(self):
        return GetActorPos(self.id)
        
    @pos.setter
    def pos(self, pos):
        try:
            x, y, z = pos
        except:
            raise ValueError("Expected pos as tuple: (x, y, z)")
        else:
            return SetActorPos(self.id, x, y, z)
        
    @property
    def facing_angle(self):
        return GetActorFacingAngle(self.id)
        
    @facing_angle.setter
    def facing_angle(self, angle):
        return SetActorFacingAngle(self.id, angle)
        
    @property
    def health(self):
        return GetActorHealth(self.id)
        
    @health.setter
    def health(self, health):
        return SetActorHealth(self.id, health)
        
    @property
    def invulnerable(self):
        return IsActorInvulnerable(self.id)
        
    @invulnerable.setter
    def invulnerable(self, invulnerable=True):
        return SetActorInvulnerable(self.id, invulnerable)
        
    @property
    def is_valid(self):
        return IsValidActor(self.id)

class Player(object):
    """Track all players and interact with them using the Player Class

    The class includes all functions that are in sa-mp where the first argument is "playerid".
    The methods and properties are also renamed, to remove "player" and "get"/"set" words. 
    
    Ex:
    -----------
    ```py
    ## old way
    name = get_player_name(playerid, 16)
    #################
    # Do this when player connects;
    player_obj = Player(playerid) 
    # Then, access properties
    name = player_obj.name
    # or, access methods
    player_obj.set_armed_weapon(weaponid)
    ```

    """
    def __init__(self, playerid):
        self.id = playerid
    def set_spawn_info(self, team, skin, x, y, z, rotation, weapon1, weapon1_ammo, weapon2, weapon2_ammo, weapon3, weapon3_ammo):
        """ | METHOD |

        This method can be used to change the spawn information of a specific player. 
        It allows you to automatically set someone's spawn weapons, their team, skin and spawn position, 
        normally used in case of minigames or automatic-spawn systems.
        
        Parameters
        -----
        ______________________________________
        - int:team \t\t The Team-ID of the chosen player.
        - int:skin \t\t The skin which the player will spawn with.
        - float:X \t\t The X-coordinate of the player's spawn position.
        - float:Y \t\t The Y-coordinate of the player's spawn position.
        - float:Z \t\t The Z-coordinate of the player's spawn position.
        - float:rotation \t The direction in which the player needs to be facing after spawning.
        - int:weapon1: \t\t The first spawn-weapon for the player.
        - int:weapon1_ammo: \t The amount of ammunition for the primary spawnweapon.
        - int:weapon2: \t\t The second spawn-weapon for the player.
        - int:weapon2_ammo: \t The amount of ammunition for the second spawnweapon.
        - int:weapon3: \t\t The third spawn-weapon for the player.
        - int:weapon3_ammo: \t The amount of ammunition for the third spawnweapon.
        ______________________________________
        Returns
        ---------
        This function does not return any specific values.
        Examples
        -----
        ```py
        def OnPlayerRequestClass(playerid, classid)
            # This simple example demonstrates how to spawn every player automatically with
            # CJ's skin, which is number 0. The player will spawn in Las Venturas, with
            # 36 Sawnoff-Shotgun rounds and 150 Tec9 rounds.
            player.set_spawn_info(0, 0, 1958.33, 1343.12, 15.36, 269.15, 26, 36, 28, 150, 0, 0 );
        ```
        """
        return SetSpawnInfo(self.id, team, skin, x, y, z, rotation, weapon1, weapon1_ammo, weapon2, weapon2_ammo, weapon3, weapon3_ammo)

    def spawn(self):
        """ | METHOD | 
        
        (Re)Spawns a player.
        ___________
        no parameters
        ___________
        
        Returns
        -------------
        - 1: The function executed successfully.
        - 0: The function failed to execute. This means the player is not connected.
        
        
        Examples
        -------------
        ```py
        if "/spawn" in cmdtext[:6]:
            player.spawn()
            return True
        ```
        """
        return SpawnPlayer(self.id)

    def set_pos_find_z(self, x, y, z):
        """| METHOD | 
        
        This sets the players position then adjusts the players z-coordinate to the nearest solid ground under the position
        ________________
        - Float:x \t The X coordinate to position the player at.
        - Float:y \t The X coordinate to position the player at.
        - Float:z \t The Z coordinate to position the player at.
        ________________
        
        Returns
        --------
        - 1: The function executed successfully.
        - 0: The function failed to execute. This means the player specified does not exist.
        
        NOTICE
        ---------
        - This function does not work if the new coordinates are far away from where the player currently is. 
        - The Z height will be 0, which will likely put them underground.
        """
        return SetPlayerPosFindZ(self.id, x, y, z)

    @property
    def pos(self):
        """| PROPERTY | 
        
        Get or Set the position. Values inside tuple are floats.

        Examples
        ---------
        - Getting the position:
        
        >>> `(x, y, z) = player.pos`
        

        - Setting the position:
        >>> `player.pos = (x, y, z)`
        
        
        Set
        ----
        - Returns true if successful, false if not.\n
        Get
        -----
        - Returns: (x, y, z), raises ValueError if unsuccessful.
        

        """
        return GetPlayerPos(self.id)

    @pos.setter
    def pos(self, pos: tuple):
        try:
            x, y, z = pos
        except:
            raise ValueError("Expected a tuple for pos. (x, y, z)")
        else:
            return SetPlayerPos(self.id, x, y, z)

    @property
    def facing_angle(self):
        """| PROPERTY | 
        
        Set / get the player's facing angle.

            Example:
            ---------- 
            ```py
            if player.facing_angle > 180:
                player.facing_angle = 180
            ```
            Value: float
        """
        return GetPlayerFacingAngle(self.id)

    @facing_angle.setter
    def facing_angle(self, angle):
        return SetPlayerFacingAngle(self.id, angle)

    def is_in_range_of_point(self, range, x, y, z):
        """| METHOD | 
        
        Checks if the player is in range of a point. 
        
        - Float:range \t The furthest distance the player can be from the point to be in range.
        - Float:x \t The X coordinate of the point to check the range to.
        - Float:y \t The Y coordinate of the point to check the range to.
        - Float:z \t The Z coordinate of the point to check the range to.

        Returns
        -------
        - True - The player is in range of the point.
        - False - The player is not in range of the point.

        Source: https://open.mp/docs/scripting/functions/IsPlayerInRangeOfPoint     
        """
        return IsPlayerInRangeOfPoint(self.id, range, x, y, z)

    def distance_from_point(self, x, y, z):
        """| METHOD | 
        
        Calculate the distance between a player and a map coordinate.

        - Float:x \t The X map coordinate.
        - Float:y \t The Y map coordinate.
        - Float:z \t The Z map coordinate.
        
        Returns
        -------
        The distance between the player and the point as a float.
        """
        return GetPlayerDistanceFromPoint(self.id, x, y, z)

    def is_streamed_in(self, forplayerid):
        """| METHOD | 
        
        Checks if the player is streamed in another player's client.

        - forplayerid \t The ID of the player to check if playerid is streamed in for.
        
        Returns
        -------
        - 1: The player is streamed in.
        - 0: The player is not streamed in.
        Examples
        ------------
        ```py
        if player.is_streamed_in(0) ## can player 0 see this player?
            player.send_client_message(-1, "ID 0 can see you.");
        ```
        """
        return IsPlayerStreamedIn(self.id, forplayerid)

    @property

    def interior(self):
        """| PROPERTY | 
        
        Set or get the player's interior. Normal world is in interior 0.

        A list of currently known interiors and their positions can be found here:
        
        https://open.mp/docs/scripting/resources/interiorids

        The interior is a positive integer.

        Example:
        --------
        ```py
        if player.interior == 0:
            player.interior = 5
        ```
        """
        return GetPlayerInterior(self.id)

    @interior.setter
    def interior(self, interiorid):
        return SetPlayerInterior(self.id, interiorid)

    @property
    def health(self):
        """| PROPERTY | 
        
        Get or set the player's health.

        Value should be a float between `0.0` and `100.0`

        Example:
        ------
        ```py
        if player.health < 10.0:
            player.send_client_message(-1, "Watch out! You are almost dead: {} hp left!".format(player.health))

        if player.health < 5.0:
            player.health = 0.0 ## Setting health to 0, kills the player.  
        ```
        """
        return GetPlayerHealth(self.id)

    @health.setter
    def health(self, health):
        return SetPlayerHealth(self.id, health)

    @property
    def armour(self):
        """| PROPERTY | 
        
        Get or set the player's armour.

        Value should be a float between `0.0` and `100.0`

        Example:
        ------
        ```py
        if player.armour < 10.0:
            player.send_client_message(-1, "You are running out of armour: {} left!".format(player.armour))

        if player.score > 90:
            player.armour = 100.0 ## Set full armour.  
        ```
        """
        return GetPlayerArmour(self.id)

    @armour.setter
    def armour(self, armour):
        return SetPlayerArmour(self.id, armour)

    @property
    def ammo(self):
        """| PROPERTY | 
        
        Get or set the amount of ammo in the player's current weapon.

        Value should be an int between 0 and 32766. 
        *Warning*: Values above 32766 can cause errors.

        Example:
        ------
        ```py
        if player.ammo < 10:
            player.ammo = 5000 # Automatically fill up to 5000 when below 10 ammo.
        ```
        """
        return GetPlayerAmmo(self.id)

    @ammo.setter
    def ammo(self, conf: tuple):
        try:
            weaponid, ammo = conf
        except:
            raise ValueError("Expected a tuple for ammo: (weaponid, ammo)")
        else:
            return SetPlayerAmmo(self.id, weaponid, ammo)

    @property
    def weapon_state(self):
        """| PROPERTY | Read only | 
        
        Check the state of the player's weapon.
        __________
        - \tID \t Constant\t\t\t Description
        >>>
        - \t-1 \t WEAPONSTATE_UNKNOWN \t\t Unknown (Set when in a vehicle)
        - \t 0 \t WEAPONSTATE_NO_BULLETS \t The weapon has no remaining ammo
        - \t 1 \t WEAPONSTATE_LAST_BULLET \t The weapon has one remaining bullet
        - \t 2 \t WEAPONSTATE_MORE_BULLETS \t The weapon has multiple bullets
        - \t 3 \t WEAPONSTATE_RELOADING \t\t The player is reloading their weapon 
        __________
        Returns
        ----
        - The state of the weapon 


        Example:
        ---------
        ```py
        if player.weapon_state = WEAPONSTATE_LAST_BULLET.get():
            player.send_client_message(-1, "You only have 1 bullet left!!")
        ```
        """
        return GetPlayerWeaponState(self.id)

    @property
    def target(self):
        """| PROPERTY | Read only |
        
        Check who the player is aiming at.

        Returns
        -----
        - The ID of the target player as an int, or `INVALID_PLAYER_ID` if none.

        Notes:
        ----
        - Does not work for joypads/controllers, and after a certain distance.
        - Does not work for the sniper rifle, as it doesn't lock on to anything and won't return a player. 

        Example:
        ----
        ```py
        ## Usually put under a timer or under on_player_update()
        if player.target == INVALID_PLAYER_ID.get():
            pass
        elif player.target == 5:
            player.send_client_message(-1, "You are currently aiming at player id 5")
        ```
        """
        return GetPlayerTargetPlayer(self.id)

    @property
    def target_actor(self):
        return GetPlayerTargetActor(self.id)

    @property
    def team(self):
        """| PROPERTY | 
        
        Get or set the player's team ID.

        -  0-254  are valid teams
        -  255 is defined as NO_TEAM. The player is not on any team `(default)`
        - -1 is returned if something went wrong reading the value. Not a valid team.

        Example
        ----
        ```py
        if player.team == NO_TEAM.get():
            player.team = 15 ## Assign to team 15
        
        ```
        """
        return GetPlayerTeam(self.id)

    @team.setter
    def team(self, teamid):
        return SetPlayerTeam(self.id, teamid)

    @property
    def score(self):
        """ | PROPERTY |
        
        Get or set the player's score as an int.

        Example:
        -----
        ```py
        if player.score == 0:
            player.score += 1000
        ```

        """
        return GetPlayerScore(self.id)

    @score.setter
    def score(self, score):
        return SetPlayerScore(self.id, score)

    @property
    def drunk_level(self):
        """ | PROPERTY |
        
        Get or set the player's drunk level.

        Values:
        ----
        - 0 to 2000 \t\t No visible effect
        - 2001 to 5000  \t Visible camera swaying and control issues in vehicles. HUD is visible.
        - 5001 and above\t Swaying continues, but HUD becomes invisible.

        NOTE: Drunk level with decrease with player fps. If you have 50 fps, the drunk level will decrease with 50 levels per second.

        More information: https://open.mp/docs/scripting/functions/SetPlayerDrunkLevel
        """
        return GetPlayerDrunkLevel(self.id)

    @drunk_level.setter
    def drunk_level(self, level):
        return SetPlayerDrunkLevel(self.id, level)

    @property
    def color(self):
        """| PROPERTY |

        Get or set the player color.

        NB: If you try to read the value before it is set, it will return 0!

        Format: `0xRRGGBBAA`

        Example:
        ----
        ```py
        player.color = 0xFFFFFFFF
        player.send_client_message(player.color, "This is a message with my color")
        ```
        """
        return GetPlayerColor(self.id)

    @color.setter
    def color(self, color):
        return SetPlayerColor(self.id, color)

    @property
    def skin(self):
        """ | PROPERTY |

        Get or set the player's skin, as an int. A skin is the character model.

        See available skins and the corresponding ID's here: https://open.mp/docs/scripting/resources/skins

        Value can be `0-73` or `75-311`. Default is `0` (CJ)

        ___________
        WARNING: 
        ----
        Known Bugs: If a player's skin is set when they are crouching, in a vehicle, or performing certain animations, 
        they will become frozen or otherwise glitched. This can be fixed by using `player.toggle_controllable(1)`.

        Players can be detected as being crouched through `player.special_action == SPECIAL_ACTION_DUCK.get()` 
        Other players around the player may crash if he is in a vehicle or if he is entering/leaving a vehicle. 
        Setting a player's skin when he is dead may crash players around him. Breaks sitting on bikes.
        ___________

        Example:
        ----------
        ```py
        ## Set the player's skin to 45
        player.skin = 45
        ```
        """
        return GetPlayerSkin(self.id)

    @skin.setter
    def skin(self, skinid):
        return SetPlayerSkin(self.id, skinid)

    def give_weapon(self, weaponid, ammo):
        """| METHOD |

        Give the player a weapon with specified amount of ammo

        See all weapon ID's here: https://open.mp/docs/scripting/resources/weaponids
        ________
        - weaponid \t Int, the ID of the weapon to give to the player.
        - ammo \t\t Int, the amount of ammo to give to the player.
        ________

        Return
        -------
        - 1: The function was executed successfully.
        - 0: The function failed to execute, player is not connected.

        Example:
        -------
        ```py
        player.give_weapon(6, 1) # Give a shovel
        player.give_weapon(WEAPON_COLT45.get(), 500) # Give a Colt45 with 500 bullets
        ```
        """
        return GivePlayerWeapon(self.id, weaponid, ammo)

    def reset_weapons(self):
        """ | METHOD |
        
        Removes all weapons from a player.

        Returns
        -------
        - 1: The function was executed successfully.
        - 0: The function failed to execute. This means the player specified does not exist.

        Example
        --------
        ```py
        
            player.reset_weapons();
            return 1;

        """
        return ResetPlayerWeapons(self.id)

    def set_armed_weapon(self, weaponid):
        """| METHOD |

        Sets which weapon the player is holding. The player needs to have this weapon for it to work. 
        It will not give the player a new weapon.

        _________
        - weaponid \t The weapon id the player should hold in hands
        _________

        Returns
        ----
        - 1: The function was executed successfully. Success is returned even when the function fails to execute (the player doesn't have the weapon specified, or it is an invalid weapon).
        - 0: The function failed to execute. The player is not connected.

        Example
        -------
        ```py
        ## Lets make the player only have hands (put away weapons)
        player.set_armed_weapon(0)

        ```        

        """
        return SetPlayerArmedWeapon(self.id, weaponid)

    def get_weapon_data(self, slot):
        """| METHOD | 

        ________
        - slot \t The weapon slot to get data for (0-12)
        ________

        Return
        ----
        This method returns a tuple containing (weapons, ammo):
        - weapons \t A variable containing the weapon ID.
        - ammo    \t A variable containing the ammo.

        Example
        -----
        ```py
        (weapon, ammo) = player.get_weapon_data(4) # Get weapon data from slot 4

        ### If you want to retrieve for all weapons, you can do something like this:
        weapon_list = []
        for slot in range(12):
            (weap, am) = player.get_weapon_data(slot)
            weapon_list.append((weap, am))

        ## Print all values like this
        for weap, am in weapon_list:
            print("Weapon: {} | Ammo: {}".format(str(weap), str(am))
        """
        return GetPlayerWeaponData(self.id, slot)

    def give_money(self, money):
        """| METHOD |

        Give money to or take money from a player

        - money \t The amount of money you want to give to the player. Negative value to take money.

        Recommendation
        ----
        You can use property `player.money += amount` or `player.money -= amount` instead.

        Example
        ------
        ```py
        player.give_money(1000) # Give player $1000
        ```
        """
        return GivePlayerMoney(self.id, money)

    def reset_money(self):
        """| METHOD | 

        Use this method to reset player money. You can also use `player.money = 0`.
        """
        return ResetPlayerMoney(self.id)

    @property
    def name(self, size):
        """| PROPERTY |

        Get or set the player's name. Max length is 25 character (`MAX_PLAYER_NAME`)

        Example:
        -------
        ```py
        ## Change the name if it contains admin or moderator in it:
        if "admin" in player.name or "moderator" in player.name:
            player.name = "[GUEST]Player_{}".format(player.id) 
        ```
        """
        return GetPlayerName(self.id, MAX_PLAYER_NAME.get())

    @name.setter
    def name(self, name):
        return SetPlayerName(self.id, name)

    @property
    def money(self):
        """| PROPERTY |

        Set or get the player money. The money can be a value between `-2147483647` and `2147483647`. 
        
        Negative numbers will be shown as red on the HUD.

        Behind the scenes, setting money will first `reset_money` and then `give_money`.

        Example
        -------
        ```py
        ## Get and set player money:
        if player.money == 0:
            player.money == 5000; 
        ```
        """
        return GetPlayerMoney(self.id)

    @money.setter
    def money(self, money):
        ResetPlayerMoney(self.id)
        return GivePlayerMoney(self.id, money)

    @property
    def state(self):
        """| PROPERTY | Read only |

        Get the current player state.
        
        https://open.mp/docs/scripting/resources/playerstates

        Returns
        -----
        - state \t Returns the state as an integer. 
        
        Example
        ------
        ```py
        ## Check the player state:
        if player.state == PLAYER_STATE_ONFOOT.get():
            player.send_client_message(-1, "You are currently on foot")
        ```
        """
        return GetPlayerState(self.id)

    @property
    def ip(self):
        """| PROPERTY | Read only |

        Get the player's IP Address. Returns as a string

        Example
        ```py
        player.send_client_message(-1, "Your IP: {}".format(player.ip))
        ```
        
        """
        return GetPlayerIp(self.id, 16)

    @property
    def ping(self):
        """| PROPERTY | Read only |

        Get the player latency to server, represented in milliseconds.

        Example
        ------
        ```py 
        player.send_client_message(-1, "Your ping right now: {}".format(player.ping))
        ```
        """
        return GetPlayerPing(self.id)

    @property
    def weapon(self):
        """| PROPERTY | Read only |

        Get the weapon id (int) of the currently held weapon.

        Return
        -----
        - weaponid \t Weapon that is currently held. May return -1 (invalid weapon)

        Notice
        -----
        When the player state is PLAYER_STATE_DRIVER or PLAYER_STATE_PASSENGER,
        this function returns the weapon held by the player before they entered the vehicle 

        Example
        ------
        ```py 
        player.send_client_message(-1, "Your current weapon right now: {}".format(str(player.weapon)))
        ```
        """
        return GetPlayerWeapon(self.id)

    @property
    def keys(self):
        """| PROPERTY | Read only |

        Check which keys a player is pressing. 
        
        See all keys here: https://sampwiki.blast.hk/wiki/Keys

        Return
        ---------
        This method returns a Tuple with 3 values. It looks like this: `(keys, ud, lr)`
        - keys   \t A set of bits containing the player's key states (bitmask)
        - updown \t Up/down state.
        - leftright\t Left/right state.

        Example
        ------
        ```py 
        (key, ud, lr) = player.keys
        ```

        Note
        -------
        Only the FUNCTION of keys can be detected; not actual keys. For example, it is not possible to detect if a player presses SPACE, 
        but you can detect if they press SPRINT (which can be mapped (assigned/binded) to ANY key (but is space by default)). 
        As of update 0.3.7, the keys "A" and "D" are not recognized when in a vehicle. 
        However, keys "W" and "S" can be detected with the "keys" parameter.
        
        """
        return GetPlayerKeys(self.id)

    @property
    def time(self):
        return GetPlayerTime(self.id)

    @time.setter
    def time(self, time: tuple):
        try: 
            hour, minute = time
        except:
            raise ValueError("Expected a tuple for time: (hour, minute)")
        else:
            return SetPlayerTime(self.id, hour, minute)

    def toggle_clock(self, toggle):
        return TogglePlayerClock(self.id, toggle)

    def set_weather(self, weather):
        return SetPlayerWeather(self.id, weather)

    def force_class_selection(self):
        return ForceClassSelection(self.id)

    @property
    def wanted_level(self):
        return GetPlayerWantedLevel(self.id)

    @wanted_level.setter
    def wanted_level(self, level):
        return SetPlayerWantedLevel(self.id, level)

    @property
    def fighting_style(self):
        return GetPlayerFightingStyle(self.id)

    @fighting_style.setter
    def fighting_style(self, style):
        return SetPlayerFightingStyle(self.id, style)

    @property
    def velocity(self):
        return GetPlayerVelocity(self.id)

    @velocity.setter
    def velocity(self, pos: tuple):
        try:
            x, y, z = pos
        except:
            raise ValueError("Expected a tuple for pos: (x, y, z)")
        else:
            return SetPlayerVelocity(self.id, x, y, z)

    def play_crime_report(self, suspectid, crime):
        return PlayCrimeReportForPlayer(self.id, suspectid, crime)

    def play_audio_stream(self, url, posX=0.0, posY=0.0, posZ=0.0, distance=50.0, usepos=False):
        return PlayAudioStreamForPlayer(self.id, url, posX, posY, posZ, distance, usepos)

    def stop_audio_stream(self):
        return StopAudioStreamForPlayer(self.id)

    def set_shop_name(self, shopname):
        return SetPlayerShopName(self.id, shopname)

    def set_skill_level(self, skill, level):
        return SetPlayerSkillLevel(self.id, skill, level)

    @property
    def surfing_vehicle_id(self):
        """| PROPERTY | Read only |

        
        """
        return GetPlayerSurfingVehicleID(self.id)

    @property
    def surfing_object_id(self):
        """| PROPERTY | Read only |

        
        """
        return GetPlayerSurfingObjectID(self.id)

    def remove_building(self, modelid, fX, fY, fZ, fRadius):
        return RemoveBuildingForPlayer(self.id, modelid, fX, fY, fZ, fRadius)

    @property
    def last_shot_vectors(self):
        """| PROPERTY | Read only |

        
        """
        return GetPlayerLastShotVectors(self.id)

    def set_attached_object(self, index, modelid, bone, fOffsetX=0.0, fOffsetY=0.0, fOffsetZ=0.0, fRotX=0.0, fRotY=0.0, fRotZ=0.0, fScaleX=1.0, fScaleY=1.0, fScaleZ=1.0, materialcolor1=0, materialcolor2=0):
        return SetPlayerAttachedObject(self.id, index, modelid, bone, fOffsetX, fOffsetY, fOffsetZ, fRotX, fRotY, fRotZ, fScaleX, fScaleY, fScaleZ, materialcolor1, materialcolor2)

    def remove_attached_object(self, index):
        return RemovePlayerAttachedObject(self.id, index)

    def is_attached_object_slot_used(self, index):
        return IsPlayerAttachedObjectSlotUsed(self.id, index)

    def edit_attached_object(self, index):
        return EditAttachedObject(self.id, index)

    def create_text_draw(self, x, y, text):
        return CreatePlayerTextDraw(self.id, x, y, text)

    def text_draw_destroy(self, text):
        return PlayerTextDrawDestroy(self.id, text)

    def text_draw_letter_size(self, text, x, y):
        return PlayerTextDrawLetterSize(self.id, text, x, y)

    def text_draw_text_size(self, text, x, y):
        return PlayerTextDrawTextSize(self.id, text, x, y)

    def text_draw_alignment(self, text, alignment):
        return PlayerTextDrawAlignment(self.id, text, alignment)

    def text_draw_color(self, text, color):
        return PlayerTextDrawColor(self.id, text, color)

    def text_draw_use_box(self, text, use):
        return PlayerTextDrawUseBox(self.id, text, use)

    def text_draw_box_color(self, text, color):
        return PlayerTextDrawBoxColor(self.id, text, color)

    def text_draw_set_shadow(self, text, size):
        return PlayerTextDrawSetShadow(self.id, text, size)

    def text_draw_set_outline(self, text, size):
        return PlayerTextDrawSetOutline(self.id, text, size)

    def text_draw_background_color(self, text, color):
        return PlayerTextDrawBackgroundColor(self.id, text, color)

    def text_draw_font(self, text, font):
        return PlayerTextDrawFont(self.id, text, font)

    def text_draw_set_proportional(self, text, set):
        return PlayerTextDrawSetProportional(self.id, text, set)

    def text_draw_set_selectable(self, text, set):
        return PlayerTextDrawSetSelectable(self.id, text, set)

    def player_text_draw_show(self, text):
        return PlayerTextDrawShow(self.id, text)

    def player_text_draw_hide(self, text):
        return PlayerTextDrawHide(self.id, text)

    def text_draw_hide_for_player(self, text):
        return TextDrawHideForPlayer(self.id, text)

    def text_draw_set_string(self, text, string):
        return PlayerTextDrawSetString(self.id, text, string)

    def text_draw_set_preview_model(self, text, modelindex):
        return PlayerTextDrawSetPreviewModel(self.id, text, modelindex)

    def text_draw_set_preview_rot(self, text, fRotX, fRotY, fRotZ, fZoom=1.0):
        return PlayerTextDrawSetPreviewRot(self.id, text, fRotX, fRotY, fRotZ, fZoom)

    def text_draw_set_preview_veh_col(self, text, color1, color2):
        return PlayerTextDrawSetPreviewVehCol(self.id, text, color1, color2)

    def get_pvar_int(self, varname):
        return GetPVarInt(self.id, varname)

    def set_pvar_int(self, varname, value):
        return SetPVarInt(self.id, varname, value)

    def get_pvar_string(self, varname, size):
        return GetPVarString(self.id, varname, size)

    def set_pvar_string(self, varname, value):
        return SetPVarString(self.id, varname, value)

    def get_pvar_float(self, varname):
        return GetPVarFloat(self.id, varname)

    def set_pvar_float(self, varname, value):
        return SetPVarFloat(self.id, varname, value)

    def delete_pvar(self, varname):
        return DeletePVar(self.id, varname)

    @property
    def pvars_upper_index(self):
        return GetPVarsUpperIndex(self.id)

    def get_pvar_name_at_index(self, index, size):
        return GetPVarNameAtIndex(self.id, index, size)

    def get_pvar_type(self, varname):
        return GetPVarType(self.id, varname)

    def set_chat_bubble(self, text, color, drawdistance, expiretime):
        return SetPlayerChatBubble(self.id, text, color, drawdistance, expiretime)

    def put_in_vehicle(self, vehicleid, seatid):
        return PutPlayerInVehicle(self.id, vehicleid, seatid)

    @property
    def vehicle_id(self):
        return GetPlayerVehicleID(self.id)

    @property
    def vehicle_seat(self):
        return GetPlayerVehicleSeat(self.id)

    def remove_from_vehicle(self):
        return RemovePlayerFromVehicle(self.id)

    def toggle_controllable(self, toggle):
        return TogglePlayerControllable(self.id, toggle)

    def play_sound(self, soundid, x, y, z):
        return PlayerPlaySound(self.id, soundid, x, y, z)

    def apply_animation(self, animlib, animname, fDelta, loop, lockx, locky, freeze, time, forcesync=False):
        return ApplyAnimation(self.id, animlib, animname, fDelta, loop, lockx, locky, freeze, time, forcesync)

    def clear_animations(self, forcesync=False):
        return ClearAnimations(self.id, forcesync)

    @property
    def animation_index(self):
        return GetPlayerAnimationIndex(self.id)

    @property
    def special_action(self):
        return GetPlayerSpecialAction(self.id)

    @special_action.setter
    def special_action(self, actionid):
        return SetPlayerSpecialAction(self.id, actionid)

    def disable_remote_vehicle_collisions(self, disable):
        return DisableRemoteVehicleCollisions(self.id, disable)

    def set_checkpoint(self, x, y, z, size):
        return SetPlayerCheckpoint(self.id, x, y, z, size)

    def disable_checkpoint(self):
        return DisablePlayerCheckpoint(self.id)

    def set_race_checkpoint(self, type, x, y, z, nextx, nexty, nextz, size):
        return SetPlayerRaceCheckpoint(self.id, type, x, y, z, nextx, nexty, nextz, size)

    def disable_race_checkpoint(self):
        return DisablePlayerRaceCheckpoint(self.id)

    def set_world_bounds(self, x_max, x_min, y_max, y_min):
        return SetPlayerWorldBounds(self.id, x_max, x_min, y_max, y_min)

    def set_marker(self, showplayerid, color):
        return SetPlayerMarkerForPlayer(self.id, showplayerid, color)

    def show_name_tag(self, showplayerid, show):
        return ShowPlayerNameTagForPlayer(self.id, showplayerid, show)

    def set_map_icon(self, iconid, x, y, z, markertype, color, style=MAPICON_LOCAL.get()):
        return SetPlayerMapIcon(self.id, iconid, x, y, z, markertype, color, style)

    def remove_map_icon(self, iconid):
        return RemovePlayerMapIcon(self.id, iconid)

    def allow_teleport(self, allow):
        return AllowPlayerTeleport(self.id, allow)

    def set_camera_look_at(self, x, y, z, cut=CAMERA_CUT.get()):
        return SetPlayerCameraLookAt(self.id, x, y, z, cut)

    def set_camera_behind(self):
        return SetCameraBehindPlayer(self.id)

    @property
    def camera_pos(self):
        return GetPlayerCameraPos(self.id)

    @camera_pos.setter
    def camera_pos(self, pos: tuple):
        try:
            x, y, z = pos
        except:
            raise ValueError("Expected x, y, z as a tuple (x, y, z)")
        else:
            return SetPlayerCameraPos(self.id, x, y, z)

    def get_camera_front_vector(self):
        return GetPlayerCameraFrontVector(self.id)

    @property
    def camera_mode(self):
        return GetPlayerCameraMode(self.id)

    def enable_camera_target(self, enable):
        return EnablePlayerCameraTarget(self.id, enable)

    @property
    def camera_target_object(self):
        return GetPlayerCameraTargetObject(self.id)

    @property
    def camera_target_vehicle(self):
        return GetPlayerCameraTargetVehicle(self.id)

    @property
    def camera_target(self):
        return GetPlayerCameraTargetPlayer(self.id)

    @property
    def camera_target_actor(self):
        return GetPlayerCameraTargetActor(self.id)

    @property
    def camera_aspect_ratio(self):
        return GetPlayerCameraAspectRatio(self.id)

    @property
    def camera_zoom(self):
        return GetPlayerCameraZoom(self.id)

    def attach_camera_to_object(self, objectid):
        return AttachCameraToObject(self.id, objectid)

    def attach_camera_to_player_object(self, playerobjectid):
        return AttachCameraToPlayerObject(self.id, playerobjectid)

    def interpolate_camera_pos(self, FromX, FromY, FromZ, ToX, ToY, ToZ, time, cut=CAMERA_CUT.get()):
        return InterpolateCameraPos(self.id, FromX, FromY, FromZ, ToX, ToY, ToZ, time, cut)

    def interpolate_camera_look_at(self, FromX, FromY, FromZ, ToX, ToY, ToZ, time, cut=CAMERA_CUT.get()):
        return InterpolateCameraLookAt(self.id, FromX, FromY, FromZ, ToX, ToY, ToZ, time, cut)

    @property
    def connected(self):
        return IsPlayerConnected(self.id)

    def is_in_vehicle(self, vehicleid):
        return IsPlayerInVehicle(self.id, vehicleid)

    def is_in_any_vehicle(self):
        return IsPlayerInAnyVehicle(self.id)

    def is_in_checkpoint(self):
        return IsPlayerInCheckpoint(self.id)

    def is_in_race_checkpoint(self):
        return IsPlayerInRaceCheckpoint(self.id)

    @property
    def virtual_world(self):
        return GetPlayerVirtualWorld(self.id)

    @virtual_world.setter
    def virtual_world(self, worldid):
        return SetPlayerVirtualWorld(self.id, worldid)

    def enable_stunt_bonus(self, enable):
        return EnableStuntBonusForPlayer(self.id, enable)

    def toggle_spectating(self, toggle):
        return TogglePlayerSpectating(self.id, toggle)

    def spectate(self, targetplayerid, mode=SPECTATE_MODE_NORMAL.get()):
        return PlayerSpectatePlayer(self.id, targetplayerid, mode)

    def spectate_vehicle(self, targetvehicleid, mode=SPECTATE_MODE_NORMAL.get()):
        return PlayerSpectateVehicle(self.id, targetvehicleid, mode)

    def start_recording_data(self, recordtype, recordname):
        return StartRecordingPlayerData(self.id, recordtype, recordname)

    def stop_recording_data(self):
        return StopRecordingPlayerData(self.id)

    def create_explosion(self, X, Y, Z, type, Radius):
        return CreateExplosionForPlayer(self.id, X, Y, Z, type, Radius)

    def edit_object(self, objectid):
        return EditObject(self.id, objectid)

    def edit_player_object(self, objectid):
        return EditPlayerObject(self.id, objectid)

    def select_object(self):
        return SelectObject(self.id)

    def cancel_edit(self):
        return CancelEdit(self.id)

    def create_object(self, modelid, x, y, z, rX, rY, rZ, DrawDistance=0.0):
        return CreatePlayerObject(self.id, modelid, x, y, z, rX, rY, rZ, DrawDistance)

    def attach_object_to_vehicle(self, objectid, vehicleid, fOffsetX, fOffsetY, fOffsetZ, fRotX, fRotY, RotZ):
        return AttachPlayerObjectToVehicle(self.id, objectid, vehicleid, fOffsetX, fOffsetY, fOffsetZ, fRotX, fRotY, RotZ)

    def get_object_pos(self, objectid):
        return GetPlayerObjectPos(self.id, objectid)

    def set_object_pos(self, objectid, x, y, z):
        return SetPlayerObjectPos(self.id, objectid, x, y, z)

    def get_object_rot(self, objectid):
        return GetPlayerObjectRot(self.id, objectid)

    def set_object_rot(self, objectid, rotX, rotY, rotZ):
        return SetPlayerObjectRot(self.id, objectid, rotX, rotY, rotZ)

    def get_object_model(self, objectid):
        return GetPlayerObjectModel(self.id, objectid)

    def set_object_no_camera_col(self, objectid):
        return SetPlayerObjectNoCameraCol(self.id, objectid)

    def is_valid_object(self, objectid):
        return IsValidPlayerObject(self.id, objectid)

    def destroy_object(self, objectid):
        return DestroyPlayerObject(self.id, objectid)

    def move_object(self, objectid, x, y, z, Speed, RotX=-1000.0, RotY=-1000.0, RotZ=-1000.0):
        return MovePlayerObject(self.id, objectid, x, y, z, Speed, RotX, RotY, RotZ)

    def stop_object(self, objectid):
        return StopPlayerObject(self.id, objectid)

    def is_object_moving(self, objectid):
        return IsPlayerObjectMoving(self.id, objectid)

    def set_object_material(self, objectid, materialindex, modelid, txdname, texturename, materialcolor=0):
        return SetPlayerObjectMaterial(self.id, objectid, materialindex, modelid, txdname, texturename, materialcolor=0)

    def set_object_material_text(self, objectid, text, materialindex=0, materialsize=OBJECT_MATERIAL_SIZE_256x128.get(),  fontface="Arial", fontsize=24, bold=True, fontcolor=0xFFFFFFFF, backcolor=0, textalignment=0):
        return SetPlayerObjectMaterialText(self.id, objectid, text, materialindex, materialsize, fontface, fontsize, bold, fontcolor, backcolor, textalignment)

    def send_client_message(self, color, message):
        return SendClientMessage(self.id, color, message)

    def send_message(self, senderid, message):
        return SendPlayerMessageToPlayer(self.id, senderid, message)

    def send_death_message(self, killer, killee, weapon):
        return SendDeathMessageToPlayer(self.id, killer, killee, weapon)

    def game_text(self, text, time, style):
        return GameTextForPlayer(self.id, text, time, style)

    @property
    def is_npc(self):
        return IsPlayerNPC(self.id)

    @property
    def is_admin(self):
        return IsPlayerAdmin(self.id)

    def kick(self):
        return Kick(self.id)

    def ban(self):
        return Ban(self.id)

    def ban_ex(self, reason):
        return BanEx(self.id, reason)

    @property
    def network_stats(self, size):
        return GetPlayerNetworkStats(self.id, size)

    def get_version(self, len):
        return GetPlayerVersion(self.id, len)

    def net_stats_get_connected_time(self):
        return NetStats_GetConnectedTime(self.id)

    def net_stats_messages_received(self):
        return NetStats_MessagesReceived(self.id)

    def net_stats_bytes_received(self):
        return NetStats_BytesReceived(self.id)

    def net_stats_messages_sent(self):
        return NetStats_MessagesSent(self.id)

    def net_stats_bytes_sent(self):
        return NetStats_BytesSent(self.id)

    def net_stats_messages_recv_per_second(self):
        return NetStats_MessagesRecvPerSecond(self.id)

    def net_stats_packet_loss_percent(self):
        return NetStats_PacketLossPercent(self.id)

    def net_stats_connection_status(self):
        return NetStats_ConnectionStatus(self.id)

    def net_stats_get_ip_port(self, ip_port_len):
        return NetStats_GetIpPort(self.id, ip_port_len)

    @property
    def menu(self):
        return GetPlayerMenu(self.id)

    def text_draw_show(self, text):
        return TextDrawShowForPlayer(self.id, text)

    def select_text_draw(self, hovercolor):
        return SelectTextDraw(self.id, hovercolor)

    def cancel_select_text_draw(self):
        return CancelSelectTextDraw(self.id)

    def gang_zone_show(self, zone, color):
        return GangZoneShowForPlayer(self.id, zone, color)

    def gang_zone_flash(self, zone, flashcolor):
        return GangZoneFlashForPlayer(self.id, zone, flashcolor)

    def gang_zone_stop_flash(self, zone):
        return GangZoneStopFlashForPlayer(self.id, zone)

    def show_dialog(self, dialogid, style, caption, info, button1, button2):
        return ShowPlayerDialog(self.id, dialogid, style, caption, info, button1, button2)

    def gpci(self, size):
        return gpci(self.id, size)

    def redirect_download(self, url):
        return RedirectDownload(self.id, url)

    def create_3d_text_label(self, text, color, x, y, z, drawDistance, attachedplayer=INVALID_PLAYER_ID.get(), attachedvehicle=INVALID_VEHICLE_ID.get(), testLOS=False):
        return CreatePlayer3DTextLabel(self.id, text, color, x, y, z, drawDistance, attachedplayer, attachedvehicle, testLOS)

    def delete_3d_text_label(self, id):
        return DeletePlayer3DTextLabel(self.id, id)

    def update_3d_text_label_text(self, id, color, text):
        return UpdatePlayer3DTextLabelText(self.id, id, color, text)

class Textdraw(object):
    def __init__(self, x, y, text):
        self.id = text_draw_create(x, y, text)
    
    def destroy(self):
        return TextDrawDestroy(self.id)

    def letter_size(self, x, y):
        return TextDrawLetterSize(self.id, x, y)

    def text_size(self, x, y):
        return TextDrawTextSize(self.id, x, y)

    def alignment(self, alignment):
        return TextDrawAlignment(self.id, alignment)

    def color(self, color):
        return TextDrawColor(self.id, color)

    def use_box(self, use):
        return TextDrawUseBox(self.id, use)

    def box_color(self, color):
        return TextDrawBoxColor(self.id, color)

    def set_shadow(self, size):
        return TextDrawSetShadow(self.id, size)

    def set_outline(self, size):
        return TextDrawSetOutline(self.id, size)

    def background_color(self, color):
        return TextDrawBackgroundColor(self.id, color)

    def font(self, font):
        return TextDrawFont(self.id, font)

    def set_proportional(self, set):
        return TextDrawSetProportional(self.id, set)

    def set_selectable(self, set):
        return TextDrawSetSelectable(self.id, set)

    def show_for_all(self):
        return TextDrawShowForAll(self.id)

    def hide_for_all(self):
        return TextDrawHideForAll(self.id)

    def set_string(self, string):
        return TextDrawSetString(self.id, string)

    def set_preview_model(self, modelindex):
        return TextDrawSetPreviewModel(self.id, modelindex)

    def set_preview_rot(self, fRotX, fRotY, fRotZ, fZoom=1.0):
        return TextDrawSetPreviewRot(self.id, fRotX, fRotY, fRotZ, fZoom=1.0)

    def set_preview_veh_col(self, color1, color2):
        return TextDrawSetPreviewVehCol(self.id, color1, color2)

class Vehicle(object):
    """
    Create a vehicle by using this class.

    Properties:
    --------
    - id
    - pos
    - z_angle
    - rotation_quat
    - params_ex
    - params_siren_state
    - params_car_doors
    - params_car_windows
    - health
    - trailer
    - model
    - velocity
    - damage_status
    - virtual_world
    __________________
    Methods:
    ---------
    - is_valid()
    - get_distance_from_point(x, y, z)
    - destroy()
    - is_streamed_in(forplayerid)
    - set_to_respawn()
    - link_to_interior(interiorid)
    - add_component(componentid)
    - remove_component(componentid)
    - change_color(color1, color2)
    - change_paintjob(paintjobid)
    - detach_trailer()
    - is_trailer_attached()
    - set_number_plate(text)
    - get_component_in_slot(slot)
    - repair()
    - set_angular_velocity(x, y, z)

    """
    def __init__(self, vehicletype, x, y, z, rotation, color1, color2, respawn_delay, addsiren=False):
        self.id = create_vehicle(
            vehicletype, x, y, z, rotation, color1, color2, respawn_delay, addsiren)

    def is_valid(self):
        return IsValidVehicle(self.id)
        
    def get_distance_from_point(self, x, y, z):
        return GetVehicleDistanceFromPoint(self.id, x, y, z)
        
    def destroy(self):
        return DestroyVehicle(self.id)
        
    def is_streamed_in(self, forplayerid):
        return IsVehicleStreamedIn(self.id, forplayerid)
        
    @property
    def pos(self):
        return GetVehiclePos(self.id)
        
    @pos.setter
    def pos(self, pos: tuple):
        try:
            x, y, z = pos
        except:
            raise ValueError("Pass position as a tuple: xx.pos = (x,y,z)")
        else:
            return SetVehiclePos(self.id, x, y, z)
        
    @property
    def z_angle(self):
        return GetVehicleZAngle(self.id)
        
    @z_angle.setter
    def z_angle(self, z_angle):
        return SetVehicleZAngle(self.id, z_angle)

    @property
    def rotation_quat(self):
        return GetVehicleRotationQuat(self.id)

    def set_params_for_player(self, playerid, objective, doorslocked):
        return SetVehicleParamsForPlayer(self.id, playerid, objective, doorslocked)

    @property
    def params_ex(self):
        return GetVehicleParamsEx(self.id)

    @params_ex.setter
    def params_ex(self, param: tuple):
        try:
            engine, lights, alarm, doors, bonnet, boot, objective = param
        except:
            raise ValueError("A tuple was expected: (engine, lights, alarm, doors, bonnet, boot, objective)")
        else:
            return SetVehicleParamsEx(self.id, engine, lights, alarm, doors, bonnet, boot, objective)

    @property
    def params_siren_state(self):
        return GetVehicleParamsSirenState(self.id)

    @property
    def params_car_doors(self):
        return GetVehicleParamsCarDoors(self.id)

    @params_car_doors.setter
    def params_car_doors(self, param: tuple):
        try:
            driver, passenger, backleft, backright = param
        except:
            raise ValueError("A tuple was expected: (driver, passenger, backleft, backright)")
        else:
            return SetVehicleParamsCarDoors(self.id, driver, passenger, backleft, backright)

    @property
    def params_car_windows(self):
        return GetVehicleParamsCarWindows(self.id)

    @params_car_windows.setter
    def params_car_windows(self, param: tuple):
        try:
            driver, passenger, backleft, backright = param
        except:
            raise ValueError("A tuple was expected: (driver, passenger, backleft, backright)")
        else:
            return SetVehicleParamsCarWindows(self.id, driver, passenger, backleft, backright)

    def set_to_respawn(self):
        return SetVehicleToRespawn(self.id)

    def link_to_interior(self, interiorid):
        return LinkVehicleToInterior(self.id, interiorid)

    def add_component(self, componentid):
        return AddVehicleComponent(self.id, componentid)

    def remove_component(self, componentid):
        return RemoveVehicleComponent(self.id, componentid)

    def change_color(self, color1, color2):
        return ChangeVehicleColor(self.id, color1, color2)

    def change_paintjob(self, paintjobid):
        return ChangeVehiclePaintjob(self.id, paintjobid)

    @property
    def health(self):
        return GetVehicleHealth(self.id)

    @health.setter
    def health(self, health):
        return SetVehicleHealth(self.id, health)

    def detach_trailer(self):
        return DetachTrailerFromVehicle(self.id)

    def is_trailer_attached(self):
        return IsTrailerAttachedToVehicle(self.id)

    @property
    def trailer(self):
        return GetVehicleTrailer(self.id)

    def set_number_plate(self, numberplate):
        return SetVehicleNumberPlate(self.id, numberplate)

    @property
    def model(self):
        return GetVehicleModel(self.id)

    def get_component_in_slot(self, slot):
        return GetVehicleComponentInSlot(self.id, slot)

    def repair(self):
        return RepairVehicle(self.id)

    @property
    def velocity(self):
        return GetVehicleVelocity(self.id)

    @velocity.setter
    def velocity(self, vector: tuple):
        try:
            X, Y, Z = vector
        except:
            raise ValueError("Expected a tuple for x,y,z: (x,y,z)")
        else:
            return SetVehicleVelocity(self.id, X, Y, Z)

    def set_angular_velocity(self, X, Y, Z):
        return SetVehicleAngularVelocity(self.id, X, Y, Z)

    @property
    def damage_status(self):
        return GetVehicleDamageStatus(self.id)

    @damage_status.setter
    def damage_status(self, param: tuple):
        try:
            panels, doors, lights, tires = param
        except:
            raise ValueError("Expected a tuple for damage_status: (panels, doors, lights, tires)")
        else:
            return UpdateVehicleDamageStatus(self.id, panels, doors, lights, tires)

    @property
    def virtual_world(self):
        return GetVehicleVirtualWorld(self.id)

    @virtual_world.setter
    def virtual_world(self, worldid):
        return SetVehicleVirtualWorld(self.id, worldid)