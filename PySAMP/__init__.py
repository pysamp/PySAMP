from samp import (HTTP, AddCharModel, AddMenuItem, AddPlayerClass,
                  AddPlayerClassEx, AddSimpleModel, AddSimpleModelTimed,
                  AddStaticPickup, AddStaticVehicle, AddStaticVehicleEx,
                  AddVehicleComponent, AllowAdminTeleport,
                  AllowInteriorWeapons, AllowPlayerTeleport,
                  ApplyActorAnimation, ApplyAnimation,
                  Attach3DTextLabelToPlayer, Attach3DTextLabelToVehicle,
                  AttachCameraToObject, AttachCameraToPlayerObject,
                  AttachObjectToObject, AttachObjectToPlayer,
                  AttachObjectToVehicle, AttachPlayerObjectToPlayer,
                  AttachPlayerObjectToVehicle, AttachTrailerToVehicle, Ban,
                  BanEx, BlockIpAddress, CancelEdit, CancelSelectTextDraw,
                  ChangeVehicleColor, ChangeVehiclePaintjob,
                  ClearActorAnimations, ClearAnimations, ConnectNPC,
                  Create3DTextLabel, CreateActor, CreateExplosion,
                  CreateExplosionForPlayer, CreateMenu, CreateObject,
                  CreatePickup, CreatePlayer3DTextLabel, CreatePlayerObject,
                  CreatePlayerTextDraw, CreateVehicle, Delete3DTextLabel,
                  DeletePlayer3DTextLabel, DeletePVar, DeleteSVar,
                  DestroyActor, DestroyMenu, DestroyObject, DestroyPickup,
                  DestroyPlayerObject, DestroyVehicle,
                  DetachTrailerFromVehicle, DisableInteriorEnterExits,
                  DisableMenu, DisableMenuRow, DisableNameTagLOS,
                  DisablePlayerCheckpoint, DisablePlayerRaceCheckpoint,
                  DisableRemoteVehicleCollisions, EditAttachedObject,
                  EditObject, EditPlayerObject, EnablePlayerCameraTarget,
                  EnableStuntBonusForAll, EnableStuntBonusForPlayer,
                  EnableTirePopping, EnableVehicleFriendlyFire,
                  EnableZoneNames, FindModelFileNameFromCRC,
                  FindTextureFileNameFromCRC, ForceClassSelection,
                  GameModeExit, GameTextForAll, GameTextForPlayer,
                  GangZoneCreate, GangZoneDestroy, GangZoneFlashForAll,
                  GangZoneFlashForPlayer, GangZoneHideForAll,
                  GangZoneHideForPlayer, GangZoneShowForAll,
                  GangZoneShowForPlayer, GangZoneStopFlashForAll,
                  GangZoneStopFlashForPlayer, GetActorFacingAngle,
                  GetActorHealth, GetActorPoolSize, GetActorPos,
                  GetActorVirtualWorld, GetAnimationName, GetConsoleVarAsBool,
                  GetConsoleVarAsInt, GetConsoleVarAsString, GetGravity,
                  GetMaxPlayers, GetNetworkStats, GetObjectModel, GetObjectPos,
                  GetObjectRot, GetPlayerAmmo, GetPlayerAnimationIndex,
                  GetPlayerArmour, GetPlayerCameraAspectRatio,
                  GetPlayerCameraFrontVector, GetPlayerCameraMode,
                  GetPlayerCameraPos, GetPlayerCameraTargetActor,
                  GetPlayerCameraTargetObject, GetPlayerCameraTargetPlayer,
                  GetPlayerCameraTargetVehicle, GetPlayerCameraZoom,
                  GetPlayerColor, GetPlayerDistanceFromPoint,
                  GetPlayerDrunkLevel, GetPlayerFacingAngle,
                  GetPlayerFightingStyle, GetPlayerHealth, GetPlayerInterior,
                  GetPlayerIp, GetPlayerKeys, GetPlayerLastShotVectors,
                  GetPlayerMenu, GetPlayerMoney, GetPlayerName,
                  GetPlayerNetworkStats, GetPlayerObjectModel,
                  GetPlayerObjectPos, GetPlayerObjectRot, GetPlayerPing,
                  GetPlayerPoolSize, GetPlayerPos, GetPlayerScore,
                  GetPlayerSkin, GetPlayerSpecialAction, GetPlayerState,
                  GetPlayerSurfingObjectID, GetPlayerSurfingVehicleID,
                  GetPlayerTargetActor, GetPlayerTargetPlayer, GetPlayerTeam,
                  GetPlayerTime, GetPlayerVehicleID, GetPlayerVehicleSeat,
                  GetPlayerVelocity, GetPlayerVersion, GetPlayerVirtualWorld,
                  GetPlayerWantedLevel, GetPlayerWeapon, GetPlayerWeaponData,
                  GetPlayerWeaponState, GetPVarFloat, GetPVarInt,
                  GetPVarNameAtIndex, GetPVarString, GetPVarsUpperIndex,
                  GetPVarType, GetServerTickRate, GetServerVarAsBool,
                  GetServerVarAsInt, GetServerVarAsString, GetSVarFloat,
                  GetSVarInt, GetSVarNameAtIndex, GetSVarString,
                  GetSVarsUpperIndex, GetSVarType, GetTickCount,
                  GetVehicleComponentInSlot, GetVehicleComponentType,
                  GetVehicleDamageStatus, GetVehicleDistanceFromPoint,
                  GetVehicleHealth, GetVehicleModel, GetVehicleModelInfo,
                  GetVehicleParamsCarDoors, GetVehicleParamsCarWindows,
                  GetVehicleParamsEx, GetVehicleParamsSirenState,
                  GetVehiclePoolSize, GetVehiclePos, GetVehicleRotationQuat,
                  GetVehicleTrailer, GetVehicleVelocity,
                  GetVehicleVirtualWorld, GetVehicleZAngle, GetWeaponName,
                  GivePlayerMoney, GivePlayerWeapon, HideMenuForPlayer,
                  InterpolateCameraLookAt, InterpolateCameraPos,
                  IsActorInvulnerable, IsActorStreamedIn, IsObjectMoving,
                  IsPlayerAdmin, IsPlayerAttachedObjectSlotUsed,
                  IsPlayerConnected, IsPlayerInAnyVehicle,
                  IsPlayerInCheckpoint, IsPlayerInRaceCheckpoint,
                  IsPlayerInRangeOfPoint, IsPlayerInVehicle, IsPlayerNPC,
                  IsPlayerObjectMoving, IsPlayerStreamedIn,
                  IsTrailerAttachedToVehicle, IsValidActor, IsValidMenu,
                  IsValidObject, IsValidPlayerObject, IsValidVehicle,
                  IsVehicleStreamedIn, Kick, LimitGlobalChatRadius,
                  LimitPlayerMarkerRadius, LinkVehicleToInterior,
                  ManualVehicleEngineAndLights, MoveObject, MovePlayerObject,
                  NetStats_BytesReceived, NetStats_BytesSent,
                  NetStats_ConnectionStatus, NetStats_GetConnectedTime,
                  NetStats_GetIpPort, NetStats_MessagesReceived,
                  NetStats_MessagesRecvPerSecond, NetStats_MessagesSent,
                  NetStats_PacketLossPercent, PlayAudioStreamForPlayer,
                  PlayCrimeReportForPlayer, PlayerPlaySound,
                  PlayerSpectatePlayer, PlayerSpectateVehicle,
                  PlayerTextDrawAlignment, PlayerTextDrawBackgroundColor,
                  PlayerTextDrawBoxColor, PlayerTextDrawColor,
                  PlayerTextDrawDestroy, PlayerTextDrawFont,
                  PlayerTextDrawHide, PlayerTextDrawLetterSize,
                  PlayerTextDrawSetOutline, PlayerTextDrawSetPreviewModel,
                  PlayerTextDrawSetPreviewRot, PlayerTextDrawSetPreviewVehCol,
                  PlayerTextDrawSetProportional, PlayerTextDrawSetSelectable,
                  PlayerTextDrawSetShadow, PlayerTextDrawSetString,
                  PlayerTextDrawShow, PlayerTextDrawTextSize,
                  PlayerTextDrawUseBox, PutPlayerInVehicle, RedirectDownload,
                  RemoveBuildingForPlayer, RemovePlayerAttachedObject,
                  RemovePlayerFromVehicle, RemovePlayerMapIcon,
                  RemoveVehicleComponent, RepairVehicle, ResetPlayerMoney,
                  ResetPlayerWeapons, SelectObject, SelectTextDraw,
                  SendClientMessage, SendClientMessageToAll, SendDeathMessage,
                  SendDeathMessageToPlayer, SendPlayerMessageToAll,
                  SendPlayerMessageToPlayer, SendRconCommand,
                  SetActorFacingAngle, SetActorHealth, SetActorInvulnerable,
                  SetActorPos, SetActorVirtualWorld, SetCameraBehindPlayer,
                  SetDeathDropAmount, SetGameModeText, SetGravity,
                  SetMenuColumnHeader, SetNameTagDrawDistance,
                  SetObjectMaterial, SetObjectMaterialText,
                  SetObjectNoCameraCol, SetObjectPos, SetObjectRot,
                  SetObjectsDefaultCameraCol, SetPlayerAmmo,
                  SetPlayerArmedWeapon, SetPlayerArmour,
                  SetPlayerAttachedObject, SetPlayerCameraLookAt,
                  SetPlayerCameraPos, SetPlayerChatBubble, SetPlayerCheckpoint,
                  SetPlayerColor, SetPlayerDrunkLevel, SetPlayerFacingAngle,
                  SetPlayerFightingStyle, SetPlayerHealth, SetPlayerInterior,
                  SetPlayerMapIcon, SetPlayerMarkerForPlayer, SetPlayerName,
                  SetPlayerObjectMaterial, SetPlayerObjectMaterialText,
                  SetPlayerObjectNoCameraCol, SetPlayerObjectPos,
                  SetPlayerObjectRot, SetPlayerPos, SetPlayerPosFindZ,
                  SetPlayerRaceCheckpoint, SetPlayerScore, SetPlayerShopName,
                  SetPlayerSkillLevel, SetPlayerSkin, SetPlayerSpecialAction,
                  SetPlayerTeam, SetPlayerTime, SetPlayerVelocity,
                  SetPlayerVirtualWorld, SetPlayerWantedLevel,
                  SetPlayerWeather, SetPlayerWorldBounds, SetPVarFloat,
                  SetPVarInt, SetPVarString, SetSpawnInfo, SetSVarFloat,
                  SetSVarInt, SetSVarString, SetTeamCount,
                  SetVehicleAngularVelocity, SetVehicleHealth,
                  SetVehicleNumberPlate, SetVehicleParamsCarDoors,
                  SetVehicleParamsCarWindows, SetVehicleParamsEx,
                  SetVehicleParamsForPlayer, SetVehiclePos,
                  SetVehicleToRespawn, SetVehicleVelocity,
                  SetVehicleVirtualWorld, SetVehicleZAngle, SetWeather,
                  SetWorldTime, ShowMenuForPlayer, ShowNameTags,
                  ShowPlayerDialog, ShowPlayerMarkers,
                  ShowPlayerNameTagForPlayer, SpawnPlayer,
                  StartRecordingPlayerData, StopAudioStreamForPlayer,
                  StopObject, StopPlayerObject, StopRecordingPlayerData,
                  TextDrawAlignment, TextDrawBackgroundColor, TextDrawBoxColor,
                  TextDrawColor, TextDrawCreate, TextDrawDestroy, TextDrawFont,
                  TextDrawHideForAll, TextDrawHideForPlayer,
                  TextDrawLetterSize, TextDrawSetOutline,
                  TextDrawSetPreviewModel, TextDrawSetPreviewRot,
                  TextDrawSetPreviewVehCol, TextDrawSetProportional,
                  TextDrawSetSelectable, TextDrawSetShadow, TextDrawSetString,
                  TextDrawShowForAll, TextDrawShowForPlayer, TextDrawTextSize,
                  TextDrawUseBox, TogglePlayerClock, TogglePlayerControllable,
                  TogglePlayerSpectating, UnBlockIpAddress,
                  Update3DTextLabelText, UpdatePlayer3DTextLabelText,
                  UpdateVehicleDamageStatus, UsePlayerPedAnims, VectorSize)

########################
# SNAKE CASE WRAPPERS FOR PEP8 COMPATIBILITY
########################


def set_spawn_info(
    player_id: int,
    team,
    skin,
    x: float,
    y: float,
    z: float,
    rotation,
    weapon1,
    weapon1_ammo,
    weapon2,
    weapon2_ammo,
    weapon3,
    weapon3_ammo,
) -> :
    return SetSpawnInfo(
        player_id,
        team,
        skin,
        x,
        y,
        z,
        rotation,
        weapon1,
        weapon1_ammo,
        weapon2,
        weapon2_ammo,
        weapon3,
        weapon3_ammo,
    )


def spawn_player(player_id: int) -> bool:
    return SpawnPlayer(player_id)


def set_player_pos(player_id: int, x: float, y: float, z: float) -> bool:
    return SetPlayerPos(player_id, x, y, z)


def set_player_pos_find_z(player_id: int, x: float, y: float, z: float) -> bool:
    return SetPlayerPosFindZ(player_id, x, y, z)


def get_player_pos(player_id: int) -> tuple[float, float, float]:
    return GetPlayerPos(player_id)


def set_player_facing_angle(player_id: int, angle: float) -> bool:
    return SetPlayerFacingAngle(player_id, angle)


def get_player_facing_angle(player_id: int) -> float:
    return GetPlayerFacingAngle(player_id)


def is_player_in_range_of_point(
    player_id: int, range: float, x: float, y: float, z: float
) -> bool:
    return IsPlayerInRangeOfPoint(player_id, range, x, y, z)


def get_player_distance_from_point(
    player_id: int, x: float, y: float, z: float
) -> float:
    return GetPlayerDistanceFromPoint(player_id, x, y, z)


def is_player_streamed_in(player_id: int, for_player_id: int) -> bool:
    return IsPlayerStreamedIn(player_id, for_player_id)


def set_player_interior(player_id: int, interior_id: int) -> bool:
    return SetPlayerInterior(player_id, interior_id)


def get_player_interior(player_id: int) -> int:
    return GetPlayerInterior(player_id)


def set_player_health(player_id: int, health: float) -> bool:
    return SetPlayerHealth(player_id, health)


def get_player_health(player_id: int) -> float:
    return GetPlayerHealth(player_id)


def set_player_armour(player_id: int, armour: int) -> bool:
    return SetPlayerArmour(player_id, armour)


def get_player_armour(player_id: int) -> float:
    return GetPlayerArmour(player_id)


def set_player_ammo(player_id: int, weapon_id: int, ammo: int) -> bool:
    return SetPlayerAmmo(player_id, weapon_id, ammo)


def get_player_ammo(player_id: int) -> int:
    return GetPlayerAmmo(player_id)


def get_player_weapon_state(player_id: int) -> int:
    return GetPlayerWeaponState(player_id)


def get_player_target_player(player_id: int) -> int:
    return GetPlayerTargetPlayer(player_id)


def get_player_target_actor(player_id: int) -> int:
    return GetPlayerTargetActor(player_id)


def set_player_team(player_id: int, team_id: int) -> bool:
    return SetPlayerTeam(player_id, team_id)


def get_player_team(player_id: int) -> int:
    return GetPlayerTeam(player_id)


def set_player_score(player_id: int, score: int) -> bool:
    return SetPlayerScore(player_id, score)


def get_player_score(player_id: int) -> int:
    return GetPlayerScore(player_id)


def get_player_drunk_level(player_id: int) -> int:
    return GetPlayerDrunkLevel(player_id)


def set_player_drunk_level(player_id: int, level: int) -> bool:
    return SetPlayerDrunkLevel(player_id, level)


def set_player_color(player_id: int, color: int) -> bool:
    return SetPlayerColor(player_id, color)


def get_player_color(player_id: int) -> int:
    return GetPlayerColor(player_id)


def set_player_skin(player_id: int, skin_id: int) -> bool:
    return SetPlayerSkin(player_id, skin_id)


def get_player_skin(player_id: int) -> int:
    return GetPlayerSkin(player_id)


def give_player_weapon(player_id: int, weapon_id: int, ammo: int) -> bool:
    return GivePlayerWeapon(player_id, weapon_id, ammo)


def reset_player_weapons(player_id: int) -> bool:
    return ResetPlayerWeapons(player_id)


def set_player_armed_weapon(player_id: int, weapon_id: int) -> bool:
    return SetPlayerArmedWeapon(player_id, weapon_id)


def get_player_weapon_data(player_id: int, slot: int) -> tuple[int, int]:
    return GetPlayerWeaponData(player_id, slot)


def give_player_money(player_id: int, money: int) -> bool:
    return GivePlayerMoney(player_id, money)


def reset_player_money(player_id: int) -> bool:
    return ResetPlayerMoney(player_id)


def set_player_name(player_id: int, name: str) -> int:
    return SetPlayerName(player_id, name)


def get_player_money(player_id: int) -> int:
    return GetPlayerMoney(player_id)


def get_player_state(player_id: int) -> int:
    return GetPlayerState(player_id)


def get_player_ip(player_id: int) -> str:
    return GetPlayerIp(player_id, 16)


def get_player_ping(player_id: int) -> int:
    return GetPlayerPing(player_id)


def get_player_weapon(player_id: int) -> int:
    return GetPlayerWeapon(player_id)


def get_player_keys(player_id: int) -> tuple[int, int, int]:
    return GetPlayerKeys(player_id)


def get_player_name(player_id: int, size: int) -> str:
    return GetPlayerName(player_id, size)


def set_player_time(player_id: int, hour: int, minute: int) -> bool:
    return SetPlayerTime(player_id, hour, minute)


def get_player_time(player_id: int) -> tuple[int,int]:
    return GetPlayerTime(player_id)


def toggle_player_clock(player_id: int, toggle: bool) -> bool:
    return TogglePlayerClock(player_id, toggle)


def set_player_weather(player_id: int, weather: int) -> bool:
    return SetPlayerWeather(player_id, weather)


def force_class_selection(player_id: int) -> bool:
    return ForceClassSelection(player_id)


def set_player_wanted_level(player_id: int, level: int) -> bool:
    return SetPlayerWantedLevel(player_id, level)


def get_player_wanted_level(player_id: int) -> int:
    return GetPlayerWantedLevel(player_id)


def set_player_fighting_style(player_id: int, style: int) -> bool:
    return SetPlayerFightingStyle(player_id, style)


def get_player_fighting_style(player_id: int) -> int:
    return GetPlayerFightingStyle(player_id)


def set_player_velocity(player_id: int, x: float, y: float, z: float) -> bool:
    return SetPlayerVelocity(player_id, x, y, z)


def get_player_velocity(player_id: int) -> tuple[float, float, float]:
    return GetPlayerVelocity(player_id)


def play_crime_report_for_player(player_id: int, suspect_id: int, crime: int) -> bool:
    return PlayCrimeReportForPlayer(player_id, suspect_id, crime)


def play_audio_stream_for_player(
    player_id, url, x=0.0, y=0.0, z=0.0, distance=50.0, use_pos=False
) -> bool:
    return PlayAudioStreamForPlayer(player_id, url, x, y, z, distance, use_pos)


def stop_audio_stream_for_player(player_id: int) -> bool:
    return StopAudioStreamForPlayer(player_id)


def set_player_shop_name(player_id: int, shop_name: str) -> bool:
    return SetPlayerShopName(player_id, shop_name)


def set_player_skill_level(player_id: int, skill, level) -> bool:
    return SetPlayerSkillLevel(player_id, skill, level)


def get_player_surfing_vehicle_id(player_id: int) -> int:
    return GetPlayerSurfingVehicleID(player_id)


def get_player_surfing_object_id(player_id: int) -> :
    return GetPlayerSurfingObjectID(player_id)


def remove_building_for_player(player_id: int, modelid, fX, fY, fZ, fRadius) -> :
    return RemoveBuildingForPlayer(player_id, modelid, fX, fY, fZ, fRadius)


def get_player_last_shot_vectors(player_id: int) -> :
    return GetPlayerLastShotVectors(player_id)


def set_player_attached_object(
    player_id,
    index,
    modelid,
    bone,
    fOffsetX=0.0,
    fOffsetY=0.0,
    fOffsetZ=0.0,
    fRotX=0.0,
    fRotY=0.0,
    fRotZ=0.0,
    fScaleX=1.0,
    fScaleY=1.0,
    fScaleZ=1.0,
    materialcolor1=0,
    materialcolor2=0,
) -> :
    return SetPlayerAttachedObject(
        player_id,
        index,
        modelid,
        bone,
        fOffsetX,
        fOffsetY,
        fOffsetZ,
        fRotX,
        fRotY,
        fRotZ,
        fScaleX,
        fScaleY,
        fScaleZ,
        materialcolor1,
        materialcolor2,
    )


def remove_player_attached_object(player_id: int, index) -> :
    return RemovePlayerAttachedObject(player_id, index)


def is_player_attached_object_slot_used(player_id: int, index) -> :
    return IsPlayerAttachedObjectSlotUsed(player_id, index)


def edit_attached_object(player_id: int, index) -> :
    return EditAttachedObject(player_id, index)


def create_player_text_draw(player_id: int, x, y, text) -> :
    return CreatePlayerTextDraw(player_id, x, y, text)


def player_text_draw_destroy(player_id: int, text) -> :
    return PlayerTextDrawDestroy(player_id, text)


def player_text_draw_letter_size(player_id: int, text, x, y) -> :
    return PlayerTextDrawLetterSize(player_id, text, x, y)


def player_text_draw_text_size(player_id: int, text, x, y) -> :
    return PlayerTextDrawTextSize(player_id, text, x, y)


def player_text_draw_alignment(player_id: int, text, alignment) -> :
    return PlayerTextDrawAlignment(player_id, text, alignment)


def player_text_draw_color(player_id: int, text, color) -> :
    return PlayerTextDrawColor(player_id, text, color)


def player_text_draw_use_box(player_id: int, text, use) -> :
    return PlayerTextDrawUseBox(player_id, text, use)


def player_text_draw_box_color(player_id: int, text, color) -> :
    return PlayerTextDrawBoxColor(player_id, text, color)


def player_text_draw_set_shadow(player_id: int, text, size) -> :
    return PlayerTextDrawSetShadow(player_id, text, size)


def player_text_draw_set_outline(player_id: int, text, size) -> :
    return PlayerTextDrawSetOutline(player_id, text, size)


def player_text_draw_background_color(player_id: int, text, color) -> :
    return PlayerTextDrawBackgroundColor(player_id, text, color)


def player_text_draw_font(player_id: int, text, font) -> :
    return PlayerTextDrawFont(player_id, text, font)


def player_text_draw_set_proportional(player_id: int, text, set) -> :
    return PlayerTextDrawSetProportional(player_id, text, set)


def player_text_draw_set_selectable(player_id: int, text, set) -> :
    return PlayerTextDrawSetSelectable(player_id, text, set)


def player_text_draw_show(player_id: int, text) -> :
    return PlayerTextDrawShow(player_id, text)


def player_text_draw_hide(player_id: int, text) -> :
    return PlayerTextDrawHide(player_id, text)


def player_text_draw_set_string(player_id: int, text, string) -> :
    return PlayerTextDrawSetString(player_id, text, string)


def player_text_draw_set_preview_model(player_id: int, text, modelindex) -> :
    return PlayerTextDrawSetPreviewModel(player_id, text, modelindex)


def player_text_draw_set_preview_rot(
    player_id: int, text, fRotX, fRotY, fRotZ, fZoom=1.0
) -> :
    return PlayerTextDrawSetPreviewRot(player_id, text, fRotX, fRotY, fRotZ, fZoom)


def player_text_draw_set_preview_veh_col(player_id: int, text, color1, color2) -> :
    return PlayerTextDrawSetPreviewVehCol(player_id, text, color1, color2)


def set_pvar_int(player_id: int, varname, value) -> :
    return SetPVarInt(player_id, varname, value)


def get_pvar_int(player_id: int, varname) -> :
    return GetPVarInt(player_id, varname)


def set_pvar_string(player_id: int, varname, value) -> :
    return SetPVarString(player_id, varname, value)


def get_pvar_string(player_id: int, varname, size) -> :
    return GetPVarString(player_id, varname, size)


def set_pvar_float(player_id: int, varname, value) -> :
    return SetPVarFloat(player_id, varname, value)


def get_pvar_float(player_id: int, varname) -> :
    return GetPVarFloat(player_id, varname)


def delete_pvar(player_id: int, varname) -> :
    return DeletePVar(player_id, varname)


def get_pvars_upper_index(player_id: int) -> :
    return GetPVarsUpperIndex(player_id)


def get_pvar_name_at_index(player_id: int, index, size) -> :
    return GetPVarNameAtIndex(player_id, index, size)


def get_pvar_type(player_id: int, varname) -> :
    return GetPVarType(player_id, varname)


def set_player_chat_bubble(player_id: int, text, color, drawdistance, expiretime) -> :
    return SetPlayerChatBubble(player_id, text, color, drawdistance, expiretime)


def put_player_in_vehicle(player_id: int, vehicleid, seatid) -> :
    return PutPlayerInVehicle(player_id, vehicleid, seatid)


def get_player_vehicle_id(player_id: int) -> :
    return GetPlayerVehicleID(player_id)


def get_player_vehicle_seat(player_id: int) -> :
    return GetPlayerVehicleSeat(player_id)


def remove_player_from_vehicle(player_id: int) -> :
    return RemovePlayerFromVehicle(player_id)


def toggle_player_controllable(player_id: int, toggle) -> :
    return TogglePlayerControllable(player_id, toggle)


def player_play_sound(player_id: int, soundid, x: float, y: float, z: float) -> :
    return PlayerPlaySound(player_id, soundid, x, y, z)


def apply_animation(
    player_id,
    animlib,
    animname,
    fDelta,
    loop,
    lockx,
    locky,
    freeze,
    time,
    forcesync=False,
) -> :
    return ApplyAnimation(
        player_id, animlib, animname, fDelta, loop, lockx, locky, freeze, time, forcesync
    )


def clear_animations(player_id: int, forcesync=False) -> :
    return ClearAnimations(player_id, forcesync)


def get_player_animation_index(player_id: int) -> :
    return GetPlayerAnimationIndex(player_id)


def get_animation_name(index, animlib_size, animname_size) -> :
    return GetAnimationName(index, animlib_size, animname_size)


def get_player_special_action(player_id: int) -> :
    return GetPlayerSpecialAction(player_id)


def set_player_special_action(player_id: int, actionid) -> :
    return SetPlayerSpecialAction(player_id, actionid)


def disable_remote_vehicle_collisions(player_id: int, disable) -> :
    return DisableRemoteVehicleCollisions(player_id, disable)


def set_player_checkpoint(player_id: int, x: float, y: float, z: float, size) -> :
    return SetPlayerCheckpoint(player_id, x, y, z, size)


def disable_player_checkpoint(player_id: int) -> :
    return DisablePlayerCheckpoint(player_id)


def set_player_race_checkpoint(
    player_id: int, type, x: float, y: float, z: float, nextx, nexty, nextz, size
) -> :
    return SetPlayerRaceCheckpoint(player_id, type, x, y, z, nextx, nexty, nextz, size)


def disable_player_race_checkpoint(player_id: int) -> :
    return DisablePlayerRaceCheckpoint(player_id)


def set_player_world_bounds(player_id: int, x_max, x_min, y_max, y_min) -> :
    return SetPlayerWorldBounds(player_id, x_max, x_min, y_max, y_min)


def set_player_marker_for_player(player_id: int, showplayer_id, color) -> :
    return SetPlayerMarkerForPlayer(player_id, showplayer_id, color)


def show_player_name_tag_for_player(player_id: int, showplayer_id, show) -> :
    return ShowPlayerNameTagForPlayer(player_id, showplayer_id, show)


def set_player_map_icon(
    player_id,
    iconid,
    x: float,
    y: float,
    z: float,
    markertype,
    color,
    style=MAPICON_LOCAL,
) -> :
    return SetPlayerMapIcon(player_id, iconid, x, y, z, markertype, color, style)


def remove_player_map_icon(player_id: int, iconid) -> :
    return RemovePlayerMapIcon(player_id, iconid)


def allow_player_teleport(player_id: int, allow) -> :
    return AllowPlayerTeleport(player_id, allow)


def set_player_camera_pos(player_id: int, x: float, y: float, z: float) -> :
    return SetPlayerCameraPos(player_id, x, y, z)


def set_player_camera_look_at(
    player_id: int, x: float, y: float, z: float, cut=CAMERA_CUT
) -> :
    return SetPlayerCameraLookAt(player_id, x, y, z, cut)


def set_camera_behind_player(player_id: int) -> :
    return SetCameraBehindPlayer(player_id)


def get_player_camera_pos(player_id: int) -> :
    return GetPlayerCameraPos(player_id)


def get_player_camera_front_vector(player_id: int) -> :
    return GetPlayerCameraFrontVector(player_id)


def get_player_camera_mode(player_id: int) -> :
    return GetPlayerCameraMode(player_id)


def enable_player_camera_target(player_id: int, enable) -> :
    return EnablePlayerCameraTarget(player_id, enable)


def get_player_camera_target_object(player_id: int) -> :
    return GetPlayerCameraTargetObject(player_id)


def get_player_camera_target_vehicle(player_id: int) -> :
    return GetPlayerCameraTargetVehicle(player_id)


def get_player_camera_target_player(player_id: int) -> :
    return GetPlayerCameraTargetPlayer(player_id)


def get_player_camera_target_actor(player_id: int) -> :
    return GetPlayerCameraTargetActor(player_id)


def get_player_camera_aspect_ratio(player_id: int) -> :
    return GetPlayerCameraAspectRatio(player_id)


def get_player_camera_zoom(player_id: int) -> :
    return GetPlayerCameraZoom(player_id)


def attach_camera_to_object(player_id: int, objectid) -> :
    return AttachCameraToObject(player_id, objectid)


def attach_camera_to_player_object(player_id: int, playerobjectid) -> :
    return AttachCameraToPlayerObject(player_id, playerobjectid)


def interpolate_camera_pos(
    player_id, FromX, FromY, FromZ, ToX, ToY, ToZ, time, cut=CAMERA_CUT
) -> :
    return InterpolateCameraPos(player_id, FromX, FromY, FromZ, ToX, ToY, ToZ, time, cut)


def interpolate_camera_look_at(
    player_id, FromX, FromY, FromZ, ToX, ToY, ToZ, time, cut=CAMERA_CUT
) -> :
    return InterpolateCameraLookAt(
        player_id, FromX, FromY, FromZ, ToX, ToY, ToZ, time, cut
    )


def is_player_connected(player_id: int) -> :
    return IsPlayerConnected(player_id)


def is_player_in_vehicle(player_id: int, vehicleid) -> :
    return IsPlayerInVehicle(player_id, vehicleid)


def is_player_in_any_vehicle(player_id: int) -> :
    return IsPlayerInAnyVehicle(player_id)


def is_player_in_checkpoint(player_id: int) -> :
    return IsPlayerInCheckpoint(player_id)


def is_player_in_race_checkpoint(player_id: int) -> :
    return IsPlayerInRaceCheckpoint(player_id)


def set_player_virtual_world(player_id: int, worldid) -> :
    return SetPlayerVirtualWorld(player_id, worldid)


def get_player_virtual_world(player_id: int) -> :
    return GetPlayerVirtualWorld(player_id)


def enable_stunt_bonus_for_player(player_id: int, enable) -> :
    return EnableStuntBonusForPlayer(player_id, enable)


def enable_stunt_bonus_for_all(enable) -> :
    return EnableStuntBonusForAll(enable)


def toggle_player_spectating(player_id: int, toggle) -> :
    return TogglePlayerSpectating(player_id, toggle)


def player_spectate_player(player_id: int, targetplayer_id, mode=SPECTATE_MODE_NORMAL) -> :
    return PlayerSpectatePlayer(player_id, targetplayer_id, mode)


def player_spectate_vehicle(player_id: int, targetvehicleid, mode=SPECTATE_MODE_NORMAL) -> :
    return PlayerSpectateVehicle(player_id, targetvehicleid, mode)


def start_recording_player_data(player_id: int, recordtype, recordname) -> :
    return StartRecordingPlayerData(player_id, recordtype, recordname)


def stop_recording_player_data(player_id: int) -> :
    return StopRecordingPlayerData(player_id)


def create_explosion_for_player(player_id: int, X, Y, Z, type, Radius) -> :
    return CreateExplosionForPlayer(player_id, X, Y, Z, type, Radius)


def create_object(modelid, x: float, y: float, z: float, rX, rY, rZ, DrawDistance=0.0) -> :
    return CreateObject(modelid, x, y, z, rX, rY, rZ, DrawDistance)


def attach_object_to_vehicle(
    objectid, vehicleid, fOffsetX, fOffsetY, fOffsetZ, fRotX, fRotY, fRotZ
) -> :
    return AttachObjectToVehicle(
        objectid, vehicleid, fOffsetX, fOffsetY, fOffsetZ, fRotX, fRotY, fRotZ
    )


def attach_object_to_object(
    objectid,
    attachtoid,
    fOffsetX,
    fOffsetY,
    fOffsetZ,
    fRotX,
    fRotY,
    fRotZ,
    SyncRotation=False,
) -> :
    return AttachObjectToObject(
        objectid,
        attachtoid,
        fOffsetX,
        fOffsetY,
        fOffsetZ,
        fRotX,
        fRotY,
        fRotZ,
        SyncRotation,
    )


def attach_object_to_player(
    objectid, player_id, fOffsetX, fOffsetY, fOffsetZ, fRotX, fRotY, fRotZ
) -> :
    return AttachObjectToPlayer(
        objectid, player_id, fOffsetX, fOffsetY, fOffsetZ, fRotX, fRotY, fRotZ
    )


def set_object_pos(objectid, x: float, y: float, z: float) -> :
    return SetObjectPos(objectid, x, y, z)


def get_object_pos(objectid) -> :
    return GetObjectPos(objectid)


def set_object_rot(objectid, rotX, rotY, rotZ) -> :
    return SetObjectRot(objectid, rotX, rotY, rotZ)


def get_object_rot(objectid) -> :
    return GetObjectRot(objectid)


def get_object_model(objectid) -> :
    return GetObjectModel(objectid)


def set_object_no_camera_col(objectid) -> :
    return SetObjectNoCameraCol(objectid)


def is_valid_object(objectid) -> :
    return IsValidObject(objectid)


def destroy_object(objectid) -> :
    return DestroyObject(objectid)


def move_object(
    objectid,
    x: float,
    y: float,
    z: float,
    Speed,
    RotX=-1000.0,
    RotY=-1000.0,
    RotZ=-1000.0,
) -> :
    return MoveObject(objectid, X, Y, Z, Speed, RotX, RotY, RotZ)


def stop_object(objectid) -> :
    return StopObject(objectid)


def is_object_moving(objectid) -> :
    return IsObjectMoving(objectid)


def edit_object(player_id: int, objectid) -> :
    return EditObject(player_id, objectid)


def edit_player_object(player_id: int, objectid) -> :
    return EditPlayerObject(player_id, objectid)


def select_object(player_id: int) -> :
    return SelectObject(player_id)


def cancel_edit(player_id: int) -> :
    return CancelEdit(player_id)


def create_player_object(
    player_id: int, modelid, x: float, y: float, z: float, rX, rY, rZ, DrawDistance=0.0
) -> :
    return CreatePlayerObject(player_id, modelid, x, y, z, rX, rY, rZ, DrawDistance)


def attach_player_object_to_player(
    objectplayer, objectid, attachplayer, OffsetX, OffsetY, OffsetZ, rX, rY, rZ
) -> :
    return AttachPlayerObjectToPlayer(
        objectplayer, objectid, attachplayer, OffsetX, OffsetY, OffsetZ, rX, rY, rZ
    )


def attach_player_object_to_vehicle(
    player_id, objectid, vehicleid, fOffsetX, fOffsetY, fOffsetZ, fRotX, fRotY, RotZ
) -> :
    return AttachPlayerObjectToVehicle(
        player_id, objectid, vehicleid, fOffsetX, fOffsetY, fOffsetZ, fRotX, fRotY, RotZ
    )


def set_player_object_pos(player_id: int, objectid, x: float, y: float, z: float) -> :
    return SetPlayerObjectPos(player_id, objectid, x, y, z)


def get_player_object_pos(player_id: int, objectid) -> :
    return GetPlayerObjectPos(player_id, objectid)


def set_player_object_rot(player_id: int, objectid, rotX, rotY, rotZ) -> :
    return SetPlayerObjectRot(player_id, objectid, rotX, rotY, rotZ)


def get_player_object_rot(player_id: int, objectid) -> :
    return GetPlayerObjectRot(player_id, objectid)


def get_player_object_model(player_id: int, objectid) -> :
    return GetPlayerObjectModel(player_id, objectid)


def set_player_object_no_camera_col(player_id: int, objectid) -> :
    return SetPlayerObjectNoCameraCol(player_id, objectid)


def is_valid_player_object(player_id: int, objectid) -> :
    return IsValidPlayerObject(player_id, objectid)


def destroy_player_object(player_id: int, objectid) -> :
    return DestroyPlayerObject(player_id, objectid)


def move_player_object(
    player_id,
    objectid,
    x: float,
    y: float,
    z: float,
    Speed,
    RotX=-1000.0,
    RotY=-1000.0,
    RotZ=-1000.0,
) -> :
    return MovePlayerObject(player_id, objectid, x, y, z, Speed, RotX, RotY, RotZ)


def stop_player_object(player_id: int, objectid) -> :
    return StopPlayerObject(player_id, objectid)


def is_player_object_moving(player_id: int, objectid) -> :
    return IsPlayerObjectMoving(player_id, objectid)


def set_object_material(
    objectid, materialindex, modelid, txdname, texturename, materialcolor=0
) -> :
    return SetObjectMaterial(
        objectid, materialindex, modelid, txdname, texturename, materialcolor
    )


def set_player_object_material(
    player_id, objectid, materialindex, modelid, txdname, texturename, materialcolor=0
) -> :
    return SetPlayerObjectMaterial(
        player_id, objectid, materialindex, modelid, txdname, texturename, materialcolor
    )


def set_object_material_text(
    objectid,
    text,
    materialindex=0,
    materialsize=OBJECT_MATERIAL_SIZE_256x128,
    fontface="Arial",
    fontsize=24,
    bold=True,
    fontcolor=0xFFFFFFFF,
    backcolor=0,
    textalignment=0,
) -> :
    return SetObjectMaterialText(
        objectid,
        text,
        materialindex,
        materialsize,
        fontface,
        fontsize,
        bold,
        fontcolor,
        backcolor,
        textalignment,
    )


def set_player_object_material_text(
    player_id,
    objectid,
    text,
    materialindex=0,
    materialsize=OBJECT_MATERIAL_SIZE_256x128,
    fontface="Arial",
    fontsize=24,
    bold=True,
    fontcolor=0xFFFFFFFF,
    backcolor=0,
    textalignment=0,
) -> :
    return SetPlayerObjectMaterialText(
        player_id,
        objectid,
        text,
        materialindex,
        materialsize,
        fontface,
        fontsize,
        bold,
        fontcolor,
        backcolor,
        textalignment,
    )


def set_objects_default_camera_col(disable) -> :
    return SetObjectsDefaultCameraCol(disable)


def send_client_message(player_id: int, color, message) -> :
    return SendClientMessage(player_id, color, message)


def send_client_message_to_all(color, message) -> :
    return SendClientMessageToAll(color, message)


def send_player_message_to_player(player_id: int, senderid, message) -> :
    return SendPlayerMessageToPlayer(player_id, senderid, message)


def send_player_message_to_all(senderid, message) -> :
    return SendPlayerMessageToAll(senderid, message)


def send_death_message(killer, killee, weapon) -> :
    return SendDeathMessage(killer, killee, weapon)


def send_death_message_to_player(player_id: int, killer, killee, weapon) -> :
    return SendDeathMessageToPlayer(player_id, killer, killee, weapon)


def game_text_for_all(text, time, style) -> :
    return GameTextForAll(text, time, style)


def game_text_for_player(player_id: int, text, time, style) -> :
    return GameTextForPlayer(player_id, text, time, style)


def get_tick_count() -> :
    return GetTickCount()


def get_max_players() -> :
    return GetMaxPlayers()


def vector_size(x: float, y: float, z: float) -> :
    return VectorSize(x, y, z)


def get_player_pool_size() -> :
    return GetPlayerPoolSize()


def get_vehicle_pool_size() -> :
    return GetVehiclePoolSize()


def get_actor_pool_size() -> :
    return GetActorPoolSize()


def set_svar_int(varname, int_value) -> :
    return SetSVarInt(varname, int_value)


def get_svar_int(varname) -> :
    return GetSVarInt(varname)


def set_svar_string(varname, string_value) -> :
    return SetSVarString(varname, string_value)


def get_svar_string(varname, len) -> :
    return GetSVarString(varname, len)


def set_svar_float(varname, float_value) -> :
    return SetSVarFloat(varname, float_value)


def get_svar_float(varname) -> :
    return GetSVarFloat(varname)


def delete_svar(varname) -> :
    return DeleteSVar(varname)


def get_svars_upper_index() -> :
    return GetSVarsUpperIndex()


def get_svar_name_at_index(index, ret_len) -> :
    return GetSVarNameAtIndex(index, ret_len)


def get_svar_type(varname) -> :
    return GetSVarType(varname)


def set_game_mode_text(text) -> :
    return SetGameModeText(text)


def set_team_count(count) -> :
    return SetTeamCount(count)


def add_player_class(
    modelid,
    spawn_x,
    spawn_y,
    spawn_z,
    z_angle,
    weapon1,
    weapon1_ammo,
    weapon2,
    weapon2_ammo,
    weapon3,
    weapon3_ammo,
) -> :
    return AddPlayerClass(
        modelid,
        spawn_x,
        spawn_y,
        spawn_z,
        z_angle,
        weapon1,
        weapon1_ammo,
        weapon2,
        weapon2_ammo,
        weapon3,
        weapon3_ammo,
    )


def add_player_class_ex(
    teamid,
    modelid,
    spawn_x,
    spawn_y,
    spawn_z,
    z_angle,
    weapon1,
    weapon1_ammo,
    weapon2,
    weapon2_ammo,
    weapon3,
    weapon3_ammo,
) -> :
    return AddPlayerClassEx(
        teamid,
        modelid,
        spawn_x,
        spawn_y,
        spawn_z,
        z_angle,
        weapon1,
        weapon1_ammo,
        weapon2,
        weapon2_ammo,
        weapon3,
        weapon3_ammo,
    )


def add_static_vehicle(
    modelid: int,
    spawn_x: float,
    spawn_y: float,
    spawn_z: float,
    z_angle: float,
    color1: int,
    color2: int,
) -> :
    return AddStaticVehicle(modelid, spawn_x, spawn_y, spawn_z, z_angle, color1, color2)


def add_static_vehicle_ex(
    modelid: int,
    spawn_x: float,
    spawn_y: float,
    spawn_z: float,
    z_angle: float,
    color1: int,
    color2: int,
    respawn_delay: int,
    addsiren=False,
) -> :
    return AddStaticVehicleEx(
        modelid,
        spawn_x,
        spawn_y,
        spawn_z,
        z_angle,
        color1,
        color2,
        respawn_delay,
        addsiren,
    )


def add_static_pickup(
    model: int, type: int, x: float, y: float, z: float, virtualworld=0
) -> :
    return AddStaticPickup(model, type, x, y, z, virtualworld)


def create_pickup(model: int, type: int, x: float, y: float, z: float, virtualworld=0) -> :
    return CreatePickup(model, type, x, y, z, virtualworld)


def destroy_pickup(pickup) -> :
    return DestroyPickup(pickup)


def show_name_tags(show) -> :
    return ShowNameTags(show)


def show_player_markers(mode) -> :
    return ShowPlayerMarkers(mode)


def game_mode_exit() -> :
    return GameModeExit()


def set_world_time(hour) -> :
    return SetWorldTime(hour)


def get_weapon_name(weapon_id, size) -> :
    return GetWeaponName(weapon_id, size)


def enable_tire_popping(enable) -> :
    return EnableTirePopping(enable)


def enable_vehicle_friendly_fire() -> :
    return EnableVehicleFriendlyFire()


def allow_interior_weapons(allow) -> :
    return AllowInteriorWeapons(allow)


def set_weather(weatherid) -> :
    return SetWeather(weatherid)


def set_gravity(gravity) -> :
    return SetGravity(gravity)


def get_gravity() -> :
    return GetGravity()


def allow_admin_teleport(allow) -> :
    return AllowAdminTeleport(allow)


def set_death_drop_amount(amount) -> :
    return SetDeathDropAmount(amount)


def create_explosion(x: float, y: float, z: float, type, radius) -> :
    return CreateExplosion(x, y, z, type, radius)


def enable_zone_names(enable) -> :
    return EnableZoneNames(enable)


def use_player_ped_anims() -> :
    return UsePlayerPedAnims()


def disable_interior_enter_exits() -> :
    return DisableInteriorEnterExits()


def set_name_tag_draw_distance(distance) -> :
    return SetNameTagDrawDistance(distance)


def disable_name_tag_los() -> :
    return DisableNameTagLOS()


def limit_global_chat_radius(chat_radius) -> :
    return LimitGlobalChatRadius(chat_radius)


def limit_player_marker_radius(marker_radius) -> :
    return LimitPlayerMarkerRadius(marker_radius)


def connect_npc(name, script) -> :
    return ConnectNPC(name, script)


def is_player_npc(player_id: int) -> :
    return IsPlayerNPC(player_id)


def is_player_admin(player_id: int) -> :
    return IsPlayerAdmin(player_id)


def kick(player_id: int) -> :
    return Kick(player_id)


def ban(player_id: int) -> :
    return Ban(player_id)


def ban_ex(player_id: int, reason) -> :
    return BanEx(player_id, reason)


def send_rcon_command(command) -> :
    return SendRconCommand(command)


def get_player_network_stats(player_id: int, size) -> :
    return GetPlayerNetworkStats(player_id, size)


def get_network_stats(size) -> :
    return GetNetworkStats(size)


def get_player_version(player_id: int, len) -> :
    return GetPlayerVersion(player_id, len)


def block_ip_address(ip_address, timems) -> :
    return BlockIpAddress(ip_address, timems)


def un_block_ip_address(ip_address) -> :
    return UnBlockIpAddress(ip_address)


def get_server_var_as_string(varname, size) -> :
    return GetServerVarAsString(varname, size)


def get_server_var_as_int(varname) -> :
    return GetServerVarAsInt(varname)


def get_server_var_as_bool(varname) -> :
    return GetServerVarAsBool(varname)


def get_console_var_as_string(varname, len) -> :
    return GetConsoleVarAsString(varname, len)


def get_console_var_as_int(varname) -> :
    return GetConsoleVarAsInt(varname)


def get_console_var_as_bool(varname) -> :
    return GetConsoleVarAsBool(varname)


def get_server_tick_rate() -> :
    return GetServerTickRate()


def net_stats_get_connected_time(player_id: int) -> :
    return NetStats_GetConnectedTime(player_id)


def net_stats_messages_received(player_id: int) -> :
    return NetStats_MessagesReceived(player_id)


def net_stats_bytes_received(player_id: int) -> :
    return NetStats_BytesReceived(player_id)


def net_stats_messages_sent(player_id: int) -> :
    return NetStats_MessagesSent(player_id)


def net_stats_bytes_sent(player_id: int) -> :
    return NetStats_BytesSent(player_id)


def net_stats_messages_recv_per_second(player_id: int) -> :
    return NetStats_MessagesRecvPerSecond(player_id)


def net_stats_packet_loss_percent(player_id: int) -> :
    return NetStats_PacketLossPercent(player_id)


def net_stats_connection_status(player_id: int) -> :
    return NetStats_ConnectionStatus(player_id)


def net_stats_get_ip_port(player_id: int, ip_port_len) -> :
    return NetStats_GetIpPort(player_id, ip_port_len)


def create_menu(title, columns, x, y, col1width, col2width=0.0) -> :
    return CreateMenu(title, columns, x, y, col1width, col2width)


def destroy_menu(menuid) -> :
    return DestroyMenu(menuid)


def add_menu_item(menuid, column, menutext) -> :
    return AddMenuItem(menuid, column, menutext)


def set_menu_column_header(menuid, column, columnheader) -> :
    return SetMenuColumnHeader(menuid, column, columnheader)


def show_menu_for_player(menuid, player_id: int) -> :
    return ShowMenuForPlayer(menuid, player_id)


def hide_menu_for_player(menuid, player_id: int) -> :
    return HideMenuForPlayer(menuid, player_id)


def is_valid_menu(menuid) -> :
    return IsValidMenu(menuid)


def disable_menu(menuid) -> :
    return DisableMenu(menuid)


def disable_menu_row(menuid, row) -> :
    return DisableMenuRow(menuid, row)


def get_player_menu(player_id: int) -> :
    return GetPlayerMenu(player_id)


def text_draw_create(x, y, text) -> :
    return TextDrawCreate(x, y, text)


def text_draw_destroy(text) -> :
    return TextDrawDestroy(text)


def text_draw_letter_size(text, x, y) -> :
    return TextDrawLetterSize(text, x, y)


def text_draw_text_size(text, x, y) -> :
    return TextDrawTextSize(text, x, y)


def text_draw_alignment(text, alignment) -> :
    return TextDrawAlignment(text, alignment)


def text_draw_color(text, color) -> :
    return TextDrawColor(text, color)


def text_draw_use_box(text, use) -> :
    return TextDrawUseBox(text, use)


def text_draw_box_color(text, color) -> :
    return TextDrawBoxColor(text, color)


def text_draw_set_shadow(text, size) -> :
    return TextDrawSetShadow(text, size)


def text_draw_set_outline(text, size) -> :
    return TextDrawSetOutline(text, size)


def text_draw_background_color(text, color) -> :
    return TextDrawBackgroundColor(text, color)


def text_draw_font(text, font) -> :
    return TextDrawFont(text, font)


def text_draw_set_proportional(text, set) -> :
    return TextDrawSetProportional(text, set)


def text_draw_set_selectable(text, set) -> :
    return TextDrawSetSelectable(text, set)


def text_draw_show_for_player(player_id: int, text) -> :
    return TextDrawShowForPlayer(player_id, text)


def text_draw_hide_for_player(player_id: int, text) -> :
    return TextDrawHideForPlayer(player_id, text)


def text_draw_show_for_all(text) -> :
    return TextDrawShowForAll(text)


def text_draw_hide_for_all(text) -> :
    return TextDrawHideForAll(text)


def text_draw_set_string(text, string) -> :
    return TextDrawSetString(text, string)


def text_draw_set_preview_model(text, modelindex) -> :
    return TextDrawSetPreviewModel(text, modelindex)


def text_draw_set_preview_rot(text, fRotX, fRotY, fRotZ, fZoom=1.0) -> :
    return TextDrawSetPreviewRot(text, fRotX, fRotY, fRotZ, fZoom)


def text_draw_set_preview_veh_col(text, color1, color2) -> :
    return TextDrawSetPreviewVehCol(text, color1, color2)


def select_text_draw(player_id: int, hovercolor) -> :
    return SelectTextDraw(player_id, hovercolor)


def cancel_select_text_draw(player_id: int) -> :
    return CancelSelectTextDraw(player_id)


def gang_zone_create(minx, miny, maxx, maxy) -> :
    return GangZoneCreate(minx, miny, maxx, maxy)


def gang_zone_destroy(zone) -> :
    return GangZoneDestroy(zone)


def gang_zone_show_for_player(player_id: int, zone, color) -> :
    return GangZoneShowForPlayer(player_id, zone, color)


def gang_zone_show_for_all(zone, color) -> :
    return GangZoneShowForAll(zone, color)


def gang_zone_hide_for_player(player_id: int, zone) -> :
    return GangZoneHideForPlayer(player_id, zone)


def gang_zone_hide_for_all(zone) -> :
    return GangZoneHideForAll(zone)


def gang_zone_flash_for_player(player_id: int, zone, flashcolor) -> :
    return GangZoneFlashForPlayer(player_id, zone, flashcolor)


def gang_zone_flash_for_all(zone, flashcolor) -> :
    return GangZoneFlashForAll(zone, flashcolor)


def gang_zone_stop_flash_for_player(player_id: int, zone) -> :
    return GangZoneStopFlashForPlayer(player_id, zone)


def gang_zone_stop_flash_for_all(zone) -> :
    return GangZoneStopFlashForAll(zone)


def show_player_dialog(player_id: int, dialogid, style, caption, info, button1, button2) -> :
    return ShowPlayerDialog(player_id, dialogid, style, caption, info, button1, button2)


def add_char_model(baseid, newid, dffname, txdname) -> :
    return AddCharModel(baseid, newid, dffname, txdname)


def add_simple_model(virtualworld, baseid, newid, dffname, txdname) -> :
    return AddSimpleModel(virtualworld, baseid, newid, dffname, txdname)


def add_simple_model_timed(
    virtualworld, baseid, newid, dffname, txdname, timeon, timeoff
) -> :
    return AddSimpleModelTimed(
        virtualworld, baseid, newid, dffname, txdname, timeon, timeoff
    )


def find_model_file_name_from_crc(crc, model_str_len) -> :
    return FindModelFileNameFromCRC(crc, model_str_len)


def find_texture_file_name_from_crc(crc, texture_str_len) -> :
    return FindTextureFileNameFromCRC(crc, texture_str_len)


def redirect_download(player_id: int, url) -> :
    return RedirectDownload(player_id, url)


def is_valid_vehicle(vehicleid) -> :
    return IsValidVehicle(vehicleid)


def get_vehicle_distance_from_point(vehicleid, x: float, y: float, z: float) -> :
    return GetVehicleDistanceFromPoint(vehicleid, x, y, z)


def create_vehicle(
    vehicletype,
    x: float,
    y: float,
    z: float,
    rotation,
    color1,
    color2,
    respawn_delay,
    addsiren=False,
) -> :
    return CreateVehicle(
        vehicletype, x, y, z, rotation, color1, color2, respawn_delay, addsiren
    )


def destroy_vehicle(vehicleid) -> :
    return DestroyVehicle(vehicleid)


def is_vehicle_streamed_in(vehicleid, forplayer_id: int) -> :
    return IsVehicleStreamedIn(vehicleid, forplayer_id)


def get_vehicle_pos(vehicleid) -> :
    return GetVehiclePos(vehicleid)


def set_vehicle_pos(vehicleid, x: float, y: float, z: float) -> :
    return SetVehiclePos(vehicleid, x, y, z)


def get_vehicle_z_angle(vehicleid) -> :
    return GetVehicleZAngle(vehicleid)


def get_vehicle_rotation_quat(vehicleid) -> :
    return GetVehicleRotationQuat(vehicleid)


def set_vehicle_z_angle(vehicleid, z_angle: float) -> :
    return SetVehicleZAngle(vehicleid, z_angle)


def set_vehicle_params_for_player(vehicleid, player_id: int, objective, doorslocked) -> :
    return SetVehicleParamsForPlayer(vehicleid, player_id, objective, doorslocked)


def manual_vehicle_engine_and_lights() -> :
    return ManualVehicleEngineAndLights()


def set_vehicle_params_ex(
    vehicleid: int,
    engine: int,
    lights: int,
    alarm: int,
    doors: int,
    bonnet: int,
    boot: int,
    objective: int,
) -> :
    return SetVehicleParamsEx(
        vehicleid, engine, lights, alarm, doors, bonnet, boot, objective
    )


def get_vehicle_params_ex(vehicleid: int) -> :
    return GetVehicleParamsEx(vehicleid)


def get_vehicle_params_siren_state(vehicleid: int) -> :
    return GetVehicleParamsSirenState(vehicleid)


def set_vehicle_params_car_doors(
    vehicleid: int, driver: int, passenger: int, backleft: int, backright: int
) -> :
    return SetVehicleParamsCarDoors(vehicleid, driver, passenger, backleft, backright)


def get_vehicle_params_car_doors(vehicleid) -> :
    return GetVehicleParamsCarDoors(vehicleid)


def set_vehicle_params_car_windows(
    vehicleid: int, driver: int, passenger: int, backleft: int, backright: int
) -> :
    return SetVehicleParamsCarWindows(vehicleid, driver, passenger, backleft, backright)


def get_vehicle_params_car_windows(vehicleid: int) -> :
    return GetVehicleParamsCarWindows(vehicleid)


def set_vehicle_to_respawn(vehicleid: int) -> :
    return SetVehicleToRespawn(vehicleid)


def link_vehicle_to_interior(vehicleid: int, interiorid: int) -> :
    return LinkVehicleToInterior(vehicleid, interiorid)


def add_vehicle_component(vehicleid: int, componentid: int) -> :
    return AddVehicleComponent(vehicleid, componentid)


def remove_vehicle_component(vehicleid: int, componentid: int) -> :
    return RemoveVehicleComponent(vehicleid, componentid)


def change_vehicle_color(vehicleid: int, color1: int, color2: int) -> :
    return ChangeVehicleColor(vehicleid, color1, color2)


def change_vehicle_paintjob(vehicleid: int, paintjobid: int) -> :
    return ChangeVehiclePaintjob(vehicleid, paintjobid)


def set_vehicle_health(vehicleid: int, health: float) -> :
    return SetVehicleHealth(vehicleid, health)


def get_vehicle_health(vehicleid: int) -> :
    return GetVehicleHealth(vehicleid)


def attach_trailer_to_vehicle(trailerid: int, vehicleid: int) -> :
    return AttachTrailerToVehicle(trailerid, vehicleid)


def detach_trailer_from_vehicle(vehicleid: int) -> :
    return DetachTrailerFromVehicle(vehicleid)


def is_trailer_attached_to_vehicle(vehicleid: int) -> :
    return IsTrailerAttachedToVehicle(vehicleid)


def get_vehicle_trailer(vehicleid: int) -> :
    return GetVehicleTrailer(vehicleid)


def set_vehicle_number_plate(vehicleid: int, numberplate) -> :
    return SetVehicleNumberPlate(vehicleid, numberplate)


def get_vehicle_model(vehicleid) -> :
    return GetVehicleModel(vehicleid)


def get_vehicle_component_in_slot(vehicleid: int, slot: int) -> :
    return GetVehicleComponentInSlot(vehicleid, slot)


def get_vehicle_component_type(component: int) -> :
    return GetVehicleComponentType(component)


def repair_vehicle(vehicleid: int) -> :
    return RepairVehicle(vehicleid)


def get_vehicle_velocity(vehicleid: int) -> :
    return GetVehicleVelocity(vehicleid)


def set_vehicle_velocity(vehicleid: int, X: float, Y: float, Z: float) -> :
    return SetVehicleVelocity(vehicleid, X, Y, Z)


def set_vehicle_angular_velocity(vehicleid: int, X: float, Y: float, Z: float) -> :
    return SetVehicleAngularVelocity(vehicleid, X, Y, Z)


def get_vehicle_damage_status(vehicleid: int) -> :
    return GetVehicleDamageStatus(vehicleid)


def update_vehicle_damage_status(
    vehicleid: int, panels: int, doors: int, lights: int, tires: int
) -> :
    return UpdateVehicleDamageStatus(vehicleid, panels, doors, lights, tires)


def set_vehicle_virtual_world(vehicleid: int, worldid: int) -> :
    return SetVehicleVirtualWorld(vehicleid, worldid)


def get_vehicle_virtual_world(vehicleid: int) -> :
    return GetVehicleVirtualWorld(vehicleid)


def get_vehicle_model_info(model: int, infotype: int) -> :
    return GetVehicleModelInfo(model, infotype)


def create_actor(modelid: int, x: float, y: float, z: float, rotation: float) -> :
    return CreateActor(modelid, x, y, z, rotation)


def destroy_actor(actorid: int) -> :
    return DestroyActor(actorid)


def is_actor_streamed_in(actorid: int, forplayer_id: int) -> :
    return IsActorStreamedIn(actorid, forplayer_id)


def set_actor_virtual_world(actorid: int, vworld: int) -> :
    return SetActorVirtualWorld(actorid, vworld)


def get_actor_virtual_world(actorid: int) -> :
    return GetActorVirtualWorld(actorid)


def apply_actor_animation(
    actorid: int,
    animlib: str,
    animname: str,
    fDelta: float,
    loop: int,
    lockx: int,
    locky: int,
    freeze: int,
    time: int,
) -> :
    return ApplyActorAnimation(
        actorid, animlib, animname, fDelta, loop, lockx, locky, freeze, time
    )


def clear_actor_animations(actorid: int) -> :
    return ClearActorAnimations(actorid)


def set_actor_pos(actorid: int, x: float, y: float, z: float) -> :
    return SetActorPos(actorid, x, y, z)


def get_actor_pos(actorid: int) -> :
    return GetActorPos(actorid)


def set_actor_facing_angle(actorid: int, angle: float) -> :
    return SetActorFacingAngle(actorid, angle)


def get_actor_facing_angle(actorid: int) -> :
    return GetActorFacingAngle(actorid)


def set_actor_health(actorid: int, health: float) -> :
    return SetActorHealth(actorid, health)


def get_actor_health(actorid: int) -> :
    return GetActorHealth(actorid)


def set_actor_invulnerable(actorid: int, invulnerable=True) -> :
    return SetActorInvulnerable(actorid, invulnerable)


def is_actor_invulnerable(actorid: int) -> :
    return IsActorInvulnerable(actorid)


def is_valid_actor(actorid: int) -> :
    return IsValidActor(actorid)


def http(index: int, type: int, url: str, data: str, callback) -> :
    return HTTP(index, type, url, data, callback)


def create_3d_text_label(
    text,
    color,
    x: float,
    y: float,
    z: float,
    drawDistance: float,
    virtualworld: int,
    testLOS=False,
) -> :
    return Create3DTextLabel(text, color, x, y, z, drawDistance, virtualworld, testLOS)


def delete_3d_text_label(id) -> :
    return Delete3DTextLabel(id)


def attach_3d_text_label_to_player(id, player_id: int, offsetX, offsetY, offsetZ) -> :
    return Attach3DTextLabelToPlayer(id, player_id, offsetX, offsetY, offsetZ)


def attach_3d_text_label_to_vehicle(id, vehicleid, offsetX, offsetY, offsetZ) -> :
    return Attach3DTextLabelToVehicle(id, vehicleid, offsetX, offsetY, offsetZ)


def update_3d_text_label_text(id, color, text) -> :
    return Update3DTextLabelText(id, color, text)


def create_player_3d_text_label(
    player_id,
    text,
    color,
    x,
    y,
    z,
    drawDistance,
    attachedplayer=INVALID_PLAYER_ID,
    attachedvehicle=INVALID_VEHICLE_ID,
    testLOS=False,
) -> :
    return CreatePlayer3DTextLabel(
        player_id,
        text,
        color,
        x,
        y,
        z,
        drawDistance,
        attachedplayer,
        attachedvehicle,
        testLOS,
    )


def delete_player_3d_text_label(player_id: int, id) -> :
    return DeletePlayer3DTextLabel(player_id, id)


def update_player_3d_text_label_text(player_id: int, id, color, text) -> :
    return UpdatePlayer3DTextLabelText(player_id, id, color, text)
