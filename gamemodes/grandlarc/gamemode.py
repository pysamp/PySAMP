import random
from samp import *
from glspawns import *
from funcs import *
from vars import *
from player import *

################################
"""
Hello dear user! 
Welcome to the Python version of the original Grand Larceny gamemode!
We wanted to convert this classic gamemode into what it would look like
in python, and here is the result. We took our liberty to nick it "PyLarc".

The intention behind converting it, was to give you all an idea of how the plugin works,
and to give you all a good example.

We have tried to show how player classes can be implemented (check player.py), and
also how the general usage works. 

Everything here should function as in the original PAWN version, and if you 
find any bugs, you can report them on our repo; https://github.com/habecker/PySAMP/issues

For now, enjoy the code, and good luck!
denNorske & Habecker
"""
################################


def OnGameModeInit():
    SetGameModeText('PyLarc')
    print("-----------------------------------------------")
    print("Running Grand Larceny - by the SA-MP team\nRe-written to python 3.8.6 by the PySAMP Team")
    print("-----------------------------------------------")
    ShowPlayerMarkers(1) # PLAYER_MARKERS_MODE_GLOBAL = 1
    ShowNameTags(True)
    SetNameTagDrawDistance(40)
    EnableStuntBonusForAll(False)
    DisableInteriorEnterExits()
    SetWeather(2)
    #LimitGlobalChatRadius(300.0)
    
    ClassSel_InitTextDraws()

    # Player Class
    AddPlayerClass(1,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    AddPlayerClass(2,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    AddPlayerClass(47,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    AddPlayerClass(48,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    AddPlayerClass(49,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    AddPlayerClass(50,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    AddPlayerClass(51,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    AddPlayerClass(52,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    AddPlayerClass(53,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    AddPlayerClass(54,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    AddPlayerClass(55,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    AddPlayerClass(56,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    AddPlayerClass(57,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    AddPlayerClass(58,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    AddPlayerClass(68,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    AddPlayerClass(69,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    AddPlayerClass(70,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    AddPlayerClass(71,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    AddPlayerClass(72,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    AddPlayerClass(73,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    AddPlayerClass(75,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    AddPlayerClass(76,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    AddPlayerClass(78,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    AddPlayerClass(79,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    AddPlayerClass(80,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    AddPlayerClass(81,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    AddPlayerClass(82,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    AddPlayerClass(83,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    AddPlayerClass(84,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    AddPlayerClass(85,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    AddPlayerClass(87,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    AddPlayerClass(88,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    AddPlayerClass(89,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    AddPlayerClass(91,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    AddPlayerClass(92,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    AddPlayerClass(93,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    AddPlayerClass(95,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    AddPlayerClass(96,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    AddPlayerClass(97,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    AddPlayerClass(98,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    AddPlayerClass(99,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    AddPlayerClass(269,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    AddPlayerClass(270,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    AddPlayerClass(271,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    AddPlayerClass(272,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)

    total_vehicles_from_files = (
    # SPECIAL:
    LoadStaticVehiclesFromFile("scriptfiles/vehicles/trains.txt")       + 
    LoadStaticVehiclesFromFile("scriptfiles/vehicles/pilots.txt")       + 
    # Las Venturas
    LoadStaticVehiclesFromFile("scriptfiles/vehicles/lv_law.txt")       +  
    LoadStaticVehiclesFromFile("scriptfiles/vehicles/lv_airport.txt")   + 
    LoadStaticVehiclesFromFile("scriptfiles/vehicles/lv_gen.txt")       + 
    # San fierro
    LoadStaticVehiclesFromFile("scriptfiles/vehicles/sf_law.txt")       + 
    LoadStaticVehiclesFromFile("scriptfiles/vehicles/sf_airport.txt")   + 
    LoadStaticVehiclesFromFile("scriptfiles/vehicles/sf_gen.txt")       + 
    # Los Santos
    LoadStaticVehiclesFromFile("scriptfiles/vehicles/ls_law.txt")       +  
    LoadStaticVehiclesFromFile("scriptfiles/vehicles/ls_airport.txt")   + 
    LoadStaticVehiclesFromFile("scriptfiles/vehicles/ls_gen_inner.txt") + 
    LoadStaticVehiclesFromFile("scriptfiles/vehicles/ls_gen_outer.txt") + 
    # Other areas
    LoadStaticVehiclesFromFile("scriptfiles/vehicles/whetstone.txt")    + 
    LoadStaticVehiclesFromFile("scriptfiles/vehicles/bone.txt")         + 
    LoadStaticVehiclesFromFile("scriptfiles/vehicles/flint.txt")        + 
    LoadStaticVehiclesFromFile("scriptfiles/vehicles/tierra.txt")       + 
    LoadStaticVehiclesFromFile("scriptfiles/vehicles/red_county.txt"))


    print("Total vehicles from files: {}".format(total_vehicles_from_files))
    return True
    
def OnGameModeExit():
    return True


def OnPlayerConnect(playerid):
    GameTextForPlayer(playerid,"~w~Grand Larceny",3000,4)
    SendClientMessage(playerid,COLOR_WHITE,"Welcome to Grand Larceny")
    _player_obj = Player(playerid, -1, False, GetTickCount())
    players.append(_player_obj)
    return True
    
def OnPlayerDisconnect(playerid, reason):
    for player in players:
        if player.playerid == playerid:
            players.remove(player)
            break
    return True
    
def OnPlayerSpawn(playerid):
    if IsPlayerNPC(playerid):
        return True
    randspawn = 0
    SetPlayerInterior(playerid, 0)
    TogglePlayerClock(playerid, 0)
    ResetPlayerMoney(playerid)
    GivePlayerMoney(playerid, 30000)


    for player in players:
        if player.playerid == playerid:
            player.has_city_selected = False
    
            if player.city_selection == CITY_LOS_SANTOS:
                randspawn = random.randint(0, len(gRandomSpawns_LosSantos))
                SetPlayerPos(playerid, 
                    gRandomSpawns_LosSantos[randspawn][0], 
                    gRandomSpawns_LosSantos[randspawn][1], 
                    gRandomSpawns_LosSantos[randspawn][2]
                )
            elif player.city_selection == CITY_SAN_FIERRO:
                randspawn = random.randint(0, len(gRandomSpawns_SanFierro))
                SetPlayerPos(playerid, 
                    gRandomSpawns_SanFierro[randspawn][0], 
                    gRandomSpawns_SanFierro[randspawn][1], 
                    gRandomSpawns_SanFierro[randspawn][2]
                )
            elif player.city_selection == CITY_LAS_VENTURAS:
                randspawn = random.randint(0, len(gRandomSpawns_LasVenturas))
                SetPlayerPos(playerid, 
                    gRandomSpawns_LasVenturas[randspawn][0], 
                    gRandomSpawns_LasVenturas[randspawn][1], 
                    gRandomSpawns_LasVenturas[randspawn][2]
                )
    SetPlayerSkillLevel(playerid,Const("WEAPONSKILL_PISTOL"),200)
    SetPlayerSkillLevel(playerid,Const("WEAPONSKILL_PISTOL_SILENCED"),200)
    SetPlayerSkillLevel(playerid,Const("WEAPONSKILL_DESERT_EAGLE"),200)
    SetPlayerSkillLevel(playerid,Const("WEAPONSKILL_SHOTGUN"),200)
    SetPlayerSkillLevel(playerid,Const("WEAPONSKILL_SAWNOFF_SHOTGUN"),200)
    SetPlayerSkillLevel(playerid,Const("WEAPONSKILL_SPAS12_SHOTGUN"),200)
    SetPlayerSkillLevel(playerid,Const("WEAPONSKILL_MICRO_UZI"),200)
    SetPlayerSkillLevel(playerid,Const("WEAPONSKILL_MP5"),200)
    SetPlayerSkillLevel(playerid,Const("WEAPONSKILL_AK47"),200)
    SetPlayerSkillLevel(playerid,Const("WEAPONSKILL_M4"),200)
    SetPlayerSkillLevel(playerid,Const("WEAPONSKILL_SNIPERRIFLE"),200)
    
    GivePlayerWeapon(playerid,22,100) # Colt 45            
    return True

def OnPlayerDeath(playerid, killerid, reason):
    if killerid == 65535:
        ResetPlayerMoney(playerid)
    else:
        GivePlayerMoney(killerid, GetPlayerMoney(playerid))
        ResetPlayerMoney(playerid)
    return True

# Used to init textdraws of city names
def ClassSel_InitCityNameText(txtInit):
    global txtClassSelHelper
    TextDrawUseBox(txtInit, 0)
    TextDrawLetterSize(txtInit,1.25,3.0)
    TextDrawFont(txtInit, 0)
    TextDrawSetShadow(txtInit,0)
    TextDrawSetOutline(txtInit,1)
    TextDrawColor(txtInit,4008636159)
    TextDrawBackgroundColor(txtClassSelHelper,255)
    return

def ClassSel_InitTextDraws():
    global txtLosSantos
    global txtSanFierro
    global txtLasVenturas
    global txtClassSelHelper
    # Init our observer helper text display
    txtLosSantos = TextDrawCreate(10.0, 380.0, "Los Santos")
    ClassSel_InitCityNameText(txtLosSantos)
    txtSanFierro = TextDrawCreate(10.0, 380.0, "San Fierro")
    ClassSel_InitCityNameText(txtSanFierro)
    txtLasVenturas = TextDrawCreate(10.0, 380.0, "Las Venturas")
    ClassSel_InitCityNameText(txtLasVenturas)

    # Init our observer helper text display
    txtClassSelHelper = TextDrawCreate(10.0, 415.0,
        " Press ~b~~k~~GO_LEFT~ ~w~or ~b~~k~~GO_RIGHT~ ~w~to switch cities.~n~ Press ~r~~k~~PED_FIREWEAPON~ ~w~to select.")
    TextDrawUseBox(txtClassSelHelper, 1)
    TextDrawBoxColor(txtClassSelHelper,572662459)
    TextDrawLetterSize(txtClassSelHelper,0.3,1.0)
    TextDrawTextSize(txtClassSelHelper,400.0,40.0)
    TextDrawFont(txtClassSelHelper, 2)
    TextDrawSetShadow(txtClassSelHelper,0)
    TextDrawSetOutline(txtClassSelHelper,1)
    TextDrawBackgroundColor(txtClassSelHelper,255)
    TextDrawColor(txtClassSelHelper,4294967295)
    return


def ClassSel_SetupCharSelection(playerid):
    for player in players:
        if player.playerid == playerid:
            if player.city_selection == CITY_LOS_SANTOS:
                SetPlayerInterior(playerid,11)
                SetPlayerPos(playerid,508.7362,-87.4335,998.9609)
                SetPlayerFacingAngle(playerid,0.0)
                SetPlayerCameraPos(playerid,508.7362,-83.4335,998.9609)
                SetPlayerCameraLookAt(playerid,508.7362,-87.4335,998.9609)
            
            elif player.city_selection == CITY_SAN_FIERRO:
                SetPlayerInterior(playerid,3)
                SetPlayerPos(playerid,-2673.8381,1399.7424,918.3516)
                SetPlayerFacingAngle(playerid,181.0)
                SetPlayerCameraPos(playerid,-2673.2776,1394.3859,918.3516)
                SetPlayerCameraLookAt(playerid,-2673.8381,1399.7424,918.3516)
            
            elif player.city_selection == CITY_LAS_VENTURAS:
                SetPlayerInterior(playerid,3)
                SetPlayerPos(playerid,349.0453,193.2271,1014.1797)
                SetPlayerFacingAngle(playerid,286.25)
                SetPlayerCameraPos(playerid,352.9164,194.5702,1014.1875)
                SetPlayerCameraLookAt(playerid,349.0453,193.2271,1014.1797)
            break
    return

def ClassSel_SetupSelectedCity(playerid):
    global txtLosSantos
    global txtSanFierro
    global txtLasVenturas

    for player in players:
        if player.playerid == playerid:
            if player.city_selection == -1:
                player.city_selection = CITY_LOS_SANTOS
            
            if player.city_selection == CITY_LOS_SANTOS:
                SetPlayerInterior(playerid,0)
                SetPlayerCameraPos(playerid,1630.6136,-2286.0298,110.0)
                SetPlayerCameraLookAt(playerid,1887.6034,-1682.1442,47.6167)

                TextDrawShowForPlayer(playerid,txtLosSantos)
                TextDrawHideForPlayer(playerid,txtSanFierro)
                TextDrawHideForPlayer(playerid,txtLasVenturas)

            elif player.city_selection == CITY_SAN_FIERRO:
                SetPlayerInterior(playerid,0)
                SetPlayerCameraPos(playerid,-1300.8754,68.0546,129.4823)
                SetPlayerCameraLookAt(playerid,-1817.9412,769.3878,132.6589)

                TextDrawHideForPlayer(playerid,txtLosSantos)
                TextDrawShowForPlayer(playerid,txtSanFierro)
                TextDrawHideForPlayer(playerid,txtLasVenturas)

            elif player.city_selection == CITY_LAS_VENTURAS:
                SetPlayerInterior(playerid,0)
                SetPlayerCameraPos(playerid,1310.6155,1675.9182,110.7390)
                SetPlayerCameraLookAt(playerid,2285.2944,1919.3756,68.2275)

                TextDrawHideForPlayer(playerid,txtLosSantos)
                TextDrawHideForPlayer(playerid,txtSanFierro)
                TextDrawShowForPlayer(playerid,txtLasVenturas)
            break
    return

def ClassSel_SwitchToNextCity(playerid):

    for player in players:
        if player.playerid == playerid:
            player.last_city_selection_tick = GetTickCount()
            player.city_selection += 1
            if player.city_selection > CITY_LAS_VENTURAS:
                    player.city_selection = CITY_LOS_SANTOS
            break
    
    PlayerPlaySound(playerid,1052,0.0,0.0,0.0)
    ClassSel_SetupSelectedCity(playerid)
    return

def ClassSel_SwitchToPreviousCity(playerid):
    for player in players:
        if player.playerid == playerid:
            player.last_city_selection_tick = GetTickCount()
            player.city_selection -= 1
            if player.city_selection < CITY_LOS_SANTOS:
                    player.city_selection = CITY_LAS_VENTURAS
            break

    PlayerPlaySound(playerid,1053,0.0,0.0,0.0)
    ClassSel_SetupSelectedCity(playerid)
    return

def ClassSel_HandleCitySelection(playerid):
    global txtLosSantos
    global txtSanFierro
    global txtLasVenturas
    global txtClassSelHelper
    (Keys, ud, lr) = GetPlayerKeys(playerid)
    for player in players:
        if player.playerid == playerid:
            # only allow selection every ~500 ms
            if GetTickCount() - player.last_city_selection_tick < 500:
                break
            if player.city_selection == -1 : 
                ClassSel_SwitchToNextCity(playerid)
                break
            if Keys & 4 :
                player.has_city_selected = True
                TextDrawHideForPlayer(playerid,txtClassSelHelper)
                TextDrawHideForPlayer(playerid,txtLosSantos)
                TextDrawHideForPlayer(playerid,txtSanFierro)
                TextDrawHideForPlayer(playerid,txtLasVenturas)
                TogglePlayerSpectating(playerid,False)
            if lr > 0 :
                ClassSel_SwitchToNextCity(playerid)
            elif lr < 0 :
                ClassSel_SwitchToPreviousCity(playerid)
            break
    return True

def OnPlayerText(playerid, text):
    return True

def OnPlayerRequestClass(playerid, classid):
    if IsPlayerNPC(playerid):
        return True
    global txtClassSelHelper
    for player in players:
        if player.playerid == playerid:
            if player.has_city_selected == True:
                ClassSel_SetupCharSelection(playerid)
                return True
            else:
                if GetPlayerState(playerid) != Const("PLAYER_STATE_SPECTATING"):
                    SpawnPlayer(playerid) # Why? 
                    #Else player does not load in correctly and the toggle below will disconnect the player. 
                    # Read the known issues on our repo wiki. 
                    TogglePlayerSpectating(playerid, 1)
                    TextDrawShowForPlayer(playerid, txtClassSelHelper)
                    player.city_selection = -1
    return True
    

    
def OnPlayerUpdate(playerid):
    if IsPlayerConnected(playerid) == False:
        return False
    if IsPlayerNPC(playerid):
        return True
    for player in players:
        if player.playerid == playerid:
            if ( player.has_city_selected == False and
            GetPlayerState(playerid) == Const("PLAYER_STATE_SPECTATING") ):
                ClassSel_HandleCitySelection(playerid)
    
    if GetPlayerInterior(playerid) != 0 and GetPlayerWeapon(playerid) != 0:
        SetPlayerArmedWeapon(playerid, 0) # Fists
        return False #No syncing until they change their weapon
    
    if GetPlayerWeapon(playerid) == 38 or GetPlayerSpecialAction(playerid) == 2: #minigun and jetpack not allowed
        Kick(playerid)
        return False
    return True
    