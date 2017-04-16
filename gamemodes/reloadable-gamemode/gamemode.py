from pysamp import *
#import pystate
import re
import imp
import pymode


def callback(name, arguments):
    """ calls callbacks remotely and waits for return value"""
    try:
        func = getattr(pymode, name)
        return func(*arguments)  
    except AttributeError as err:
        print(err)
    return False

def callback_single(name, argument):
    """ calls callbacks remotely and waits for return value"""
    try:
        func = getattr(pymode, name)
        return func(argument)  

    except AttributeError as err:
        print(err)
    return False

def callback_none(name):
    """ calls callbacks remotely and waits for return value"""
    try:
        func = getattr(pymode, name)
        return func()

    except AttributeError as err:
        print(err)
    return False

def OnGameModeInit():
    SetGameModeText("Funnymode 2.0");
    AddPlayerClass(0, 1958.3783, 1343.1572, 15.3746, 269.1425, 0, 0, 0, 0, 0, 0);
    AddPlayerClass(18, 1960.3783, 1343.1572, 15.3746, 269.1425, 0, 0, 0, 0, 0, 0)
    AddPlayerClass(0,1585.1819,-1674.7336,5.8949,176.0211,0,0,0,0,0,0)
    return callback_none('OnGameModeInit')

def OnGameModeExit():
    return callback_none('OnGameModeExit')

def OnPlayerConnect(playerid):
    return callback_single('OnPlayerConnect', (playerid))

def OnPlayerDisconnect(playerid, reason):
    return callback('OnPlayerDisconnect', (playerid, reason))

def OnPlayerSpawn(playerid):
    return callback_single('OnPlayerSpawn', (playerid))

def OnPlayerDeath(playerid, killerid, reason):
    return callback('OnPlayerDeath', (playerid, killerid, reason))

def OnVehicleSpawn(vehicleid):
    return callback_single('OnVehicleSpawn', (vehicleid))

def OnVehicleDeath(vehicleid, killerid):
    return callback('OnVehicleDeath', (vehicleid, killerid))

def OnPlayerText(playerid, text):
    return callback('OnPlayerText', (playerid, text))

def OnPlayerCommandText(playerid, cmdtext):
    if cmdtext == '/pyreload':
        imp.reload(pymode)
        print('reloading pymode')
        return True
    elif(cmdtext == "/v"):
        RX = GetPlayerFacingAngle(playerid)
        (X,Y,Z) = GetPlayerPos(playerid)
        CreateVehicle(400, X, Y, Z, RX+90, 0, 0, 100000)		
        #LinkVehicleToInterior(in, GetPlayerInterior(playerid)
        SendClientMessage(playerid, 0, 'Spawned')
        return True	

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
    return callback_single('OnPlayerEnterCheckpoint', (playerid))

def OnPlayerLeaveCheckpoint(playerid):
    return callback_single('OnPlayerLeaveCheckpoint', (playerid))

def OnPlayerEnterRaceCheckpoint(playerid):
    return callback_single('OnPlayerEnterRaceCheckpoint', (playerid))

def OnPlayerLeaveRaceCheckpoint(playerid):
    return callback_single('OnPlayerLeaveRaceCheckpoint', (playerid))

def OnRconCommand(cmd):
    return callback_single('OnRconCommand', (cmd))

def OnPlayerRequestSpawn(playerid):
    return callback_single('OnPlayerRequestSpawn', (playerid))

def OnObjectMoved(objectid):
    return callback_single('OnObjectMoved', (objectid))

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
    return callback_single('OnPlayerExitedMenu', (playerid))

def OnPlayerInteriorChange(playerid, newinteriorid, oldinteriorid):
    return callback('OnPlayerInteriorChange', (playerid, newinteriorid, oldinteriorid))

def OnPlayerKeyStateChange(playerid, newkeys, oldkeys):
    return callback('OnPlayerKeyStateChange', (playerid, newkeys, oldkeys))

def OnRconLoginAttempt(ip, password, success):
    return callback('OnRconLoginAttempt', (ip, password, success))

def OnPlayerUpdate(playerid):
    return callback_single('OnPlayerUpdate', (playerid))

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
