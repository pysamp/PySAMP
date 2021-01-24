from samp import *
from const import *

def OnGameModeInit():
    SetGameModeText('PySAMP')
    return True
    
def OnGameModeExit():
    return True

def OnPyUnload():
    OnGameModeExit()
    return True

def OnPyReload():
    OnGameModeInit()
    return True

def OnPlayerConnect(playerid):
    SendClientMessage(playerid, 0xFF000000, "Hello %s from Python" % GetPlayerName(playerid, MAX_PLAYER_NAME.get()))
    return True
    
def OnPlayerDisconnect(playerid, reason):
    return True
    
def OnPlayerSpawn(playerid):
    return True
    
def OnPlayerDeath(playerid, killerid, reason):
    return True
    
def OnVehicleSpawn(vehicleid):
    return True
    
def OnVehicleDeath(vehicleid, killerid):
    return False
    
def OnPlayerText(playerid, text):
    text = decode(text)
    return False
    
def OnPlayerCommandText(playerid, cmdtext):
    cmdtext = decode(cmdtext)
    return False
    
def OnPlayerRequestClass(playerid, classid):
    return True
    
def OnPlayerEnterVehicle(playerid, vehicleid, ispassenger):
    return False
    
def OnPlayerExitVehicle(playerid, vehicleid):
    return False
    
def OnPlayerStateChange(playerid, newstate, oldstate):
    return False
    
def OnPlayerEnterCheckpoint(playerid):
    return False
    
def OnPlayerLeaveCheckpoint(playerid):
    return False
    
def OnPlayerEnterRaceCheckpoint(playerid):
    return False
    
def OnPlayerLeaveRaceCheckpoint(playerid):
    return False
    
def OnRconCommand(cmd):
    cmd = decode(cmd)
    return False
    
def OnPlayerRequestSpawn(playerid):
    return True
    
def OnObjectMoved(objectid):
    return False
    
def OnPlayerObjectMoved(playerid, objectid):
    return False
    
def OnPlayerPickUpPickup(playerid, pickupid):
    return False
    
def OnVehicleMod(playerid, vehicleid, componentid):
    return True
    
def OnEnterExitModShop(playerid, enterexit, interiorid):
    return False
    
def OnVehiclePaintjob(playerid, vehicleid, paintjobid):
    return True
    
def OnVehicleRespray(playerid, vehicleid, color1, color2):
    return True
    
def OnVehicleDamageStatusUpdate(vehicleid, playerid):
    return False
    
def OnUnoccupiedVehicleUpdate(vehicleid, playerid, passenger_seat, new_x, new_y, new_z, vel_x, vel_y, vel_z):
    return True
    
def OnPlayerSelectedMenuRow(playerid, row):
    return False
    
def OnPlayerExitedMenu(playerid):
    return False
    
def OnPlayerInteriorChange(playerid, newinteriorid, oldinteriorid):
    return False
    
def OnPlayerKeyStateChange(playerid, newkeys, oldkeys):
    return False
    
def OnRconLoginAttempt(ip, password, success):
    password = decode(password)
    return False
    
def OnPlayerUpdate(playerid):
    return True
    
def OnPlayerStreamIn(playerid, forplayerid):
    return False
    
def OnPlayerStreamOut(playerid, forplayerid):
    return False
    
def OnVehicleStreamIn(vehicleid, forplayerid):
    return False
        
def OnVehicleStreamOut(vehicleid, forplayerid):
    return False
    
def OnActorStreamIn(actorid, forplayerid):
    return False
    
def OnActorStreamOut(actorid, forplayerid):
    return False
    
def OnDialogResponse(playerid, dialogid, response, listitem, inputtext):
    return False
    
def OnPlayerTakeDamage(playerid, issuerid, amount, weaponid, bodypart):
    return False
    
def OnPlayerGiveDamage(playerid, damagedid, amount, weaponid, bodypart):
    return False
    
def OnPlayerGiveDamageActor(playerid, damaged_actorid, amount, weaponid, bodypart):
    return False
    
def OnPlayerClickMap(playerid, fX, fY, fZ):
    return False
    
def OnPlayerClickTextDraw(playerid, clickedid):
    return False
    
def OnPlayerClickPlayerTextDraw(playerid, playertextid):
    return False
    
def OnIncomingConnection(playerid, ip_address, port):
    ip_address = decode(ip_address)
    return False
    
def OnTrailerUpdate(playerid, vehicleid):
    return True
    
def OnVehicleSirenStateChange(playerid, vehicleid, newstate):
    return False
    
def OnPlayerClickPlayer(playerid, clickedplayerid, source):
    return False
    
def OnPlayerEditObject(playerid, playerobject, objectid, response, fX, fY, fZ, fRotX, fRotY, fRotZ):
    return False
    
def OnPlayerEditAttachedObject(playerid, response, index, modelid, boneid, fOffsetX, fOffsetY, fOffsetZ, fRotX, fRotY, fRotZ, fScaleX, fScaleY, fScaleZ):
    return False
    
def OnPlayerSelectObject(playerid, type, objectid, modelid, fX, fY, fZ):
    return False
    
def OnPlayerWeaponShot(playerid, weaponid, hittype, hitid, fX, fY, fZ):
    return True

def OnProcessTick():
    return None

""" you can initialize your own additional threads here, note that OnThreadingInit isn't supposed to be a worker thread but gives you the ability to start them. Otherwise it would block the plugin initialization """
def OnThreadingInit():
    return None

""" your initialized threads must be shutdown during this callbac """
def OnThreadingStopSignal():
    return None