from pysamp.vehicle import Vehicle
from pysamp.player import Player
from pysamp import (
    attach_3d_text_label_to_player,
    attach_3d_text_label_to_vehicle,
    create_3d_text_label,
    delete_3d_text_label,
    update_3d_text_label_text,
)


class Text_Label:
    """
    Create and adjust 3D Text Labels that can be attached to
    vehicles, players or world coordinates.

    
    """

    def __init__(
        self,
        text: str,
        color: int,
        x: float,
        y: float,
        z: float,
        drawDistance: float,
        virtualworld: int,
        testLOS=False,
    ) -> None:

        self.text = text
        self.color = color
        self.x = x
        self.y = y
        self.z = z
        self.draw_distance = drawDistance
        self.virtual_world = virtualworld
        self.test_los = testLOS
        self.id = create_3d_text_label(
            self.text,
            self.color,
            self.x,
            self.y,
            self.z,
            self.draw_distance,
            self.virtual_world,
            self.test_los,
        )

    def delete(self):
        return delete_3d_text_label(self.id)

    def attach_to_player(
        self, player: Player, offsetX: float, offsetY: float, offsetZ: float
    ) -> int:
        return attach_3d_text_label_to_player(
            self.id, player.id, offsetX, offsetY, offsetZ
        )

    def attach_to_vehicle(
        self, vehicle: Vehicle, offsetX: float, offsetY: float, offsetZ: float
    ) -> int:
        return attach_3d_text_label_to_vehicle(
            self.id, vehicle.id, offsetX, offsetY, offsetZ
        )

    def update_text(self, color: int, text: str) -> None:
        return update_3d_text_label_text(self.id, color, text)
