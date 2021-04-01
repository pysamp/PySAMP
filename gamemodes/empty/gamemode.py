from samp import *
from const import *

def on_game_mode_init():
    set_game_mode_text('PySAMP')
    return True
    
def on_gamemode_exit():
    return True

def on_py_unload():
    on_gamemode_exit()
    return True

def on_py_reload():
    on_game_mode_init()
    return True

def on_player_connect(playerid):
    send_client_message(playerid, 0xFF000000, "Hello %s from Python" % get_player_name(playerid, MAX_PLAYER_NAME.get()))
    return True
    
def on_player_disconnect(playerid, reason):
    return True
    
def on_player_spawn(playerid):
    return True
    
def on_player_death(playerid, killerid, reason):
    return True
    
def on_vehicle_spawn(vehicleid):
    return True
    
def on_vehicle_death(vehicleid, killerid):
    return False
    
def on_player_text(playerid, text):
    text = decode(text)
    return False
    
def on_player_command_text(playerid, cmdtext):
    cmdtext = decode(cmdtext)
    return False
    
def on_player_request_class(playerid, classid):
    return True
    
def on_player_enter_vehicle(playerid, vehicleid, ispassenger):
    return False
    
def on_player_exit_vehicle(playerid, vehicleid):
    return False
    
def on_player_state_change(playerid, newstate, oldstate):
    return False
    
def on_player_enter_checkpoint(playerid):
    return False
    
def on_player_leave_checkpoint(playerid):
    return False
    
def on_player_enter_race_checkpoint(playerid):
    return False
    
def on_player_leave_race_checkpoint(playerid):
    return False
    
def on_rcon_command(cmd):
    cmd = decode(cmd)
    return False
    
def on_player_request_spawn(playerid):
    return True
    
def on_object_moved(objectid):
    return False
    
def on_player_object_moved(playerid, objectid):
    return False
    
def on_player_pick_up_pickup(playerid, pickupid):
    return False
    
def on_vehicle_mod(playerid, vehicleid, componentid):
    return True
    
def on_enter_exit_mod_shop(playerid, enterexit, interiorid):
    return False
    
def on_vehicle_paintjob(playerid, vehicleid, paintjobid):
    return True
    
def on_vehicle_respray(playerid, vehicleid, color1, color2):
    return True
    
def on_vehicle_damage_status_update(vehicleid, playerid):
    return False
    
def on_unoccupied_vehicle_update(vehicleid, playerid, passenger_seat, new_x, new_y, new_z, vel_x, vel_y, vel_z):
    return True
    
def on_player_selected_menu_row(playerid, row):
    return False
    
def on_player_exited_menu(playerid):
    return False
    
def on_player_interior_change(playerid, newinteriorid, oldinteriorid):
    return False
    
def on_player_key_state_change(playerid, newkeys, oldkeys):
    return False
    
def on_rcon_login_attempt(ip, password, success):
    password = decode(password)
    return False
    
def on_player_update(playerid):
    return True
    
def on_player_stream_in(playerid, forplayerid):
    return False
    
def on_player_stream_out(playerid, forplayerid):
    return False
    
def on_vehicle_stream_in(vehicleid, forplayerid):
    return False
        
def on_vehicle_stream_out(vehicleid, forplayerid):
    return False
    
def on_actor_stream_in(actorid, forplayerid):
    return False
    
def on_actor_stream_out(actorid, forplayerid):
    return False
    
def on_dialog_response(playerid, dialogid, response, listitem, inputtext):
    return False
    
def on_player_take_damage(playerid, issuerid, amount, weaponid, bodypart):
    return False
    
def on_player_give_damage(playerid, damagedid, amount, weaponid, bodypart):
    return False
    
def on_player_give_damage_actor(playerid, damaged_actorid, amount, weaponid, bodypart):
    return False
    
def on_player_click_map(playerid, fX, fY, fZ):
    return False
    
def on_player_click_textdraw(playerid, clickedid):
    return False
    
def on_player_click_player_textdraw(playerid, playertextid):
    return False
    
def on_incoming_connection(playerid, ip_address, port):
    ip_address = decode(ip_address)
    return False
    
def on_trailer_update(playerid, vehicleid):
    return True
    
def on_vehicle_siren_state_change(playerid, vehicleid, newstate):
    return False
    
def on_player_click_player(playerid, clickedplayerid, source):
    return False
    
def on_player_edit_object(playerid, playerobject, objectid, response, fX, fY, fZ, fRotX, fRotY, fRotZ):
    return False
    
def on_player_edit_attached_object(playerid, response, index, modelid, boneid, fOffsetX, fOffsetY, fOffsetZ, fRotX, fRotY, fRotZ, fScaleX, fScaleY, fScaleZ):
    return False
    
def on_player_select_object(playerid, type, objectid, modelid, fX, fY, fZ):
    return False
    
def on_player_weapon_shot(playerid, weaponid, hittype, hitid, fX, fY, fZ):
    return True

def on_process_tick():
    return None

""" you can initialize your own additional threads here, note that OnThreadingInit isn't supposed to be a worker thread but gives you the ability to start them. Otherwise it would block the plugin initialization """
def on_threading_init():
    return None

""" your initialized threads must be shutdown during this callbac """
def on_threading_stop_signal():
    return None