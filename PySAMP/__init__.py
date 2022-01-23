from samp import *

########################
# SNAKE CASE WRAPPERS FOR PEP8 COMPATIBILITY
########################


def set_spawn_info(
    playerid: int,
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
):
    return SetSpawnInfo(
        playerid,
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


def spawn_player(playerid: int):
    return SpawnPlayer(playerid)


def set_player_pos(playerid: int, x: float, y: float, z: float):
    return SetPlayerPos(playerid, x, y, z)


def set_player_pos_find_z(playerid: int, x: float, y: float, z: float):
    return SetPlayerPosFindZ(playerid, x, y, z)


def get_player_pos(playerid: int):
    return GetPlayerPos(playerid)


def set_player_facing_angle(playerid: int, angle: float):
    return SetPlayerFacingAngle(playerid, angle)


def get_player_facing_angle(playerid: int):
    return GetPlayerFacingAngle(playerid)


def is_player_in_range_of_point(
    playerid: int, range: float, x: float, y: float, z: float
):
    return IsPlayerInRangeOfPoint(playerid, range, x, y, z)


def get_player_distance_from_point(playerid: int, x: float, y: float, z: float):
    return GetPlayerDistanceFromPoint(playerid, x, y, z)


def is_player_streamed_in(playerid: int, forplayerid):
    return IsPlayerStreamedIn(playerid, forplayerid)


def set_player_interior(playerid: int, interiorid):
    return SetPlayerInterior(playerid, interiorid)


def get_player_interior(playerid: int):
    return GetPlayerInterior(playerid)


def set_player_health(playerid: int, health):
    return SetPlayerHealth(playerid, health)


def get_player_health(playerid: int):
    return GetPlayerHealth(playerid)


def set_player_armour(playerid: int, armour):
    return SetPlayerArmour(playerid, armour)


def get_player_armour(playerid: int):
    return GetPlayerArmour(playerid)


def set_player_ammo(playerid: int, weaponid, ammo):
    return SetPlayerAmmo(playerid, weaponid, ammo)


def get_player_ammo(playerid: int):
    return GetPlayerAmmo(playerid)


def get_player_weapon_state(playerid: int):
    return GetPlayerWeaponState(playerid)


def get_player_target_player(playerid: int):
    return GetPlayerTargetPlayer(playerid)


def get_player_target_actor(playerid: int):
    return GetPlayerTargetActor(playerid)


def set_player_team(playerid: int, teamid):
    return SetPlayerTeam(playerid, teamid)


def get_player_team(playerid: int):
    return GetPlayerTeam(playerid)


def set_player_score(playerid: int, score):
    return SetPlayerScore(playerid, score)


def get_player_score(playerid: int):
    return GetPlayerScore(playerid)


def get_player_drunk_level(playerid: int):
    return GetPlayerDrunkLevel(playerid)


def set_player_drunk_level(playerid: int, level):
    return SetPlayerDrunkLevel(playerid, level)


def set_player_color(playerid: int, color):
    return SetPlayerColor(playerid, color)


def get_player_color(playerid: int):
    return GetPlayerColor(playerid)


def set_player_skin(playerid: int, skinid):
    return SetPlayerSkin(playerid, skinid)


def get_player_skin(playerid: int):
    return GetPlayerSkin(playerid)


def give_player_weapon(playerid: int, weaponid, ammo):
    return GivePlayerWeapon(playerid, weaponid, ammo)


def reset_player_weapons(playerid: int):
    return ResetPlayerWeapons(playerid)


def set_player_armed_weapon(playerid: int, weaponid):
    return SetPlayerArmedWeapon(playerid, weaponid)


def get_player_weapon_data(playerid: int, slot):
    return GetPlayerWeaponData(playerid, slot)


def give_player_money(playerid: int, money):
    return GivePlayerMoney(playerid, money)


def reset_player_money(playerid: int):
    return ResetPlayerMoney(playerid)


def set_player_name(playerid: int, name):
    return SetPlayerName(playerid, name)


def get_player_money(playerid: int):
    return GetPlayerMoney(playerid)


def get_player_state(playerid: int):
    return GetPlayerState(playerid)


def get_player_ip(playerid: int, size):
    return GetPlayerIp(playerid, size)


def get_player_ping(playerid: int):
    return GetPlayerPing(playerid)


def get_player_weapon(playerid: int):
    return GetPlayerWeapon(playerid)


def get_player_keys(playerid: int):
    return GetPlayerKeys(playerid)


def get_player_name(playerid: int, size):
    return GetPlayerName(playerid, size)


def set_player_time(playerid: int, hour, minute):
    return SetPlayerTime(playerid, hour, minute)


def get_player_time(playerid: int):
    return GetPlayerTime(playerid)


def toggle_player_clock(playerid: int, toggle):
    return TogglePlayerClock(playerid, toggle)


def set_player_weather(playerid: int, weather):
    return SetPlayerWeather(playerid, weather)


def force_class_selection(playerid: int):
    return ForceClassSelection(playerid)


def set_player_wanted_level(playerid: int, level):
    return SetPlayerWantedLevel(playerid, level)


def get_player_wanted_level(playerid: int):
    return GetPlayerWantedLevel(playerid)


def set_player_fighting_style(playerid: int, style):
    return SetPlayerFightingStyle(playerid, style)


def get_player_fighting_style(playerid: int):
    return GetPlayerFightingStyle(playerid)


def set_player_velocity(playerid: int, x: float, y: float, z: float):
    return SetPlayerVelocity(playerid, x, y, z)


def get_player_velocity(playerid: int):
    return GetPlayerVelocity(playerid)


def play_crime_report_for_player(playerid: int, suspectid, crime):
    return PlayCrimeReportForPlayer(playerid, suspectid, crime)


def play_audio_stream_for_player(
    playerid, url, posX=0.0, posY=0.0, posZ=0.0, distance=50.0, usepos=False
):
    return PlayAudioStreamForPlayer(playerid, url, posX, posY, posZ, distance, usepos)


def stop_audio_stream_for_player(playerid: int):
    return StopAudioStreamForPlayer(playerid)


def set_player_shop_name(playerid: int, shopname):
    return SetPlayerShopName(playerid, shopname)


def set_player_skill_level(playerid: int, skill, level):
    return SetPlayerSkillLevel(playerid, skill, level)


def get_player_surfing_vehicle_id(playerid: int):
    return GetPlayerSurfingVehicleID(playerid)


def get_player_surfing_object_id(playerid: int):
    return GetPlayerSurfingObjectID(playerid)


def remove_building_for_player(playerid: int, modelid, fX, fY, fZ, fRadius):
    return RemoveBuildingForPlayer(playerid, modelid, fX, fY, fZ, fRadius)


def get_player_last_shot_vectors(playerid: int):
    return GetPlayerLastShotVectors(playerid)


def set_player_attached_object(
    playerid,
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
):
    return SetPlayerAttachedObject(
        playerid,
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


def remove_player_attached_object(playerid: int, index):
    return RemovePlayerAttachedObject(playerid, index)


def is_player_attached_object_slot_used(playerid: int, index):
    return IsPlayerAttachedObjectSlotUsed(playerid, index)


def edit_attached_object(playerid: int, index):
    return EditAttachedObject(playerid, index)


def create_player_text_draw(playerid: int, x, y, text):
    return CreatePlayerTextDraw(playerid, x, y, text)


def player_text_draw_destroy(playerid: int, text):
    return PlayerTextDrawDestroy(playerid, text)


def player_text_draw_letter_size(playerid: int, text, x, y):
    return PlayerTextDrawLetterSize(playerid, text, x, y)


def player_text_draw_text_size(playerid: int, text, x, y):
    return PlayerTextDrawTextSize(playerid, text, x, y)


def player_text_draw_alignment(playerid: int, text, alignment):
    return PlayerTextDrawAlignment(playerid, text, alignment)


def player_text_draw_color(playerid: int, text, color):
    return PlayerTextDrawColor(playerid, text, color)


def player_text_draw_use_box(playerid: int, text, use):
    return PlayerTextDrawUseBox(playerid, text, use)


def player_text_draw_box_color(playerid: int, text, color):
    return PlayerTextDrawBoxColor(playerid, text, color)


def player_text_draw_set_shadow(playerid: int, text, size):
    return PlayerTextDrawSetShadow(playerid, text, size)


def player_text_draw_set_outline(playerid: int, text, size):
    return PlayerTextDrawSetOutline(playerid, text, size)


def player_text_draw_background_color(playerid: int, text, color):
    return PlayerTextDrawBackgroundColor(playerid, text, color)


def player_text_draw_font(playerid: int, text, font):
    return PlayerTextDrawFont(playerid, text, font)


def player_text_draw_set_proportional(playerid: int, text, set):
    return PlayerTextDrawSetProportional(playerid, text, set)


def player_text_draw_set_selectable(playerid: int, text, set):
    return PlayerTextDrawSetSelectable(playerid, text, set)


def player_text_draw_show(playerid: int, text):
    return PlayerTextDrawShow(playerid, text)


def player_text_draw_hide(playerid: int, text):
    return PlayerTextDrawHide(playerid, text)


def player_text_draw_set_string(playerid: int, text, string):
    return PlayerTextDrawSetString(playerid, text, string)


def player_text_draw_set_preview_model(playerid: int, text, modelindex):
    return PlayerTextDrawSetPreviewModel(playerid, text, modelindex)


def player_text_draw_set_preview_rot(
    playerid: int, text, fRotX, fRotY, fRotZ, fZoom=1.0
):
    return PlayerTextDrawSetPreviewRot(playerid, text, fRotX, fRotY, fRotZ, fZoom)


def player_text_draw_set_preview_veh_col(playerid: int, text, color1, color2):
    return PlayerTextDrawSetPreviewVehCol(playerid, text, color1, color2)


def set_pvar_int(playerid: int, varname, value):
    return SetPVarInt(playerid, varname, value)


def get_pvar_int(playerid: int, varname):
    return GetPVarInt(playerid, varname)


def set_pvar_string(playerid: int, varname, value):
    return SetPVarString(playerid, varname, value)


def get_pvar_string(playerid: int, varname, size):
    return GetPVarString(playerid, varname, size)


def set_pvar_float(playerid: int, varname, value):
    return SetPVarFloat(playerid, varname, value)


def get_pvar_float(playerid: int, varname):
    return GetPVarFloat(playerid, varname)


def delete_pvar(playerid: int, varname):
    return DeletePVar(playerid, varname)


def get_pvars_upper_index(playerid: int):
    return GetPVarsUpperIndex(playerid)


def get_pvar_name_at_index(playerid: int, index, size):
    return GetPVarNameAtIndex(playerid, index, size)


def get_pvar_type(playerid: int, varname):
    return GetPVarType(playerid, varname)


def set_player_chat_bubble(playerid: int, text, color, drawdistance, expiretime):
    return SetPlayerChatBubble(playerid, text, color, drawdistance, expiretime)


def put_player_in_vehicle(playerid: int, vehicleid, seatid):
    return PutPlayerInVehicle(playerid, vehicleid, seatid)


def get_player_vehicle_id(playerid: int):
    return GetPlayerVehicleID(playerid)


def get_player_vehicle_seat(playerid: int):
    return GetPlayerVehicleSeat(playerid)


def remove_player_from_vehicle(playerid: int):
    return RemovePlayerFromVehicle(playerid)


def toggle_player_controllable(playerid: int, toggle):
    return TogglePlayerControllable(playerid, toggle)


def player_play_sound(playerid: int, soundid, x: float, y: float, z: float):
    return PlayerPlaySound(playerid, soundid, x, y, z)


def apply_animation(
    playerid,
    animlib,
    animname,
    fDelta,
    loop,
    lockx,
    locky,
    freeze,
    time,
    forcesync=False,
):
    return ApplyAnimation(
        playerid, animlib, animname, fDelta, loop, lockx, locky, freeze, time, forcesync
    )


def clear_animations(playerid: int, forcesync=False):
    return ClearAnimations(playerid, forcesync)


def get_player_animation_index(playerid: int):
    return GetPlayerAnimationIndex(playerid)


def get_animation_name(index, animlib_size, animname_size):
    return GetAnimationName(index, animlib_size, animname_size)


def get_player_special_action(playerid: int):
    return GetPlayerSpecialAction(playerid)


def set_player_special_action(playerid: int, actionid):
    return SetPlayerSpecialAction(playerid, actionid)


def disable_remote_vehicle_collisions(playerid: int, disable):
    return DisableRemoteVehicleCollisions(playerid, disable)


def set_player_checkpoint(playerid: int, x: float, y: float, z: float, size):
    return SetPlayerCheckpoint(playerid, x, y, z, size)


def disable_player_checkpoint(playerid: int):
    return DisablePlayerCheckpoint(playerid)


def set_player_race_checkpoint(
    playerid: int, type, x: float, y: float, z: float, nextx, nexty, nextz, size
):
    return SetPlayerRaceCheckpoint(playerid, type, x, y, z, nextx, nexty, nextz, size)


def disable_player_race_checkpoint(playerid: int):
    return DisablePlayerRaceCheckpoint(playerid)


def set_player_world_bounds(playerid: int, x_max, x_min, y_max, y_min):
    return SetPlayerWorldBounds(playerid, x_max, x_min, y_max, y_min)


def set_player_marker_for_player(playerid: int, showplayerid, color):
    return SetPlayerMarkerForPlayer(playerid, showplayerid, color)


def show_player_name_tag_for_player(playerid: int, showplayerid, show):
    return ShowPlayerNameTagForPlayer(playerid, showplayerid, show)


def set_player_map_icon(
    playerid,
    iconid,
    x: float,
    y: float,
    z: float,
    markertype,
    color,
    style=MAPICON_LOCAL,
):
    return SetPlayerMapIcon(playerid, iconid, x, y, z, markertype, color, style)


def remove_player_map_icon(playerid: int, iconid):
    return RemovePlayerMapIcon(playerid, iconid)


def allow_player_teleport(playerid: int, allow):
    return AllowPlayerTeleport(playerid, allow)


def set_player_camera_pos(playerid: int, x: float, y: float, z: float):
    return SetPlayerCameraPos(playerid, x, y, z)


def set_player_camera_look_at(
    playerid: int, x: float, y: float, z: float, cut=CAMERA_CUT
):
    return SetPlayerCameraLookAt(playerid, x, y, z, cut)


def set_camera_behind_player(playerid: int):
    return SetCameraBehindPlayer(playerid)


def get_player_camera_pos(playerid: int):
    return GetPlayerCameraPos(playerid)


def get_player_camera_front_vector(playerid: int):
    return GetPlayerCameraFrontVector(playerid)


def get_player_camera_mode(playerid: int):
    return GetPlayerCameraMode(playerid)


def enable_player_camera_target(playerid: int, enable):
    return EnablePlayerCameraTarget(playerid, enable)


def get_player_camera_target_object(playerid: int):
    return GetPlayerCameraTargetObject(playerid)


def get_player_camera_target_vehicle(playerid: int):
    return GetPlayerCameraTargetVehicle(playerid)


def get_player_camera_target_player(playerid: int):
    return GetPlayerCameraTargetPlayer(playerid)


def get_player_camera_target_actor(playerid: int):
    return GetPlayerCameraTargetActor(playerid)


def get_player_camera_aspect_ratio(playerid: int):
    return GetPlayerCameraAspectRatio(playerid)


def get_player_camera_zoom(playerid: int):
    return GetPlayerCameraZoom(playerid)


def attach_camera_to_object(playerid: int, objectid):
    return AttachCameraToObject(playerid, objectid)


def attach_camera_to_player_object(playerid: int, playerobjectid):
    return AttachCameraToPlayerObject(playerid, playerobjectid)


def interpolate_camera_pos(
    playerid, FromX, FromY, FromZ, ToX, ToY, ToZ, time, cut=CAMERA_CUT
):
    return InterpolateCameraPos(playerid, FromX, FromY, FromZ, ToX, ToY, ToZ, time, cut)


def interpolate_camera_look_at(
    playerid, FromX, FromY, FromZ, ToX, ToY, ToZ, time, cut=CAMERA_CUT
):
    return InterpolateCameraLookAt(
        playerid, FromX, FromY, FromZ, ToX, ToY, ToZ, time, cut
    )


def is_player_connected(playerid: int):
    return IsPlayerConnected(playerid)


def is_player_in_vehicle(playerid: int, vehicleid):
    return IsPlayerInVehicle(playerid, vehicleid)


def is_player_in_any_vehicle(playerid: int):
    return IsPlayerInAnyVehicle(playerid)


def is_player_in_checkpoint(playerid: int):
    return IsPlayerInCheckpoint(playerid)


def is_player_in_race_checkpoint(playerid: int):
    return IsPlayerInRaceCheckpoint(playerid)


def set_player_virtual_world(playerid: int, worldid):
    return SetPlayerVirtualWorld(playerid, worldid)


def get_player_virtual_world(playerid: int):
    return GetPlayerVirtualWorld(playerid)


def enable_stunt_bonus_for_player(playerid: int, enable):
    return EnableStuntBonusForPlayer(playerid, enable)


def enable_stunt_bonus_for_all(enable):
    return EnableStuntBonusForAll(enable)


def toggle_player_spectating(playerid: int, toggle):
    return TogglePlayerSpectating(playerid, toggle)


def player_spectate_player(playerid: int, targetplayerid, mode=SPECTATE_MODE_NORMAL):
    return PlayerSpectatePlayer(playerid, targetplayerid, mode)


def player_spectate_vehicle(playerid: int, targetvehicleid, mode=SPECTATE_MODE_NORMAL):
    return PlayerSpectateVehicle(playerid, targetvehicleid, mode)


def start_recording_player_data(playerid: int, recordtype, recordname):
    return StartRecordingPlayerData(playerid, recordtype, recordname)


def stop_recording_player_data(playerid: int):
    return StopRecordingPlayerData(playerid)


def create_explosion_for_player(playerid: int, X, Y, Z, type, Radius):
    return CreateExplosionForPlayer(playerid, X, Y, Z, type, Radius)


def create_object(modelid, x: float, y: float, z: float, rX, rY, rZ, DrawDistance=0.0):
    return CreateObject(modelid, x, y, z, rX, rY, rZ, DrawDistance)


def attach_object_to_vehicle(
    objectid, vehicleid, fOffsetX, fOffsetY, fOffsetZ, fRotX, fRotY, fRotZ
):
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
):
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
    objectid, playerid, fOffsetX, fOffsetY, fOffsetZ, fRotX, fRotY, fRotZ
):
    return AttachObjectToPlayer(
        objectid, playerid, fOffsetX, fOffsetY, fOffsetZ, fRotX, fRotY, fRotZ
    )


def set_object_pos(objectid, x: float, y: float, z: float):
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


def move_object(
    objectid,
    x: float,
    y: float,
    z: float,
    Speed,
    RotX=-1000.0,
    RotY=-1000.0,
    RotZ=-1000.0,
):
    return MoveObject(objectid, X, Y, Z, Speed, RotX, RotY, RotZ)


def stop_object(objectid):
    return StopObject(objectid)


def is_object_moving(objectid):
    return IsObjectMoving(objectid)


def edit_object(playerid: int, objectid):
    return EditObject(playerid, objectid)


def edit_player_object(playerid: int, objectid):
    return EditPlayerObject(playerid, objectid)


def select_object(playerid: int):
    return SelectObject(playerid)


def cancel_edit(playerid: int):
    return CancelEdit(playerid)


def create_player_object(
    playerid: int, modelid, x: float, y: float, z: float, rX, rY, rZ, DrawDistance=0.0
):
    return CreatePlayerObject(playerid, modelid, x, y, z, rX, rY, rZ, DrawDistance)


def attach_player_object_to_player(
    objectplayer, objectid, attachplayer, OffsetX, OffsetY, OffsetZ, rX, rY, rZ
):
    return AttachPlayerObjectToPlayer(
        objectplayer, objectid, attachplayer, OffsetX, OffsetY, OffsetZ, rX, rY, rZ
    )


def attach_player_object_to_vehicle(
    playerid, objectid, vehicleid, fOffsetX, fOffsetY, fOffsetZ, fRotX, fRotY, RotZ
):
    return AttachPlayerObjectToVehicle(
        playerid, objectid, vehicleid, fOffsetX, fOffsetY, fOffsetZ, fRotX, fRotY, RotZ
    )


def set_player_object_pos(playerid: int, objectid, x: float, y: float, z: float):
    return SetPlayerObjectPos(playerid, objectid, x, y, z)


def get_player_object_pos(playerid: int, objectid):
    return GetPlayerObjectPos(playerid, objectid)


def set_player_object_rot(playerid: int, objectid, rotX, rotY, rotZ):
    return SetPlayerObjectRot(playerid, objectid, rotX, rotY, rotZ)


def get_player_object_rot(playerid: int, objectid):
    return GetPlayerObjectRot(playerid, objectid)


def get_player_object_model(playerid: int, objectid):
    return GetPlayerObjectModel(playerid, objectid)


def set_player_object_no_camera_col(playerid: int, objectid):
    return SetPlayerObjectNoCameraCol(playerid, objectid)


def is_valid_player_object(playerid: int, objectid):
    return IsValidPlayerObject(playerid, objectid)


def destroy_player_object(playerid: int, objectid):
    return DestroyPlayerObject(playerid, objectid)


def move_player_object(
    playerid,
    objectid,
    x: float,
    y: float,
    z: float,
    Speed,
    RotX=-1000.0,
    RotY=-1000.0,
    RotZ=-1000.0,
):
    return MovePlayerObject(playerid, objectid, x, y, z, Speed, RotX, RotY, RotZ)


def stop_player_object(playerid: int, objectid):
    return StopPlayerObject(playerid, objectid)


def is_player_object_moving(playerid: int, objectid):
    return IsPlayerObjectMoving(playerid, objectid)


def set_object_material(
    objectid, materialindex, modelid, txdname, texturename, materialcolor=0
):
    return SetObjectMaterial(
        objectid, materialindex, modelid, txdname, texturename, materialcolor
    )


def set_player_object_material(
    playerid, objectid, materialindex, modelid, txdname, texturename, materialcolor=0
):
    return SetPlayerObjectMaterial(
        playerid, objectid, materialindex, modelid, txdname, texturename, materialcolor
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
):
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
    playerid,
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
):
    return SetPlayerObjectMaterialText(
        playerid,
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


def set_objects_default_camera_col(disable):
    return SetObjectsDefaultCameraCol(disable)


def send_client_message(playerid: int, color, message):
    return SendClientMessage(playerid, color, message)


def send_client_message_to_all(color, message):
    return SendClientMessageToAll(color, message)


def send_player_message_to_player(playerid: int, senderid, message):
    return SendPlayerMessageToPlayer(playerid, senderid, message)


def send_player_message_to_all(senderid, message):
    return SendPlayerMessageToAll(senderid, message)


def send_death_message(killer, killee, weapon):
    return SendDeathMessage(killer, killee, weapon)


def send_death_message_to_player(playerid: int, killer, killee, weapon):
    return SendDeathMessageToPlayer(playerid, killer, killee, weapon)


def game_text_for_all(text, time, style):
    return GameTextForAll(text, time, style)


def game_text_for_player(playerid: int, text, time, style):
    return GameTextForPlayer(playerid, text, time, style)


def get_tick_count():
    return GetTickCount()


def get_max_players():
    return GetMaxPlayers()


def vector_size(x: float, y: float, z: float):
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
):
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
):
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
):
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
):
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
):
    return AddStaticPickup(model, type, x, y, z, virtualworld)


def create_pickup(model: int, type: int, x: float, y: float, z: float, virtualworld=0):
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


def create_explosion(x: float, y: float, z: float, type, radius):
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


def is_player_npc(playerid: int):
    return IsPlayerNPC(playerid)


def is_player_admin(playerid: int):
    return IsPlayerAdmin(playerid)


def kick(playerid: int):
    return Kick(playerid)


def ban(playerid: int):
    return Ban(playerid)


def ban_ex(playerid: int, reason):
    return BanEx(playerid, reason)


def send_rcon_command(command):
    return SendRconCommand(command)


def get_player_network_stats(playerid: int, size):
    return GetPlayerNetworkStats(playerid, size)


def get_network_stats(size):
    return GetNetworkStats(size)


def get_player_version(playerid: int, len):
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


def net_stats_get_connected_time(playerid: int):
    return NetStats_GetConnectedTime(playerid)


def net_stats_messages_received(playerid: int):
    return NetStats_MessagesReceived(playerid)


def net_stats_bytes_received(playerid: int):
    return NetStats_BytesReceived(playerid)


def net_stats_messages_sent(playerid: int):
    return NetStats_MessagesSent(playerid)


def net_stats_bytes_sent(playerid: int):
    return NetStats_BytesSent(playerid)


def net_stats_messages_recv_per_second(playerid: int):
    return NetStats_MessagesRecvPerSecond(playerid)


def net_stats_packet_loss_percent(playerid: int):
    return NetStats_PacketLossPercent(playerid)


def net_stats_connection_status(playerid: int):
    return NetStats_ConnectionStatus(playerid)


def net_stats_get_ip_port(playerid: int, ip_port_len):
    return NetStats_GetIpPort(playerid, ip_port_len)


def create_menu(title, columns, x, y, col1width, col2width=0.0):
    return CreateMenu(title, columns, x, y, col1width, col2width)


def destroy_menu(menuid):
    return DestroyMenu(menuid)


def add_menu_item(menuid, column, menutext):
    return AddMenuItem(menuid, column, menutext)


def set_menu_column_header(menuid, column, columnheader):
    return SetMenuColumnHeader(menuid, column, columnheader)


def show_menu_for_player(menuid, playerid: int):
    return ShowMenuForPlayer(menuid, playerid)


def hide_menu_for_player(menuid, playerid: int):
    return HideMenuForPlayer(menuid, playerid)


def is_valid_menu(menuid):
    return IsValidMenu(menuid)


def disable_menu(menuid):
    return DisableMenu(menuid)


def disable_menu_row(menuid, row):
    return DisableMenuRow(menuid, row)


def get_player_menu(playerid: int):
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


def text_draw_show_for_player(playerid: int, text):
    return TextDrawShowForPlayer(playerid, text)


def text_draw_hide_for_player(playerid: int, text):
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


def select_text_draw(playerid: int, hovercolor):
    return SelectTextDraw(playerid, hovercolor)


def cancel_select_text_draw(playerid: int):
    return CancelSelectTextDraw(playerid)


def gang_zone_create(minx, miny, maxx, maxy):
    return GangZoneCreate(minx, miny, maxx, maxy)


def gang_zone_destroy(zone):
    return GangZoneDestroy(zone)


def gang_zone_show_for_player(playerid: int, zone, color):
    return GangZoneShowForPlayer(playerid, zone, color)


def gang_zone_show_for_all(zone, color):
    return GangZoneShowForAll(zone, color)


def gang_zone_hide_for_player(playerid: int, zone):
    return GangZoneHideForPlayer(playerid, zone)


def gang_zone_hide_for_all(zone):
    return GangZoneHideForAll(zone)


def gang_zone_flash_for_player(playerid: int, zone, flashcolor):
    return GangZoneFlashForPlayer(playerid, zone, flashcolor)


def gang_zone_flash_for_all(zone, flashcolor):
    return GangZoneFlashForAll(zone, flashcolor)


def gang_zone_stop_flash_for_player(playerid: int, zone):
    return GangZoneStopFlashForPlayer(playerid, zone)


def gang_zone_stop_flash_for_all(zone):
    return GangZoneStopFlashForAll(zone)


def show_player_dialog(playerid: int, dialogid, style, caption, info, button1, button2):
    return ShowPlayerDialog(playerid, dialogid, style, caption, info, button1, button2)


def add_char_model(baseid, newid, dffname, txdname):
    return AddCharModel(baseid, newid, dffname, txdname)


def add_simple_model(virtualworld, baseid, newid, dffname, txdname):
    return AddSimpleModel(virtualworld, baseid, newid, dffname, txdname)


def add_simple_model_timed(
    virtualworld, baseid, newid, dffname, txdname, timeon, timeoff
):
    return AddSimpleModelTimed(
        virtualworld, baseid, newid, dffname, txdname, timeon, timeoff
    )


def find_model_file_name_from_crc(crc, model_str_len):
    return FindModelFileNameFromCRC(crc, model_str_len)


def find_texture_file_name_from_crc(crc, texture_str_len):
    return FindTextureFileNameFromCRC(crc, texture_str_len)


def redirect_download(playerid: int, url):
    return RedirectDownload(playerid, url)


def is_valid_vehicle(vehicleid):
    return IsValidVehicle(vehicleid)


def get_vehicle_distance_from_point(vehicleid, x: float, y: float, z: float):
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
):
    return CreateVehicle(
        vehicletype, x, y, z, rotation, color1, color2, respawn_delay, addsiren
    )


def destroy_vehicle(vehicleid):
    return DestroyVehicle(vehicleid)


def is_vehicle_streamed_in(vehicleid, forplayerid: int):
    return IsVehicleStreamedIn(vehicleid, forplayerid)


def get_vehicle_pos(vehicleid):
    return GetVehiclePos(vehicleid)


def set_vehicle_pos(vehicleid, x: float, y: float, z: float):
    return SetVehiclePos(vehicleid, x, y, z)


def get_vehicle_z_angle(vehicleid):
    return GetVehicleZAngle(vehicleid)


def get_vehicle_rotation_quat(vehicleid):
    return GetVehicleRotationQuat(vehicleid)


def set_vehicle_z_angle(vehicleid, z_angle: float):
    return SetVehicleZAngle(vehicleid, z_angle)


def set_vehicle_params_for_player(vehicleid, playerid: int, objective, doorslocked):
    return SetVehicleParamsForPlayer(vehicleid, playerid, objective, doorslocked)


def manual_vehicle_engine_and_lights():
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
):
    return SetVehicleParamsEx(
        vehicleid, engine, lights, alarm, doors, bonnet, boot, objective
    )


def get_vehicle_params_ex(vehicleid: int):
    return GetVehicleParamsEx(vehicleid)


def get_vehicle_params_siren_state(vehicleid: int):
    return GetVehicleParamsSirenState(vehicleid)


def set_vehicle_params_car_doors(
    vehicleid: int, driver: int, passenger: int, backleft: int, backright: int
):
    return SetVehicleParamsCarDoors(vehicleid, driver, passenger, backleft, backright)


def get_vehicle_params_car_doors(vehicleid):
    return GetVehicleParamsCarDoors(vehicleid)


def set_vehicle_params_car_windows(
    vehicleid: int, driver: int, passenger: int, backleft: int, backright: int
):
    return SetVehicleParamsCarWindows(vehicleid, driver, passenger, backleft, backright)


def get_vehicle_params_car_windows(vehicleid: int):
    return GetVehicleParamsCarWindows(vehicleid)


def set_vehicle_to_respawn(vehicleid: int):
    return SetVehicleToRespawn(vehicleid)


def link_vehicle_to_interior(vehicleid: int, interiorid: int):
    return LinkVehicleToInterior(vehicleid, interiorid)


def add_vehicle_component(vehicleid: int, componentid: int):
    return AddVehicleComponent(vehicleid, componentid)


def remove_vehicle_component(vehicleid: int, componentid: int):
    return RemoveVehicleComponent(vehicleid, componentid)


def change_vehicle_color(vehicleid: int, color1: int, color2: int):
    return ChangeVehicleColor(vehicleid, color1, color2)


def change_vehicle_paintjob(vehicleid: int, paintjobid: int):
    return ChangeVehiclePaintjob(vehicleid, paintjobid)


def set_vehicle_health(vehicleid: int, health: float):
    return SetVehicleHealth(vehicleid, health)


def get_vehicle_health(vehicleid: int):
    return GetVehicleHealth(vehicleid)


def attach_trailer_to_vehicle(trailerid: int, vehicleid: int):
    return AttachTrailerToVehicle(trailerid, vehicleid)


def detach_trailer_from_vehicle(vehicleid: int):
    return DetachTrailerFromVehicle(vehicleid)


def is_trailer_attached_to_vehicle(vehicleid: int):
    return IsTrailerAttachedToVehicle(vehicleid)


def get_vehicle_trailer(vehicleid: int):
    return GetVehicleTrailer(vehicleid)


def set_vehicle_number_plate(vehicleid: int, numberplate):
    return SetVehicleNumberPlate(vehicleid, numberplate)


def get_vehicle_model(vehicleid):
    return GetVehicleModel(vehicleid)


def get_vehicle_component_in_slot(vehicleid: int, slot: int):
    return GetVehicleComponentInSlot(vehicleid, slot)


def get_vehicle_component_type(component: int):
    return GetVehicleComponentType(component)


def repair_vehicle(vehicleid: int):
    return RepairVehicle(vehicleid)


def get_vehicle_velocity(vehicleid: int):
    return GetVehicleVelocity(vehicleid)


def set_vehicle_velocity(vehicleid: int, X: float, Y: float, Z: float):
    return SetVehicleVelocity(vehicleid, X, Y, Z)


def set_vehicle_angular_velocity(vehicleid: int, X: float, Y: float, Z: float):
    return SetVehicleAngularVelocity(vehicleid, X, Y, Z)


def get_vehicle_damage_status(vehicleid: int):
    return GetVehicleDamageStatus(vehicleid)


def update_vehicle_damage_status(
    vehicleid: int, panels: int, doors: int, lights: int, tires: int
):
    return UpdateVehicleDamageStatus(vehicleid, panels, doors, lights, tires)


def set_vehicle_virtual_world(vehicleid: int, worldid: int):
    return SetVehicleVirtualWorld(vehicleid, worldid)


def get_vehicle_virtual_world(vehicleid: int):
    return GetVehicleVirtualWorld(vehicleid)


def get_vehicle_model_info(model: int, infotype: int):
    return GetVehicleModelInfo(model, infotype)


def create_actor(modelid: int, x: float, y: float, z: float, rotation: float):
    return CreateActor(modelid, x, y, z, rotation)


def destroy_actor(actorid: int):
    return DestroyActor(actorid)


def is_actor_streamed_in(actorid: int, forplayerid: int):
    return IsActorStreamedIn(actorid, forplayerid)


def set_actor_virtual_world(actorid: int, vworld: int):
    return SetActorVirtualWorld(actorid, vworld)


def get_actor_virtual_world(actorid: int):
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
):
    return ApplyActorAnimation(
        actorid, animlib, animname, fDelta, loop, lockx, locky, freeze, time
    )


def clear_actor_animations(actorid: int):
    return ClearActorAnimations(actorid)


def set_actor_pos(actorid: int, x: float, y: float, z: float):
    return SetActorPos(actorid, x, y, z)


def get_actor_pos(actorid: int):
    return GetActorPos(actorid)


def set_actor_facing_angle(actorid: int, angle: float):
    return SetActorFacingAngle(actorid, angle)


def get_actor_facing_angle(actorid: int):
    return GetActorFacingAngle(actorid)


def set_actor_health(actorid: int, health: float):
    return SetActorHealth(actorid, health)


def get_actor_health(actorid: int):
    return GetActorHealth(actorid)


def set_actor_invulnerable(actorid: int, invulnerable=True):
    return SetActorInvulnerable(actorid, invulnerable)


def is_actor_invulnerable(actorid: int):
    return IsActorInvulnerable(actorid)


def is_valid_actor(actorid: int):
    return IsValidActor(actorid)


def http(index: int, type: int, url: str, data: str, callback):
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
):
    return Create3DTextLabel(text, color, x, y, z, drawDistance, virtualworld, testLOS)


def delete_3d_text_label(id):
    return Delete3DTextLabel(id)


def attach_3d_text_label_to_player(id, playerid: int, offsetX, offsetY, offsetZ):
    return Attach3DTextLabelToPlayer(id, playerid, offsetX, offsetY, offsetZ)


def attach_3d_text_label_to_vehicle(id, vehicleid, offsetX, offsetY, offsetZ):
    return Attach3DTextLabelToVehicle(id, vehicleid, offsetX, offsetY, offsetZ)


def update_3d_text_label_text(id, color, text):
    return Update3DTextLabelText(id, color, text)


def create_player_3d_text_label(
    playerid,
    text,
    color,
    x,
    y,
    z,
    drawDistance,
    attachedplayer=INVALID_PLAYER_ID,
    attachedvehicle=INVALID_VEHICLE_ID,
    testLOS=False,
):
    return CreatePlayer3DTextLabel(
        playerid,
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


def delete_player_3d_text_label(playerid: int, id):
    return DeletePlayer3DTextLabel(playerid, id)


def update_player_3d_text_label_text(playerid: int, id, color, text):
    return UpdatePlayer3DTextLabelText(playerid, id, color, text)
