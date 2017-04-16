from pysamp import *
import pystate

def callback(name, arguments):
    """ calls callbacks remotely and waits for return value"""
    return False

def OnGameModeInit():
    return callback('OnGameModeInit', ())

def OnGameModeExit():
    return callback('OnGameModeExit', ())

def OnPlayerConnect(playerid):
    return callback('OnPlayerConnect', (playerid))

def OnPlayerDisconnect(playerid, reason):
    return callback('OnPlayerDisconnect', (playerid, reason))

def OnPlayerSpawn(playerid):
    return callback('OnPlayerSpawn', (playerid))

def OnPlayerDeath(playerid, killerid, reason):
    return callback('OnPlayerDeath', (playerid, killerid, reason))

def OnVehicleSpawn(vehicleid):
    return callback('OnVehicleSpawn', (vehicleid))

def OnVehicleDeath(vehicleid, killerid):
    return callback('OnVehicleDeath', (vehicleid, killerid))

def OnPlayerText(playerid, text):
    return callback('OnPlayerText', (playerid, text))

def OnPlayerCommandText(playerid, cmdtext):
    return callback('OnPlayerCommandText', (playerid, cmdtext))

def OnPlayerRequestClass(playerid, classid):
    return callback('OnPlayerRequestClass', (playerid, classid))

def OnPlayerEnterVehicle(playerid, vehicleid, ispassenger):
    return callback('OnPlayerEnterVehicle', (playerid, vehicleid, ispassenger))

def OnPlayerExitVehicle(playerid, vehicleid):
    return callback('OnPlayerExitVehicle', (playerid, vehicleid))

def OnPlayerStateChange(playerid, newstate, oldstate):
    return callback('OnPlayerStateChange', (playerid, newstate, oldstate))

def OnPlayerEnterCheckpoint(playerid):
    return callback('OnPlayerEnterCheckpoint', (playerid))

def OnPlayerLeaveCheckpoint(playerid):
    return callback('OnPlayerLeaveCheckpoint', (playerid))

def OnPlayerEnterRaceCheckpoint(playerid):
    return callback('OnPlayerEnterRaceCheckpoint', (playerid))

def OnPlayerLeaveRaceCheckpoint(playerid):
    return callback('OnPlayerLeaveRaceCheckpoint', (playerid))

def OnRconCommand(cmd):
    return callback('OnRconCommand', (cmd))

def OnPlayerRequestSpawn(playerid):
    return callback('OnPlayerRequestSpawn', (playerid))

def OnObjectMoved(objectid):
    return callback('OnObjectMoved', (objectid))

def OnPlayerObjectMoved(playerid, objectid):
    return callback('OnPlayerObjectMoved', (playerid, objectid))

def OnPlayerPickUpPickup(playerid, pickupid):
    return callback('OnPlayerPickUpPickup', (playerid, pickupid))

def OnVehicleMod(playerid, vehicleid, componentid):
    return callback('OnVehicleMod', (playerid, vehicleid, componentid))

def OnEnterExitModShop(playerid, enterexit, interiorid):
    return callback('OnEnterExitModShop', (playerid, enterexit, interiorid))

def OnVehiclePaintjob(playerid, vehicleid, paintjobid):
    return callback('OnVehiclePaintjob', (playerid, vehicleid, paintjobid))

def OnVehicleRespray(playerid, vehicleid, color1, color2):
    return callback('OnVehicleRespray', (playerid, vehicleid, color1, color2))

def OnVehicleDamageStatusUpdate(vehicleid, playerid):
    return callback('OnVehicleDamageStatusUpdate', (vehicleid, playerid))

def OnUnoccupiedVehicleUpdate(vehicleid, playerid, passenger_seat, new_x, new_y, new_z, vel_x, vel_y, vel_z):
    return callback('OnUnoccupiedVehicleUpdate', (vehicleid, playerid, passenger_seat, new_x, new_y, new_z, vel_x, vel_y, vel_z))

def OnPlayerSelectedMenuRow(playerid, row):
    return callback('OnPlayerSelectedMenuRow', (playerid, row))

def OnPlayerExitedMenu(playerid):
    return callback('OnPlayerExitedMenu', (playerid))

def OnPlayerInteriorChange(playerid, newinteriorid, oldinteriorid):
    return callback('OnPlayerInteriorChange', (playerid, newinteriorid, oldinteriorid))

def OnPlayerKeyStateChange(playerid, newkeys, oldkeys):
    return callback('OnPlayerKeyStateChange', (playerid, newkeys, oldkeys))

def OnRconLoginAttempt(ip, password, success):
    return callback('OnRconLoginAttempt', (ip, password, success))

def OnPlayerUpdate(playerid):
    return callback('OnPlayerUpdate', (playerid))

def OnPlayerStreamIn(playerid, forplayerid):
    return callback('OnPlayerStreamIn', (playerid, forplayerid))

def OnPlayerStreamOut(playerid, forplayerid):
    return callback('OnPlayerStreamOut', (playerid, forplayerid))

def OnVehicleStreamIn(vehicleid, forplayerid):
    return callback('OnVehicleStreamIn', (vehicleid, forplayerid))

def OnVehicleStreamOut(vehicleid, forplayerid):
    return callback('OnVehicleStreamOut', (vehicleid, forplayerid))

def OnActorStreamIn(actorid, forplayerid):
    return callback('OnActorStreamIn', (actorid, forplayerid))

def OnActorStreamOut(actorid, forplayerid):
    return callback('OnActorStreamOut', (actorid, forplayerid))

def OnDialogResponse(playerid, dialogid, response, listitem, inputtext):
    return callback('OnDialogResponse', (playerid, dialogid, response, listitem, inputtext))

def OnPlayerTakeDamage(playerid, issuerid, amount, weaponid, bodypart):
    return callback('OnPlayerTakeDamage', (playerid, issuerid, amount, weaponid, bodypart))

def OnPlayerGiveDamage(playerid, damagedid, amount, weaponid, bodypart):
    return callback('OnPlayerGiveDamage', (playerid, damagedid, amount, weaponid, bodypart))

def OnPlayerGiveDamageActor(playerid, damaged_actorid, amount, weaponid, bodypart):
    return callback('OnPlayerGiveDamageActor', (playerid, damaged_actorid, amount, weaponid, bodypart))

def OnPlayerClickMap(playerid, fX, fY, fZ):
    return callback('OnPlayerClickMap', (playerid, fX, fY, fZ))

def OnPlayerClickTextDraw(playerid, clickedid):
    return callback('OnPlayerClickTextDraw', (playerid, clickedid))

def OnPlayerClickPlayerTextDraw(playerid, playertextid):
    return callback('OnPlayerClickPlayerTextDraw', (playerid, playertextid))

def OnIncomingConnection(playerid, ip_address, port):
    return callback('OnIncomingConnection', (playerid, ip_address, port))

def OnTrailerUpdate(playerid, vehicleid):
    return callback('OnTrailerUpdate', (playerid, vehicleid))

def OnVehicleSirenStateChange(playerid, vehicleid, newstate):
    return callback('OnVehicleSirenStateChange', (playerid, vehicleid, newstate))

def OnPlayerClickPlayer(playerid, clickedplayerid, source):
    return callback('OnPlayerClickPlayer', (playerid, clickedplayerid, source))

def OnPlayerEditObject(playerid, playerobject, objectid, response, fX, fY, fZ, fRotX, fRotY, fRotZ):
    return callback('OnPlayerEditObject', (playerid, playerobject, objectid, response, fX, fY, fZ, fRotX, fRotY, fRotZ))

def OnPlayerEditAttachedObject(playerid, response, index, modelid, boneid, fOffsetX, fOffsetY, fOffsetZ, fRotX, fRotY, fRotZ, fScaleX, fScaleY, fScaleZ):
    return callback('OnPlayerEditAttachedObject', (playerid, response, index, modelid, boneid, fOffsetX, fOffsetY, fOffsetZ, fRotX, fRotY, fRotZ, fScaleX, fScaleY, fScaleZ))

def OnPlayerSelectObject(playerid, otype, objectid, modelid, fX, fY, fZ):
    return callback('OnPlayerSelectObject', (playerid, otype, objectid, modelid, fX, fY, fZ))

def OnPlayerWeaponShot(playerid, weaponid, hittype, hitid, fX, fY, fZ):
    return callback('OnPlayerWeaponShot', (playerid, weaponid, hittype, hitid, fX, fY, fZ))
