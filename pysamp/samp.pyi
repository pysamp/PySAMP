def SetSpawnInfo(
    player_id: int,
    team: int,
    skin: int,
    x: float,
    y: float,
    z: float,
    rotation: float,
    weapon1: int,
    weapon1_ammo: int,
    weapon2: int,
    weapon2_ammo: int,
    weapon3: int,
    weapon3_ammo: int,
) -> bool:
    pass


def SpawnPlayer(player_id: int) -> bool:
    pass


def SetPlayerPos(player_id: int, x: float, y: float, z: float) -> bool:
    pass


def SetPlayerPosFindZ(player_id: int, x: float, y: float, z: float) -> bool:
    pass


def GetPlayerPos(player_id: int) -> tuple[float, float, float]:
    pass


def SetPlayerFacingAngle(player_id: int, angle: float) -> bool:
    pass


def GetPlayerFacingAngle(player_id: int) -> float:
    pass


def IsPlayerInRangeOfPoint(
    player_id: int, range: float, x: float, y: float, z: float
) -> bool:
    pass


def GetPlayerDistanceFromPoint(
    player_id: int, x: float, y: float, z: float
) -> float:
    pass


def IsPlayerStreamedIn(player_id: int, for_player_id: int) -> bool:
    pass


def SetPlayerInterior(player_id: int, interior_id: int) -> bool:
    pass


def GetPlayerInterior(player_id: int) -> int:
    pass


def SetPlayerHealth(player_id: int, health: float) -> bool:
    pass


def GetPlayerHealth(player_id: int) -> float:
    pass


def SetPlayerArmour(player_id: int, armour: float) -> bool:
    pass


def GetPlayerArmour(player_id: int) -> float:
    pass


def SetPlayerAmmo(player_id: int, weapon_id: int, ammo: int) -> bool:
    pass


def GetPlayerAmmo(player_id: int) -> int:
    pass


def GetPlayerWeaponState(player_id: int) -> int:
    pass


def GetPlayerTargetPlayer(player_id: int) -> int:
    pass


def GetPlayerTargetActor(player_id: int) -> int:
    pass


def SetPlayerTeam(player_id: int, team_id: int) -> bool:
    pass


def GetPlayerTeam(player_id: int) -> int:
    pass


def SetPlayerScore(player_id: int, score: int) -> bool:
    pass


def GetPlayerScore(player_id: int) -> int:
    pass


def GetPlayerDrunkLevel(player_id: int) -> int:
    pass


def SetPlayerDrunkLevel(player_id: int, level: int) -> bool:
    pass


def SetPlayerColor(player_id: int, color: int) -> bool:
    pass


def GetPlayerColor(player_id: int) -> int:
    pass


def SetPlayerSkin(player_id: int, skin_id: int) -> bool:
    pass


def GetPlayerSkin(player_id: int) -> int:
    pass


def GivePlayerWeapon(player_id: int, weapon_id: int, ammo: int) -> bool:
    pass


def ResetPlayerWeapons(player_id: int) -> bool:
    pass


def SetPlayerArmedWeapon(player_id: int, weapon_id: int) -> bool:
    pass


def GetPlayerWeaponData(player_id: int, slot: int) -> tuple[int, int]:
    pass


def GivePlayerMoney(player_id: int, money: int) -> bool:
    pass


def ResetPlayerMoney(player_id: int) -> bool:
    pass


def SetPlayerName(player_id: int, name: str) -> int:
    pass


def GetPlayerMoney(player_id: int) -> int:
    pass


def GetPlayerState(player_id: int) -> int:
    pass


def GetPlayerIp(player_id: int) -> str:
    pass


def GetPlayerPing(player_id: int) -> int:
    pass


def GetPlayerWeapon(player_id: int) -> int:
    pass


def GetPlayerKeys(player_id: int) -> tuple[int, int, int]:
    pass


def GetPlayerName(player_id: int) -> str:
    pass


def SetPlayerTime(player_id: int, hour: int, minute: int) -> bool:
    pass


def GetPlayerTime(player_id: int) -> tuple[int, int]:
    pass


def TogglePlayerClock(player_id: int, toggle: bool) -> bool:
    pass


def SetPlayerWeather(player_id: int, weather: int) -> bool:
    pass


def ForceClassSelection(player_id: int) -> bool:
    pass


def SetPlayerWantedLevel(player_id: int, level: int) -> bool:
    pass


def GetPlayerWantedLevel(player_id: int) -> int:
    pass


def SetPlayerFightingStyle(player_id: int, style: int) -> bool:
    pass


def GetPlayerFightingStyle(player_id: int) -> int:
    pass


def SetPlayerVelocity(player_id: int, x: float, y: float, z: float) -> bool:
    pass


def GetPlayerVelocity(player_id: int) -> tuple[float, float, float]:
    pass


def PlayCrimeReportForPlayer(
    player_id: int, suspect_id: int, crime: int
) -> bool:
    pass


def PlayAudioStreamForPlayer(
    player_id: int,
    url: str,
    x: float = 0.0,
    y: float = 0.0,
    z: float = 0.0,
    distance: float = 50.0,
    use_pos: bool = False,
) -> bool:
    pass


def StopAudioStreamForPlayer(player_id: int) -> bool:
    pass


def SetPlayerShopName(player_id: int, shop_name: str) -> bool:
    pass


def SetPlayerSkillLevel(player_id: int, skill: int, level: int) -> bool:
    pass


def GetPlayerSurfingVehicleID(player_id: int) -> int:
    pass


def GetPlayerSurfingObjectID(player_id: int) -> int:
    pass


def RemoveBuildingForPlayer(
    player_id: int, model_id: int, x: float, y: float, z: float, radius: float
) -> bool:
    pass


def GetPlayerLastShotVectors(
    player_id: int,
) -> tuple[float, float, float, float, float, float]:
    pass


def SetPlayerAttachedObject(
    player_id: int,
    index: int,
    model_id: int,
    bone: int,
    offset_x: float,
    offset_y: float,
    offset_z: float,
    rotation_x: float,
    rotation_y: float,
    rotation_z: float,
    scale_x: float,
    scale_y: float,
    scale_z: float,
    material_color_1: int,
    material_color_2: int,
) -> bool:
    pass


def RemovePlayerAttachedObject(player_id: int, index: int) -> bool:
    pass


def IsPlayerAttachedObjectSlotUsed(player_id: int, index: int) -> bool:
    pass


def EditAttachedObject(player_id: int, index: int) -> bool:
    pass


def CreatePlayerTextDraw(player_id: int, x: float, y: float, text: str) -> int:
    pass


def PlayerTextDrawDestroy(player_id: int, textdraw_id: int) -> bool:
    pass


def PlayerTextDrawLetterSize(
    player_id: int, textdraw_id: int, x: float, y: float
) -> bool:
    pass


def PlayerTextDrawTextSize(
    player_id: int, textdraw_id: int, x: float, y: float
) -> bool:
    pass


def PlayerTextDrawAlignment(
    player_id: int, textdraw_id: int, alignment: int
) -> bool:
    pass


def PlayerTextDrawColor(player_id: int, textdraw_id: int, color: int) -> bool:
    pass


def PlayerTextDrawUseBox(player_id: int, textdraw_id: int, use: bool) -> bool:
    pass


def PlayerTextDrawBoxColor(
    player_id: int, textdraw_id: int, color: int
) -> bool:
    pass


def PlayerTextDrawSetShadow(
    player_id: int, textdraw_id: int, size: int
) -> bool:
    pass


def PlayerTextDrawSetOutline(
    player_id: int, textdraw_id: int, size: int
) -> bool:
    pass


def PlayerTextDrawBackgroundColor(
    player_id: int, textdraw_id: int, color: int
) -> bool:
    pass


def PlayerTextDrawFont(player_id: int, textdraw_id: int, font: int) -> bool:
    pass


def PlayerTextDrawSetProportional(
    player_id: int, textdraw_id: int, set: int
) -> bool:
    pass


def PlayerTextDrawSetSelectable(
    player_id: int, textdraw_id: int, set: int
) -> bool:
    pass


def PlayerTextDrawShow(player_id: int, textdraw_id: int) -> bool:
    pass


def PlayerTextDrawHide(player_id: int, textdraw_id: int) -> bool:
    pass


def PlayerTextDrawSetString(
    player_id: int, textdraw_id: int, string: str
) -> bool:
    pass


def PlayerTextDrawSetPreviewModel(
    player_id: int, textdraw_id: int, modelindex: int
) -> bool:
    pass


def PlayerTextDrawSetPreviewRot(
    player_id: int,
    textdraw_id: int,
    rotation_x: float,
    rotation_y: float,
    rotation_z: float,
    zoom: float,
) -> bool:
    pass


def PlayerTextDrawSetPreviewVehCol(
    player_id: int, textdraw_id: int, color1: int, color2: int
) -> bool:
    pass


def SetPVarInt(player_id: int, var_name: str, value: int) -> bool:
    pass


def GetPVarInt(player_id: int, var_name: str) -> int:
    pass


def SetPVarString(player_id: int, var_name: str, value: str) -> bool:
    pass


def GetPVarString(player_id: int, var_name: str, size: int) -> str:
    pass


def SetPVarFloat(player_id: int, var_name: str, value: float) -> bool:
    pass


def GetPVarFloat(player_id: int, var_name: str) -> float:
    pass


def DeletePVar(player_id: int, var_name: str) -> bool:
    pass


def GetPVarsUpperIndex(player_id: int) -> int:
    pass


def GetPVarNameAtIndex(player_id: int, index: int, size: int) -> str:
    pass


def GetPVarType(player_id: int, var_name: str) -> int:
    pass


def SetPlayerChatBubble(
    player_id: int, text: str, color: int, drawdistance: float, expiretime: int
) -> bool:
    pass


def PutPlayerInVehicle(player_id: int, vehicle_id: int, seat_id: int) -> bool:
    pass


def GetPlayerVehicleID(player_id: int) -> int:
    pass


def GetPlayerVehicleSeat(player_id: int) -> int:
    pass


def RemovePlayerFromVehicle(player_id: int) -> bool:
    pass


def TogglePlayerControllable(player_id: int, toggle: bool) -> bool:
    pass


def PlayerPlaySound(
    player_id: int, sound_id: int, x: float, y: float, z: float
) -> bool:
    pass


def ApplyAnimation(
    player_id: int,
    anim_lib: str,
    anim_name: str,
    delta: float,
    loop: bool,
    lock_x: bool,
    lock_y: bool,
    freeze: bool,
    time: int,
    forcesync: bool,
) -> bool:
    pass


def ClearAnimations(player_id: int, force_sync: bool) -> bool:
    pass


def GetPlayerAnimationIndex(player_id: int) -> int:
    pass


def GetAnimationName(index: int) -> str:
    pass


def GetPlayerSpecialAction(player_id: int) -> int:
    pass


def SetPlayerSpecialAction(player_id: int, action_id: int) -> bool:
    pass


def DisableRemoteVehicleCollisions(player_id: int, disable: bool) -> bool:
    pass


def SetPlayerCheckpoint(
    player_id: int, x: float, y: float, z: float, size: int
) -> bool:
    pass


def DisablePlayerCheckpoint(player_id: int) -> bool:
    pass


def SetPlayerRaceCheckpoint(
    player_id: int,
    type: int,
    x: float,
    y: float,
    z: float,
    next_x: float,
    next_y: float,
    next_z: float,
    size: int,
) -> bool:
    pass


def DisablePlayerRaceCheckpoint(player_id: int) -> bool:
    pass


def SetPlayerWorldBounds(
    player_id: int, x_max: float, x_min: float, y_max: float, y_min: float
) -> bool:
    pass


def SetPlayerMarkerForPlayer(
    player_id: int, showplayer_id: int, color: int
) -> bool:
    pass


def ShowPlayerNameTagForPlayer(
    player_id: int, showplayer_id: int, show: bool
) -> bool:
    pass


def SetPlayerMapIcon(
    player_id: int,
    iconid: int,
    x: float,
    y: float,
    z: float,
    markertype: int,
    color: int,
    style: int,
) -> bool:
    pass


def RemovePlayerMapIcon(player_id: int, icon_id: int) -> bool:
    pass


def AllowPlayerTeleport(player_id: int, allow: bool) -> bool:
    pass


def SetPlayerCameraPos(player_id: int, x: float, y: float, z: float) -> bool:
    pass


def SetPlayerCameraLookAt(
    player_id: int, x: float, y: float, z: float, cut: int
) -> bool:
    pass


def SetCameraBehindPlayer(player_id: int) -> bool:
    pass


def GetPlayerCameraPos(player_id: int) -> tuple[float, float, float]:
    pass


def GetPlayerCameraFrontVector(
    player_id: int,
) -> tuple[float, float, float]:
    pass


def GetPlayerCameraMode(player_id: int) -> int:
    pass


def EnablePlayerCameraTarget(player_id: int, enable: bool) -> bool:
    pass


def GetPlayerCameraTargetObject(player_id: int) -> int:
    pass


def GetPlayerCameraTargetVehicle(player_id: int) -> int:
    pass


def GetPlayerCameraTargetPlayer(player_id: int) -> int:
    pass


def GetPlayerCameraTargetActor(player_id: int) -> int:
    pass


def GetPlayerCameraAspectRatio(player_id: int) -> float:
    pass


def GetPlayerCameraZoom(player_id: int) -> float:
    pass


def AttachCameraToObject(player_id: int, object_id: int) -> bool:
    pass


def AttachCameraToPlayerObject(player_id: int, player_object_id: int) -> bool:
    pass


def InterpolateCameraPos(
    player_id: int,
    from_x: float,
    from_y: float,
    from_z: float,
    to_x: float,
    to_y: float,
    to_z: float,
    time: int,
    cut: int,
) -> bool:
    pass


def InterpolateCameraLookAt(
    player_id: int,
    from_x: float,
    from_y: float,
    from_z: float,
    to_x: float,
    to_y: float,
    to_z: float,
    time: int,
    cut: int,
) -> bool:
    pass


def IsPlayerConnected(player_id: int) -> bool:
    pass


def IsPlayerInVehicle(player_id: int, vehicle_id: int) -> bool:
    pass


def IsPlayerInAnyVehicle(player_id: int) -> bool:
    pass


def IsPlayerInCheckpoint(player_id: int) -> bool:
    pass


def IsPlayerInRaceCheckpoint(player_id: int) -> bool:
    pass


def SetPlayerVirtualWorld(player_id: int, world_id: int) -> bool:
    pass


def GetPlayerVirtualWorld(player_id: int) -> int:
    pass


def EnableStuntBonusForPlayer(player_id: int, enable: bool) -> bool:
    pass


def EnableStuntBonusForAll(enable: bool) -> bool:
    pass


def TogglePlayerSpectating(player_id: int, toggle: bool) -> bool:
    pass


def PlayerSpectatePlayer(
    player_id: int, target_player_id: int, mode: int
) -> bool:
    pass


def PlayerSpectateVehicle(
    player_id: int, target_vehicle_id: int, mode: int
) -> bool:
    pass


def StartRecordingPlayerData(
    player_id: int,
    record_type: int,
    record_name: str,
) -> bool:
    pass


def StopRecordingPlayerData(player_id: int) -> bool:
    pass


def CreateExplosionForPlayer(
    player_id: int, x: float, y: float, z: float, type: int, radius: float
) -> bool:
    pass


def CreateObject(
    model_id: int,
    x: float,
    y: float,
    z: float,
    rotation_x: float,
    rotation_y: float,
    rotation_z: float,
    draw_distance: float,
) -> bool:
    pass


def AttachObjectToVehicle(
    object_id: int,
    vehicle_id: int,
    offset_x: float,
    offset_y: float,
    offset_z: float,
    rotation_x: float,
    rotation_y: float,
    rotation_z: float,
) -> bool:
    pass


def AttachObjectToObject(
    object_id: int,
    attachtoid: int,
    fOffsetX: float,
    fOffsetY: float,
    fOffsetZ: float,
    fRotX: float,
    fRotY: float,
    fRotZ: float,
    SyncRotation: bool,
) -> bool:
    pass


def AttachObjectToPlayer(
    object_id: int,
    player_id: int,
    offset_x: float,
    offset_y: float,
    offset_z: float,
    rotation_x: float,
    rotation_y: float,
    rotation_z: float,
) -> bool:
    pass


def SetObjectPos(object_id: int, x: float, y: float, z: float) -> bool:
    pass


def GetObjectPos(object_id: int) -> tuple[float, float, float]:
    pass


def SetObjectRot(
    object_id: int, rotation_x: float, rotation_y: float, rotation_z: float
) -> bool:
    pass


def GetObjectRot(object_id: int) -> tuple[float, float, float]:
    pass


def GetObjectModel(object_id: int) -> int:
    pass


def SetObjectNoCameraCol(object_id: int) -> bool:
    pass


def IsValidObject(object_id: int) -> bool:
    pass


def DestroyObject(object_id: int) -> bool:
    pass


def MoveObject(
    object_id: int,
    x: float,
    y: float,
    z: float,
    speed: float,
    rotation_x: float,
    rotation_y: float,
    rotation_z: float,
) -> int:
    pass


def StopObject(object_id: int) -> bool:
    pass


def IsObjectMoving(object_id: int) -> bool:
    pass


def EditObject(player_id: int, object_id: int) -> bool:
    pass


def EditPlayerObject(player_id: int, object_id: int) -> bool:
    pass


def SelectObject(player_id: int) -> bool:
    pass


def CancelEdit(player_id: int) -> bool:
    pass


def CreatePlayerObject(
    player_id: int,
    model_id: int,
    x: float,
    y: float,
    z: float,
    rotation_x: float,
    rotation_y: float,
    rotation_z: float,
    draw_distance: float,
) -> int:
    pass


def AttachPlayerObjectToPlayer(
    objectplayer: int,
    object_id: int,
    attachplayer: int,
    offset_x: float,
    offset_y: float,
    offset_z: float,
    rotation_x: float,
    rotation_y: float,
    rotation_z: float,
) -> bool:
    pass


def AttachPlayerObjectToVehicle(
    player_id: int,
    object_id: int,
    vehicle_id: int,
    offset_x: float,
    offset_y: float,
    offset_z: float,
    rotation_x: float,
    rotation_y: float,
    rotation_z: float,
) -> bool:
    pass


def SetPlayerObjectPos(
    player_id: int, object_id: int, x: float, y: float, z: float
) -> bool:
    pass


def GetPlayerObjectPos(
    player_id: int, object_id: int
) -> tuple[float, float, float]:
    pass


def SetPlayerObjectRot(
    player_id: int,
    object_id: int,
    rotation_x: float,
    rotation_y: float,
    rotation_z: float,
) -> bool:
    pass


def GetPlayerObjectRot(
    player_id: int, object_id: int
) -> tuple[float, float, float]:
    pass


def GetPlayerObjectModel(player_id: int, object_id: int) -> int:
    pass


def SetPlayerObjectNoCameraCol(player_id: int, object_id: int) -> bool:
    pass


def IsValidPlayerObject(player_id: int, object_id: int) -> bool:
    pass


def DestroyPlayerObject(player_id: int, object_id: int) -> bool:
    pass


def MovePlayerObject(
    player_id: int,
    object_id: int,
    x: float,
    y: float,
    z: float,
    speed: float,
    rotation_x: float,
    rotation_y: float,
    rotation_z: float,
) -> int:
    pass


def StopPlayerObject(player_id: int, object_id: int) -> bool:
    pass


def IsPlayerObjectMoving(player_id: int, object_id: int) -> bool:
    pass


def SetObjectMaterial(
    object_id: int,
    material_index: int,
    model_id: int,
    txd_name: str,
    texture_name: str,
    material_color: int,
) -> bool:
    pass


def SetPlayerObjectMaterial(
    player_id: int,
    object_id: int,
    material_index: int,
    model_id: int,
    txd_name: str,
    texture_name: str,
    material_color: int,
) -> bool:
    pass


def SetObjectMaterialText(
    object_id: int,
    text: str,
    material_index: int,
    material_size: int,
    font_face: str,
    font_size: int,
    bold: bool,
    font_color: int,
    back_color: int,
    text_alignment: int,
) -> bool:
    pass


def SetPlayerObjectMaterialText(
    player_id: int,
    object_id: int,
    text: str,
    material_index: int,
    material_size: int,
    font_face: str,
    font_size: int,
    bold: bool,
    font_color: int,
    back_color: int,
    text_alignment: int,
) -> bool:
    pass


def SetObjectsDefaultCameraCol(disable: bool) -> bool:
    pass


def SendClientMessage(player_id: int, color: int, message: str) -> bool:
    pass


def SendClientMessageToAll(color: int, message: str) -> bool:
    pass


def SendPlayerMessageToPlayer(
    player_id: int, senderid: int, message: str
) -> bool:
    pass


def SendPlayerMessageToAll(senderid: int, message: str) -> bool:
    pass


def SendDeathMessage(killer: int, killee: int, weapon: int) -> bool:
    pass


def SendDeathMessageToPlayer(
    player_id: int, killer: int, killee: int, weapon: int
) -> bool:
    pass


def GameTextForAll(text: str, time: int, style: int) -> bool:
    pass


def GameTextForPlayer(
    player_id: int, text: str, time: int, style: int
) -> bool:
    pass


def GetTickCount() -> int:
    pass


def GetMaxPlayers() -> int:
    pass


def VectorSize(x: float, y: float, z: float) -> float:
    pass


def GetPlayerPoolSize() -> int:
    pass


def GetVehiclePoolSize() -> int:
    pass


def GetActorPoolSize() -> int:
    pass


def SetSVarInt(var_name: str, int_value: int) -> bool:
    pass


def GetSVarInt(var_name: str) -> int:
    pass


def SetSVarString(var_name: str, string_value: str) -> bool:
    pass


def GetSVarString(var_name: str) -> str:
    pass


def SetSVarFloat(var_name: str, float_value: float) -> bool:
    pass


def GetSVarFloat(var_name: str) -> float:
    pass


def DeleteSVar(var_name: str) -> bool:
    pass


def GetSVarsUpperIndex() -> int:
    pass


def GetSVarNameAtIndex(index: int) -> str:
    pass


def GetSVarType(var_name: str) -> int:
    pass


def SetGameModeText(text: str) -> bool:
    pass


def SetTeamCount(count: int) -> bool:
    pass


def AddPlayerClass(
    model_id: int,
    spawn_x: float,
    spawn_y: float,
    spawn_z: float,
    z_angle: float,
    weapon1: int,
    weapon1_ammo: int,
    weapon2: int,
    weapon2_ammo: int,
    weapon3: int,
    weapon3_ammo: int,
) -> int:
    pass


def AddPlayerClassEx(
    teamid: int,
    model_id: int,
    spawn_x: float,
    spawn_y: float,
    spawn_z: float,
    z_angle: float,
    weapon1: int,
    weapon1_ammo: int,
    weapon2: int,
    weapon2_ammo: int,
    weapon3: int,
    weapon3_ammo: int,
) -> int:
    pass


def AddStaticVehicle(
    model_id: int,
    spawn_x: float,
    spawn_y: float,
    spawn_z: float,
    z_angle: float,
    color1: int,
    color2: int,
) -> int:
    pass


def AddStaticVehicleEx(
    model_id: int,
    spawn_x: float,
    spawn_y: float,
    spawn_z: float,
    z_angle: float,
    color1: int,
    color2: int,
    respawn_delay: int,
    addsiren: bool,
) -> int:
    pass


def AddStaticPickup(
    model: int, type: int, x: float, y: float, z: float, virtualworld: int
) -> int:
    pass


def CreatePickup(
    model: int, type: int, x: float, y: float, z: float, virtualworld: int
) -> int:
    pass


def DestroyPickup(pickup: int) -> bool:
    pass


def ShowNameTags(show: bool) -> bool:
    pass


def ShowPlayerMarkers(mode: int) -> bool:
    pass


def GameModeExit() -> bool:
    pass


def SetWorldTime(hour: int) -> bool:
    pass


def GetWeaponName(weapon_id: int) -> str:
    pass


def EnableTirePopping(enable: bool) -> bool:
    pass


def EnableVehicleFriendlyFire() -> bool:
    pass


def AllowInteriorWeapons(allow: bool) -> bool:
    pass


def SetWeather(weather_id: int) -> bool:
    pass


def SetGravity(gravity: float) -> bool:
    pass


def GetGravity() -> float:
    pass


def AllowAdminTeleport(allow: bool) -> bool:
    pass


def SetDeathDropAmount(amount: int) -> bool:
    pass


def CreateExplosion(
    x: float, y: float, z: float, type: int, radius: float
) -> bool:
    pass


def EnableZoneNames(enable: bool) -> bool:
    pass


def UsePlayerPedAnims() -> bool:
    pass


def DisableInteriorEnterExits() -> bool:
    pass


def SetNameTagDrawDistance(distance: float) -> bool:
    pass


def DisableNameTagLOS() -> bool:
    pass


def LimitGlobalChatRadius(chat_radius: float) -> bool:
    pass


def LimitPlayerMarkerRadius(marker_radius: float) -> bool:
    pass


def ConnectNPC(name: str, script: str) -> bool:
    pass


def IsPlayerNPC(player_id: int) -> bool:
    pass


def IsPlayerAdmin(player_id: int) -> bool:
    pass


def Kick(player_id: int) -> bool:
    pass


def Ban(player_id: int) -> bool:
    pass


def BanEx(player_id: int, reason: str) -> bool:
    pass


def SendRconCommand(command: str) -> bool:
    pass


def GetPlayerNetworkStats(player_id: int) -> str:
    pass


def GetNetworkStats() -> str:
    pass


def GetPlayerVersion(player_id: int) -> str:
    pass


def BlockIpAddress(ip_address: str, time_in_ms: int) -> bool:
    pass


def UnBlockIpAddress(ip_address: str) -> bool:
    pass


def GetServerVarAsString(var_name: str) -> str:
    pass


def GetServerVarAsInt(var_name: str) -> int:
    pass


def GetServerVarAsBool(var_name: str) -> bool:
    pass


def GetConsoleVarAsString(var_name: str) -> str:
    pass


def GetConsoleVarAsInt(var_name: str) -> int:
    pass


def GetConsoleVarAsBool(var_name: str) -> bool:
    pass


def GetServerTickRate() -> int:
    pass


def NetStats_GetConnectedTime(player_id: int) -> int:
    pass


def NetStats_MessagesReceived(player_id: int) -> int:
    pass


def NetStats_BytesReceived(player_id: int) -> int:
    pass


def NetStats_MessagesSent(player_id: int) -> int:
    pass


def NetStats_BytesSent(player_id: int) -> int:
    pass


def NetStats_MessagesRecvPerSecond(player_id: int) -> int:
    pass


def NetStats_PacketLossPercent(player_id: int) -> float:
    pass


def NetStats_ConnectionStatus(player_id: int) -> int:
    pass


def NetStats_GetIpPort(player_id: int) -> str:
    pass


def CreateMenu(
    title: str,
    columns: int,
    x: float,
    y: float,
    column_1_width: float,
    column_2_width: float,
) -> bool:
    pass


def DestroyMenu(menu_id: int) -> bool:
    pass


def AddMenuItem(menu_id: int, column: int, menu_text: str) -> int:
    pass


def SetMenuColumnHeader(menu_id: int, column: int, column_header: str) -> bool:
    pass


def ShowMenuForPlayer(menu_id: int, player_id: int) -> bool:
    pass


def HideMenuForPlayer(menu_id: int, player_id: int) -> bool:
    pass


def IsValidMenu(menu_id: int) -> bool:
    pass


def DisableMenu(menu_id: int) -> bool:
    pass


def DisableMenuRow(menu_id: int, row: int) -> bool:
    pass


def GetPlayerMenu(player_id: int) -> int:
    pass


def TextDrawCreate(x: float, y: float, text: str) -> int:
    pass


def TextDrawDestroy(text_draw_id: int) -> bool:
    pass


def TextDrawLetterSize(text_draw_id: int, x: float, y: float) -> bool:
    pass


def TextDrawTextSize(text_draw_id: int, x: float, y: float) -> bool:
    pass


def TextDrawAlignment(text_draw_id: int, alignment: int) -> bool:
    pass


def TextDrawColor(text_draw_id: int, color: int) -> bool:
    pass


def TextDrawUseBox(text_draw_id: int, use: bool) -> bool:
    pass


def TextDrawBoxColor(text_draw_id: int, color: int) -> bool:
    pass


def TextDrawSetShadow(text_draw_id: int, size: int) -> bool:
    pass


def TextDrawSetOutline(text_draw_id: int, size: int) -> bool:
    pass


def TextDrawBackgroundColor(text_draw_id: int, color: int) -> bool:
    pass


def TextDrawFont(text_draw_id: int, font: int) -> bool:
    pass


def TextDrawSetProportional(text_draw_id: int, set: bool) -> bool:
    pass


def TextDrawSetSelectable(text_draw_id: int, set: bool) -> bool:
    pass


def TextDrawShowForPlayer(player_id: int, text_draw_id: int) -> bool:
    pass


def TextDrawHideForPlayer(player_id: int, text_draw_id: int) -> bool:
    pass


def TextDrawShowForAll(text_draw_id: int) -> bool:
    pass


def TextDrawHideForAll(text_draw_id: int) -> bool:
    pass


def TextDrawSetString(text_draw_id: int, string: str) -> bool:
    pass


def TextDrawSetPreviewModel(text_draw_id: int, modelindex: int) -> bool:
    pass


def TextDrawSetPreviewRot(
    text_draw_id: int,
    rotation_x: float,
    rotation_y: float,
    rotation_z: float,
    zoom: float,
) -> bool:
    pass


def TextDrawSetPreviewVehCol(
    text_draw_id: int, color1: int, color2: int
) -> bool:
    pass


def SelectTextDraw(player_id: int, hover_color: int) -> bool:
    pass


def CancelSelectTextDraw(player_id: int) -> bool:
    pass


def GangZoneCreate(
    min_x: float, min_y: float, max_x: float, max_y: float
) -> int:
    pass


def GangZoneDestroy(zone_id: int) -> bool:
    pass


def GangZoneShowForPlayer(player_id: int, zone_id: int, color: int) -> bool:
    pass


def GangZoneShowForAll(zone_id: int, color: int) -> bool:
    pass


def GangZoneHideForPlayer(player_id: int, zone_id: int) -> bool:
    pass


def GangZoneHideForAll(zone_id: int) -> bool:
    pass


def GangZoneFlashForPlayer(
    player_id: int, zone_id: int, flashcolor: int
) -> bool:
    pass


def GangZoneFlashForAll(zone_id: int, flashcolor: int) -> bool:
    pass


def GangZoneStopFlashForPlayer(player_id: int, zone_id: int) -> bool:
    pass


def GangZoneStopFlashForAll(zone_id: int) -> bool:
    pass


def ShowPlayerDialog(
    player_id: int,
    dialog_id: int,
    style: int,
    caption: str,
    info: str,
    button1: str,
    button2: str,
) -> bool:
    pass


def IsValidVehicle(vehicle_id: int) -> bool:
    pass


def GetVehicleDistanceFromPoint(
    vehicle_id: int, x: float, y: float, z: float
) -> float:
    pass


def CreateVehicle(
    vehicletype: int,
    x: float,
    y: float,
    z: float,
    rotation: float,
    color1: int,
    color2: int,
    respawn_delay: int,
    addsiren: bool,
) -> int:
    pass


def DestroyVehicle(vehicle_id: int) -> bool:
    pass


def IsVehicleStreamedIn(vehicle_id: int, forplayer_id: int) -> bool:
    pass


def GetVehiclePos(vehicle_id: int) -> tuple[float, float, float]:
    pass


def SetVehiclePos(vehicle_id: int, x: float, y: float, z: float) -> bool:
    pass


def GetVehicleZAngle(vehicle_id: int) -> float:
    pass


def GetVehicleRotationQuat(
    vehicle_id: int,
) -> tuple[float, float, float, float]:
    pass


def SetVehicleZAngle(vehicle_id: int, z_angle: float) -> bool:
    pass


def SetVehicleParamsForPlayer(
    vehicle_id: int, player_id: int, objective: int, doorslocked: int
) -> bool:
    pass


def ManualVehicleEngineAndLights() -> bool:
    pass


def SetVehicleParamsEx(
    vehicle_id: int,
    engine: int,
    lights: int,
    alarm: int,
    doors: int,
    bonnet: int,
    boot: int,
    objective: int,
) -> bool:
    pass


def GetVehicleParamsEx(
    vehicle_id: int,
) -> tuple[int, int, int, int, int, int, int]:
    pass


def GetVehicleParamsSirenState(vehicle_id: int) -> bool:
    pass


def SetVehicleParamsCarDoors(
    vehicle_id: int,
    driver: int,
    passenger: int,
    back_left: int,
    back_right: int,
) -> bool:
    pass


def GetVehicleParamsCarDoors(vehicle_id: int) -> tuple[int, int, int, int]:
    pass


def SetVehicleParamsCarWindows(
    vehicle_id: int,
    driver: int,
    passenger: int,
    back_left: int,
    back_right: int,
) -> bool:
    pass


def GetVehicleParamsCarWindows(
    vehicle_id: int,
) -> tuple[int, int, int, int]:
    pass


def SetVehicleToRespawn(vehicle_id: int) -> bool:
    pass


def LinkVehicleToInterior(vehicle_id: int, interior_id: int) -> bool:
    pass


def AddVehicleComponent(vehicle_id: int, component_id: int) -> bool:
    pass


def RemoveVehicleComponent(vehicle_id: int, component_id: int) -> bool:
    pass


def ChangeVehicleColor(vehicle_id: int, color1: int, color2: int) -> bool:
    pass


def ChangeVehiclePaintjob(vehicle_id: int, paint_job_id: int) -> bool:
    pass


def SetVehicleHealth(vehicle_id: int, health: float) -> bool:
    pass


def GetVehicleHealth(vehicle_id: int) -> float:
    pass


def AttachTrailerToVehicle(trailer_id: int, vehicle_id: int) -> bool:
    pass


def DetachTrailerFromVehicle(vehicle_id: int) -> bool:
    pass


def IsTrailerAttachedToVehicle(vehicle_id: int) -> bool:
    pass


def GetVehicleTrailer(vehicle_id: int) -> int:
    pass


def SetVehicleNumberPlate(vehicle_id: int, number_plate: str) -> bool:
    pass


def GetVehicleModel(vehicle_id: int) -> int:
    pass


def GetVehicleComponentInSlot(vehicle_id: int, slot: int) -> int:
    pass


def GetVehicleComponentType(component: int) -> int:
    pass


def RepairVehicle(vehicle_id: int) -> bool:
    pass


def GetVehicleVelocity(vehicle_id: int) -> tuple[float, float, float]:
    pass


def SetVehicleVelocity(vehicle_id: int, x: float, y: float, z: float) -> bool:
    pass


def SetVehicleAngularVelocity(
    vehicle_id: int, x: float, y: float, z: float
) -> bool:
    pass


def GetVehicleDamageStatus(vehicle_id: int) -> tuple[int, int, int, int]:
    pass


def UpdateVehicleDamageStatus(
    vehicle_id: int, panels: int, doors: int, lights: int, tires: int
) -> bool:
    pass


def SetVehicleVirtualWorld(vehicle_id: int, world_id: int) -> bool:
    pass


def GetVehicleVirtualWorld(vehicle_id: int) -> int:
    pass


def GetVehicleModelInfo(
    model: int, infotype: int
) -> tuple[float, float, float]:
    pass


def CreateActor(
    model_id: int, x: float, y: float, z: float, rotation: float
) -> int:
    pass


def DestroyActor(actorid: int) -> bool:
    pass


def IsActorStreamedIn(actorid: int, forplayer_id: int) -> bool:
    pass


def SetActorVirtualWorld(actorid: int, vworld: int) -> bool:
    pass


def GetActorVirtualWorld(actorid: int) -> int:
    pass


def ApplyActorAnimation(
    actorid: int,
    animation_library: str,
    animation_name: str,
    delta: float,
    loop: bool,
    lock_x: bool,
    lock_y: bool,
    freeze: bool,
    time: int,
) -> bool:
    pass


def ClearActorAnimations(actorid: int) -> bool:
    pass


def SetActorPos(actorid: int, x: float, y: float, z: float) -> bool:
    pass


def GetActorPos(actorid: int) -> tuple[float, float, float]:
    pass


def SetActorFacingAngle(actorid: int, angle: float) -> bool:
    pass


def GetActorFacingAngle(actorid: int) -> float:
    pass


def SetActorHealth(actorid: int, health: float) -> bool:
    pass


def GetActorHealth(actorid: int) -> float:
    pass


def SetActorInvulnerable(actorid: int, invulnerable: bool = True) -> bool:
    pass


def IsActorInvulnerable(actorid: int) -> bool:
    pass


def IsValidActor(actorid: int) -> bool:
    pass


def Create3DTextLabel(
    text: str,
    color: int,
    x: float,
    y: float,
    z: float,
    draw_distance: float,
    virtual_world: int,
    test_line_of_sight: bool,
) -> int:
    pass


def Delete3DTextLabel(id: int) -> bool:
    pass


def Attach3DTextLabelToPlayer(
    id: int, player_id: int, offset_x: float, offset_y: float, offset_z: float
) -> bool:
    pass


def Attach3DTextLabelToVehicle(
    id: int, vehicle_id: int, offset_x: float, offset_y: float, offset_z: float
) -> bool:
    pass


def Update3DTextLabelText(id: int, color: int, text: str) -> bool:
    pass


def CreatePlayer3DTextLabel(
    player_id: int,
    text: str,
    color: int,
    x: float,
    y: float,
    z: float,
    draw_distance: float,
    attached_player: int,
    attached_vehicle: int,
    test_line_of_sight: bool,
) -> int:
    pass


def DeletePlayer3DTextLabel(player_id: int, id: int) -> bool:
    pass


def UpdatePlayer3DTextLabelText(
    player_id: int, id: int, color: int, text: str
) -> bool:
    pass


MAX_PLAYER_NAME = 24
MAX_CLIENT_MESSAGE = 144
MAX_PLAYERS = 1000
MAX_VEHICLES = 2000
MAX_ACTORS = 1000
INVALID_PLAYER_ID = 0xFFFF
INVALID_VEHICLE_ID = 0xFFFF
INVALID_ACTOR_ID = 0xFFFF
NO_TEAM = 255
MAX_OBJECTS = 1000
INVALID_OBJECT_ID = 0xFFFF
MAX_GANG_ZONES = 1024
MAX_TEXT_DRAWS = 2048
MAX_PLAYER_TEXT_DRAWS = 256
MAX_MENUS = 128
MAX_3DTEXT_GLOBAL = 1024
MAX_3DTEXT_PLAYER = 1024
MAX_PICKUPS = 4096
INVALID_MENU = 0xFF
INVALID_TEXT_DRAW = 0xFFFF
INVALID_GANG_ZONE = -1
INVALID_3DTEXT_ID = 0xFFFF
SERVER_VARTYPE_NONE = 0
SERVER_VARTYPE_INT = 1
SERVER_VARTYPE_STRING = 2
SERVER_VARTYPE_FLOAT = 3
TEXT_DRAW_FONT_SPRITE_DRAW = 4
TEXT_DRAW_FONT_MODEL_PREVIEW = 5
DIALOG_STYLE_MSGBOX = 0
DIALOG_STYLE_INPUT = 1
DIALOG_STYLE_LIST = 2
DIALOG_STYLE_PASSWORD = 3
DIALOG_STYLE_TABLIST = 4
DIALOG_STYLE_TABLIST_HEADERS = 5
PLAYER_STATE_NONE = 0
PLAYER_STATE_ONFOOT = 1
PLAYER_STATE_DRIVER = 2
PLAYER_STATE_PASSENGER = 3
PLAYER_STATE_EXIT_VEHICLE = 4
PLAYER_STATE_ENTER_VEHICLE_DRIVER = 5
PLAYER_STATE_ENTER_VEHICLE_PASSENGER = 6
PLAYER_STATE_WASTED = 7
PLAYER_STATE_SPAWNED = 8
PLAYER_STATE_SPECTATING = 9
PLAYER_MARKERS_MODE_OFF = 0
PLAYER_MARKERS_MODE_GLOBAL = 1
PLAYER_MARKERS_MODE_STREAMED = 2
WEAPON_BRASSKNUCKLE = 1
WEAPON_GOLFCLUB = 2
WEAPON_NITESTICK = 3
WEAPON_KNIFE = 4
WEAPON_BAT = 5
WEAPON_SHOVEL = 6
WEAPON_POOLSTICK = 7
WEAPON_KATANA = 8
WEAPON_CHAINSAW = 9
WEAPON_DILDO = 10
WEAPON_DILDO2 = 11
WEAPON_VIBRATOR = 12
WEAPON_VIBRATOR2 = 13
WEAPON_FLOWER = 14
WEAPON_CANE = 15
WEAPON_GRENADE = 16
WEAPON_TEARGAS = 17
WEAPON_MOLTOV = 18
WEAPON_COLT45 = 22
WEAPON_SILENCED = 23
WEAPON_DEAGLE = 24
WEAPON_SHOTGUN = 25
WEAPON_SAWEDOFF = 26
WEAPON_SHOTGSPA = 27
WEAPON_UZI = 28
WEAPON_MP5 = 29
WEAPON_AK47 = 30
WEAPON_M4 = 31
WEAPON_TEC9 = 32
WEAPON_RIFLE = 33
WEAPON_SNIPER = 34
WEAPON_ROCKETLAUNCHER = 35
WEAPON_HEATSEEKER = 36
WEAPON_FLAMETHROWER = 37
WEAPON_MINIGUN = 38
WEAPON_SATCHEL = 39
WEAPON_BOMB = 40
WEAPON_SPRAYCAN = 41
WEAPON_FIREEXTINGUISHER = 42
WEAPON_CAMERA = 43
WEAPON_NIGHTVISION = 44
WEAPON_INFRARED = 45
WEAPON_PARACHUTE = 46
WEAPON_VEHICLE = 49
WEAPON_DROWN = 53
WEAPON_COLLISION = 54
KEY_ACTION = 1
KEY_CROUCH = 2
KEY_FIRE = 4
KEY_SPRINT = 8
KEY_SECONDARY_ATTACK = 16
KEY_JUMP = 32
KEY_LOOK_RIGHT = 64
KEY_HANDBRAKE = 128
KEY_LOOK_LEFT = 256
KEY_SUBMISSION = 512
KEY_LOOK_BEHIND = 512
KEY_WALK = 1024
KEY_ANALOG_UP = 2048
KEY_ANALOG_DOWN = 4096
KEY_ANALOG_LEFT = 8192
KEY_ANALOG_RIGHT = 16384
KEY_YES = 65536
KEY_NO = 131072
KEY_CTRL_BACK = 262144
KEY_UP = -128
KEY_DOWN = 128
KEY_LEFT = -128
KEY_RIGHT = 128
BODY_PART_TORSO = 3
BODY_PART_GROIN = 4
BODY_PART_LEFT_ARM = 5
BODY_PART_RIGHT_ARM = 6
BODY_PART_LEFT_LEG = 7
BODY_PART_RIGHT_LEG = 8
BODY_PART_HEAD = 9
CLICK_SOURCE_SCOREBOARD = 0
EDIT_RESPONSE_CANCEL = 0
EDIT_RESPONSE_FINAL = 1
EDIT_RESPONSE_UPDATE = 2
SELECT_OBJECT_GLOBAL_OBJECT = 1
SELECT_OBJECT_PLAYER_OBJECT = 2
BULLET_HIT_TYPE_NONE = 0
BULLET_HIT_TYPE_PLAYER = 1
BULLET_HIT_TYPE_VEHICLE = 2
BULLET_HIT_TYPE_OBJECT = 3
BULLET_HIT_TYPE_PLAYER_OBJECT = 4
CARMODTYPE_SPOILER = 0
CARMODTYPE_HOOD = 1
CARMODTYPE_ROOF = 2
CARMODTYPE_SIDESKIRT = 3
CARMODTYPE_LAMPS = 4
CARMODTYPE_NITRO = 5
CARMODTYPE_EXHAUST = 6
CARMODTYPE_WHEELS = 7
CARMODTYPE_STEREO = 8
CARMODTYPE_HYDRAULICS = 9
CARMODTYPE_FRONT_BUMPER = 10
CARMODTYPE_REAR_BUMPER = 11
CARMODTYPE_VENT_RIGHT = 12
CARMODTYPE_VENT_LEFT = 13
VEHICLE_PARAMS_UNSET = -1
VEHICLE_PARAMS_OFF = 0
VEHICLE_PARAMS_ON = 1
VEHICLE_MODEL_INFO_SIZE = 1
VEHICLE_MODEL_INFO_FRONTSEAT = 2
VEHICLE_MODEL_INFO_REARSEAT = 3
VEHICLE_MODEL_INFO_PETROLCAP = 4
VEHICLE_MODEL_INFO_WHEELSFRONT = 5
VEHICLE_MODEL_INFO_WHEELSREAR = 6
VEHICLE_MODEL_INFO_WHEELSMID = 7
VEHICLE_MODEL_INFO_FRONT_BUMPER_Z = 8
VEHICLE_MODEL_INFO_REAR_BUMPER_Z = 9
OBJECT_MATERIAL_SIZE_32x32 = 10
OBJECT_MATERIAL_SIZE_64x32 = 20
OBJECT_MATERIAL_SIZE_64x64 = 30
OBJECT_MATERIAL_SIZE_128x32 = 40
OBJECT_MATERIAL_SIZE_128x64 = 50
OBJECT_MATERIAL_SIZE_128x128 = 60
OBJECT_MATERIAL_SIZE_256x32 = 70
OBJECT_MATERIAL_SIZE_256x64 = 80
OBJECT_MATERIAL_SIZE_256x128 = 90
OBJECT_MATERIAL_SIZE_256x256 = 100
OBJECT_MATERIAL_SIZE_512x64 = 110
OBJECT_MATERIAL_SIZE_512x128 = 120
OBJECT_MATERIAL_SIZE_512x256 = 130
OBJECT_MATERIAL_SIZE_512x512 = 140
OBJECT_MATERIAL_TEXT_ALIGN_LEFT = 0
OBJECT_MATERIAL_TEXT_ALIGN_CENTER = 1
OBJECT_MATERIAL_TEXT_ALIGN_RIGHT = 2
SPECIAL_ACTION_NONE = 0
SPECIAL_ACTION_DUCK = 1
SPECIAL_ACTION_USEJETPACK = 2
SPECIAL_ACTION_ENTER_VEHICLE = 3
SPECIAL_ACTION_EXIT_VEHICLE = 4
SPECIAL_ACTION_DANCE1 = 5
SPECIAL_ACTION_DANCE2 = 6
SPECIAL_ACTION_DANCE3 = 7
SPECIAL_ACTION_DANCE4 = 8
SPECIAL_ACTION_HANDSUP = 10
SPECIAL_ACTION_USECELLPHONE = 11
SPECIAL_ACTION_SITTING = 12
SPECIAL_ACTION_STOPUSECELLPHONE = 13
SPECIAL_ACTION_DRINK_BEER = 20
SPECIAL_ACTION_SMOKE_CIGGY = 21
SPECIAL_ACTION_DRINK_WINE = 22
SPECIAL_ACTION_DRINK_SPRUNK = 23
SPECIAL_ACTION_CUFFED = 24
SPECIAL_ACTION_CARRY = 25
FIGHT_STYLE_NORMAL = 4
FIGHT_STYLE_BOXING = 5
FIGHT_STYLE_KUNGFU = 6
FIGHT_STYLE_KNEEHEAD = 7
FIGHT_STYLE_GRABKICK = 15
FIGHT_STYLE_ELBOW = 16
WEAPONSKILL_PISTOL = 0
WEAPONSKILL_PISTOL_SILENCED = 1
WEAPONSKILL_DESERT_EAGLE = 2
WEAPONSKILL_SHOTGUN = 3
WEAPONSKILL_SAWNOFF_SHOTGUN = 4
WEAPONSKILL_SPAS12_SHOTGUN = 5
WEAPONSKILL_MICRO_UZI = 6
WEAPONSKILL_MP5 = 7
WEAPONSKILL_AK47 = 8
WEAPONSKILL_M4 = 9
WEAPONSKILL_SNIPERRIFLE = 10
WEAPONSTATE_UNKNOWN = -1
WEAPONSTATE_NO_BULLETS = 0
WEAPONSTATE_LAST_BULLET = 1
WEAPONSTATE_MORE_BULLETS = 2
WEAPONSTATE_RELOADING = 3
MAX_PLAYER_ATTACHED_OBJECTS = 10
PLAYER_VARTYPE_NONE = 0
PLAYER_VARTYPE_INT = 1
PLAYER_VARTYPE_STRING = 2
PLAYER_VARTYPE_FLOAT = 3
MAX_CHATBUBBLE_LENGTH = 144
MAPICON_LOCAL = 0
MAPICON_GLOBAL = 1
MAPICON_LOCAL_CHECKPOINT = 2
MAPICON_GLOBAL_CHECKPOINT = 3
CAMERA_CUT = 2
CAMERA_MOVE = 1
SPECTATE_MODE_NORMAL = 1
SPECTATE_MODE_FIXED = 2
SPECTATE_MODE_SIDE = 3
PLAYER_RECORDING_TYPE_NONE = 0
PLAYER_RECORDING_TYPE_DRIVER = 1
PLAYER_RECORDING_TYPE_ONFOOT = 2
