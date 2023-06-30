from pysamp import (
    on_gamemode_init,
    on_gamemode_exit,
    set_game_mode_text,
    show_player_markers,
    show_name_tags,
    set_name_tag_draw_distance,
    enable_stunt_bonus_for_all,
    disable_interior_enter_exits,
    set_weather,
    limit_global_chat_radius,
    add_player_class,
    send_client_message,
    get_tick_count,
    )
from .spawns import *
from .funcs import load_from_file
from .vars import *
from .player import Player
from pysamp.textdraw import TextDraw
from pysamp.commands import cmd
from pysamp import callbacks
import random

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
find any bugs, you can report them on our repo; https://github.com/pysamp/PySAMP/issues
For now, enjoy the code, and good luck!
denNorske & Habecker

Re-written for PySAMP 2.1.0 by Ykpauneu
"""
################################

@on_gamemode_init
def on_ready():
    set_game_mode_text("PyLarc")
    print("-----------------------------------------------")
    print("Running Grand Larceny - by the SA-MP team\nRe-written to Python by the PySAMP Team")
    print("-----------------------------------------------")
    show_player_markers(1) # PLAYER_MARKERS_MODE_GLOBAL = 1
    show_name_tags(True)
    set_name_tag_draw_distance(40)
    enable_stunt_bonus_for_all(False)
    disable_interior_enter_exits()
    set_weather(2)
    class_selection_init_textdraws()
    add_player_class(1, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1)
    add_player_class(2, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1)
    add_player_class(47, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1)
    add_player_class(48, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1)
    add_player_class(49, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1)
    add_player_class(50, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1)
    add_player_class(51, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1)
    add_player_class(52, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1)
    add_player_class(53, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1)
    add_player_class(54, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1)
    add_player_class(55, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1)
    add_player_class(56, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1)
    add_player_class(57, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1)
    add_player_class(58, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1)
    add_player_class(68, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1)
    add_player_class(69, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1)
    add_player_class(70, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1)
    add_player_class(71, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1)
    add_player_class(72, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1)
    add_player_class(73, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1)
    add_player_class(75, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1)
    add_player_class(76, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1)
    add_player_class(78, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1)
    add_player_class(79, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1)
    add_player_class(80, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1)
    add_player_class(81, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1)
    add_player_class(82, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1)
    add_player_class(83, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1)
    add_player_class(84, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1)
    add_player_class(85, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1)
    add_player_class(87, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1)
    add_player_class(88, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1)
    add_player_class(89, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1)
    add_player_class(91, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1)
    add_player_class(92, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1)
    add_player_class(93, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1)
    add_player_class(95, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1)
    add_player_class(96, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1)
    add_player_class(97, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1)
    add_player_class(98, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1)
    add_player_class(99, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1)
    add_player_class(269, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1)
    add_player_class(270, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1)
    add_player_class(271, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1)
    add_player_class(272, 1759.0189, -1898.1260, 13.5622, 266.4503, -1, -1, -1, -1, -1, -1)
    total_vehicles_from_files = (
        load_from_file("scriptfiles/vehicles/lv_law.txt"),
        load_from_file("scriptfiles/vehicles/lv_airport.txt"),
        load_from_file("scriptfiles/vehicles/lv_gen.txt"),
        load_from_file("scriptfiles/vehicles/sf_law.txt"),
        load_from_file("scriptfiles/vehicles/sf_airport.txt"),
        load_from_file("scriptfiles/vehicles/sf_gen.txt"),
        load_from_file("scriptfiles/vehicles/ls_law.txt"),
        load_from_file("scriptfiles/vehicles/ls_airport.txt"),
        load_from_file("scriptfiles/vehicles/ls_gen_inner.txt"),
        load_from_file("scriptfiles/vehicles/ls_gen_outer.txt"),
        load_from_file("scriptfiles/vehicles/whetstone.txt"),
        load_from_file("scriptfiles/vehicles/bone.txt"),
        load_from_file("scriptfiles/vehicles/flint.txt"),
        load_from_file("scriptfiles/vehicles/tierra.txt"),
        load_from_file("scriptfiles/vehicles/red_county.txt"),
    )
    print(f"Total vehicles from files: {total_vehicles_from_files}")


@on_gamemode_exit
def on_exit():
    ...


@Player.on_connect
@Player.using_registry
def on_player_connect(player: Player):
    player.game_text("~w~Grand Larceny", 3000, 4)
    player.send_client_message(COLOR_WHITE, "Welcome to Grand Larceny")
    player.last_city_selection_tick = get_tick_count()


@Player.on_disconnect
@Player.using_registry
def on_player_disconnect(player: Player, reason: int):
    player.delete_registry(player)


@Player.on_spawn
@Player.using_registry
def on_player_spawn(player: Player):
    if player.is_npc():
        return

    randspawn = 0
    player.set_interior(0)
    player.toggle_clock(False)
    player.reset_money()
    player.give_money(30000)
    player.has_city_selected = False
    if player.city_selection == CITY_LOS_SANTOS:
        randspawn = random.randint(0, len(los_santos_spawns))
        player.set_pos(
            los_santos_spawns[randspawn][0],
            los_santos_spawns[randspawn][1],
            los_santos_spawns[randspawn][2]
        )

    if player.city_selection == CITY_SAN_FIERRO:
        randspawn = random.randint(0, len(san_fierro_spawns))
        player.set_pos(
            san_fierro_spawns[randspawn][0],
            san_fierro_spawns[randspawn][1],
            san_fierro_spawns[randspawn][2]
        )

    if player.city_selection == CITY_LAS_VENTURAS:
        randspawn = random.randint(0, len(las_venturas_spawns))
        player.set_pos(
            las_venturas_spawns[randspawn][0],
            las_venturas_spawns[randspawn][1],
            las_venturas_spawns[randspawn][2]
        )

    player.set_skill_level(0, 200)
    player.set_skill_level(1, 200)
    player.set_skill_level(2, 200)
    player.set_skill_level(3, 200)
    player.set_skill_level(4, 200)
    player.set_skill_level(5, 200)
    player.set_skill_level(6, 200)
    player.set_skill_level(7, 200)
    player.set_skill_level(8, 200)
    player.set_skill_level(9, 200)
    player.set_skill_level(10, 200)
    player.give_weapon(22, 100) # Colt 45


@Player.on_death
@Player.using_registry
def on_player_death(player: Player, killer: Player, reason: int):
    if killer.id == 65535:
        player.reset_money()

    else:
        killer.give_money(player.get_money())
        player.reset_money()


# Used to init textdraws of city names
def class_selection_init_city_names(textdraw: TextDraw):
    textdraw.use_box(False)
    textdraw.letter_size(1.25, 3.0)
    textdraw.font(0)
    textdraw.set_shadow(0)
    textdraw.set_outline(1)
    textdraw.color(4008636159)


def class_selection_init_textdraws():
    global los_santos_txd
    global san_fierro_txd
    global las_venturas_txd
    global class_helper_txd

    # Init our observer helper text display
    los_santos_txd = TextDraw.create(10.0, 380.0, "Los Santos")
    class_selection_init_city_names(los_santos_txd)

    san_fierro_txd = TextDraw.create(10.0, 380.0, "San Fierro")
    class_selection_init_city_names(san_fierro_txd)

    las_venturas_txd = TextDraw.create(10.0, 380.0, "Las Venturas")
    class_selection_init_city_names(las_venturas_txd)

    # Init our observer helper text display
    class_helper_txd = TextDraw.create(10.0, 415.0,
        "Press ~b~~k~~GO_LEFT~ ~w~or ~b~~k~~GO_RIGHT~ ~w~to switch cities.~n~ Press ~r~~k~~PED_FIREWEAPON~ ~w~to select.")
    class_helper_txd.use_box(True)
    class_helper_txd.box_color(572662459)
    class_helper_txd.letter_size(0.3, 1.0)
    class_helper_txd.text_size(400.0, 40.0)
    class_helper_txd.font(2)
    class_helper_txd.set_shadow(0)
    class_helper_txd.set_outline(1)
    class_helper_txd.background_color(255)
    class_helper_txd.color(4294967295)


def class_selection_setup_char(player: Player):
    if player.city_selection == CITY_LOS_SANTOS:
        player.set_interior(11)
        player.set_pos(508.7362, -87.4335, 998.9609)
        player.set_facing_angle(0.0)
        player.set_camera_position(508.7362, -83.4335, 998.9609)
        player.set_camera_look_at(508.7362, -87.4335, 998.9609)

    if player.city_selection == CITY_SAN_FIERRO:
        player.set_interior(3)
        player.set_pos(-2673.8381, 1399.7424, 918.3516)
        player.set_facing_angle(181.0)
        player.set_camera_position(-2673.2776, 1394.3859, 918.3516)
        player.set_camera_look_at(-2673.8381, 1399.7424, 918.3516)

    if player.city_selection == CITY_LAS_VENTURAS:
        player.set_interior(3)
        player.set_pos(49.0453, 193.2271, 1014.1797)
        player.set_facing_angle(286.25)
        player.set_camera_position(352.9164,194.5702,1014.1875)
        player.set_camera_look_at(349.0453, 193.2271, 1014.1797)


def class_selection_setup_selected_city(player: Player):
    if player.city_selection == -1:
        player.city_selection = CITY_LOS_SANTOS

    if player.city_selection == CITY_LOS_SANTOS:
        player.set_interior(0)
        player.set_camera_position(1630.6136, -2286.0298, 110.0)
        player.set_camera_look_at(1887.6034, -1682.1442, 47.6167)
        los_santos_txd.show_for_player(player)
        san_fierro_txd.hide_for_player(player)
        las_venturas_txd.hide_for_player(player)

    if player.city_selection == CITY_SAN_FIERRO:
        player.set_interior(0)
        player.set_camera_position(-1300.8754, 68.0546, 129.4823)
        player.set_camera_look_at(-1817.9412, 769.3878, 132.6589)
        los_santos_txd.hide_for_player(player)
        san_fierro_txd.show_for_player(player)
        las_venturas_txd.hide_for_player(player)

    if player.city_selection == CITY_LAS_VENTURAS:
        player.set_interior(0)
        player.set_camera_position(1310.6155, 1675.9182, 110.7390)
        player.set_camera_look_at(2285.2944, 1919.3756, 68.2275)
        los_santos_txd.hide_for_player(player)
        san_fierro_txd.hide_for_player(player)
        las_venturas_txd.show_for_player(player)


def class_selection_switch_next_city(player: Player):
    player.last_city_selection_tick = get_tick_count()
    player.city_selection += 1

    if player.city_selection > CITY_LAS_VENTURAS:
        player.city_selection = CITY_LOS_SANTOS

    player.play_sound(1052, 0.0, 0.0, 0.0)
    class_selection_setup_selected_city(player)


def class_selection_previous_next_city(player: Player):
    player.last_city_selection_tick = get_tick_count()
    player.city_selection -= 1

    if player.city_selection < CITY_LOS_SANTOS:
        player.city_selection = CITY_LAS_VENTURAS

    player.play_sound(1053, 0.0, 0.0, 0.0)
    class_selection_setup_selected_city(player)


def class_selection_handle(player: Player):
    (keys, ud, lr) = player.get_keys()
    if get_tick_count() - player.last_city_selection_tick < 500:
        return

    if player.city_selection == -1 :
        class_selection_switch_next_city(player)

    if keys & 4 :
        player.has_city_selected = True
        los_santos_txd.hide_for_player(player)
        san_fierro_txd.hide_for_player(player)
        las_venturas_txd.hide_for_player(player)
        class_helper_txd.hide_for_player(player)

        player.toggle_spectating(False)

    if lr > 0 :
        class_selection_switch_next_city(player)

    if lr < 0 :
        class_selection_previous_next_city(player)


@Player.on_text
@Player.using_registry
def on_player_text(player: Player, text: str):
    ...


@Player.on_request_class
@Player.using_registry
def on_player_request_class(player: Player, classid: int):
    if player.is_npc():
        return

    if player.has_city_selected == True:
        class_selection_setup_char(player)

    else:
        if player.get_state() != 9: # PLAYER_STATE_SPECTATING
            player.spawn() # Why?
            # Else player does not load in correctly and the toggle below will disconnect the player.
            # Read the known issues on our repo wiki.
            player.toggle_spectating(True)
            class_helper_txd.show_for_player(player)
            player.city_selection = -1


@Player.on_update
@Player.using_registry
def on_player_update(player: Player):
    if not player.is_connected():
        return

    if player.is_npc():
        return

    if player.has_city_selected == False and player.get_state() == 9:
        class_selection_handle(player)

    if player.get_interior()!= 0 and player.weapon() != 0:
        player.set_armed_weapon(0) # Fists

    if player.weapon() == 38 or player.get_special_action()== 2: # Minigun and jetpack not allowed
        player.kick()
