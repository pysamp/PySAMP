from pysamp import (
    attach_camera_to_player_object,
    edit_player_object,
    create_player_object,
    attach_player_object_to_player,
    attach_player_object_to_vehicle,
    set_player_object_pos,
    get_player_object_pos,
    set_player_object_rot,
    get_player_object_rot,
    get_player_object_model,
    set_player_object_no_camera_col,
    is_valid_player_object,
    destroy_player_object,
    move_player_object,
    stop_player_object,
    is_player_object_moving,
    set_player_object_material,
    set_player_object_material_text
)


class PlayerObject:
    """Create, modify and remove Player Objects using this class.

    Player Objects are almost same as normal objects, except for that they
    are only shown for the player they are created for.

    Situations you can consider objects like these, are to preview things for
    a player, maybe while they are adjusting said thing. Could be used for
    custom gate systems, where you only want the player to see what they are
    working on. Or race in systems if you want to show an object for a player
    in a checkpoint or so.

    .. note:: Please note that the global object limit still applies to player
        object.
    """
    def __init__(self, id: int):
        self.id = id

    @classmethod
    def create(
        cls,
        player: "Player",
        model_id: int,
        x: float,
        y: float,
        z: float,
        rotation_x: float,
        rotation_y: float,
        rotation_z: float,
        draw_distance: float
    ) -> "PlayerObject":
        """Create a player object.

        :param Player player: The player that should have an object created.
        :param int model_id: Which model of the object to create.
        :param float x: The world x-coordinate to create the object at.
        :param float y: The world y-coordinate to create the object at.
        :param float z: The world z-coordinate to create the object at.
        :param float rotation_x: X-axis rotation of the object.
        :param float rotation_y: Y-axis rotation of the object.
        :param float rotation_z: Z-axis rotation of the object.
        :param optional float draw_distance: The distance at which the object 
            should start being visible at.
        """
        return cls(create_player_object(
            player.id,
            model_id,
            x,
            y,
            z,
            rotation_x,
            rotation_y,
            rotation_z,
            draw_distance
        ))

from pysamp.player import Player  # noqa