from pysamp import (
    attach_camera_to_player_object,
    edit_player_object,
    create_player_object,
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
    def __init__(self, id: int, player: "Player"):
        self.id = id
        self.player = player

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
        :returns: An instance of :class:`~PlayerObject`.

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
        ), player)

    def attach_to_vehicle(
        self,
        vehicle: "Vehicle",
        offset_x: float,
        offset_y: float,
        offset_z: float,
        rotation_x: float,
        rotation_y: float,
        rotation_z: float
    ) -> bool:
        """Attach the player object to a vehicle.

        :param Vehicle vehicle: The vehicle to attach the player object to.
        :param float offset_x: X-coordinate relative to car center.
        :param float offset_y: Y-coordinate relative to car center.
        :param float offset_z: Z-coordinate relative to car center.
        :param float rotation_x: X-axis rotation of the object.
        :param float rotation_y: Y-axis rotation of the object.
        :param float rotation_z: Z-axis rotation of the object.
        :returns: No return value.

        .. note:: You need to create the object before attaching it.
            If you are calling this method after :meth:`~set_material_text`
            you most likely will lose the text. Call this method first, then
            call :meth:`~set_material_text` after to circumvent it.
        """
        return attach_player_object_to_vehicle(
            self.player.id,
            self.id,
            vehicle.id,
            offset_x,
            offset_y,
            offset_z,
            rotation_x,
            rotation_y,
            rotation_z,
        )

    def set_material_text(
        self,
        text: str,
        material_index: int,
        material_size: int,
        font_face: str,
        font_size: int,
        bold: bool,
        font_color: int,
        back_color: int,
        text_alignment: int
    ) -> bool:
        """Replace the texture of a player object with text.

        :param str text: The text to set. Max 2048 characters.
        :param optional int material_index: The material index to replace with
            text. Default is 0. Valid values are 0-15.
        :param optional int material_size: The size of the material.
            Default size is 256x128. See table below for all possible values.
        :param optional str font_face: The font to use. Default is "Arial".
        :param optional int font_size: The size of the font. Default is 24.
        :param optional bool bold: Whether the text should be bold or not.
        :param optional int font_color: The color of the text.
            Default is white (-1).
        :param optional int back_color: The background color.
            Default is transparent.
        :param optional int text_alignment: The alignment of the text. Can be
            0 (left), 1 (center) or 2 (right). Default value is 0.
        :returns: No return value.

        .. list-table:: material_size's for :meth:`set_material_text`.
            :widths: 30 25
            :header-rows: 1

            * - Constant
              - Value as integer
            * - OBJECT_MATERIAL_SIZE_32x32
              - 10
            * - OBJECT_MATERIAL_SIZE_64x32
              - 20
            * - OBJECT_MATERIAL_SIZE_64x64
              - 30
            * - OBJECT_MATERIAL_SIZE_128x32
              - 40
            * - OBJECT_MATERIAL_SIZE_128x64
              - 50
            * - OBJECT_MATERIAL_SIZE_128x128
              - 60
            * - OBJECT_MATERIAL_SIZE_256x32
              - 70
            * - OBJECT_MATERIAL_SIZE_256x64
              - 80
            * - OBJECT_MATERIAL_SIZE_256x128
              - 90
            * - OBJECT_MATERIAL_SIZE_256x256
              - 100
            * - OBJECT_MATERIAL_SIZE_512x64
              - 110
            * - OBJECT_MATERIAL_SIZE_512x128
              - 120
            * - OBJECT_MATERIAL_SIZE_512x256
              - 130
            * - OBJECT_MATERIAL_SIZE_512x512
              - 140

        """
        return set_player_object_material_text(
            self.player.id,
            self.id,
            text,
            material_index,
            material_size,
            font_face,
            font_size,
            bold,
            font_color,
            back_color,
            text_alignment,
        )

    def set_pos(self, x: float, y: float, z: float) -> bool:
        """Set the world coordinates of the player object

        :param float x: The world x coordinate to set.
        :param float y: The world y coordinate to set.
        :param float z: The world z coordinate to set.
        :returns: No return value.
        """

from pysamp.player import Player  # noqa
from pysamp.vehicle import Vehicle  # noqa