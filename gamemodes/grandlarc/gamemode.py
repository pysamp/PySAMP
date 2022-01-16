import random
from typing import Dict

from .funcs import load_vehs_from_file
from .glspawns import spawn_ls, spawn_lv, spawn_sf
from .player import PlayerVars, Textdraw
from .pysamp import (
    add_player_class,
    disable_interior_enter_exits,
    set_game_mode_text,
    set_name_tag_draw_distance,
    set_weather,
    show_name_tags,
    show_player_markers,
    enable_stunt_bonus_for_all,
    get_tick_count,
    is_player_npc,
    is_player_connected,
    WEAPONSKILL_PISTOL,
    WEAPONSKILL_PISTOL_SILENCED,
    WEAPONSKILL_DESERT_EAGLE,
    WEAPONSKILL_SHOTGUN,
    WEAPONSKILL_SAWNOFF_SHOTGUN,
    WEAPONSKILL_MP5,
    WEAPONSKILL_SPAS12_SHOTGUN,
    WEAPONSKILL_M4,
    WEAPONSKILL_MICRO_UZI,
    WEAPONSKILL_AK47,
    WEAPONSKILL_SNIPERRIFLE,
    PLAYER_STATE_SPECTATING,
)
from .vars import (
    CITY_LAS_VENTURAS, CITY_LOS_SANTOS, CITY_SAN_FIERRO, COLOR_WHITE
)

player: Dict[int, PlayerVars] = {}
textdraw: Dict[str, Textdraw] = {}
################################
"""
Hello dear user!
Welcome to the Python version of the original Grand Larceny gamemode!
We wanted to convert this classic gamemode into what it would look like
in python, and here is the result. We took our liberty to nick it "PyLarc".

The intention behind converting it, was to give you all an idea of how
the plugin works, and to give you all a good example.

EDIT January 2022: Converted gamemode to use newly made classes in samp.py
for Players, Vehicles, Textdraws and Actors.
Also, converted to snake_case

Everything here should function as in the original PAWN version, and if you
find any bugs, you can report them on our repo;
https://github.com/habecker/PySAMP/issues

For now, enjoy the code, and good luck!
denNorske, Cheaterman & Habecker
"""
################################


def OnGameModeInit():
    set_game_mode_text("PyLarc")
    print("-----------------------------------------------")
    print(
        "Running Grand Larceny - by the SA-MP team\n\
            Re-written to python 3.8.6 by the PySAMP Team"
    )
    print("-----------------------------------------------")
    show_player_markers(1)  # PLAYER_MARKERS_MODE_GLOBAL = 1
    show_name_tags(True)
    set_name_tag_draw_distance(40)
    enable_stunt_bonus_for_all(False)
    disable_interior_enter_exits()
    set_weather(2)
    # LimitGlobalChatRadius(300.0)

    class_sel_init_textdraws()

    # Player Class
    add_player_class(
        1, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1
    )
    add_player_class(
        2, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1
    )
    add_player_class(
        47, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1
    )
    add_player_class(
        48, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1
    )
    add_player_class(
        49, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1
    )
    add_player_class(
        50, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1
    )
    add_player_class(
        51, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1
    )
    add_player_class(
        52, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1
    )
    add_player_class(
        53, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1
    )
    add_player_class(
        54, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1
    )
    add_player_class(
        55, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1
    )
    add_player_class(
        56, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1
    )
    add_player_class(
        57, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1
    )
    add_player_class(
        58, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1
    )
    add_player_class(
        68, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1
    )
    add_player_class(
        69, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1
    )
    add_player_class(
        70, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1
    )
    add_player_class(
        71, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1
    )
    add_player_class(
        72, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1
    )
    add_player_class(
        73, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1
    )
    add_player_class(
        75, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1
    )
    add_player_class(
        76, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1
    )
    add_player_class(
        78, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1
    )
    add_player_class(
        79, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1
    )
    add_player_class(
        80, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1
    )
    add_player_class(
        81, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1
    )
    add_player_class(
        82, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1
    )
    add_player_class(
        83, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1
    )
    add_player_class(
        84, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1
    )
    add_player_class(
        85, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1
    )
    add_player_class(
        87, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1
    )
    add_player_class(
        88, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1
    )
    add_player_class(
        89, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1
    )
    add_player_class(
        91, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1
    )
    add_player_class(
        92, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1
    )
    add_player_class(
        93, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1
    )
    add_player_class(
        95, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1
    )
    add_player_class(
        96, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1
    )
    add_player_class(
        97, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1
    )
    add_player_class(
        98, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1
    )
    add_player_class(
        99, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1
    )
    add_player_class(
        269, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1
    )
    add_player_class(
        270, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1
    )
    add_player_class(
        271, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1
    )
    add_player_class(
        272, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1
    )

    total_vehicles_from_files = (
        load_vehs_from_file("scriptfiles/vehicles/trains.txt")
        + load_vehs_from_file("scriptfiles/vehicles/pilots.txt")
        +
        # Las Venturas
        load_vehs_from_file("scriptfiles/vehicles/lv_law.txt")
        + load_vehs_from_file("scriptfiles/vehicles/lv_airport.txt")
        + load_vehs_from_file("scriptfiles/vehicles/lv_gen.txt")
        +
        # San fierro
        load_vehs_from_file("scriptfiles/vehicles/sf_law.txt")
        + load_vehs_from_file("scriptfiles/vehicles/sf_airport.txt")
        + load_vehs_from_file("scriptfiles/vehicles/sf_gen.txt")
        +
        # Los Santos
        load_vehs_from_file("scriptfiles/vehicles/ls_law.txt")
        + load_vehs_from_file("scriptfiles/vehicles/ls_airport.txt")
        + load_vehs_from_file("scriptfiles/vehicles/ls_gen_inner.txt")
        + load_vehs_from_file("scriptfiles/vehicles/ls_gen_outer.txt")
        +
        # Other areas
        load_vehs_from_file("scriptfiles/vehicles/whetstone.txt")
        + load_vehs_from_file("scriptfiles/vehicles/bone.txt")
        + load_vehs_from_file("scriptfiles/vehicles/flint.txt")
        + load_vehs_from_file("scriptfiles/vehicles/tierra.txt")
        + load_vehs_from_file("scriptfiles/vehicles/red_county.txt")
    )

    print("Total vehicles from files: {}".format(total_vehicles_from_files))
    return True


def OnGameModeExit():
    return True


def OnPlayerConnect(playerid):
    global player
    player_obj = PlayerVars(playerid)  # Create the player object
    player[playerid] = player_obj  # then keep it tracked in a dict.
    player[playerid].game_text("~w~Grand Larceny", 3000, 4)
    player[playerid].send_client_message(
        COLOR_WHITE, "Welcome to Grand Larceny"
    )
    return True


def OnPlayerDisconnect(playerid, reason):
    player.pop(playerid, 0)
    return True


def OnPlayerSpawn(playerid):
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
        player[playerid].pos = (
            spawn_ls[randspawn][0],
            spawn_ls[randspawn][1],
            spawn_ls[randspawn][2],
        )
    elif player[playerid].city_selection == CITY_SAN_FIERRO:
        randspawn = random.randint(0, len(spawn_sf))
        player[playerid].pos = (
            spawn_sf[randspawn][0],
            spawn_sf[randspawn][1],
            spawn_sf[randspawn][2],
        )

    elif player[playerid].city_selection == CITY_LAS_VENTURAS:
        randspawn = random.randint(0, len(spawn_lv))
        player[playerid].pos = (
            spawn_lv[randspawn][0],
            spawn_lv[randspawn][1],
            spawn_lv[randspawn][2],
        )

    player[playerid].set_skill_level(WEAPONSKILL_PISTOL, 200)
    player[playerid].set_skill_level(WEAPONSKILL_PISTOL_SILENCED, 200)
    player[playerid].set_skill_level(WEAPONSKILL_DESERT_EAGLE, 200)
    player[playerid].set_skill_level(WEAPONSKILL_SHOTGUN, 200)
    player[playerid].set_skill_level(WEAPONSKILL_SAWNOFF_SHOTGUN, 200)
    player[playerid].set_skill_level(WEAPONSKILL_SPAS12_SHOTGUN, 200)
    player[playerid].set_skill_level(WEAPONSKILL_MICRO_UZI, 200)
    player[playerid].set_skill_level(WEAPONSKILL_MP5, 200)
    player[playerid].set_skill_level(WEAPONSKILL_AK47, 200)
    player[playerid].set_skill_level(WEAPONSKILL_M4, 200)
    player[playerid].set_skill_level(WEAPONSKILL_SNIPERRIFLE, 200)

    player[playerid].give_weapon(22, 100)  # Colt 45
    return True


def OnPlayerDeath(playerid, killerid, reason):
    if killerid == 65535:
        player[playerid].reset_money()
    else:
        player[killerid].money += player[playerid].money
        # Alternatively, can also do:
        # player[killerid].give_money(player[playerid].money)

        player[playerid].money = 0
    return True


# Used to init textdraws of city names
def class_sel_init_city_textdraws(txtInit: str):
    global textdraw
    textdraw[txtInit].use_box(0)
    textdraw[txtInit].letter_size(1.25, 3.0)
    textdraw[txtInit].font(0)
    textdraw[txtInit].set_shadow(0)
    textdraw[txtInit].set_outline(1)
    textdraw[txtInit].color(4008636159)
    return


def class_sel_init_textdraws():
    global textdraw
    # Init our observer helper text display

    # Create new textdraws, our dict can be named with string indexes;
    textdraw["ls"] = Textdraw(10.0, 380.0, "Los Santos")
    textdraw["sf"] = Textdraw(10.0, 380.0, "San Fierro")
    textdraw["lv"] = Textdraw(10.0, 380.0, "Las Venturas")

    class_sel_init_city_textdraws("ls")
    class_sel_init_city_textdraws("sf")
    class_sel_init_city_textdraws("lv")

    # Init our observer helper text display
    textdraw["txt_class_sel_helper"] = Textdraw(
        10.0,
        415.0,
        " Press ~b~~k~~GO_LEFT~ ~w~or ~b~~k~~GO_RIGHT~ ~w~to switch cities.~n~\
        Press ~r~~k~~PED_FIREWEAPON~ ~w~to select.",
    )

    textdraw["txt_class_sel_helper"].use_box(1)
    textdraw["txt_class_sel_helper"].box_color(572662459)
    textdraw["txt_class_sel_helper"].letter_size(0.3, 1.0)
    textdraw["txt_class_sel_helper"].text_size(400.0, 40.0)
    textdraw["txt_class_sel_helper"].font(2)
    textdraw["txt_class_sel_helper"].set_shadow(0)
    textdraw["txt_class_sel_helper"].set_outline(1)
    textdraw["txt_class_sel_helper"].background_color(255)
    textdraw["txt_class_sel_helper"].color(4294967295)
    return


def class_sel_setup_char_selection(playerid):
    global player
    if player[playerid].city_selection == CITY_LOS_SANTOS:
        player[playerid].interior = 11
        player[playerid].pos = (508.7362, -87.4335, 998.9609)
        player[playerid].facing_angle = 0.0
        player[playerid].camera_pos = (508.7362, -83.4335, 998.9609)
        player[playerid].set_camera_look_at(508.7362, -87.4335, 998.9609)

    elif player[playerid].city_selection == CITY_SAN_FIERRO:
        player[playerid].interior = 3
        player[playerid].pos = (-2673.8381, 1399.7424, 918.3516)
        player[playerid].facing_angle = 181.0
        player[playerid].camera_pos = (-2673.2776, 1394.3859, 918.3516)
        player[playerid].set_camera_look_at(-2673.8381, 1399.7424, 918.3516)

    elif player[playerid].city_selection == CITY_LAS_VENTURAS:
        player[playerid].interior = 3
        player[playerid].pos = (349.0453, 193.2271, 1014.1797)
        player[playerid].facing_angle = 286.25
        player[playerid].camera_pos = (352.9164, 194.5702, 1014.1875)
        player[playerid].set_camera_look_at(349.0453, 193.2271, 1014.1797)


def class_sel_setup_selected_city(playerid):
    global player
    global textdraw
    if player[playerid].city_selection == -1:
        player[playerid].city_selection = CITY_LOS_SANTOS

    if player[playerid].city_selection == CITY_LOS_SANTOS:
        player[playerid].interior = 0
        player[playerid].camera_pos = (1630.6136, -2286.0298, 110.0)
        player[playerid].set_camera_look_at(1887.6034, -1682.1442, 47.6167)

        player[playerid].text_draw_show(textdraw["ls"].id)
        player[playerid].text_draw_hide_for_player(textdraw["sf"].id)
        player[playerid].text_draw_hide_for_player(textdraw["lv"].id)

    elif player[playerid].city_selection == CITY_SAN_FIERRO:
        player[playerid].interior = 0
        player[playerid].camera_pos = (-1300.8754, 68.0546, 129.4823)
        player[playerid].set_camera_look_at(-1817.9412, 769.3878, 132.6589)

        player[playerid].text_draw_hide_for_player(textdraw["ls"].id)
        player[playerid].text_draw_show(textdraw["sf"].id)
        player[playerid].text_draw_hide_for_player(textdraw["lv"].id)

    elif player[playerid].city_selection == CITY_LAS_VENTURAS:
        player[playerid].interior = 0
        player[playerid].camera_pos = (1310.6155, 1675.9182, 110.7390)
        player[playerid].set_camera_look_at(2285.2944, 1919.3756, 68.2275)

        player[playerid].text_draw_hide_for_player(textdraw["ls"].id)
        player[playerid].text_draw_hide_for_player(textdraw["sf"].id)
        player[playerid].text_draw_show(textdraw["lv"].id)


def class_sel_go_next_city(playerid):
    global player
    player[playerid].last_city_selection_tick = get_tick_count()
    player[playerid].city_selection += 1
    if player[playerid].city_selection > CITY_LAS_VENTURAS:
        player[playerid].city_selection = CITY_LOS_SANTOS

    player[playerid].play_sound(1052, 0.0, 0.0, 0.0)
    class_sel_setup_selected_city(playerid)
    return


def class_sel_go_previous_city(playerid):
    global player
    player[playerid].last_city_selection_tick = get_tick_count()
    player[playerid].city_selection -= 1
    if player[playerid].city_selection < CITY_LOS_SANTOS:
        player[playerid].city_selection = CITY_LAS_VENTURAS

    player[playerid].play_sound(1053, 0.0, 0.0, 0.0)
    class_sel_setup_selected_city(playerid)
    return


def class_sel_handle_city_selection(playerid):
    global player
    (Keys, ud, lr) = player[playerid].keys
    if ud:
        pass  # remove warning for unused variable
    # only allow selection every ~500 ms
    if get_tick_count() - player[playerid].last_city_selection_tick < 500:
        return True
    if player[playerid].city_selection == -1:
        class_sel_go_next_city(playerid)
        return True
    if Keys & 4:
        player[playerid].has_city_selected = True
        player[playerid].text_draw_hide_for_player(
            textdraw["txt_class_sel_helper"].id
        )
        player[playerid].text_draw_hide_for_player(textdraw["ls"].id)
        player[playerid].text_draw_hide_for_player(textdraw["sf"].id)
        player[playerid].text_draw_hide_for_player(textdraw["lv"].id)
        player[playerid].toggle_spectating(False)
    if lr > 0:
        class_sel_go_next_city(playerid)
    elif lr < 0:
        class_sel_go_previous_city(playerid)

    return True


def OnPlayerText(playerid, text):
    return True


def OnPlayerRequestClass(playerid, classid):
    global player
    if is_player_npc(playerid):
        return True

    if player[playerid].has_city_selected is True:
        class_sel_setup_char_selection(playerid)
        return True
    else:
        if player[playerid].state != PLAYER_STATE_SPECTATING:
            player[playerid].spawn()  # Why?
            # Else player does not load in correctly
            # and the toggle below will disconnect the player.
            # Read the known issues on our repo wiki.
            player[playerid].toggle_spectating(1)
            player[playerid].text_draw_show(
                textdraw["txt_class_sel_helper"].id
            )
            player[playerid].city_selection = -1
    return True


def OnPlayerUpdate(playerid):
    global player
    if is_player_connected(playerid) is False:
        return False
    if is_player_npc(playerid):
        return True

    if (
        player[playerid].has_city_selected is False
        and player[playerid].state == PLAYER_STATE_SPECTATING
    ):
        class_sel_handle_city_selection(playerid)

    if player[playerid].interior != 0 and player[playerid].weapon != 0:
        player[playerid].set_armed_weapon(0)  # Fists
        return False  # No syncing until they change their weapon

    if (
        player[playerid].weapon == 38 or player[playerid].special_action == 2
    ):  # minigun and jetpack not allowed
        player[playerid].kick()
        return False
    return True
