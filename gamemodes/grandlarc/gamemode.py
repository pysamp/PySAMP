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

EDIT April 2021: Converted gamemode to use newly made classes in samp.py for Players, Vehicles and Actors.

Everything here should function as in the original PAWN version, and if you 
find any bugs, you can report them on our repo; https://github.com/habecker/PySAMP/issues

For now, enjoy the code, and good luck!
denNorske & Habecker
"""
################################


def on_game_mode_init():
    set_game_mode_text('PyLarc')
    print("-----------------------------------------------")
    print("Running Grand Larceny - by the SA-MP team\nRe-written to python 3.8.6 by the PySAMP Team")
    print("-----------------------------------------------")
    show_player_markers(1) # PLAYER_MARKERS_MODE_GLOBAL = 1
    show_name_tags(True)
    set_name_tag_draw_distance(40)
    enable_stunt_bonus_for_all(False)
    disable_interior_enter_exits()
    set_weather(2)
    #LimitGlobalChatRadius(300.0)
    
    class_sel_init_textdraws()

    # Player Class
    add_player_class(1,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    add_player_class(2,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    add_player_class(47,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    add_player_class(48,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    add_player_class(49,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    add_player_class(50,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    add_player_class(51,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    add_player_class(52,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    add_player_class(53,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    add_player_class(54,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    add_player_class(55,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    add_player_class(56,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    add_player_class(57,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    add_player_class(58,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    add_player_class(68,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    add_player_class(69,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    add_player_class(70,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    add_player_class(71,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    add_player_class(72,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    add_player_class(73,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    add_player_class(75,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    add_player_class(76,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    add_player_class(78,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    add_player_class(79,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    add_player_class(80,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    add_player_class(81,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    add_player_class(82,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    add_player_class(83,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    add_player_class(84,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    add_player_class(85,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    add_player_class(87,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    add_player_class(88,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    add_player_class(89,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    add_player_class(91,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    add_player_class(92,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    add_player_class(93,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    add_player_class(95,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    add_player_class(96,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    add_player_class(97,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    add_player_class(98,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    add_player_class(99,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    add_player_class(269,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    add_player_class(270,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    add_player_class(271,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)
    add_player_class(272,1759.0189,-1898.1260,13.5622,266.4503,-1,-1,-1,-1,-1,-1)

    total_vehicles_from_files = (
    # SPECIAL:
    load_vehs_from_file("scriptfiles/vehicles/trains.txt")       + 
    load_vehs_from_file("scriptfiles/vehicles/pilots.txt")       + 
    # Las Venturas
    load_vehs_from_file("scriptfiles/vehicles/lv_law.txt")       +  
    load_vehs_from_file("scriptfiles/vehicles/lv_airport.txt")   + 
    load_vehs_from_file("scriptfiles/vehicles/lv_gen.txt")       + 
    # San fierro
    load_vehs_from_file("scriptfiles/vehicles/sf_law.txt")       + 
    load_vehs_from_file("scriptfiles/vehicles/sf_airport.txt")   + 
    load_vehs_from_file("scriptfiles/vehicles/sf_gen.txt")       + 
    # Los Santos
    load_vehs_from_file("scriptfiles/vehicles/ls_law.txt")       +  
    load_vehs_from_file("scriptfiles/vehicles/ls_airport.txt")   + 
    load_vehs_from_file("scriptfiles/vehicles/ls_gen_inner.txt") + 
    load_vehs_from_file("scriptfiles/vehicles/ls_gen_outer.txt") + 
    # Other areas
    load_vehs_from_file("scriptfiles/vehicles/whetstone.txt")    + 
    load_vehs_from_file("scriptfiles/vehicles/bone.txt")         + 
    load_vehs_from_file("scriptfiles/vehicles/flint.txt")        + 
    load_vehs_from_file("scriptfiles/vehicles/tierra.txt")       + 
    load_vehs_from_file("scriptfiles/vehicles/red_county.txt"))


    print("Total vehicles from files: {}".format(total_vehicles_from_files))
    return True
    
def on_gamemode_exit():
    return True


def on_player_connect(playerid):
    global player
    player_obj = PlayerVars(playerid) ## Create the player object
    player[playerid] = player_obj ## then keep it tracked in a dict. (lookup by playerid)
    player[playerid].game_text("~w~Grand Larceny",3000,4)
    player[playerid].send_client_message(COLOR_WHITE,"Welcome to Grand Larceny")
    return True
    
def on_player_disconnect(playerid, reason):
    player.pop(playerid, 0)
    return True
    
def on_player_spawn(playerid):
    global player
    if player[playerid].is_npc:
        return True
    randspawn = 0
    player[playerid].interior = 0
    player[playerid].toggle_clock(0)
    player[playerid].reset_money()
    player[playerid].give_money(30000)

    player[playerid].has_city_selected = False
    
    if player[playerid].city_selection == CITY_LOS_SANTOS:
        randspawn = random.randint(0, len(spawn_ls))
        player[playerid].pos() 
            spawn_ls[randspawn][0], 
            spawn_ls[randspawn][1], 
            spawn_ls[randspawn][2]
        )
    elif player[playerid].city_selection == CITY_SAN_FIERRO:
        randspawn = random.randint(0, len(spawn_sf))
        set_player_pos(playerid, 
            spawn_sf[randspawn][0], 
            spawn_sf[randspawn][1], 
            spawn_sf[randspawn][2]
        )
    elif player[playerid].city_selection == CITY_LAS_VENTURAS:
        randspawn = random.randint(0, len(spawn_lv))
        set_player_pos(playerid, 
            spawn_lv[randspawn][0], 
            spawn_lv[randspawn][1], 
            spawn_lv[randspawn][2]
        )
    set_player_skill_level(playerid,Const("WEAPONSKILL_PISTOL"),200)
    set_player_skill_level(playerid,Const("WEAPONSKILL_PISTOL_SILENCED"),200)
    set_player_skill_level(playerid,Const("WEAPONSKILL_DESERT_EAGLE"),200)
    set_player_skill_level(playerid,Const("WEAPONSKILL_SHOTGUN"),200)
    set_player_skill_level(playerid,Const("WEAPONSKILL_SAWNOFF_SHOTGUN"),200)
    set_player_skill_level(playerid,Const("WEAPONSKILL_SPAS12_SHOTGUN"),200)
    set_player_skill_level(playerid,Const("WEAPONSKILL_MICRO_UZI"),200)
    set_player_skill_level(playerid,Const("WEAPONSKILL_MP5"),200)
    set_player_skill_level(playerid,Const("WEAPONSKILL_AK47"),200)
    set_player_skill_level(playerid,Const("WEAPONSKILL_M4"),200)
    set_player_skill_level(playerid,Const("WEAPONSKILL_SNIPERRIFLE"),200)
    
    give_player_weapon(playerid,22,100) # Colt 45            
    return True

def on_player_death(playerid, killerid, reason):
    if killerid == 65535:
        reset_player_money(playerid)
    else:
        give_player_money(killerid, get_player_money(playerid))
        reset_player_money(playerid)
    return True

# Used to init textdraws of city names
def class_sel_init_city_textdraws(txtInit):
    global txt_class_sel_helper
    text_draw_use_box(txtInit, 0)
    text_draw_letter_size(txtInit,1.25,3.0)
    text_draw_font(txtInit, 0)
    text_draw_set_shadow(txtInit,0)
    text_draw_set_outline(txtInit,1)
    text_draw_color(txtInit,4008636159)
    text_draw_background_color(txt_class_sel_helper,255)
    return

def class_sel_init_textdraws():
    global txt_ls
    global txt_sf
    global txt_lv
    global txt_class_sel_helper
    # Init our observer helper text display
    txt_ls = text_draw_create(10.0, 380.0, "Los Santos")
    class_sel_init_city_textdraws(txt_ls)
    txt_sf = text_draw_create(10.0, 380.0, "San Fierro")
    class_sel_init_city_textdraws(txt_sf)
    txt_lv = text_draw_create(10.0, 380.0, "Las Venturas")
    class_sel_init_city_textdraws(txt_lv)

    # Init our observer helper text display
    txt_class_sel_helper = text_draw_create(10.0, 415.0,
        " Press ~b~~k~~GO_LEFT~ ~w~or ~b~~k~~GO_RIGHT~ ~w~to switch cities.~n~ Press ~r~~k~~PED_FIREWEAPON~ ~w~to select.")
    text_draw_use_box(txt_class_sel_helper, 1)
    text_draw_box_color(txt_class_sel_helper,572662459)
    text_draw_letter_size(txt_class_sel_helper,0.3,1.0)
    text_draw_text_size(txt_class_sel_helper,400.0,40.0)
    text_draw_font(txt_class_sel_helper, 2)
    text_draw_set_shadow(txt_class_sel_helper,0)
    text_draw_set_outline(txt_class_sel_helper,1)
    text_draw_background_color(txt_class_sel_helper,255)
    text_draw_color(txt_class_sel_helper,4294967295)
    return


def class_sel_setup_char_selection(playerid):
    for player in players:
        if player.playerid == playerid:
            if player.city_selection == CITY_LOS_SANTOS:
                set_player_interior(playerid,11)
                set_player_pos(playerid,508.7362,-87.4335,998.9609)
                set_player_facing_angle(playerid,0.0)
                set_player_camera_pos(playerid,508.7362,-83.4335,998.9609)
                set_player_camera_look_at(playerid,508.7362,-87.4335,998.9609)
            
            elif player.city_selection == CITY_SAN_FIERRO:
                set_player_interior(playerid,3)
                set_player_pos(playerid,-2673.8381,1399.7424,918.3516)
                set_player_facing_angle(playerid,181.0)
                set_player_camera_pos(playerid,-2673.2776,1394.3859,918.3516)
                set_player_camera_look_at(playerid,-2673.8381,1399.7424,918.3516)
            
            elif player.city_selection == CITY_LAS_VENTURAS:
                set_player_interior(playerid,3)
                set_player_pos(playerid,349.0453,193.2271,1014.1797)
                set_player_facing_angle(playerid,286.25)
                set_player_camera_pos(playerid,352.9164,194.5702,1014.1875)
                set_player_camera_look_at(playerid,349.0453,193.2271,1014.1797)
            break
    return

def class_sel_setup_selected_city(playerid):
    global txt_ls
    global txt_sf
    global txt_lv

    for player in players:
        if player.playerid == playerid:
            if player.city_selection == -1:
                player.city_selection = CITY_LOS_SANTOS
            
            if player.city_selection == CITY_LOS_SANTOS:
                set_player_interior(playerid,0)
                set_player_camera_pos(playerid,1630.6136,-2286.0298,110.0)
                set_player_camera_look_at(playerid,1887.6034,-1682.1442,47.6167)

                text_draw_show_for_player(playerid,txt_ls)
                text_draw_hide_for_player(playerid,txt_sf)
                text_draw_hide_for_player(playerid,txt_lv)

            elif player.city_selection == CITY_SAN_FIERRO:
                set_player_interior(playerid,0)
                set_player_camera_pos(playerid,-1300.8754,68.0546,129.4823)
                set_player_camera_look_at(playerid,-1817.9412,769.3878,132.6589)

                text_draw_hide_for_player(playerid,txt_ls)
                text_draw_show_for_player(playerid,txt_sf)
                text_draw_hide_for_player(playerid,txt_lv)

            elif player.city_selection == CITY_LAS_VENTURAS:
                set_player_interior(playerid,0)
                set_player_camera_pos(playerid,1310.6155,1675.9182,110.7390)
                set_player_camera_look_at(playerid,2285.2944,1919.3756,68.2275)

                text_draw_hide_for_player(playerid,txt_ls)
                text_draw_hide_for_player(playerid,txt_sf)
                text_draw_show_for_player(playerid,txt_lv)
            break
    return

def class_sel_go_next_city(playerid):

    for player in players:
        if player.playerid == playerid:
            player.last_city_selection_tick = get_tick_count()
            player.city_selection += 1
            if player.city_selection > CITY_LAS_VENTURAS:
                    player.city_selection = CITY_LOS_SANTOS
            break
    
    player_play_sound(playerid,1052,0.0,0.0,0.0)
    class_sel_setup_selected_city(playerid)
    return

def class_sel_go_previous_city(playerid):
    for player in players:
        if player.playerid == playerid:
            player.last_city_selection_tick = get_tick_count()
            player.city_selection -= 1
            if player.city_selection < CITY_LOS_SANTOS:
                    player.city_selection = CITY_LAS_VENTURAS
            break

    player_play_sound(playerid,1053,0.0,0.0,0.0)
    class_sel_setup_selected_city(playerid)
    return

def class_sel_handle_city_selection(playerid):
    global txt_ls
    global txt_sf
    global txt_lv
    global txt_class_sel_helper
    (Keys, ud, lr) = get_player_keys(playerid)
    for player in players:
        if player.playerid == playerid:
            # only allow selection every ~500 ms
            if get_tick_count() - player.last_city_selection_tick < 500:
                break
            if player.city_selection == -1 : 
                class_sel_go_next_city(playerid)
                break
            if Keys & 4 :
                player.has_city_selected = True
                text_draw_hide_for_player(playerid,txt_class_sel_helper)
                text_draw_hide_for_player(playerid,txt_ls)
                text_draw_hide_for_player(playerid,txt_sf)
                text_draw_hide_for_player(playerid,txt_lv)
                toggle_player_spectating(playerid,False)
            if lr > 0 :
                class_sel_go_next_city(playerid)
            elif lr < 0 :
                class_sel_go_previous_city(playerid)
            break
    return True

def on_player_text(playerid, text):
    return True

def on_player_request_class(playerid, classid):
    if is_player_npc(playerid):
        return True
    global txt_class_sel_helper
    for player in players:
        if player.playerid == playerid:
            if player.has_city_selected == True:
                class_sel_setup_char_selection(playerid)
                return True
            else:
                if get_player_state(playerid) != Const("PLAYER_STATE_SPECTATING"):
                    spawn_player(playerid) # Why? 
                    #Else player does not load in correctly and the toggle below will disconnect the player. 
                    # Read the known issues on our repo wiki. 
                    toggle_player_spectating(playerid, 1)
                    text_draw_show_for_player(playerid, txt_class_sel_helper)
                    player.city_selection = -1
    return True
    

    
def on_player_update(playerid):
    if is_player_connected(playerid) == False:
        return False
    if is_player_npc(playerid):
        return True
    for player in players:
        if player.playerid == playerid:
            if ( player.has_city_selected == False and
            get_player_state(playerid) == Const("PLAYER_STATE_SPECTATING") ):
                class_sel_handle_city_selection(playerid)
    
    if get_player_interior(playerid) != 0 and get_player_weapon(playerid) != 0:
        set_player_armed_weapon(playerid, 0) # Fists
        return False #No syncing until they change their weapon
    
    if get_player_weapon(playerid) == 38 or get_player_special_action(playerid) == 2: #minigun and jetpack not allowed
        kick(playerid)
        return False
    return True
    
