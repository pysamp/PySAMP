from pysamp import (
    allow_player_teleport,
    apply_animation,
    ban,
    ban_ex,
    clear_animations,
    create_explosion_for_player,
    create_player_text_draw,
    delete_pvar,
    disable_player_checkpoint,
    disable_player_race_checkpoint,
    disable_remote_vehicle_collisions,
    edit_attached_object,
    enable_player_camera_target,
    enable_stunt_bonus_for_player,
    force_class_selection,
    get_player_ammo,
    get_player_animation_index,
    get_player_armour,
    get_player_camera_aspect_ratio,
    get_player_camera_front_vector,
    get_player_camera_mode,
    get_player_camera_pos,
    get_player_camera_target_actor,
    get_player_camera_target_object,
    get_player_camera_target_player,
    get_player_camera_target_vehicle,
    get_player_camera_zoom,
    get_player_color,
    get_player_distance_from_point,
    get_player_drunk_level,
    get_player_facing_angle,
    get_player_fighting_style,
    get_player_health,
    get_player_interior,
    get_player_ip,
    get_player_keys,
    get_player_last_shot_vectors,
    get_player_menu,
    get_player_money,
    get_player_name,
    get_player_ping,
    get_player_pos,
    get_player_score,
    get_player_skin,
    get_player_special_action,
    get_player_state,
    get_player_surfing_object_id,
    get_player_surfing_vehicle_id,
    get_player_target_actor,
    get_player_target_player,
    get_player_team,
    get_player_time,
    get_player_vehicle_id,
    get_player_vehicle_seat,
    get_player_velocity,
    get_player_version,
    get_player_virtual_world,
    get_player_wanted_level,
    get_player_weapon,
    get_player_weapon_data,
    get_player_weapon_state,
    get_pvar_float,
    get_pvar_int,
    get_pvar_name_at_index,
    get_pvar_string,
    get_pvar_type,
    get_pvars_upper_index,
    give_player_money,
    give_player_weapon,
    interpolate_camera_look_at,
    interpolate_camera_pos,
    is_player_admin,
    is_player_attached_object_slot_used,
    is_player_connected,
    is_player_in_any_vehicle,
    is_player_in_checkpoint,
    is_player_in_race_checkpoint,
    is_player_in_range_of_point,
    is_player_in_vehicle,
    is_player_npc,
    is_player_streamed_in,
    kick,
    play_audio_stream_for_player,
    play_crime_report_for_player,
    player_play_sound,
    player_spectate_player,
    player_spectate_vehicle,
    player_text_draw_alignment,
    player_text_draw_background_color,
    player_text_draw_box_color,
    player_text_draw_color,
    player_text_draw_destroy,
    player_text_draw_font,
    player_text_draw_hide,
    player_text_draw_letter_size,
    player_text_draw_set_outline,
    player_text_draw_set_preview_model,
    player_text_draw_set_preview_rot,
    player_text_draw_set_preview_veh_col,
    player_text_draw_set_proportional,
    player_text_draw_set_selectable,
    player_text_draw_set_shadow,
    player_text_draw_set_string,
    player_text_draw_show,
    player_text_draw_text_size,
    player_text_draw_use_box,
    put_player_in_vehicle,
    remove_building_for_player,
    remove_player_attached_object,
    remove_player_from_vehicle,
    remove_player_map_icon,
    reset_player_money,
    reset_player_weapons,
    select_object,
    select_text_draw,
    send_client_message,
    send_client_message_to_all,
    send_death_message,
    send_death_message_to_player,
    send_player_message_to_all,
    send_player_message_to_player,
    set_camera_behind_player,
    set_player_ammo,
    set_player_armed_weapon,
    set_player_armour,
    set_player_attached_object,
    set_player_camera_look_at,
    set_player_camera_pos,
    set_player_chat_bubble,
    set_player_checkpoint,
    set_player_color,
    set_player_drunk_level,
    set_player_facing_angle,
    set_player_fighting_style,
    set_player_health,
    set_player_interior,
    set_player_map_icon,
    set_player_marker_for_player,
    set_player_name,
    set_player_pos,
    set_player_pos_find_z,
    set_player_race_checkpoint,
    set_player_score,
    set_player_shop_name,
    set_player_skill_level,
    set_player_skin,
    set_player_special_action,
    set_player_team,
    set_player_time,
    set_player_velocity,
    set_player_virtual_world,
    set_player_wanted_level,
    set_player_weather,
    set_player_world_bounds,
    set_pvar_float,
    set_pvar_int,
    set_pvar_string,
    set_spawn_info,
    show_player_dialog,
    show_player_name_tag_for_player,
    spawn_player,
    start_recording_player_data,
    stop_audio_stream_for_player,
    stop_recording_player_data,
    toggle_player_clock,
    toggle_player_controllable,
    toggle_player_spectating,
    INVALID_PLAYER_ID,
    INVALID_VEHICLE_ID,
    MAPICON_LOCAL,
    CAMERA_CUT,
    SPECTATE_MODE_NORMAL
)


class Player:
    """Class to interact with players that are online.

    A player is a client controlled character inside the server.
    The characters that are not controlled by a player are called non-player
    characters (NPCs), and are found in the ``Actor`` class.
    """

    def __init__(self, playerid):
        self.id: int = playerid

    def set_spawn_info(
        self,
        team: int,
        skin: int,
        x: float,
        y: float,
        z: float,
        rotation,
        weapon1: int,
        weapon1_ammo: int,
        weapon2: int,
        weapon2_ammo: int,
        weapon3: int,
        weapon3_ammo: int,
    ) -> bool:
        """This method can be used to change the spawn information of a
        specific player.

        It allows you to automatically set someone's weapons to spawn with,
        their team, skin and spawn position, normally used for things like
        minigames or automatic-spawn systems.
        This information is used after a player dies, to know where / how
        to spawn them.
        """
        return set_spawn_info(
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

    def get_id(self) -> int:
        """Get the player's player id."""
        return self.id

    def spawn(self) -> bool:
        """(Re)Spawns a player.

        .. note:: Kills the player if they are in a vehicle and then they spawn
            with a bottle in their hand.
        """
        return spawn_player(self.id)

    def set_pos_find_z(self, position: "tuple[float, float, float]") -> bool:
        """This sets the players position then adjusts the players
        z-coordinate to the nearest solid ground under the position.

        This function does not work if the new coordinates are far away
        from where the player currently is. The Z height will then be 0,
        which will likely put them underground.
        """
        try:
            x, y, z = position
        except:
            raise ValueError("Expected a tuple for pos. (x, y, z)")
        else:
            return set_player_pos_find_z(self.id, x, y, z)

    def get_pos(self) -> "tuple[float, float, float]":
        """Get the position of the player."""
        return get_player_pos(self.id)

    def set_pos(self, pos: "tuple[float, float, float]") -> bool:
        """Set the player's position"""
        try:
            x, y, z = pos
        except:
            raise ValueError("Expected a tuple for pos. (x, y, z)")
        else:
            return set_player_pos(self.id, x, y, z)

    def get_facing_angle(self) -> float:
        """Get the player's facing angle."""
        return get_player_facing_angle(self.id)

    def set_facing_angle(self, angle: float) -> bool:
        """Set the player's facing angle (0.0-359.9)"""
        return set_player_facing_angle(self.id, angle)

    def is_in_range_of_point(self, range: float, x: float, y: float, z: float) -> bool:
        """Checks if the player is in range of a point"""
        return is_player_in_range_of_point(self.id, range, x, y, z)

    def distance_from_point(self, x: float, y: float, z: float) -> float:
        """Calculate the distance between the player and a map coordinate."""
        return get_player_distance_from_point(self.id, x, y, z)

    def is_streamed_in(self, player: "Player") -> bool:
        """Checks if the player is streamed in on another player's client."""
        return is_player_streamed_in(self.id, player.id)

    def get_interior(self) -> int:
        """Get the player's interior. Normal world is in interior 0.

        A list of currently known interiors and their positions can be found here:

        https://open.mp/docs/scripting/resources/interiorids

        The interior is a positive integer.

        """
        return get_player_interior(self.id)

    def set_interior(self, interior_id: int) -> bool:
        """Set the interior the player to be in. Syncs for all players even when the player is desynced"""
        return set_player_interior(self.id, interior_id)

    def get_health(self) -> float:
        """Get the player's health."""
        return get_player_health(self.id)

    def set_health(self, health: float) -> bool:
        return set_player_health(self.id, health)

    def get_armour(self) -> float:
        """Get the player's armour.

        Value is a float between `0.0` and `100.0`.
        """
        return get_player_armour(self.id)

    def set_armour(self, armour: float) -> bool:
        return set_player_armour(self.id, armour)

    def get_ammo(self) -> int:
        """Get the amount of ammo in the player's current weapon."""
        return get_player_ammo(self.id)

    def set_ammo(self, conf: tuple) -> bool:
        """Set ammo for a weapon id. Value should be an int between 0 and 32766."""
        try:
            weaponid, ammo = conf
        except:
            raise ValueError("Expected a tuple for ammo: (weaponid, ammo)")
        else:
            return set_player_ammo(self.id, weaponid, ammo)

    def get_weapon_state(self) -> int:  # PS - this is a test docstring w/rst!
        """Check the state of the player's weapon.

        * - ID
            - Constant
            - Description
        * - -1
            - WEAPONSTATE_UNKNOWN
            - Unknown (Set when in a vehicle)
        * - 0
            - WEAPONSTATE_NO_BULLETS
            - The weapon has no remaining ammo
        * - 1
            - WEAPONSTATE_LAST_BULLET
            - The weapon has one remaining bullet
        * - 2
            - WEAPONSTATE_MORE_BULLETS
            - The weapon has multiple bullets
        * - 3
            - WEAPONSTATE_RELOADING
            - he player is reloading their weapon

        Example:

        .. code-block:: python
            if player.weapon_state = WEAPONSTATE_LAST_BULLET:
                player.send_client_message(-1, "You only have 1 bullet left!")
        """
        return get_player_weapon_state(self.id)

    def get_target_player(self) -> int:
        """Check who the player is aiming at. Returns the playerid"""
        return get_player_target_player(self.id)

    def get_target_actor(self) -> int:
        """Get which actor that the player is currently aiming at."""
        return get_player_target_actor(self.id)

    def get_team(self) -> int:
        """Get the player's team ID.

        -  0-254  are valid teams
        -  255 is defined as NO_TEAM. The player is not on any team `(default)`
        - -1 is returned if something went wrong reading the value.

        """
        return get_player_team(self.id)

    def set_team(self, teamid: int) -> bool:
        """Set the team the player should belong to.
        
        0-254 are valid teams. 255 is defined as NO_TEAM.
        That means you need to set team to 255 to remove from a team.
        """
        return set_player_team(self.id, teamid)

    def get_score(self) -> int:
        """Get the player's score."""
        return get_player_score(self.id)

    def set_score(self, score: int) -> bool:
        """Set the player's score to a given value."""
        return set_player_score(self.id, score)

    def get_drunk_level(self) -> int:
        """Get the player's drunk level.

        - 0 to 2000 - No visible effect
        - 2001 to 5000 - Visible camera swaying and control issues\
            in vehicles. HUD is visible.
        - 5001 and above - Swaying continues, but HUD becomes invisible.

        .. note:: Drunk level with decrease with player fps.
            If you have 50 fps, the drunk level will decrease with 50 levels
            per second. This makes this method very useful to determine user
            FPS from server side.

        More information:
        https://open.mp/docs/scripting/functions/SetPlayerDrunkLevel
        """
        return get_player_drunk_level(self.id)

    def set_drunk_level(self, level: int) -> bool:
        """Set the player's drunk level.

        - 0 to 2000 - No visible effect
        - 2001 to 5000 - Visible camera swaying and control issues
        in vehicles. HUD is visible.
        - 5001 and above - Swaying continues, but HUD becomes invisible.
        """
        return set_player_drunk_level(self.id, level)

    def get_color(self) -> int:
        """Get the player's color.

        .. note:: If you try to read the value before it is set, it will 
            return 0 (Black).
        """
        return get_player_color(self.id)

    def set_color(self, color: int) -> bool:
        """Set a player's color to a given `color` value.

        You can use Hexadecimal numbers to make it easier. The value is
        expected in the following format ``0xRRGGBBAA``,
        where:
            - ``RR`` is red
            - ``GG`` is green
            - ``BB`` is blue
            - ``AA`` is the opacity.
        """
        return set_player_color(self.id, color)

    def get_skin(self) -> int:
        """Get or set the player's skin, as an int.

        A skin is the character model.
        """
        return get_player_skin(self.id)

    def set_skin(self, skinid: int) -> bool:
        """Change the skin/character of the player.

        See available skins and the corresponding ID's here:
        https://open.mp/docs/scripting/resources/skins

        ``skinid`` can be between 0 and 311*.

        .. warning:: Skin ID 74 is not available.

        Known Bugs: If a player's skin is set when they are crouching,
        in a vehicle, or performing certain animations, they will become frozen
        or otherwise glitched. This can (in most cases) be fixed by using
        ``player.toggle_controllable(1)``.

        Players can be detected as being crouched through
        ``player.get_special_action() == SPECIAL_ACTION_DUCK``

        Other players around the player may crash if they are in a vehicle or
        if he is entering/leaving a vehicle when the skin is changed.
        Setting a player's skin when the player is dead may crash players 
        around them. Breaks the sitting animation on bikes.

        Example:

        .. code-block:: python

            player.set_skin(45)

        """
        return set_player_skin(self.id, skinid)

    def give_weapon(self, weapon_id: int, ammo: int) -> bool:
        """Give the player a weapon with specified amount of ammo.

        See all weapon ID's here:
        https://open.mp/docs/scripting/resources/weaponids

        Also, notice how you can use the constants as in pawn too, to define
        the weapon.

        .. code-block:: python

            player.give_weapon(6, 1)  # Give a shovel
            player.give_weapon(WEAPON_COLT45, 500)  # Give a Colt45 with 500 bullets
        """
        return give_player_weapon(self.id, weapon_id, ammo)

    def reset_weapons(self) -> bool:
        """Removes all weapons from a player."""
        return reset_player_weapons(self.id)

    def set_armed_weapon(self, weapon_id: int) -> bool:
        """Sets which weapon the player is holding.

        The player needs to have this weapon for it to work.
        Calling this method will not give the player a new weapon.
        """
        return set_player_armed_weapon(self.id, weapon_id)

    def get_weapon_data(self, slot: int) -> "tuple[int, int]":
        """Get weapon data on a given slot.

        The weapon slot can be 0-13.
        The tuple returned contains `weapon, ammo`.

        Example:

        .. code-block:: python

            weapon, ammo = player.get_weapon_data(3)  # Get data in slot 3
            print(f"Weapon ID: {weapon} || Ammo: {ammo}")

        """
        return get_player_weapon_data(self.id, slot)

    def give_money(self, money: int) -> bool:
        """Give money or take money from a player

        The amount of money you want to give can be negative to reduce money.

        Example:

        .. code-block:: python
            player.give_money(1000)  # Give player $1000

        """
        return give_player_money(self.id, money)

    def reset_money(self) -> bool:
        """Use this method to reset player money to 0`."""
        return reset_player_money(self.id)

    def get_name(self) -> str:
        """Get the player's name."""
        return get_player_name(self.id)

    def set_name(self, name: str) -> int:
        """Set a new name for the player.

        Name needs to be less than 25 characters long, and should not contain
        invalid characters.
        """
        return set_player_name(self.id, name)

    def get_money(self) -> int:
        """Get the player's money."""
        return get_player_money(self.id)

    def set_money(self, money: int) -> bool:
        """Set the money a player should have.

        Negative numbers will be shown as red on the HUD.

        Behind the scenes, setting money will first do ``reset_money`` and then
        ``give_money``.
        """
        reset_player_money(self.id)
        return give_player_money(self.id, money)

    def get_state(self) -> int:
        """Get the current player state.

        https://open.mp/docs/scripting/resources/playerstates for more info.
        """
        return get_player_state(self.id)

    def get_ip(self) -> str:
        """Get the player's IP Address."""
        return get_player_ip(self.id)

    def get_ping(self) -> int:
        """Get the player latency to server, represented in milliseconds."""
        return get_player_ping(self.id)

    def weapon(self) -> int:
        """Get the weapon id of the currently held weapon.

        When the player state is PLAYER_STATE_DRIVER or PLAYER_STATE_PASSENGER,
        this function returns the weapon held by the player before they entered
        the vehicle.
        """
        return get_player_weapon(self.id)

    def get_keys(self) -> "tuple[int, int, int]":
        """Check which keys a player is pressing.

        See all keys here: https://sampwiki.blast.hk/wiki/Keys

        This method returns a Tuple with 3 values. It looks like this:
        ``(keys, updown, leftright)``

            - keys: A set of bits containing the player's key states (bitmask)
            - updown: Up/down state.
            - leftright: Left/right state.

        Only the FUNCTION of keys can be detected; not the actual keys.
        For example, it is not possible to detect if a player presses SPACE,
        but you can detect if they press SPRINT (which can be mapped
        (assigned/binded) to ANY key (but is space by default)).

        As of update 0.3.7, the keys "A" and "D" are not recognized when in
        a vehicle. However, keys "W" and "S" can be detected with the "keys"
        parameter.

        """
        return get_player_keys(self.id)

    def get_time(self) -> "tuple[int, int]":
        """Get the player's game time.

        Value is represented as a tuple with two values: `hour, minute`
        """
        return get_player_time(self.id)

    def set_time(self, time: tuple) -> bool:
        try:
            hour, minute = time
        except ValueError:
            raise ValueError("Expected a tuple for time: (hour, minute)")
        else:
            return set_player_time(self.id, hour, minute)

    def toggle_clock(self, toggle: bool) -> bool:
        """Toggle the in-game clock (top-right corner) for a specific player.

        When this is enabled, time will progress at 1 minute per second.
        Weather will also interpolate (slowly change over time) when set using
        `Player.set_weather()`
        """
        return toggle_player_clock(self.id, toggle)

    def set_weather(self, weather: int) -> bool:
        """Set the player's weather. 
        
        If player.toggle_clock is on, then the weather will change slowly too.

            - weather: The weather ID to set between 0 and 20.

        .. list-table:: Available weather IDs
            :widths: 30 30 30
            :header-rows: 1

            *  - ID
               - Constant name
               - Comments
            *  - 0
               - EXTRASUNNY_LA
               -
            *  - 1
               - SUNNY_LA
               -
            *  - 2
               - EXTRASUNNY_SMOG_LA
               -
            *  - 3
               - SUNNY_SMOG_LA
               -
            *  - 4
               - CLOUDY_LA
               -
            *  - 5
               - SUNNY_SF
               -
            *  - 6
               - EXTRASUNNY_SF
               -
            *  - 7
               - CLOUDY_SF
               -
            *  - 8
               - RAINY_SF
               -
            *  - 9
               - FOGGY_SF
               -
            *  - 10
               - SUNNY_VEGAS
               -
            *  - 11
               - EXTRASUNNY_VEGAS 
               - Has heat wave effect
            *  - 12
               - CLOUDY_VEGAS
               -
            *  - 13
               - EXTRASUNNY_COUNTRYSIDE
               -
            *  - 14
               - SUNNY_COUNTRYSIDE
               -
            *  - 15
               - CLOUDY_COUNTRYSIDE
               -
            *  - 16
               - RAINY_COUNTRYSIDE
               -
            *  - 17
               - EXTRASUNNY_DESERT
               -
            *  - 18
               - SUNNY_DESERT
               -
            *  - 19
               - SANDSTORM_DESERT
               -
            *  - 20
               - UNDERWATER
               - greenish, foggy effect

        More information and details:
        https://dev.prineside.com/en/gtasa_weather_id/

        To set weather for everyone, use ``set_weather(weatherid)`` which is a
        global function.
        """
        return set_player_weather(self.id, weather)

    def force_class_selection(self) -> bool:
        """Forces a player to go back to class selection on next spawn.

        .. note:: You can quickly get the player into class selection by
            toggling spectating on and then off. Will not perform a state
            change to ``PLAYER_STATE_WASTED`` if the spectate toggle method
            is used.
        """
        return force_class_selection(self.id)

    def get_wanted_level(self) -> int:
        """Get the player's wanted level."""
        return get_player_wanted_level(self.id)

    def set_wanted_level(self, level: int) -> bool:
        """Set the player's wanted level."""
        return set_player_wanted_level(self.id, level)

    def get_fighting_style(self) -> int:
        """Get the player's special fighting style."""
        return get_player_fighting_style(self.id)

    def set_fighting_style(self, style: int) -> bool:
        """Set the player's fighting style.

        To use in-game, aim and press the 'secondary attack' key
        (ENTER by default).

        Available Values:

            - 4 - FIGHT_STYLE_NORMAL
            - 5 - FIGHT_STYLE_BOXING
            - 6 - FIGHT_STYLE_KUNGFU
            - 7 - FIGHT_STYLE_KNEEHEAD
            - 15 - FIGHT_STYLE_GRABKICK
            - 16 - FIGHT_STYLE_ELBOW
        """
        return set_player_fighting_style(self.id, style)

    def get_velocity(self) -> "tuple[float, float, float]":
        """Get the velocity of the player."""
        return get_player_velocity(self.id)

    def set_velocity(self, pos: "tuple[float, float, float]") -> bool:
        """Set the velocity of a player in X,Y,Z direction."""
        try:
            x, y, z = pos
        except ValueError:
            raise ValueError("Expected a tuple for velocity: (x, y, z).")
        else:
            return set_player_velocity(self.id, x, y, z)

    def play_crime_report(self, suspect: 'Player', crime: int) -> bool:
        """Plays a crime report for the player.

        You know when the player gets wanted in single player,
        the dispatch on the radio reads out actions and positions.
        You can also do this on SA-MP, by calling this method.

        .. list-table:: Parameters
            :widths: 30 30
            :header-rows: 1

            *  - Parameter
               - Description
            *  - suspect
               - The player you want to play the crime report for
            *  - crime
               - One of the available crime ID's in below table.

        .. list-table:: Crime ID's
            :widths: 30 30 30
            :header-rows: 1

            * - Crime id
              - 10-code that is used
              - Message from dispatcher
            * - 3
              - 10-71
              - Advise nature of fire (size, type, contents of building)
            * - 4
              - 10-47
              - Emergency road repairs needed
            * - 5
              - 10-81
              - Breatherlizer Report
            * - 6
              - 10-24
              - Assignment Completed
            * - 7
              - 10-21
              - Call () by phone
            * - 8
              - 10-21
              - Call () by phone
            * - 9
              - 10-21
              - Call () by phone
            * - 10
              - 10-17
              - Meet Complainant
            * - 11
              - 10-81
              - Breatherlizer Report
            * - 12
              - 10-91
              - Pick up prisoner/subject
            * - 13
              - 10-28
              - Vehicle registration information
            * - 14
              - 10-81
              - Breathalyzer
            * - 15
              - 10-28
              - Vehicle registration information
            * - 16
              - 10-91
              - Pick up prisoner/subject
            * - 17
              - 10-34
              - Riot
            * - 18
              - 10-37
              - (Investigate) suspicious vehicle
            * - 19
              - 10-81
              - Breathalyzer
            * - 21
              - 10-7
              - Out of service
            * - 22
              - 10-7
              - Out of service
        """
        return play_crime_report_for_player(self.id, suspect.get_id(), crime)

    def play_audio_stream(
        self,
        url: str,
        position_x: float = 0.0,
        position_y: float = 0.0,
        position_z: float = 0.0,
        distance: float = 50.0,
        usepos: bool = False
    ) -> bool:
        """Play an audio stream for a player.

        Normal files can also be streamed, such as MP3.
        """
        return play_audio_stream_for_player(
            self.id,
            url,
            position_x,
            position_y,
            position_z,
            distance,
            usepos
        )

    def stop_audio_stream(self) -> bool:
        """Stops the player's audio stream."""
        return stop_audio_stream_for_player(self.id)

    def set_shop_name(self, shop_name: str) -> bool:
        """Loads or unloads an interior script for a player.

        This can for example be the ammunation menu, that belongs to the
        ammunition interior.

        Learn more here:
        https://sampwiki.blast.hk/wiki/ShopNames
        """
        return set_player_shop_name(self.id, shop_name)

    def set_skill_level(self, weapon_skill: int, level: int) -> bool:
        """Set the skill level of a certain weapon type for a player.

        .. list-table:: Parameters
            :widths: 15 30
            :header-rows: 1

            * - Parameter
              - Description
            * - weapon_skill
              - The weapon to set skill on (see below table)
            * - level
              - The level, range 0-999 where 999 is max skill

        ``weapon_skill`` available values:

        .. list-table:: Weapon skills
            :widths: 10 30
            :header-rows: 1

            * - ID
              - Constant
            * - 0
              - WEAPONSKILL_PISTOL
            * - 1
              - WEAPONSKILL_PISTOL_SILENCED
            * - 2
              - WEAPONSKILL_DESERT_EAGLE
            * - 3
              - WEAPONSKILL_SHOTGUN
            * - 4
              - WEAPONSKILL_SAWNOFF_SHOTGUN
            * - 5
              - WEAPONSKILL_SPAS12_SHOTGUN
            * - 6
              - WEAPONSKILL_MICRO_UZI
            * - 7
              - WEAPONSKILL_MP5
            * - 8
              - WEAPONSKILL_AK47
            * - 9
              - WEAPONSKILL_M4
            * - 10
              - WEAPONSKILL_SNIPERRIFLE
        """
        return set_player_skill_level(self.id, weapon_skill, level)

    def get_surfing_vehicle_id(self) -> int:
        # TODO: Make it return a vehicle instance
        """Get which vehicle the player is standing on.

        Can return `INVALID_VEHICLE_ID` if there's no driver in the car.

        https://open.mp/docs/scripting/functions/GetPlayerSurfingVehicleID for
        more information.
        """
        return get_player_surfing_vehicle_id(self.id)

    def get_surfing_object_id(self) -> int:
        # TODO: Return an object instance
        """Get which MOVING object the player is standing on.

        https://open.mp/docs/scripting/functions/GetPlayerSurfingObjectID for
        more information.
        """
        return get_player_surfing_object_id(self.id)

    def remove_building(
        self,
        model_id: int,
        x: float,
        y: float,
        z: float,
        radius: float
    ) -> bool:
        """Removes a standard San Andreas model for a single player within a
        specified range.

        .. list-table:: Parameters
            :widths: 30 25
            :header-rows: 1

            * - Parameter
              - Desccription
            * - model_id
              - The model to remove.
            * - Float:fX
              - The X coordinate around which the objects will be removed.
            * - Float:fY
              - The Y coordinate around which the objects will be removed.
            * - Float:fZ
              - The Z coordinate around which the objects will be removed.
            * - Float:fRadius
              - The radius around the specified point to remove objects with\
                the specified model.

        .. warning::
            - There appears to be a limit of around 1000 lines/objects.\
            There is no workaround.
            - When removing the same object for a player, they will crash.
            - Commonly, players crash when *re-connecting* to the server\
                because the server removes buildings on ``OnPlayerConnect``.

        Example usage:

        .. code-block:: python

            # This will remove ALL map objects for the player:
            player.remove_building(-1, 0.0, 0.0, 0.0, 6000.0)

        """
        return remove_building_for_player(self.id, model_id, x, y, z, radius)

    def get_last_shot_vectors(
        self
    ) -> "tuple[float, float, float, float, float, float]":
        """Find out from where a bullet was shot, and where it hit/collided.

        The values are returned as a tuple, listed in the following table:

        .. note:: This function will only work when lag compensation is
            enabled. If the player hit nothing, the hit positions will be 0.
            This means you can't currently calculate how far a bullet travels
            through open air.

        .. list-table:: Return values (in order)
            :widths: 30 30
            :header-rows: 1

            * - Return parameter
              - Description
            * - From X
              - X coordinate of where the bullet originated from.
            * - From Y
              - Y coordinate of where the bullet originated from.
            * - From Z
              - Z coordinate of where the bullet originated from.
            * - Hit X
              - X coordinate of where the bullet hit.
            * - Hit Y
              - Y coordinate of where the bullet hit.
            * - Hit Z
              - Z coordinate of where the bullet hit.

        Here is an example of how you can use it:

        .. code-block:: python

            if "/lastshot" in cmdtext[0:9]:
                # Get the coordinates
                (
                    x,
                    y,
                    z,
                    to_x,
                    to_y,
                    to_y
                ) = player.get_last_shot_vectors()

                # Send them to the player
                player.send_client_message(
                    -1,
                    "Last shot info: {}, {}, {}.Hit pos: {}, {}, {}".format(
                        str(x),
                        str(y),
                        str(z),
                        str(to_x),
                        str(to_y),
                        str(to_y)
                    )
                )

        """
        return get_player_last_shot_vectors(self.id)

    def set_attached_object(
        self,
        index: int,
        model_id: int,
        bone: int,
        offset_x: float = 0.0,
        offset_y: float = 0.0,
        offset_z: float = 0.0,
        rotation_x: float = 0.0,
        rotation_y: float = 0.0,
        rotation_z: float = 0.0,
        scale_x: float = 1.0,
        scale_y: float = 1.0,
        scale_z: float = 1.0,
        material_color_1: int = 0,
        material_color_2: int = 0,
    ) -> bool:
        """Attach an object to a specific bone on a player.

        .. list-table:: Parameters
            :widths: 30 25
            :header-rows: 1

            * - Parameter
              - Description
            * - index
              - The index (slot) to assign the object to (0-9).
            * - model_id
              - The model to attach.
            * - bone
              - The bone to attach the object to. (0-18)
            * - offset_x
              - (optional) X axis offset for the object position.
            * - offset_y
              - (optional) Y axis offset for the object position.
            * - offset_z
              - (optional) Z axis offset for the object position.
            * - rotation_x
              - (optional) X axis rotation of the object.
            * - rotation_y
              - (optional) Y axis rotation of the object.
            * - rotation_z
              - (optional) Z axis rotation of the object.
            * - scale_x
              - (optional) X axis scale of the object.
            * - scale_y
              - (optional) Y axis scale of the object.
            * - scale_z
              - (optional) Z axis scale of the object.
            * - material_color_1
              - (optional) The first object color to set, as an integer or hex in ARGB color format.
            * - material_color_2
              - (optional) The second object color to set, as an integer or hex in ARGB color format


        Available bones:

        .. list-table:: Parameters
            :widths: 30 25
            :header-rows: 1

            * - ID
              - Bodypart
            * - 1
              - Spine
            * - 2
              - Head
            * - 3
              - Left upper arm
            * - 4
              - Right upper arm
            * - 5
              - Left hand
            * - 6
              - Right hand
            * - 7
              - Left thigh
            * - 8
              - Right thigh
            * - 9
              - Left foot
            * - 10
              - Right foot
            * - 11
              - Right calf
            * - 12
              - Left calf
            * - 13
              - Left forearm
            * - 14
              - Right forearm
            * - 15
              - Left clavicle (shoulder)
            * - 16
              - Right clavicle (shoulder)
            * - 17
              - Neck
            * - 18
              - Jaw

        Example:

        .. code-block:: python

            # Give player a white hat, and paint it green
            player.set_attached_object(3, 19487, 2, 0.101, -0.0, 0.0, 5.50, 84.60, 83.7, 1.0, 1.0, 1.0, 0xFF00FF00)
        """
        return set_player_attached_object(
            self.id,
            index,
            model_id,
            bone,
            offset_x,
            offset_y,
            offset_z,
            rotation_x,
            rotation_y,
            rotation_z,
            scale_x,
            scale_y,
            scale_z,
            material_color_1,
            material_color_2,
        )

    def remove_attached_object(self, index: int) -> bool:
        """Remove an attached object from a player.

            - ``index``: The index to remove the object from (0-9)

        .. code-block:: python

            # Remove all player-attached objects
            if "/removeall" in cmdtext[0:9]:
                for slot in range(MAX_PLAYER_ATTACHED_OBJECTS) :
                    if player.is_attached_object_slot_used(slot):
                        player.remove_attached_object(slot)
        """
        return remove_player_attached_object(self.id, index)

    def is_attached_object_slot_used(self, index: int) -> bool:
        """Check if a player has an object attached in the specified index (slot).

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
        return is_player_attached_object_slot_used(self.id, index)

    def edit_attached_object(self, index: int) -> bool:
        """Enter edit mode for an attached object.

            - ``index``: The slot of the attached object to edit.

        Available slots indexes are 0 to 9.

        See more here: https://sampwiki.blast.hk/wiki/EditAttachedObject
        """
        return edit_attached_object(self.id, index)

    def get_pvar_int(self, varname):
        """| METHOD |"""
        return get_pvar_int(self.id, varname)

    def set_pvar_int(self, varname, value):
        """| METHOD |"""
        return set_pvar_int(self.id, varname, value)

    def get_pvar_string(self, varname, size):
        """| METHOD |"""
        return get_pvar_string(self.id, varname, size)

    def set_pvar_string(self, varname, value):
        """| METHOD |"""
        return set_pvar_string(self.id, varname, value)

    def get_pvar_float(self, varname):
        """| METHOD |"""
        return get_pvar_float(self.id, varname)

    def set_pvar_float(self, varname, value):
        """| METHOD |"""
        return set_pvar_float(self.id, varname, value)

    def delete_pvar(self, varname):
        """| METHOD |"""
        return delete_pvar(self.id, varname)

    def pvars_upper_index(self):
        """Get or set
        """
        return get_pvars_upper_index(self.id)

    def get_pvar_name_at_index(self, index, size):
        """| METHOD |"""
        return get_pvar_name_at_index(self.id, index, size)

    def get_pvar_type(self, varname):
        """| METHOD |"""
        return get_pvar_type(self.id, varname)

    def set_chat_bubble(self, text, color, drawdistance, expiretime):
        """| METHOD |"""
        return set_player_chat_bubble(
            self.id, text, color, drawdistance, expiretime
        )

    def put_in_vehicle(self, vehicleid, seatid):
        """| METHOD |"""
        return put_player_in_vehicle(self.id, vehicleid, seatid)

    def vehicle_id(self):
        """Get or set
        """
        return get_player_vehicle_id(self.id)

    def vehicle_seat(self):
        """Get or set
        """
        return get_player_vehicle_seat(self.id)

    def remove_from_vehicle(self):
        """| METHOD |"""
        return remove_player_from_vehicle(self.id)

    def toggle_controllable(self, toggle):
        """| METHOD |"""
        return toggle_player_controllable(self.id, toggle)

    def play_sound(self, soundid, x: float, y: float, z: float):
        """| METHOD |"""
        return player_play_sound(self.id, soundid, x, y, z)

    def apply_animation(
        self,
        animation_library: str,
        animation_name: str,
        delta: float,
        loop: bool,
        lock_x: bool,
        lock_y: bool,
        freeze: bool,
        time: int,
        force_sync: bool = False,
    ) -> bool:
        """Apply a given animation to the player."""
        return apply_animation(
            self.id,
            animation_library,
            animation_name,
            delta,
            loop,
            lock_x,
            lock_y,
            freeze,
            time,
            force_sync,
        )

    def clear_animations(self, forcesync=False):
        """| METHOD |"""
        return clear_animations(self.id, forcesync)

    def animation_index(self) -> int:
        """Get the current playing animation index of the player."""
        return get_player_animation_index(self.id)

    def get_special_action(self):
        return get_player_special_action(self.id)

    def set_special_action(self, actionid):
        return set_player_special_action(self.id, actionid)

    def disable_remote_vehicle_collisions(self, disable):
        """| METHOD |"""
        return disable_remote_vehicle_collisions(self.id, disable)

    def set_checkpoint(self, x: float, y: float, z: float, size):
        """| METHOD |"""
        return set_player_checkpoint(self.id, x, y, z, size)

    def disable_checkpoint(self):
        """| METHOD |"""
        return disable_player_checkpoint(self.id)

    def set_race_checkpoint(
        self,
        type,
        x: float,
        y: float,
        z: float,
        next_x: float,
        next_y: float,
        next_z: float,
        size: float
    ) -> bool:
        """Race checkpoints are red checkpoints, as used in singleplayer races.

        .. list-table:: Parameters
            :widths: 10 30
            :header-rows: 1

            * - Parameter
            - Description
            * - player
            - The player that should get the checkpoint set.
            * - type
            - Can be values 0-8, see table further down for reference.
            * - x
            - World X coordinate to place the race checkpoint.
            * - y
            - World Y coordinate to place the race checkpoint.
            * - z
            - World Z coordinate to place the race checkpoint.
            * - next_x
            - The X coordinate of the next race checkpoint.
            * - next_y
            - The Y coordinate of the next race checkpoint.
            * - next_z
            - The Z coordinate of the next race checkpoint.
            * - size
            - The radius of the checkpoint. Also acts as the trigger area.

        .. list-table:: The available types
            :widths: 10 30 30
            :header-rows: 1

            * - ID
            - Constant name
            - Description
            * - 0
            - RACE_NORMAL
            - Normal checkpoint with arrow to the next coordinates.
            * - 1
            - RACE_FINISH
            - Checkpoint with finish flag on it.
            * - 2
            - RACE_NOTHING
            - An empty checkpoint with nothing on it.
            * - 3
            - RACE_AIR_NORMAL
            - A normal air race checkpoint (Circle).
            * - 4
            - RACE_AIR_FINISH
            - Air checkpoint with finish flag on it.
            * - 5
            - RACE_AIR_ONE
            - Air race checkpoint that rotates and stops.
            * - 6
            - RACE_AIR_TWO
            - Air race checkpoint that increases, decreases and disappears.
            * - 7
            - RACE_AIR_THREE
            - Air race checkpoint, this type swings up and down.
            * - 8
            - RACE_AIR_FOUR
            - Air race checkpoint, swings up and down.

        .. note:: If you use ``RACE_FINISH`` and at the same time use coordinates
            for the next checkpoint, it will automatically show ``RACE_NORMAL`` 
            instead

        .. warning:: Race checkpoints are asynchronous, that means only one
            can be shown at a time.
        """
        return set_player_race_checkpoint(
            self.id, type, x, y, z, next_x, next_y, next_z, size
        )

    def disable_race_checkpoint(self) -> bool:
        """Removes the active race checkpoint for the player."""
        return disable_player_race_checkpoint(self.id)

    def set_world_bounds(self, x_max, x_min, y_max, y_min):
        """| METHOD |"""
        return set_player_world_bounds(self.id, x_max, x_min, y_max, y_min)

    def set_marker(self, showplayerid, color):
        """| METHOD |"""
        return set_player_marker_for_player(self.id, showplayerid, color)

    def show_name_tag(self, showplayerid, show):
        """| METHOD |"""
        return show_player_name_tag_for_player(self.id, showplayerid, show)

    def set_map_icon(
        self,
        iconid,
        x: float,
        y: float,
        z: float,
        markertype,
        color,
        style = MAPICON_LOCAL,
    ):
        """| METHOD |"""
        return set_player_map_icon(
            self.id, iconid, x, y, z, markertype, color, style
        )

    def remove_map_icon(self, iconid):
        """| METHOD |"""
        return remove_player_map_icon(self.id, iconid)

    def allow_teleport(self, allow):
        """Enable or disable teleporting when marking the map with the map-
        marker.
        
        .. note:: Deprecated since 0.3d
        This method is deprecated.
        Please use :obj:`Player.on_click_map()` instead.
        """
        return allow_player_teleport(self.id, allow)

    def set_camera_look_at(self, x: float, y: float, z: float, cut=CAMERA_CUT):
        """| METHOD |"""
        return set_player_camera_look_at(self.id, x, y, z, cut)

    def set_camera_behind(self):
        """| METHOD |"""
        return set_camera_behind_player(self.id)

    def camera_pos(self):
        return get_player_camera_pos(self.id)

    def camera_pos(self, pos: tuple):
        try:
            x, y, z = pos
        except:
            raise ValueError("Expected x, y, z as a tuple (x, y, z)")
        else:
            return set_player_camera_pos(self.id, x, y, z)

    def get_camera_front_vector(self):
        return get_player_camera_front_vector(self.id)

    def camera_mode(self):
        return get_player_camera_mode(self.id)

    def enable_camera_target(self, enable):
        """| METHOD |"""
        return enable_player_camera_target(self.id, enable)

    def camera_target_object(self):
        return get_player_camera_target_object(self.id)

    def camera_target_vehicle(self):
        return get_player_camera_target_vehicle(self.id)

    def camera_target(self):
        return get_player_camera_target_player(self.id)

    def camera_target_actor(self):
        return get_player_camera_target_actor(self.id)

    def camera_aspect_ratio(self):
        return get_player_camera_aspect_ratio(self.id)

    def camera_zoom(self):
        return get_player_camera_zoom(self.id)

    def attach_camera_to_object(self, objectid):
        """Attach the camera to an object.
        
        If the object moves, the camera will follow.        
        """
        return attach_camera_to_object(self.id, objectid)

    def attach_camera_to_player_object(self, playerobjectid):
        """Attach the camera to an object which is created for a player."""
        return attach_camera_to_player_object(self.id, playerobjectid)

    def interpolate_camera_pos(
        self, FromX, FromY, FromZ, ToX, ToY, ToZ, time, cut=CAMERA_CUT
    ):
        """| METHOD |"""
        return interpolate_camera_pos(
            self.id, FromX, FromY, FromZ, ToX, ToY, ToZ, time, cut
        )

    def interpolate_camera_look_at(
        self, FromX, FromY, FromZ, ToX, ToY, ToZ, time, cut=CAMERA_CUT
    ):
        """| METHOD |"""
        return interpolate_camera_look_at(
            self.id, FromX, FromY, FromZ, ToX, ToY, ToZ, time, cut
        )

    def connected(self):
        return is_player_connected(self.id)

    def is_in_vehicle(self, vehicleid):
        """| METHOD |"""
        return is_player_in_vehicle(self.id, vehicleid)

    def is_in_any_vehicle(self):
        """| METHOD |"""
        return is_player_in_any_vehicle(self.id)

    def is_in_checkpoint(self):
        """| METHOD |"""
        return is_player_in_checkpoint(self.id)

    def is_in_race_checkpoint(self) -> bool:
        """Check if the given player is inside the checkpoint."""
        return is_player_in_race_checkpoint(self.id)

    def virtual_world(self):
        return get_player_virtual_world(self.id)

    def virtual_world(self, worldid):
        return set_player_virtual_world(self.id, worldid)

    def enable_stunt_bonus(self, enable):
        """| METHOD |"""
        return enable_stunt_bonus_for_player(self.id, enable)

    def toggle_spectating(self, toggle):
        """| METHOD |"""
        return toggle_player_spectating(self.id, toggle)

    def spectate(self, targetplayerid, mode=SPECTATE_MODE_NORMAL):
        """| METHOD |"""
        return player_spectate_player(self.id, targetplayerid, mode)

    def spectate_vehicle(self, targetvehicleid, mode=SPECTATE_MODE_NORMAL):
        """| METHOD |"""
        return player_spectate_vehicle(self.id, targetvehicleid, mode)

    def start_recording_data(self, recordtype, recordname):
        """| METHOD |"""
        return start_recording_player_data(self.id, recordtype, recordname)

    def stop_recording_data(self):
        """| METHOD |"""
        return stop_recording_player_data(self.id)

    def create_explosion(self, X, Y, Z, type, Radius):
        """| METHOD |"""
        return create_explosion_for_player(self.id, X, Y, Z, type, Radius)

    def send_client_message(self, color, message):
        """| METHOD |"""
        return send_client_message(self.id, color, message)

    def send_message(self, senderid, message):
        """| METHOD |"""
        return send_player_message_to_player(self.id, senderid, message)

    def send_death_message(self, killer, killee, weapon):
        """| METHOD |"""
        return send_death_message_to_player(self.id, killer, killee, weapon)

    def game_text(self, text, time, style):
        """| METHOD |"""
        return game_text_for_player(self.id, text, time, style)

    def is_npc(self):
        return is_player_npc(self.id)

    def is_admin(self):
        return is_player_admin(self.id)

    def kick(self):
        """| METHOD |"""
        return kick(self.id)

    def ban(self):
        """| METHOD |"""
        return ban(self.id)

    def ban_ex(self, reason):
        """| METHOD |"""
        return ban_ex(self.id, reason)

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

from pysamp.vehicle import Vehicle
from pysamp.object import Object