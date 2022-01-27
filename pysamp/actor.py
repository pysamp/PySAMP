from pysamp import (apply_actor_animation, clear_actor_animations,
                    create_actor, destroy_actor, get_actor_facing_angle,
                    get_actor_health, get_actor_pos, get_actor_virtual_world,
                    is_actor_invulnerable, is_actor_streamed_in,
                    is_valid_actor, set_actor_facing_angle, set_actor_health,
                    set_actor_invulnerable, set_actor_pos,
                    set_actor_virtual_world)


class Actor:
    """
    Read more about actors here: https://open.mp/docs/scripting/functions/CreateActor
    -----------------
    """

    def __init__(self, modelid, x: float, y: float, z: float, rot):
        self.id = create_actor(modelid, x, y, z, rot)

    def destroy(self):
        return destroy_actor(self.id)

    def streamed_in(self, forplayerid):
        return is_actor_streamed_in(self.id, forplayerid)

    @property
    def virtual_world(self):
        return get_actor_virtual_world(self.id)

    @virtual_world.setter
    def virtual_world(self, vworld):
        return set_actor_virtual_world(self.id, vworld)

    def apply_animation(
        self, animlib, animname, fDelta, loop, lockx, locky, freeze, time
    ):
        return apply_actor_animation(
            self.id, animlib, animname, fDelta, loop, lockx, locky, freeze, time
        )

    def clear_animations(self):
        return clear_actor_animations(self.id)

    @property
    def pos(self):
        return get_actor_pos(self.id)

    @pos.setter
    def pos(self, pos):
        try:
            x, y, z = pos
        except:
            raise ValueError("Expected pos as tuple: (x, y, z)")
        else:
            return set_actor_pos(self.id, x, y, z)

    @property
    def facing_angle(self):
        return get_actor_facing_angle(self.id)

    @facing_angle.setter
    def facing_angle(self, angle: float):
        return set_actor_facing_angle(self.id, angle)

    @property
    def health(self):
        return get_actor_health(self.id)

    @health.setter
    def health(self, health):
        return set_actor_health(self.id, health)

    @property
    def invulnerable(self):
        return is_actor_invulnerable(self.id)

    @invulnerable.setter
    def invulnerable(self, invulnerable=True):
        return set_actor_invulnerable(self.id, invulnerable)

    @property
    def is_valid(self):
        return is_valid_actor(self.id)
