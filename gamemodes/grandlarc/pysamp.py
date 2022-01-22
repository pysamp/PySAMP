from dataclasses import dataclass
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


def is_player_in_range_of_point(playerid: int, range: float, x: float, y: float, z: float):
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


def player_text_draw_set_preview_rot(playerid: int, text, fRotX, fRotY, fRotZ, fZoom=1.0):
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


def set_player_race_checkpoint(playerid: int, type, x: float, y: float, z: float, nextx, nexty, nextz, size):
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
    playerid, iconid, x: float, y: float, z: float, markertype, color, style=MAPICON_LOCAL
):
    return SetPlayerMapIcon(playerid, iconid, x, y, z, markertype, color, style)


def remove_player_map_icon(playerid: int, iconid):
    return RemovePlayerMapIcon(playerid, iconid)


def allow_player_teleport(playerid: int, allow):
    return AllowPlayerTeleport(playerid, allow)


def set_player_camera_pos(playerid: int, x: float, y: float, z: float):
    return SetPlayerCameraPos(playerid, x, y, z)


def set_player_camera_look_at(playerid: int, x: float, y: float, z: float, cut=CAMERA_CUT):
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


def move_object(objectid, x: float, y: float, z: float, Speed, RotX=-1000.0, RotY=-1000.0, RotZ=-1000.0):
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


def create_player_object(playerid: int, modelid, x: float, y: float, z: float, rX, rY, rZ, DrawDistance=0.0):
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
    playerid, objectid, x: float, y: float, z: float, Speed, RotX=-1000.0, RotY=-1000.0, RotZ=-1000.0
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


def add_static_vehicle(modelid: int, spawn_x: float, spawn_y: float, spawn_z: float, z_angle: float, color1: int, color2: int):
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


def add_static_pickup(model: int, type: int, x: float, y: float, z: float, virtualworld=0):
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
    vehicletype, x: float, y: float, z: float, rotation, color1, color2, respawn_delay, addsiren=False
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
    vehicleid: int, engine: int, lights: int, alarm: int, doors: int, bonnet: int, boot: int, objective: int
):
    return SetVehicleParamsEx(
        vehicleid, engine, lights, alarm, doors, bonnet, boot, objective
    )


def get_vehicle_params_ex(vehicleid: int):
    return GetVehicleParamsEx(vehicleid)


def get_vehicle_params_siren_state(vehicleid: int):
    return GetVehicleParamsSirenState(vehicleid)


def set_vehicle_params_car_doors(vehicleid: int, driver: int, passenger: int, backleft: int, backright: int):
    return SetVehicleParamsCarDoors(vehicleid, driver, passenger, backleft, backright)


def get_vehicle_params_car_doors(vehicleid):
    return GetVehicleParamsCarDoors(vehicleid)


def set_vehicle_params_car_windows(vehicleid: int, driver: int, passenger: int, backleft: int, backright: int):
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


def update_vehicle_damage_status(vehicleid: int, panels: int, doors: int, lights: int, tires: int):
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
    actorid: int, animlib: str, animname: str, fDelta: float, loop: int, lockx: int, locky: int, freeze: int, time: int
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
    text, color, x: float, y: float, z: float, drawDistance: float, virtualworld: int, testLOS=False
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


class Actor:
    """
    Read more about actors here: https://open.mp/docs/scripting/functions/CreateActor
    -----------------
    """

    def __init__(self, modelid, x: float, y: float, z: float, rot):
        self.id = create_actor(modelid, x, y, z, rot)

    def destroy(self):
        return destroy_actor(self.id)

    def streamed_in(self, forplayerid):
        return is_actor_streamed_in(self.id, forplayerid)

    @property
    def virtual_world(self):
        return get_actor_virtual_world(self.id)

    @virtual_world.setter
    def virtual_world(self, vworld):
        return set_actor_virtual_world(self.id, vworld)

    def apply_animation(
        self, animlib, animname, fDelta, loop, lockx, locky, freeze, time
    ):
        return apply_actor_animation(
            self.id, animlib, animname, fDelta, loop, lockx, locky, freeze, time
        )

    def clear_animations(self):
        return clear_actor_animations(self.id)

    @property
    def pos(self):
        return get_actor_pos(self.id)

    @pos.setter
    def pos(self, pos):
        try:
            x, y, z = pos
        except:
            raise ValueError("Expected pos as tuple: (x, y, z)")
        else:
            return set_actor_pos(self.id, x, y, z)

    @property
    def facing_angle(self):
        return get_actor_facing_angle(self.id)

    @facing_angle.setter
    def facing_angle(self, angle: float):
        return set_actor_facing_angle(self.id, angle)

    @property
    def health(self):
        return get_actor_health(self.id)

    @health.setter
    def health(self, health):
        return set_actor_health(self.id, health)

    @property
    def invulnerable(self):
        return is_actor_invulnerable(self.id)

    @invulnerable.setter
    def invulnerable(self, invulnerable=True):
        return set_actor_invulnerable(self.id, invulnerable)

    @property
    def is_valid(self):
        return is_valid_actor(self.id)


class Player:
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

    def set_spawn_info(
        self,
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
    ):
        """| METHOD |

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
        return SetSpawnInfo(
            self.id,
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

    def spawn(self):
        """| METHOD |

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

    def set_pos_find_z(self, x: float, y: float, z: float):
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

        >>> `x, y, z = player.pos`


        - Setting the position:
        >>> `player.pos = (x, y, z)`


        Set
        ----
        - Returns true if successful, false if not.\n
        Get
        -----
        - Returns: (x, y, z), raises ValueError if unsuccessful.

        Example
        ----
        ```py
        x,y,z = player.pos
        if z > 1000.0:
            player.send_client_message(-1, "oh.. wow, you are really high! Let us put you lower.")
            player.pos = (x, y, 0) ## set to height 0, but keep other values same.
        ```
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

        Set or get the player's facing angle.

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
    def facing_angle(self, angle: float):
        return SetPlayerFacingAngle(self.id, angle)

    def is_in_range_of_point(self, range, x: float, y: float, z: float):
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

    def distance_from_point(self, x: float, y: float, z: float):
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
        Values above 32766 can cause errors.

        * NB: To set ammo, you need to pass a Tuple! Check example.

        Example:
        ------
        ```py
        weaponid = player.weapon

        if player.ammo < 10 and weaponid > 15 and weaponid < 21:
            player.ammo = (weaponid, 5000) # Automatically fill up to 5000 when below 10 ammo.
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
        if player.weapon_state = WEAPONSTATE_LAST_BULLET:
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
        if player.target == INVALID_PLAYER_ID:
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
        if player.team == NO_TEAM:
            player.team = 15 ## Assign to team 15

        ```
        """
        return GetPlayerTeam(self.id)

    @team.setter
    def team(self, teamid):
        return SetPlayerTeam(self.id, teamid)

    @property
    def score(self):
        """| PROPERTY |

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
        """| PROPERTY |

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
        """| PROPERTY |

        Get or set the player's skin, as an int. A skin is the character model.

        See available skins and the corresponding ID's here: https://open.mp/docs/scripting/resources/skins

        Value can be `0-73` or `75-311`. Default is `0` (CJ)

        ___________

        WARNING:
        ----
        Known Bugs: If a player's skin is set when they are crouching, in a vehicle, or performing certain animations,
        they will become frozen or otherwise glitched. This can be fixed by using `player.toggle_controllable(1)`.

        Players can be detected as being crouched through `player.special_action == SPECIAL_ACTION_DUCK`
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
        player.give_weapon(WEAPON_COLT45, 500) # Give a Colt45 with 500 bullets
        ```
        """
        return GivePlayerWeapon(self.id, weaponid, ammo)

    def reset_weapons(self):
        """| METHOD |

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
    def name(self):
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
        return GetPlayerName(self.id, MAX_PLAYER_NAME)

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
        if player.state == PLAYER_STATE_ONFOOT:
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
        """| PROPERTY |

        Get or set the player's game time.

        Value is represented as a tuple with two values: (hour, minute)

        Example
        -----
        ```py
        hour, minute = player.time
        if hour > 21:
            player.time = (10, minute) # make hour 10

        ```
        """
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
        """| METHOD |

        Toggle the in-game clock (top-right corner) for a specific player. When this is enabled, time will progress at 1 minute per second.
        Weather will also interpolate (slowly change over time) when set using SetWeather/SetPlayerWeather

        - toggle \t 1 to show and 0 to hide. Hidden by default.

        Example
        ----
        ```py
        def on_player_connect(playerid):
            player.toggle_clock(1) # Show the clock for the player
        ```
        """
        return TogglePlayerClock(self.id, toggle)

    def set_weather(self, weather):
        """| METHOD |

        Set the player's weather. If player.toggle_clock is on, then the weather will change slowly.
        _________________

        - weather \t The weather ID to set, as an int between 0 and 20.
        _________________

        Weather IDs
        ----
        - 0 = EXTRASUNNY_LA
        - 1 = SUNNY_LA
        - 2 = EXTRASUNNY_SMOG_LA
        - 3 = SUNNY_SMOG_LA
        - 4 = CLOUDY_LA
        - 5 = SUNNY_SF
        - 6 = EXTRASUNNY_SF
        - 7 = CLOUDY_SF
        - 8 = RAINY_SF
        - 9 = FOGGY_SF
        - 10 = SUNNY_VEGAS
        - 11 = EXTRASUNNY_VEGAS (heat waves)
        - 12 = CLOUDY_VEGAS
        - 13 = EXTRASUNNY_COUNTRYSIDE
        - 14 = SUNNY_COUNTRYSIDE
        - 15 = CLOUDY_COUNTRYSIDE
        - 16 = RAINY_COUNTRYSIDE
        - 17 = EXTRASUNNY_DESERT
        - 18 = SUNNY_DESERT
        - 19 = SANDSTORM_DESERT
        - 20 = UNDERWATER (greenish, foggy)
        https://dev.prineside.com/en/gtasa_weather_id/

        To set weather for everyone, use `set_weather(weatherid)`.

        Example
        ---------
        ```py
        def on_player_spawn(playerid):
            if "storm" in player.name:
                player.weather(RAINY_SF) # ID 8
        ```
        """
        return SetPlayerWeather(self.id, weather)

    def force_class_selection(self):
        """| METHOD |

        Forces a player to go back to class selection

        https://open.mp/docs/scripting/functions/ForceClassSelection

        Returns
        ------
        - Nothing

        Example
        -----
        ```py
        if "/class" in cmdtext[0:7]:
            player.force_class_selection()
            player.toggle_spectating(1)
            player.toggle_spectating(0)
            # Spectating avoids PLAYER_STATE_WASTED.

        ```
        """
        return ForceClassSelection(self.id)

    @property
    def wanted_level(self):
        """| PROPERTY |

        Get or set the player's wanted level

        Value is an integer between `0` and `6`

        Example
        ------
        ```py
        if "/maxwanted" in cmdtext[0:10]:
            if player.wanted != 6: #get
                player.wanted = 6  #set
        ```
        """
        return GetPlayerWantedLevel(self.id)

    @wanted_level.setter
    def wanted_level(self, level):
        return SetPlayerWantedLevel(self.id, level)

    @property
    def fighting_style(self):
        """| PROPERTY |

        Get or set the player's special fighting style. To use in-game, aim and press the 'secondary attack' key (ENTER by default).

        Available Values
        ----
        - 4  - FIGHT_STYLE_NORMAL
        - 5  - FIGHT_STYLE_BOXING
        - 6  - FIGHT_STYLE_KUNGFU
        - 7  - FIGHT_STYLE_KNEEHEAD
        - 15 - FIGHT_STYLE_GRABKICK
        - 16 - FIGHT_STYLE_ELBOW

        Example
        ------
        ```py
        if "/kneehead" in cmdtext[0:9]:
            if player.fighting_style != 7: #get
                player.fighting_style = 7  #set
        ```
        """
        return GetPlayerFightingStyle(self.id)

    @fighting_style.setter
    def fighting_style(self, style):
        return SetPlayerFightingStyle(self.id, style)

    @property
    def velocity(self):
        """| PROPERTY |

        Get or set the velocity of the player, vector presented as a tuple with 3 floats.

        Values
        -----
        The tuple looks like this: (X, Y, Z)
        - Float:X \t The velocity (speed) on the X axis.
        - Float:Y \t The velocity (speed) on the Y axis.
        - Float:Z \t The velocity (speed) on the Z axis.

        Example
        -------
        ```py
        if "/jump" in cmdtext[0:5]:
            x, y, z = player.velocity
            player.velocity = (x,y,z + 0.2) # Add 0.2 on z axis

        ```
        """
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
        """| METHOD |

        Plays a crime report for the player. You know when the player gets wanted in single player,
        the dispatch on the radio reads out actions and positions.
        You can also do this on SA-MP.

        _________

        - suspectid \t The suspected player to be described in crime report
        - crimeid   \t The Crime ID, which will be reported as a 10-code.
        _________

        Available Crime IDs
        ------------
         ID  \t 10-Code \t Description

         3 \t 10-71 \t Advise nature of fire (size, type, contents of building)
         4 \t 10-47 \t Emergency road repairs needed
         5 \t 10-81 \t Breatherlizer Report
         6 \t 10-24 \t Assignment Completed
         7 \t 10-21 \t Call () by phone
         8 \t 10-21 \t Call () by phone
         9 \t 10-21 \t Call () by phone
        10 \t 10-17 \t Meet Complainant
        11 \t 10-81 \t Breatherlizer Report
        12 \t 10-91 \t Pick up prisoner/subject
        13 \t 10-28 \t Vehicle registration information
        14 \t 10-81 \t Breathalyzer
        15 \t 10-28 \t Vehicle registration information
        16 \t 10-91 \t Pick up prisoner/subject
        17 \t 10-34 \t Riot
        18 \t 10-37 \t (Investigate) suspicious vehicle
        19 \t 10-81 \t Breathalyzer
        21 \t 10-7 \t Out of service
        22 \t 10-7 \t Out of service
        ____________________

        Example
        -----
        ```py
            player.player_crime_report(0, 16) # Crime ID for playerid 0
            player.send_client_message(-1, "ID 0 committed a crime! (10-16).")
        ```

        """
        return PlayCrimeReportForPlayer(self.id, suspectid, crime)

    def play_audio_stream(
        self, url, posX=0.0, posY=0.0, posZ=0.0, distance=50.0, usepos=False
    ):
        """| METHOD |

        Play an audio stream for a player. Normal files can also be streamed, such as MP3

        _______

        - url        \t The url to play. Valid formats are mp3/ogg/pls.
        - Float:PosX \t The X position at to play the audio. No effect if usepos is set to 0.
        - Float:PosY \t The Y position at to play the audio. No effect if usepos is set to 0.
        - Float:PosZ \t The Z position at to play the audio. No effect if usepos is set to 0.
        - Float:distance The distance over the audio will be heard. No effect if usepos is set to 0.
        - usepos     \t Use the positions and distance specified. If false = global sound.
        _______

        Return
        ------
        - 1: The function was executed successfully.
        - 0: The function failed to execute. The player specified does not exist.

        Example
        -------
        ```py
        if "/radiopos" in cmdtext[0:9]:
            x, y, z = player.pos
            distance = 15.0
            player.play_audio_stream("http://somafm.com/tags.pls", x, y, z, distance)
        ```
        """
        return PlayAudioStreamForPlayer(
            self.id, url, posX, posY, posZ, distance, usepos
        )

    def stop_audio_stream(self):
        """| METHOD |

        Stops the player's audio stream

        This method takes no values.

        Returns
        -----
        - Does not return any specific values

        Example
        -----
        ```py
            # Stop any active audio streams;
            player.stop_audio_stream()
        ```
        """
        return StopAudioStreamForPlayer(self.id)

    def set_shop_name(self, shopname):
        """| METHOD |

        Loads or unloads an interior script for a player (for example the ammunation menu).
        https://sampwiki.blast.hk/wiki/ShopNames

        ________

        - shopname \t The shop script to load. Leave blank to unload scripts.
        ________

        Available values
        ----------
        - Script name\t What is it\t\t  Position \t\t     Interior
        -
        - "FDPIZA" \t Pizza Stack \t 374.0000, -119.6410, 1001.4922  \t 5
        - "FDBURG" \t Burger Shot \t 375.5660, -68.2220, 1001.5151   \t 10
        - "FDCHICK" \t Cluckin' Bell \t 368.7890, -6.8570, 1001.8516   \t 9
        - "AMMUN1" \t Ammunation 1 \t 296.5395, -38.2739, 1001.515   \t 1
        - "AMMUN2" \t Ammunation 2 \t 295.7359, -80.6865, 1001.5156  \t 4
        - "AMMUN3" \t Ammunation 3 \t 290.2011, -109.5698, 1001.5156 \t 6
        - "AMMUN4" \t Ammunation 4 \t 308.1619, -141.2549, 999.6016  \t 7
        - "AMMUN5" \t Ammunation 5 \t 312.7883, -166.0069, 999.6010  \t 6
        Return
        -----
        - Does not return any specific value

        Example
        -----
        ```py
            player.interior = 5
            player.pos = (372.56, -131.36, 1001.5)
            player.set_shop_name("FDPIZA")
            player.send_client_message(-1, "Welcome to Pizza Stack!")
        ```
        """
        return SetPlayerShopName(self.id, shopname)

    def set_skill_level(self, skill, level):
        """| METHOD |

        Set the skill level of a certain weapon type for a player.
        ___________

        - skill \t The weapon to set skill on
        - level \t The level, range 0-999 where 999 is max skill.
        ___________


        Available values for skill
        -----

        -  0 - WEAPONSKILL_PISTOL
        -  1 - WEAPONSKILL_PISTOL_SILENCED
        -  2 - WEAPONSKILL_DESERT_EAGLE
        -  3 - WEAPONSKILL_SHOTGUN
        -  4 - WEAPONSKILL_SAWNOFF_SHOTGUN
        -  5 - WEAPONSKILL_SPAS12_SHOTGUN
        -  6 - WEAPONSKILL_MICRO_UZI
        -  7 - WEAPONSKILL_MP5
        -  8 - WEAPONSKILL_AK47
        -  9 - WEAPONSKILL_M4
        - 10 - WEAPONSKILL_SNIPERRIFLE

        Example
        ------
        ```py
            player.set_skill_level(WEAPONSKILL_MP5, 999)
        ```
        -
        """
        return SetPlayerSkillLevel(self.id, skill, level)

    @property
    def surfing_vehicle_id(self):
        """| PROPERTY | Read only |

        Get which vehicle the player is standing on.

        Return
        ------
        - vehicleid \t The vehicle the player is "surfing". Can return `INVALID_VEHICLE_ID` if there's no driver in the car.

        Example
        ------
        ```py
            if player.surfing_vehicle_id == INVALID_VEHICLE_ID:
                player.send_client_message(-1, "You are not surfing!")
        ```

        https://open.mp/docs/scripting/functions/GetPlayerSurfingVehicleID
        """
        return GetPlayerSurfingVehicleID(self.id)

    @property
    def surfing_object_id(self):
        """| PROPERTY | Read only |

        Get which MOVING object the player is standing on.

        Return
        ------
        - objectid: The object being surfed. If the player isn't surfing a moving object = INVALID_OBJECT_ID.

        Example
        ------
        ```py
            if player.surfing_object_id == INVALID_OBJECT_ID:
                player.send_client_message(-1, "You are not surfing a moving object!")
        ```

        https://open.mp/docs/scripting/functions/GetPlayerSurfingObjectID
        """
        return GetPlayerSurfingObjectID(self.id)

    def remove_building(self, modelid, fX, fY, fZ, fRadius):
        """| METHOD |

        Removes a standard San Andreas model for a single player within a specified range

        _____________

        - modelid      \t The model to remove.
        - Float:fX     \t The X coordinate around which the objects will be removed.
        - Float:fY     \t The Y coordinate around which the objects will be removed.
        - Float:fZ     \t The Z coordinate around which the objects will be removed.
        - Float:fRadius\t The radius around the specified point to remove objects with the specified model.
        _____________

        Returns
        -----
        - No value is returned

        Warnings
        -----
        - There appears to be a limit of around 1000 lines/objects. There is no workaround.
        - When removing the same object for a player, they will crash.
        - Commonly, players crash when *reconnecting* to the server because the server removes buildings on OnPlayerConnect.

        Example
        -----
        ```py
        # This will remove ALL map objects:
        player.remove_building(-1, 0.0, 0.0, 0.0, 6000.0)

        ```
        """
        return RemoveBuildingForPlayer(self.id, modelid, fX, fY, fZ, fRadius)

    @property
    def last_shot_vectors(self):
        """| PROPERTY | Read only |

        ___________

        This method returns a Tuple; `(fOriginX,fOriginY,fOriginZ,fHitPosX,fHitPosY,fHitPosY)`
        - Float:fOriginX	A float variable with the X coordinate of where the bullet originated from.
        - Float:fOriginY	A float variable with the Y coordinate of where the bullet originated from.
        - Float:fOriginZ	A float variable with the Z coordinate of where the bullet originated from.
        - Float:fHitPosX	A float variable with the X coordinate of where the bullet hit.
        - Float:fHitPosY	A float variable with the Y coordinate of where the bullet hit.
        - Float:fHitPosY	A float variable with the Z coordinate of where the bullet hit.
        ___________

        Example:
        --------
        ```py
        if "/lastshot" in cmdtext[0:9]:
            # Get the coordinates
            fOriginX, fOriginY, fOriginZ, fHitPosX, fHitPosY, fHitPosY = player.last_shot_vectors
            # Send them to the player
            player.send_client_message(
                -1, "Last shot info: Origin: {}, {}, {}. Hit pos: {}, {}, {}".format(
                    str(fOriginX), str(fOriginY), str(fOriginZ), str(fHitPosX), str(fHitPosY), str(fHitPosY)
                )
            )
        ```
        """
        return GetPlayerLastShotVectors(self.id)

    def set_attached_object(
        self,
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
        """| METHOD |

        Attach an object to a specific bone on a player.

        ___________

        - index \t\tThe index (slot) to assign the object to (0-9).
        - modelid  \t\tThe model to attach.
        - bone     \t\tThe bone to attach the object to. (0-18)
        - fOffsetX \t\t(optional) X axis offset for the object position.
        - fOffsetY \t\t(optional) Y axis offset for the object position.
        - fOffsetZ \t\t(optional) Z axis offset for the object position.
        - fRotX   \t \t(optional) X axis rotation of the object.
        - fRotY   \t \t(optional) Y axis rotation of the object.
        - fRotZ   \t \t(optional) Z axis rotation of the object.
        - fScaleX \t \t(optional) X axis scale of the object.
        - fScaleY \t \t(optional) Y axis scale of the object.
        - fScaleZ \t \t(optional) Z axis scale of the object.
        - materialcolor1 \t(optional) The first object color to set, as an integer or hex in ARGB color format.
        - materialcolor2 \t(optional) The second object color to set, as an integer or hex in ARGB color format
        ___________


        Bone values
        -------
         1 	Spine
         2 	Head
         3 	Left upper arm
         4 	Right upper arm
         5 	Left hand
         6 	Right hand
         7 	Left thigh
         8 	Right thigh
         9 	Left foot
        10 	Right foot
        11 	Right calf
        12 	Left calf
        13 	Left forearm
        14 	Right forearm
        15 	Left clavicle (shoulder)
        16 	Right clavicle (shoulder)
        17 	Neck
        18 	Jaw

        Returns
        -------
        0   on failure
        1   on success

        Example
        --------
        ```py
        # Give player a white hat, and paint it green
        player.set_attached_object(3, 19487, 2, 0.101, -0.0, 0.0, 5.50, 84.60, 83.7, 1.0, 1.0, 1.0, 0xFF00FF00)
        ```
        """
        return SetPlayerAttachedObject(
            self.id,
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

    def remove_attached_object(self, index):
        """| METHOD |

        Remove an attached object from a player.

        - index \t The index to remove the object from (0-9)

        Returns
        ------
        1   on success
        0   on failure

        Example
        ------
        ```py
        # Remove all player-attached objects
        if "/removeall" in cmdtext[0:10]:
            for slot in range(MAX_PLAYER_ATTACHED_OBJECTS) :
                if player.is_attached_object_slot_used(slot):
                    player.remove_attached_object(slot)
        ```

        """
        return RemovePlayerAttachedObject(self.id, index)

    def is_attached_object_slot_used(self, index):
        """| METHOD |

        Check if a player has an object attached in the specified index (slot).

        - index \t The index (slot) to check.

        Returns
        -------
        - 1: The specified slot is used for an attached object.
        - 0: The specified slot is not in use for an attached object

        Example
        -------
        ```py
        # Count amount of attached objects currently on player
        count = 0
        for slot in range(MAX_PLAYER_ATTACHED_OBJECTS):
            if player.is_attached_object_slot_used(slot):
                count +=1
        print(count) # then shows the count in the log
        ```
        """
        return IsPlayerAttachedObjectSlotUsed(self.id, index)

    def edit_attached_object(self, index):
        """| METHOD |

        Enter edition mode for an attached object.

        - index \t the slot of the attached object to edit.

        Returns
        -------
        1: success
        0: failure

        https://sampwiki.blast.hk/wiki/EditAttachedObject
        """
        return EditAttachedObject(self.id, index)

    def create_text_draw(self, x, y, text):
        """| METHOD |

        Create a textdraw

        - x: \t x-position as a float on the screen
        - y: \t y-position as a float on the screen
        - text:  the text to show.

        https://sampwiki.blast.hk/wiki/CreatePlayerTextDraw

        Returns
        -----
        - id \t The textdraw ID that references this textdraw as an integer.

        Notes
        ----
        - You need the textdraw ID later in order to remove or edit it.
        - The x,y coordinate is the top left coordinate for the text draw area based on a 640x448 "canvas" (irrespective of screen resolution). If you plan on using TextDrawAlignment with alignment 3 (right), the x,y coordinate is the top right coordinate for the text draw.
        - This function merely CREATES the textdraw, you must use PlayerTextDrawShow to show it to a player.
        - It is recommended to use WHOLE numbers instead of decimal positions when creating player textdraws to ensure resolution friendly design.
        - Player-textdraws are automatically destroyed when a player disconnects
        - Keyboard key mapping codes (such as ~k~~VEHICLE_ENTER_EXIT~) Doesn't work beyond 255th character.

        Warnings
        ----
        - If you choose values for y that are less than 1, the first text row will be invisible and only the shadow is visible.
        - `text` must NOT be empty or the server will crash! Use " " (a space) or _ (underscore) instead
        - If the last character in the text is a space (" "), the text will all be blank.
        - If part of the text is off-screen, the color of the text will not show, only the shadow (if enabled) will.

        """
        return CreatePlayerTextDraw(self.id, x, y, text)

    def text_draw_destroy(self, text):
        """| METHOD |

        Destroy a textdraw with a given textdraw ID.

        - text \t The textdraw ID to destroy.

        Returns
        --------
        0: failure
        1: success
        """
        return PlayerTextDrawDestroy(self.id, text)

    def text_draw_letter_size(self, text, x, y):
        """| METHOD |

        Sets the width and height of the letters in a player-textdraw.
        ___________

        - text    \t The ID of the player-textdraw to change the letter size of
        - Float:x \t Width of a char.
        - Float:y \t Height of a char.
        ___________

        Returns
        ------
        - Does not return any value

        Tips
        -----
        - Fonts appear to look the best with an X to Y ratio of 1 to 4 (e.g. if x is 0.5 then y should be 2).
        - When using this function purely for the benefit of affecting the textdraw box, multiply 'Y' by 0.135 to convert to TextDrawTextSize-like measurements
        Example
        -----

        No example available for player-textdraws, but check: https://sampwiki.blast.hk/wiki/PlayerTextDrawLetterSize


        """
        return PlayerTextDrawLetterSize(self.id, text, x, y)

    def text_draw_text_size(self, text, x, y):
        """| METHOD |

        Change the size of a player-textdraw (box if PlayerTextDrawUseBox is enabled and/or clickable area for use with PlayerTextDrawSetSelectable).
        __________

        - text    \t The ID of the player-textdraw to set the size of.
        - Float:x \t The size on the X axis (left/right) following the same 640x480 grid as TextDrawCreate.
        - Float:y \t The size on the Y axis (up/down) following the same 640x480 grid as TextDrawCreate.
        __________

        Returns
        -----
        - Does not return any value

        Notes
        -----
        The x and y have different meanings with different player.text_draw_alignment values:
            1 (left): they are the right-most corner of the box, absolute coordinates.
            2 (center): they need to inverted (switch the two) and the x value is the overall width of the box.
            3 (right): the x and y are the coordinates of the left-most corner of the box
        Using font type 4 (sprite) and 5 (model preview) converts X and Y of this function from corner coordinates to WIDTH and HEIGHT (offsets).

        The TextDraw box starts 10.0 units up and 5.0 to the left as the origin (TextDrawCreate coordinate).

        This function defines the clickable area for use with PlayerTextDrawSetSelectable, whether a box is shown or not.


        Example
        -----
        No example available for player-textdraws, but check: https://sampwiki.blast.hk/wiki/PlayerTextDrawTextSize

        """
        return PlayerTextDrawTextSize(self.id, text, x, y)

    def text_draw_alignment(self, text, alignment):
        """| METHOD |

        Set the text-alignment of a player-textdraw
        ___________

        - text   	The ID of the player-textdraw to set the alignment of.
        - alignment	1-left, 2-centered, 3-right
        ___________

        Returns
        ------
        - No sepcific value is returned

        Note
        ------
        - For alignment 2 (center) the x and y values of TextSize need to be swapped

        Example
        ----
        No example available for player-textdraws, but read more here: https://sampwiki.blast.hk/wiki/PlayerTextDrawAlignment
        """
        return PlayerTextDrawAlignment(self.id, text, alignment)

    def text_draw_color(self, text, color):
        """| METHOD |

        Sets the text color of a player-textdraw

        You can also use Gametext colors in textdraws.

        *NOTE* The textdraw must be re-shown to the player in order to update the color.
        ________

        - text  \t Textdraw id to be changed color of, as an int
        - color \t Color in Hexadecimal format
        ________

        Returns
        -----
        - No value is returned

        Example
        -----
        No example available for player-textdraws, but check out: https://sampwiki.blast.hk/wiki/PlayerTextDrawColor
        """
        return PlayerTextDrawColor(self.id, text, color)

    def text_draw_use_box(self, text, use):
        """| METHOD |

        Toggle the box on a player-textdraw.
        ________

        - text \t Textdraw ID
        - use  \t 1 to use a box, 0 to hide the box.
        ________

        Returns
        -----
        - No value is returned

        Example
        ----
        No example available for player-textdraws, but check out: https://sampwiki.blast.hk/wiki/PlayerTextDrawUseBox
        """
        return PlayerTextDrawUseBox(self.id, text, use)

    def text_draw_box_color(self, text, color):
        """| METHOD |

        Sets the text color of a player-textdraw box
        ________

        - text  \t Textdraw id to be changed box color of, as an int
        - color \t Color in Hexadecimal format. Alpha (transparency) is supported
        ________

        Returns
        -----
        - No value is returned

        Example
        -----
        No example available for player-textdraws, but check out: https://sampwiki.blast.hk/wiki/PlayerTextDrawBoxColor
        """
        return PlayerTextDrawBoxColor(self.id, text, color)

    def text_draw_set_shadow(self, text, size):
        """| METHOD |

        Adds a shadow to the bottom-right side of the text in a player-textdraw. The shadow font matches the text font.
        _________

        - text	\tThe ID of the player-textdraw to change the shadow of
        - size	\tThe size of the shadow. 0 will hide the shadow.
        _________

        Returns
        ----
        1: successful
        0: failed - maybe player textdraw doesn't exist?

        Note
        ----
        - The shadow can be cut by the box area if the size is set too big for the area

        Example
        ----
        No example available for player-textdraws
        """
        return PlayerTextDrawSetShadow(self.id, text, size)

    def text_draw_set_outline(self, text, size):
        """| METHOD |

        Set the outline of a player-textdraw. The outline colour cannot be changed unless PlayerTextDrawBackgroundColor is used
        ___________

        - text\t\tThe ID of the player-textdraw to set the outline of
        - size\t\tThe thickness of the outline
        ___________

        Returns
        ----
        - No values are returned

        Example
        ----
        No example available for player-textdraws
        """
        return PlayerTextDrawSetOutline(self.id, text, size)

    def text_draw_background_color(self, text, color):
        """| METHOD |
        _________

        - text	    The ID of the player-textdraw to set the background color of
        - color	    The color that the textdraw should be set to.
        _________
        Notes
        -----
        - If PlayerTextDrawSetOutline is used with size > 0, the outline color will match the color used in text_draw_background_color.
        - Changing the value of color seems to alter the color used in text_draw_color

        Returns
        ------
        - No value returned

        Example
        -------
        No example available for player-textdraws

        """
        return PlayerTextDrawBackgroundColor(self.id, text, color)

    def text_draw_font(self, text, font):
        """| METHOD |

        Change the font of a textdraw.

        See all fonts here: https://sampwiki.blast.hk/wiki/PlayerTextDrawFont
        ________

        - text \t The ID of the player-textdraw to change the font of
        - font \t There are four fonts, 0-3. Above 4 may crash the client.
        ________

        Returns
        -----
        - No value is returned

        """
        return PlayerTextDrawFont(self.id, text, font)

    def text_draw_set_proportional(self, text, set):
        """| METHOD |

        Appears to scale text spacing to a proportional ratio.
        Useful when using PlayerTextDrawLetterSize to ensure the text has even character spacing.
        _______________

        - text \t The ID of the player-textdraw to set the proportionality of
        - set  \t 1 to enable proportionality, 0 to disable
        _______________

        Returns
        -----
        - No value is returned

        """
        return PlayerTextDrawSetProportional(self.id, text, set)

    def text_draw_set_selectable(self, text, set):
        """| METHOD |

        This method MUST be used BEFORE the textdraw is shown to the player!

        This method makes the textdraw selectable. `player.text_draw_text_size` defines the clickable area.

        _________

        - text	        The ID of the player-textdraw
        - set	        The color that the textdraw should be set to.
        _________


        Returns
        ----
        - No value returned

        Example
        ----
        No example available for player-textdraws.
        """
        return PlayerTextDrawSetSelectable(self.id, text, set)

    def player_text_draw_show(self, text):
        """| METHOD |

        Use this method to show a player-textdraw for the player.

        - text \t\t The textdraw id to show for the player
        """
        return PlayerTextDrawShow(self.id, text)

    def player_text_draw_hide(self, text):
        """| METHOD |

        Use this method to hide a player-textdraw for the player.

        - text\t\t The textdraw id to hide for the player

        Returns
        ----
        - No values returned
        """
        return PlayerTextDrawHide(self.id, text)

    def text_draw_hide_for_player(self, text):
        """| METHOD |

        This method hides a *global* textdraw for the player. To hide a player-textdraw, check `player.player_text_draw_hide`

        - text\t\tThe global textdraw id to hide for the player.

        Returns
        ----
        - No values returned
        """
        return TextDrawHideForPlayer(self.id, text)

    def text_draw_set_string(self, text, string):
        """| METHOD |

        Update the shown text in the player-textdraw. You don't have to show the textdraw again in order to apply the changes

        ____________

        - text  	The ID of the textdraw to change
        - string	The new string for the TextDraw. Max length: 1023 characters
        ____________

        Returns
        -----
        - No values returned

        """
        return PlayerTextDrawSetString(self.id, text, string)

    def text_draw_set_preview_model(self, text, modelindex):
        """| METHOD |

        Sets a player textdraw 2D preview sprite of a specified model ID.
        ____________

        - text  	The ID of the textdraw to change
        - modelid	The modelid to show. Can be any valid object id.
        ____________

        Returns
        ----
        1: The function executed successfully. If an invalid model is passed 'success' is reported, but the model will appear as a yellow/black question mark.
        0: The function failed to execute. Player and/or textdraw do not exist.


        """
        return PlayerTextDrawSetPreviewModel(self.id, text, modelindex)

    def text_draw_set_preview_rot(self, text, fRotX, fRotY, fRotZ, fZoom=1.0):
        """| METHOD |

        Sets the rotation and zoom of a 3D model preview player-textdraw.
        __________________

        - text	\tThe ID of the player-textdraw to change.
        - Float:fRotX	The X rotation value.
        - Float:fRotY	The Y rotation value.
        - Float:fRotZ	The Z rotation value.
        - Float:fZoom	The zoom value, default value 1.0, smaller values make the camera closer and larger values make the camera further away.
        __________________

        Returns
        ------
        - No values returned
        """
        return PlayerTextDrawSetPreviewRot(self.id, text, fRotX, fRotY, fRotZ, fZoom)

    def text_draw_set_preview_veh_col(self, text, color1, color2):
        """| METHOD |

        Set the color of a vehicle in a player-textdraw model preview (if a vehicle is shown).

        The textdraw MUST use the font TEXT_DRAW_FONT_MODEL_PREVIEW and be showing a vehicle, in order for this method to have an effect.

        _______________

        - text  	The ID of the player's player-textdraw to change.
        - color1	The color to set the vehicle's primary color to.
        - color2	The color to set the vehicle's secondary color to.
        _______________

        Returns
        ------
        - No values returned

        """
        return PlayerTextDrawSetPreviewVehCol(self.id, text, color1, color2)

    def get_pvar_int(self, varname):
        """| METHOD |"""
        return GetPVarInt(self.id, varname)

    def set_pvar_int(self, varname, value):
        """| METHOD |"""
        return SetPVarInt(self.id, varname, value)

    def get_pvar_string(self, varname, size):
        """| METHOD |"""
        return GetPVarString(self.id, varname, size)

    def set_pvar_string(self, varname, value):
        """| METHOD |"""
        return SetPVarString(self.id, varname, value)

    def get_pvar_float(self, varname):
        """| METHOD |"""
        return GetPVarFloat(self.id, varname)

    def set_pvar_float(self, varname, value):
        """| METHOD |"""
        return SetPVarFloat(self.id, varname, value)

    def delete_pvar(self, varname):
        """| METHOD |"""
        return DeletePVar(self.id, varname)

    @property
    def pvars_upper_index(self):
        """| PROPERTY |

        Get or set
        """
        return GetPVarsUpperIndex(self.id)

    def get_pvar_name_at_index(self, index, size):
        """| METHOD |"""
        return GetPVarNameAtIndex(self.id, index, size)

    def get_pvar_type(self, varname):
        """| METHOD |"""
        return GetPVarType(self.id, varname)

    def set_chat_bubble(self, text, color, drawdistance, expiretime):
        """| METHOD |"""
        return SetPlayerChatBubble(self.id, text, color, drawdistance, expiretime)

    def put_in_vehicle(self, vehicleid, seatid):
        """| METHOD |"""
        return PutPlayerInVehicle(self.id, vehicleid, seatid)

    @property
    def vehicle_id(self):
        """| PROPERTY |

        Get or set
        """
        return GetPlayerVehicleID(self.id)

    @property
    def vehicle_seat(self):
        """| PROPERTY |

        Get or set
        """
        return GetPlayerVehicleSeat(self.id)

    def remove_from_vehicle(self):
        """| METHOD |"""
        return RemovePlayerFromVehicle(self.id)

    def toggle_controllable(self, toggle):
        """| METHOD |"""
        return TogglePlayerControllable(self.id, toggle)

    def play_sound(self, soundid, x: float, y: float, z: float):
        """| METHOD |"""
        return PlayerPlaySound(self.id, soundid, x, y, z)

    def apply_animation(
        self,
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
        """| METHOD |"""
        return ApplyAnimation(
            self.id,
            animlib,
            animname,
            fDelta,
            loop,
            lockx,
            locky,
            freeze,
            time,
            forcesync,
        )

    def clear_animations(self, forcesync=False):
        """| METHOD |"""
        return ClearAnimations(self.id, forcesync)

    @property
    def animation_index(self):
        """| PROPERTY | Read only |"""
        return GetPlayerAnimationIndex(self.id)

    @property
    def special_action(self):
        return GetPlayerSpecialAction(self.id)

    @special_action.setter
    def special_action(self, actionid):
        return SetPlayerSpecialAction(self.id, actionid)

    def disable_remote_vehicle_collisions(self, disable):
        """| METHOD |"""
        return DisableRemoteVehicleCollisions(self.id, disable)

    def set_checkpoint(self, x: float, y: float, z: float, size):
        """| METHOD |"""
        return SetPlayerCheckpoint(self.id, x, y, z, size)

    def disable_checkpoint(self):
        """| METHOD |"""
        return DisablePlayerCheckpoint(self.id)

    def set_race_checkpoint(self, type, x: float, y: float, z: float, nextx, nexty, nextz, size):
        """| METHOD |"""
        return SetPlayerRaceCheckpoint(
            self.id, type, x, y, z, nextx, nexty, nextz, size
        )

    def disable_race_checkpoint(self):
        """| METHOD |"""
        return DisablePlayerRaceCheckpoint(self.id)

    def set_world_bounds(self, x_max, x_min, y_max, y_min):
        """| METHOD |"""
        return SetPlayerWorldBounds(self.id, x_max, x_min, y_max, y_min)

    def set_marker(self, showplayerid, color):
        """| METHOD |"""
        return SetPlayerMarkerForPlayer(self.id, showplayerid, color)

    def show_name_tag(self, showplayerid, show):
        """| METHOD |"""
        return ShowPlayerNameTagForPlayer(self.id, showplayerid, show)

    def set_map_icon(self, iconid, x: float, y: float, z: float, markertype, color, style=MAPICON_LOCAL):
        """| METHOD |"""
        return SetPlayerMapIcon(self.id, iconid, x, y, z, markertype, color, style)

    def remove_map_icon(self, iconid):
        """| METHOD |"""
        return RemovePlayerMapIcon(self.id, iconid)

    def allow_teleport(self, allow):
        """| METHOD |"""
        return AllowPlayerTeleport(self.id, allow)

    def set_camera_look_at(self, x: float, y: float, z: float, cut=CAMERA_CUT):
        """| METHOD |"""
        return SetPlayerCameraLookAt(self.id, x, y, z, cut)

    def set_camera_behind(self):
        """| METHOD |"""
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
        """| METHOD |"""
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
        """| METHOD |"""
        return AttachCameraToObject(self.id, objectid)

    def attach_camera_to_player_object(self, playerobjectid):
        """| METHOD |"""
        return AttachCameraToPlayerObject(self.id, playerobjectid)

    def interpolate_camera_pos(
        self, FromX, FromY, FromZ, ToX, ToY, ToZ, time, cut=CAMERA_CUT
    ):
        """| METHOD |"""
        return InterpolateCameraPos(
            self.id, FromX, FromY, FromZ, ToX, ToY, ToZ, time, cut
        )

    def interpolate_camera_look_at(
        self, FromX, FromY, FromZ, ToX, ToY, ToZ, time, cut=CAMERA_CUT
    ):
        """| METHOD |"""
        return InterpolateCameraLookAt(
            self.id, FromX, FromY, FromZ, ToX, ToY, ToZ, time, cut
        )

    @property
    def connected(self):
        return IsPlayerConnected(self.id)

    def is_in_vehicle(self, vehicleid):
        """| METHOD |"""
        return IsPlayerInVehicle(self.id, vehicleid)

    def is_in_any_vehicle(self):
        """| METHOD |"""
        return IsPlayerInAnyVehicle(self.id)

    def is_in_checkpoint(self):
        """| METHOD |"""
        return IsPlayerInCheckpoint(self.id)

    def is_in_race_checkpoint(self):
        """| METHOD |"""
        return IsPlayerInRaceCheckpoint(self.id)

    @property
    def virtual_world(self):
        return GetPlayerVirtualWorld(self.id)

    @virtual_world.setter
    def virtual_world(self, worldid):
        return SetPlayerVirtualWorld(self.id, worldid)

    def enable_stunt_bonus(self, enable):
        """| METHOD |"""
        return EnableStuntBonusForPlayer(self.id, enable)

    def toggle_spectating(self, toggle):
        """| METHOD |"""
        return TogglePlayerSpectating(self.id, toggle)

    def spectate(self, targetplayerid, mode=SPECTATE_MODE_NORMAL):
        """| METHOD |"""
        return PlayerSpectatePlayer(self.id, targetplayerid, mode)

    def spectate_vehicle(self, targetvehicleid, mode=SPECTATE_MODE_NORMAL):
        """| METHOD |"""
        return PlayerSpectateVehicle(self.id, targetvehicleid, mode)

    def start_recording_data(self, recordtype, recordname):
        """| METHOD |"""
        return StartRecordingPlayerData(self.id, recordtype, recordname)

    def stop_recording_data(self):
        """| METHOD |"""
        return StopRecordingPlayerData(self.id)

    def create_explosion(self, X, Y, Z, type, Radius):
        """| METHOD |"""
        return CreateExplosionForPlayer(self.id, X, Y, Z, type, Radius)

    def edit_object(self, objectid):
        """| METHOD |"""
        return EditObject(self.id, objectid)

    def edit_player_object(self, objectid):
        """| METHOD |"""
        return EditPlayerObject(self.id, objectid)

    def select_object(self):
        """| METHOD |"""
        return SelectObject(self.id)

    def cancel_edit(self):
        """| METHOD |"""
        return CancelEdit(self.id)

    def create_object(self, modelid, x: float, y: float, z: float, rX, rY, rZ, DrawDistance=0.0):
        """| METHOD |"""
        return CreatePlayerObject(self.id, modelid, x, y, z, rX, rY, rZ, DrawDistance)

    def attach_object_to_vehicle(
        self, objectid, vehicleid, fOffsetX, fOffsetY, fOffsetZ, fRotX, fRotY, RotZ
    ):
        """| METHOD |"""
        return AttachPlayerObjectToVehicle(
            self.id,
            objectid,
            vehicleid,
            fOffsetX,
            fOffsetY,
            fOffsetZ,
            fRotX,
            fRotY,
            RotZ,
        )

    def get_object_pos(self, objectid):
        """| METHOD |"""
        return GetPlayerObjectPos(self.id, objectid)

    def set_object_pos(self, objectid, x: float, y: float, z: float):
        """| METHOD |"""
        return SetPlayerObjectPos(self.id, objectid, x, y, z)

    def get_object_rot(self, objectid):
        """| METHOD |"""
        return GetPlayerObjectRot(self.id, objectid)

    def set_object_rot(self, objectid, rotX, rotY, rotZ):
        """| METHOD |"""
        return SetPlayerObjectRot(self.id, objectid, rotX, rotY, rotZ)

    def get_object_model(self, objectid):
        """| METHOD |"""
        return GetPlayerObjectModel(self.id, objectid)

    def set_object_no_camera_col(self, objectid):
        """| METHOD |"""
        return SetPlayerObjectNoCameraCol(self.id, objectid)

    def is_valid_object(self, objectid):
        """| METHOD |"""
        return IsValidPlayerObject(self.id, objectid)

    def destroy_object(self, objectid):
        """| METHOD |"""
        return DestroyPlayerObject(self.id, objectid)

    def move_object(
        self, objectid, x: float, y: float, z: float, Speed, RotX=-1000.0, RotY=-1000.0, RotZ=-1000.0
    ):
        """| METHOD |"""
        return MovePlayerObject(self.id, objectid, x, y, z, Speed, RotX, RotY, RotZ)

    def stop_object(self, objectid):
        """| METHOD |"""
        return StopPlayerObject(self.id, objectid)

    def is_object_moving(self, objectid):
        """| METHOD |"""
        return IsPlayerObjectMoving(self.id, objectid)

    def set_object_material(
        self, objectid, materialindex, modelid, txdname, texturename, materialcolor=0
    ):
        """| METHOD |"""
        return SetPlayerObjectMaterial(
            self.id,
            objectid,
            materialindex,
            modelid,
            txdname,
            texturename,
            materialcolor=0,
        )

    def set_object_material_text(
        self,
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
        """| METHOD |"""
        return SetPlayerObjectMaterialText(
            self.id,
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

    def send_client_message(self, color, message):
        """| METHOD |"""
        return SendClientMessage(self.id, color, message)

    def send_message(self, senderid, message):
        """| METHOD |"""
        return SendPlayerMessageToPlayer(self.id, senderid, message)

    def send_death_message(self, killer, killee, weapon):
        """| METHOD |"""
        return SendDeathMessageToPlayer(self.id, killer, killee, weapon)

    def game_text(self, text, time, style):
        """| METHOD |"""
        return GameTextForPlayer(self.id, text, time, style)

    @property
    def is_npc(self):
        return IsPlayerNPC(self.id)

    @property
    def is_admin(self):
        return IsPlayerAdmin(self.id)

    def kick(self):
        """| METHOD |"""
        return Kick(self.id)

    def ban(self):
        """| METHOD |"""
        return Ban(self.id)

    def ban_ex(self, reason):
        """| METHOD |"""
        return BanEx(self.id, reason)

    @property
    def network_stats(self, size):
        return GetPlayerNetworkStats(self.id, size)

    def get_version(self, len):
        """| METHOD |"""
        return GetPlayerVersion(self.id, len)

    def net_stats_get_connected_time(self):
        """| METHOD |"""
        return NetStats_GetConnectedTime(self.id)

    def net_stats_messages_received(self):
        """| METHOD |"""
        return NetStats_MessagesReceived(self.id)

    def net_stats_bytes_received(self):
        """| METHOD |"""
        return NetStats_BytesReceived(self.id)

    def net_stats_messages_sent(self):
        """| METHOD |"""
        return NetStats_MessagesSent(self.id)

    def net_stats_bytes_sent(self):
        """| METHOD |"""
        return NetStats_BytesSent(self.id)

    def net_stats_messages_recv_per_second(self):
        """| METHOD |"""
        return NetStats_MessagesRecvPerSecond(self.id)

    def net_stats_packet_loss_percent(self):
        """| METHOD |"""
        return NetStats_PacketLossPercent(self.id)

    def net_stats_connection_status(self):
        """| METHOD |"""
        return NetStats_ConnectionStatus(self.id)

    def net_stats_get_ip_port(self, ip_port_len):
        """| METHOD |"""
        return NetStats_GetIpPort(self.id, ip_port_len)

    @property
    def menu(self):
        return GetPlayerMenu(self.id)

    def text_draw_show(self, text):
        """| METHOD |"""
        return TextDrawShowForPlayer(self.id, text)

    def select_text_draw(self, hovercolor):
        """| METHOD |"""
        return SelectTextDraw(self.id, hovercolor)

    def cancel_select_text_draw(self):
        """| METHOD |"""
        return CancelSelectTextDraw(self.id)

    def gang_zone_show(self, zone, color):
        """| METHOD |"""
        return GangZoneShowForPlayer(self.id, zone, color)

    def gang_zone_flash(self, zone, flashcolor):
        """| METHOD |"""
        return GangZoneFlashForPlayer(self.id, zone, flashcolor)

    def gang_zone_stop_flash(self, zone):
        """| METHOD |"""
        return GangZoneStopFlashForPlayer(self.id, zone)

    def show_dialog(self, dialogid, style, caption, info, button1, button2):
        """| METHOD |

        ________________

        - dialogid    An ID to assign this dialog to, so responses can be processed. Max 32767.
        - style       The style of the dialog.
        - caption     The title at the top of the dialog. Max 64 characters.
        - info        The text to display in the main dialog. Use \\n to start a new line and \\t to tabulate.
        - button1     The text on the left button.
        - button2     The text on the right button. Leave it blank ( "" ) to hide it.
        ________________

        Notes
        ------
        - Using negative values for dialogid will close any open dialog.
        - The length of the caption can not exceed more than 64 characters before it starts to cut off.

        Returns
        -----
        1: The function executed successfully.
        0: The function failed to execute. This means the player is not connected.

        Example
        --------
        ```py
            player.show_dialog(123, DIALOG_STYLE_PASSWORD,
                "Please enter your password",
                "Put your password below:",
                "Login", "Quit"
            )
        ```
        """
        return ShowPlayerDialog(
            self.id, dialogid, style, caption, info, button1, button2
        )

    @property
    def gpci(self):
        """| PEROPERTY | Read only |

        Fetch the GPCI of a user, this is linked to their SAMP/GTA on their computer. This hash is NOT Unique, and can be same across multiple players.

        Example
        ------
        ```py
            print(player.gpci)
        ```
        """
        return gpci(self.id, 41)

    def redirect_download(self, url):
        """| METHOD |
        0.3DL Only!!
        """
        return RedirectDownload(self.id, url)

    def create_3d_text_label(
        self,
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
        """| METHOD |

        Params
        -----
        - text 	            The text to display.
        - color	            The text color
        - x                 X Coordinate (or offset if attached)
        - y                 Y Coordinate (or offset if attached)
        - z                 Z Coordinate (or offset if attached)
        - DrawDistance	    The distance where you are able to see the 3D Text Label
        - attachedplayer    The player you want to attach the 3D Text Label to. (None: INVALID_PLAYER_ID)
        - attachedvehicle   The vehicle you want to attach the 3D Text Label to. (None: INVALID_VEHICLE_ID)
        - testLOS	    0/1 Test the line-of-sight so this text can't be seen through walls

        Returns
        -----
        - labelid \t\t The ID of the 3d text label. Used later to update/delete label.

        Example
        ------
        ```py
        label =
            player.create_3d_text_label("test", -1, 0.0,0.0,0.1, 50.0, player.id, INVALID_VEHICLE_ID, 0)
        ```
        """
        return CreatePlayer3DTextLabel(
            self.id,
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

    def delete_3d_text_label(self, id):
        """| METHOD |

        Delete a player 3D-text-label with the given ID.

        Returns
        ----
        1: The function executed successfully.
        0: The function failed to execute. This means the label specified doesn't exist.
        """
        return DeletePlayer3DTextLabel(self.id, id)

    def update_3d_text_label_text(self, id, color, text):
        """| METHOD |

        Updates a player 3D Text Label's text and color. If text is empty, the server/clients next to the text might crash!

        _____________

        - id	    The 3D Text Label you want to update.
        - color	    The color the 3D Text Label should have from now on.
        - text	    The new text which the 3D Text Label should have from now on
        _____________

        Returns
        -----
        - No value returned

        Example
        ------
        ```py
        label =
            player.create_3d_text_label("test", -1, 0.0,0.0,0.1, 50.0, player.id, INVALID_VEHICLE_ID, 0)
        # Change text:
        player.update_3d_text_label_text(label, -1, "New test text")
        ```
        """
        return UpdatePlayer3DTextLabelText(self.id, id, color, text)


class Textdraw:
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


class Vehicle:
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

    def __init__(
        self,
        vehicletype,
        x,
        y,
        z,
        rotation,
        color1,
        color2,
        respawn_delay,
        addsiren=False,
    ):
        self.vehicletype = vehicletype
        self.x = x
        self.y = y
        self.z = z
        self.rotation = rotation
        self.color1 = color1
        self.color2 = color2
        self.respawn_delay = respawn_delay
        self.addsiren=         addsiren
        
        self.id = create_vehicle(
            vehicletype, x, y, z, rotation, color1, color2, respawn_delay, addsiren
        )

    def is_valid(self):
        return is_valid_vehicle(self.id)

    def get_distance_from_point(self, x: float, y: float, z: float):
        return get_vehicle_distance_from_point(self.id, x, y, z)

    def destroy(self):
        return destroy_vehicle(self.id)

    def is_streamed_in(self, forplayerid):
        return is_vehicle_streamed_in(self.id, forplayerid)

    @property
    def pos(self):
        return get_vehicle_pos(self.id)

    @pos.setter
    def pos(self, pos: tuple):
        try:
            x, y, z = pos
        except:
            raise ValueError("Pass position as a tuple: xx.pos = (x,y,z)")
        else:
            return set_vehicle_pos(self.id, x, y, z)

    @property
    def z_angle(self):
        return get_vehicle_z_angle(self.id)

    @z_angle.setter
    def z_angle(self, z_angle: float):
        return set_vehicle_z_angle(self.id, z_angle)

    @property
    def rotation_quat(self):
        return get_vehicle_rotation_quat(self.id)

    def set_params_for_player(self, player: Player, objective, doorslocked):
        return set_vehicle_params_for_player(self.id, player.id, objective, doorslocked)

    @property
    def params_ex(self):
        return GetVehicleParamsEx(self.id)

    @params_ex.setter
    def params_ex(self, param: tuple):
        try:
            engine, lights, alarm, doors, bonnet, boot, objective = param
        except:
            raise ValueError(
                "A tuple was expected: (engine, lights, alarm, doors, bonnet, boot, objective)"
            )
        else:
            return SetVehicleParamsEx(
                self.id, engine, lights, alarm, doors, bonnet, boot, objective
            )

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
            raise ValueError(
                "A tuple was expected: (driver, passenger, backleft, backright)"
            )
        else:
            return SetVehicleParamsCarDoors(
                self.id, driver, passenger, backleft, backright
            )

    @property
    def params_car_windows(self):
        return GetVehicleParamsCarWindows(self.id)

    @params_car_windows.setter
    def params_car_windows(self, param: tuple):
        try:
            driver, passenger, backleft, backright = param
        except:
            raise ValueError(
                "A tuple was expected: (driver, passenger, backleft, backright)"
            )
        else:
            return SetVehicleParamsCarWindows(
                self.id, driver, passenger, backleft, backright
            )

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

    def set_angular_velocity(self, x: float, y: float, z: float):
        return SetVehicleAngularVelocity(self.id, X, Y, Z)

    @property
    def damage_status(self):
        return GetVehicleDamageStatus(self.id)

    @damage_status.setter
    def damage_status(self, param: tuple):
        try:
            panels, doors, lights, tires = param
        except:
            raise ValueError(
                "Expected a tuple for damage_status: (panels, doors, lights, tires)"
            )
        else:
            return UpdateVehicleDamageStatus(self.id, panels, doors, lights, tires)

    @property
    def virtual_world(self):
        return GetVehicleVirtualWorld(self.id)

    @virtual_world.setter
    def virtual_world(self, worldid):
        return SetVehicleVirtualWorld(self.id, worldid)

class Gang_Zone:
    def __init__(self, minx: float, miny: float, maxx: float, maxy: float):
        self.minx = minx
        self.miny = miny
        self.maxx = maxx
        self.maxy = maxy
        self.id = gang_zone_create(minx, miny, maxx, maxy)

    # TODO: Check this, 
    # Not sure if this is right. I want to tell the server the object is no longer needed.
    def __del__(self):
        gang_zone_destroy(self.id)


    def show_for_player(self, player: Player, color: int): # yes, swapped places on args
        return gang_zone_show_for_player(player.id, self.id, color)


    def show_for_all(self, color: int):
        return gang_zone_show_for_all(self.id, color)


    def hide_for_player(self, player: Player): # yes, swapped places on args
        return gang_zone_hide_for_player(player.id, self.id)


    def hide_for_all(self):
        return gang_zone_hide_for_all(self.id)


    def flash_for_player(self, player: Player, flashcolor: int): # yes, swapped places on args
        return gang_zone_flash_for_player(player.id, self.id, flashcolor)


    def flash_for_all(self, flashcolor: int):
        return gang_zone_flash_for_all(self.id, flashcolor)


    def stop_flash_for_player(self, player: Player): # yes, swapped places on args
        return gang_zone_stop_flash_for_player(player.id, self.id)


    def stop_flash_for_all(self):
        return gang_zone_stop_flash_for_all(self.id)


@dataclass
class Text_Label:

    def __init__(self, text: str, color: int, x: float, y: float, z: float, drawDistance: float, virtualworld: int, testLOS=False) -> None:
        
        self.text = text
        self.color = color
        self.x = x
        self.y = y
        self.z = z
        self.draw_distance = drawDistance
        self.virtual_world = virtualworld
        self.test_los = testLOS
        self.id = create_3d_text_label(
            self.text, self.color, self.x, self.y, self.z, self.draw_distance, self.virtual_world, self.test_los
        )
    
    def __del__(self):
        return delete_3d_text_label(self.id)


    def attach_to_player(self, player: Player, offsetX: float, offsetY: float, offsetZ: float) -> int:
        return attach_3d_text_label_to_player(self.id, player.id, offsetX, offsetY, offsetZ)


    def attach_to_vehicle(self, vehicle: Vehicle, offsetX: float, offsetY: float, offsetZ: float) -> int:
        return attach_3d_text_label_to_vehicle(self.id, vehicle.id, offsetX, offsetY, offsetZ)


    def update_text(self, color: int, text: str) -> None:
        return update_3d_text_label_text(self.id, color, text)