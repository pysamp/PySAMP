from pysamp import *

def OnGameModeInit():
    return True
    
def OnGameModeExit():
    return True
    
def OnPlayerConnect(playerid):
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
    return True
    
def OnPlayerText(playerid, text):
    return True
    
def OnPlayerCommandText(playerid, cmdtext):
    return False
    
def OnPlayerRequestClass(playerid, classid):
    return True
    
def OnPlayerEnterVehicle(playerid, vehicleid, ispassenger):
    return True
    
def OnPlayerExitVehicle(playerid, vehicleid):
    return True
    
def OnPlayerStateChange(playerid, newstate, oldstate):
    return True
    
def OnPlayerEnterCheckpoint(playerid):
    return True
    
def OnPlayerLeaveCheckpoint(playerid):
    return True
    
def OnPlayerEnterRaceCheckpoint(playerid):
    return True
    
def OnPlayerLeaveRaceCheckpoint(playerid):
    return True
    
def OnRconCommand(cmd):
    return False
    
def OnPlayerRequestSpawn(playerid):
    return True
    
def OnObjectMoved(objectid):
    return True
    
def OnPlayerObjectMoved(playerid, objectid):
    return True
    
def OnPlayerPickUpPickup(playerid, pickupid):
    return True
    
def OnVehicleMod(playerid, vehicleid, componentid):
    return True
    
def OnEnterExitModShop(playerid, enterexit, interiorid):
    return True
    
def OnVehiclePaintjob(playerid, vehicleid, paintjobid):
    return True
    
def OnVehicleRespray(playerid, vehicleid, color1, color2):
    return True
    
def OnVehicleDamageStatusUpdate(vehicleid, playerid):
    return False
    
def OnUnoccupiedVehicleUpdate(vehicleid, playerid, passenger_seat, new_x, new_y, new_z, vel_x, vel_y, vel_z):
    return True
    
def OnPlayerSelectedMenuRow(playerid, row):
    return True
    
def OnPlayerExitedMenu(playerid):
    return True
    
def OnPlayerInteriorChange(playerid, newinteriorid, oldinteriorid):
    return True
    
def OnPlayerKeyStateChange(playerid, newkeys, oldkeys):
    return True
    
def OnRconLoginAttempt(ip, password, success):
    return True
    
def OnPlayerUpdate(playerid):
    return True
    
def OnPlayerStreamIn(playerid, forplayerid):
    return True
    
def OnPlayerStreamOut(playerid, forplayerid):
    return True
    
def OnVehicleStreamIn(vehicleid, forplayerid):
        return True
        
def OnVehicleStreamOut(vehicleid, forplayerid):
    return True
    
def OnActorStreamIn(actorid, forplayerid):
    return True
    
def OnActorStreamOut(actorid, forplayerid):
    return True
    
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
    return False
    
def OnTrailerUpdate(playerid, vehicleid):
    return True
    
def OnVehicleSirenStateChange(playerid, vehicleid, newstate):
    return True
    
def OnPlayerClickPlayer(playerid, clickedplayerid, source):
    return False
    
def OnPlayerEditObject(playerid, playerobject, objectid, response, fX, fY, fZ, fRotX, fRotY, fRotZ):
    return False
    
def OnPlayerEditAttachedObject(playerid, response, index, modelid, boneid, fOffsetX, fOffsetY, fOffsetZ, fRotX, fRotY, fRotZ, fScaleX, fScaleY, fScaleZ):
    return False
    
def OnPlayerSelectObject(playerid, type, objectid, modelid, fX, fY, fZ):
    return False
    
def OnPlayerWeaponShot(playerid, weaponid, hittype, hitid, fX, fY, fZ):
    return False

def OnProcessTick():
    return None

""" you can initialize your own additional threads here, note that OnThreadingInit isn't supposed to be a worker thread but gives you the ability to start them. Otherwise it would block the plugin initialization """
def OnThreadingInit():
    return None

""" your initialized threads must be shutdown during this callbac """
def OnThreadingStopSignal():
    return None