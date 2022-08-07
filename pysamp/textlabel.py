from pysamp import (
    attach_3d_textlabel_to_player,
    attach_3d_textlabel_to_vehicle,
    create_3d_textlabel,
    delete_3d_textlabel,
    update_3d_textlabel_text,
)


class TextLabel:
    """Create and adjust 3D-Textlabels that can be attached to
    vehicles, players or world coordinates.
    """

    def __init__(
        self,
        text: str,
        color: int,
        x: float,
        y: float,
        z: float,
        draw_distance: float,
        virtual_world: int = 0,
        test_line_of_sight: bool = False
    ) -> None:
        self.text = text
        self.color = color
        self.x = x
        self.y = y
        self.z = z
        self.draw_distance = draw_distance
        self.virtual_world = virtual_world
        self.test_line_of_sight = test_line_of_sight
        self.id = create_3d_textlabel(
            self.text,
            self.color,
            self.x,
            self.y,
            self.z,
            self.draw_distance,
            self.virtual_world,
            self.test_line_of_sight
        )

    def delete(self) -> bool:
        """Deletes a 3D text label.

        :return: This method does not return any value.
        """
        return delete_3d_textlabel(self.id)

    def attach_to_player(
            self,
            player: "Player",
            offset_x: float,
            offset_y: float,
            offset_z: float
    ) -> bool:
        """Attach a 3D Textlabel to a player.

        :param Player player: The player to attach to.
        :param float offset_x: The relative X coordinate offset on the player.
        :param float offset_y: The relative Y coordinate offset on the player.
        :param float offset_z: The relative Z coordinate offset on the player.
        :return: This method does not return anything.
        """
        return attach_3d_textlabel_to_player(
            self.id,
            player.id,
            offset_x,
            offset_y,
            offset_z
        )

    def attach_to_vehicle(
            self,
            vehicle: "Vehicle",
            offset_x: float,
            offset_y: float,
            offset_z: float
    ) -> bool:
        """Attach a 3D Textlabel to a vehicle.

        :param Vehicle vehicle: The vehicle to attach to.
        :param float offset_x: The relative X coordinate offset on the vehicle.
        :param float offset_y: The relative Y coordinate offset on the vehicle.
        :param float offset_z: The relative Z coordinate offset on the vehicle.
        :return: This method does not return anything.
        """
        return attach_3d_textlabel_to_vehicle(
            self.id, vehicle.id, offset_x, offset_y, offset_z
        )

    def update_text(self, color: int, text: str) -> bool:
        """Update the 3D Textlabel text.

        :param int color: The color you would like the text to have.
        :param str text: The text you want to show.
        :return: This method does not return anything.
        """
        return update_3d_textlabel_text(self.id, color, text)

from pysamp.vehicle import Vehicle  # noqa
from pysamp.player import Player  # noqa
