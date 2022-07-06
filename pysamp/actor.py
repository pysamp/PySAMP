from pysamp import (
    apply_actor_animation,
    clear_actor_animations,
    create_actor,
    destroy_actor,
    get_actor_facing_angle,
    get_actor_health,
    get_actor_pos,
    get_actor_virtual_world,
    is_actor_invulnerable,
    is_actor_streamed_in,
    is_valid_actor,
    set_actor_facing_angle,
    set_actor_health,
    set_actor_invulnerable,
    set_actor_pos,
    set_actor_virtual_world,
)
from samp import INVALID_ACTOR_ID
from typing import Optional, Tuple
from pysamp.event import event


class Actor:
    """A class that represents actors, also known as NPC's.

    These 'actors' are like NPCs, however they have limited functionality.
    They do not take up server player slots.

    Read more about actors here:
    https://open.mp/docs/scripting/functions/CreateActor
    """

    def __init__(self, id: int) -> None:
        self.id: int = id

    @classmethod
    def create(
        cls, modelid: int, x: float, y: float, z: float, rotation: float
    ) -> Optional["Actor"]:
        """Create a new actor.

        :param int modelid: The model of the actor.
        :param float x: The model of the actor.
        :param float y: The model of the actor.
        :param float z: The model of the actor.
        :param float rotation: The model of the actor.
        :return: An :class:`Actor` object. Will return ``None`` if the actor
            limit is reached of 1000 actors.
        """
        actor_id = create_actor(modelid, x, y, z, rotation)
        if actor_id == INVALID_ACTOR_ID:
            return None
        return cls(actor_id)

    def get_id(self) -> int:
        """Get the Actor's ID.

        :returns: The ID of the Actor.
        """
        return self.id

    def destroy(self) -> bool:
        """Remove a created actor from the world.

        :returns: No value returned.
        """
        return destroy_actor(self.id)

    def streamed_in(self, for_player: "Player") -> bool:
        """Check if a player has streamed in the actor.

        :param Player for_player: Which player you want to check if streamed in
        :returns: A boolean, ``True`` if the actor is streamed in, otherwise
            ``False``.
        """
        return is_actor_streamed_in(self.id, for_player.id)

    def get_virtual_world(self) -> int:
        """Get which virtual world ID the actor is in.

        .. note:: If the actor does not exist, this will still return 0.

        :returns: An integer (0-65535) that represents the world ID.
        """
        return get_actor_virtual_world(self.id)

    def virtual_world(self, virtual_world: int) -> bool:
        """Set the actor to a specific virtual world id.

        :returns: No value returned.
        """
        return set_actor_virtual_world(self.id, virtual_world)

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
    ) -> bool:
        """Set an animation on the actor.

        :param str animation_library: The library where the animation resides.
        :param str animation_name: The specific animation you'd like to apply.
        :param float delta: The speed to play the animation at. Use ``4.1``.
        :param bool loop: Set to ``True`` if you want it to loop, otherwise
            ``False`` if you want it to stop after completion.
        :param bool lock_x: Choose whether you want to allow the animation to
            move the Actor along the X-axis, and not return to original
            position when it is done playing. ``True`` means the Actor will
            return to original position.
        :param bool lock_y: Same as ``lock_x`` above, but for the y-axis.
        :param bool freeze: ``True`` makes the actor freeze when the animation
            is done playing. ``False`` will not.
        :param int time: Timer in milliseconds, set to 0 for never-ending
            loops.
        :returns: No value returned.
        """
        return apply_actor_animation(
            self.id,
            animation_library,
            animation_name,
            delta,
            loop,
            lock_x,
            lock_y,
            freeze,
            time,
        )

    def clear_animations(self) -> bool:
        """Clear the animations that are in use by the actor, if any.

        If you have set an animation to play on the actor, this clears/stops
        that.

        :returns: No value returned.
        """
        return clear_actor_animations(self.id)

    def get_position(self) -> Tuple[float, float, float]:
        """Gets the current world coordinates of where the actor is located.

        :returns: A tuple with three floats representing the x, y and z
            world-coordinate.
        """
        return get_actor_pos(self.id)

    def set_position(self, position: Tuple[float, float, float]) -> bool:
        """Set a new position for the actor.

        :param Tuple position: A tuple with three floats that represents the
            world coordinate in x, y and z.
        :returns: No value returned.
        """
        try:
            x, y, z = position
        except ValueError:
            raise ValueError("Expected position as tuple: (x, y, z)")
        else:
            return set_actor_pos(self.id, x, y, z)

    def get_facing_angle(self) -> float:
        """Get the actor's facing angle.

        :returns: Float that represents the current facing angle. (0-360).
        """
        return get_actor_facing_angle(self.id)

    def set_facing_angle(self, angle: float) -> bool:
        """Set the actor's facing angle.

        :param float angle: The new facing angle for the actor.
        :returns: No value returned.
        """
        return set_actor_facing_angle(self.id, angle)

    def get_health(self) -> float:
        """Get how much health the actor has.

        :returns: A float that represents the current health of the actor.
        """
        return get_actor_health(self.id)

    def set_health(self, health: float) -> bool:
        """Set the health of the actor.

        :param float health: The health to set on the actor (0-100.0).
        :returns: No value returned.
        """
        return set_actor_health(self.id, health)

    def is_invulnerable(self) -> bool:
        """See if the actor is invulnerable to damage.

        :returns: ``True`` if the actor is invulnerable, otherwise ``False``.
        """
        return is_actor_invulnerable(self.id)

    def set_invulnerable(self, invulnerable: bool = True) -> bool:
        """Set the actor to be invlunerable to damage.

        :param optional bool invulnerable: Set to ``True`` if you want to set
            the actor invulnerable to damage (default). Otherwise, set to
            ``False``.
        :returns: No value returned.
        """
        return set_actor_invulnerable(self.id, invulnerable)

    def is_valid(self) -> bool:
        """Check if the actor is valid.

        :returns: Boolean that is ``True`` if valid, otherwise ``False``.
        """
        return is_valid_actor(self.id)

    @event("OnActorStreamIn")
    def on_stream_in(cls, actorid: int, forplayerid: int):
        return (cls(actorid), Player(forplayerid))

    @event("OnActorStreamOut")
    def on_stream_out(cls, actorid: int, forplayerid: int):
        return (cls(actorid), Player(forplayerid))


from pysamp.player import Player  # noqa
