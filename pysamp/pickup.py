from pysamp import (
    create_pickup, destroy_pickup,
    # add_static_pickup
)


class Pickup:
    """
    Pickups are global items that can be "picked" up by a player.
    Pickups trigger an event `TODO: PLACEHOLDER` when picked up.
    Benefit of having pickups compared to static pickups, is that you can
    recreate, destroy and modify pickups, while static pickups can only be
    created and have pre-made actions that make them work (such as health).
    """

    def __init__(self, id: int) -> None:
        self.id = id

    @classmethod
    def create(
        cls,
        model_id: int,
        type: int,
        x: float,
        y: float,
        z: float,
        virtual_world: int = 0,
    ) -> "Pickup":
        return cls(create_pickup(model_id, type, x, y, z, virtual_world))

    def destroy(self) -> bool:
        """
        Destroy the pickup.

        :return: No return value.

        This removes the pickup from the world.
        """
        return destroy_pickup(self.id)
