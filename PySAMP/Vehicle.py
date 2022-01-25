from Player import Player
from PySAMP import (
    add_vehicle_component,
    change_vehicle_color,
    change_vehicle_paintjob,
    create_vehicle,
    destroy_vehicle,
    detach_trailer_from_vehicle,
    get_vehicle_component_in_slot,
    get_vehicle_damage_status,
    get_vehicle_distance_from_point,
    get_vehicle_health,
    get_vehicle_model,
    get_vehicle_params_car_doors,
    get_vehicle_params_car_windows,
    get_vehicle_params_ex,
    get_vehicle_params_siren_state,
    get_vehicle_pos,
    get_vehicle_rotation_quat,
    get_vehicle_trailer,
    get_vehicle_velocity,
    get_vehicle_virtual_world,
    get_vehicle_z_angle,
    is_trailer_attached_to_vehicle,
    is_valid_vehicle,
    is_vehicle_streamed_in,
    link_vehicle_to_interior,
    remove_vehicle_component,
    repair_vehicle,
    set_vehicle_angular_velocity,
    set_vehicle_health,
    set_vehicle_number_plate,
    set_vehicle_params_car_doors,
    set_vehicle_params_car_windows,
    set_vehicle_params_ex,
    set_vehicle_params_for_player,
    set_vehicle_pos,
    set_vehicle_to_respawn,
    set_vehicle_velocity,
    set_vehicle_virtual_world,
    set_vehicle_z_angle,
    update_vehicle_damage_status,
)


class Vehicle:
    """Create server vehicles. Edit and work on them using this class."""

    def __init__(
        self,
        vehicle_type,
        x,
        y,
        z,
        rotation,
        color1,
        color2,
        respawn_delay,
        add_siren: bool = False,
    ):
        self.vehicletype = vehicle_type
        self.x = x
        self.y = y
        self.z = z
        self.rotation = rotation
        self.color1 = color1
        self.color2 = color2
        self.respawn_delay = respawn_delay
        self.addsiren = add_siren

        self.id = create_vehicle(
            vehicle_type,
            x,
            y,
            z,
            rotation,
            color1,
            color2,
            respawn_delay,
            add_siren
        )

    def is_valid(self) -> bool:
        """Check if the vehicle is valid"""
        return is_valid_vehicle(self.id)

    def get_distance_from_point(self, x: float, y: float, z: float) -> float:
        """Check how far away the vehicle is from a given coordinate."""
        return get_vehicle_distance_from_point(self.id, x, y, z)

    def destroy(self) -> bool:
        """Removes the vehicle from the server."""
        return destroy_vehicle(self.id)

    def is_streamed_in(self, for_player: Player):
        """Lets you know if a specific player has streamed in the vehicle."""
        return is_vehicle_streamed_in(self.id, for_player.id)

    def get_pos(self) -> tuple[float, float, float]:
        """Get the vehicle's current position."""
        return get_vehicle_pos(self.id)

    def set_pos(self, position: tuple[float, float, float]) -> bool:
        """Sets the vehicle position directly on the passed position."""
        try:
            x, y, z = position
        except ValueError:
            raise ValueError(
                "Method set_pos() expects the position to be a tuple = \
                    (x: float, y: float, z: float)"
            )
        else:
            return set_vehicle_pos(self.id, x, y, z)

    def get_z_angle(self) -> float:
        """Returns the heading the vehicle has. Can be >= 0.0 and < 360."""
        return get_vehicle_z_angle(self.id)

    def set_z_angle(self, z_angle: float):
        """Set the vehicle's heading hangle. 0.0 => z_angle < 360.0"""
        return set_vehicle_z_angle(self.id, z_angle)

    def get_rotation_quat(self) -> tuple[float, float, float, float]:
        """Returns a vehicle's rotation on all axes as a quaternion"""
        return get_vehicle_rotation_quat(self.id)

    def set_params_for_player(
        self, player: Player, objective: int, doors_locked: int
    ) -> bool:
        """Set the parameters of the vehicle."""
        return set_vehicle_params_for_player(
            self.id, player.id, objective, doors_locked
        )

    def get_params_ex(self) -> tuple[int, int, int, int, int, int, int]:
        """Get the vehicle's params."""
        return get_vehicle_params_ex(self.id)

    def set_params_ex(self, param: tuple) -> bool:
        """Set the parameters of the vehicle."""
        try:
            engine, lights, alarm, doors, bonnet, boot, objective = param
        except ValueError:
            raise ValueError(
                "A tuple was expected: \
                    (engine, lights, alarm, doors, bonnet, boot, objective)"
            )
        else:
            return set_vehicle_params_ex(
                self.id, engine, lights, alarm, doors, bonnet, boot, objective
            )

    @property
    def params_siren_state(self):
        return get_vehicle_params_siren_state(self.id)

    @property
    def params_car_doors(self):
        return get_vehicle_params_car_doors(self.id)

    @params_car_doors.setter
    def params_car_doors(self, param: tuple):
        try:
            driver, passenger, backleft, backright = param
        except ValueError:
            raise ValueError(
                "A tuple was expected: \
                    (driver, passenger, backleft, backright)"
            )
        else:
            return set_vehicle_params_car_doors(
                self.id, driver, passenger, backleft, backright
            )

    @property
    def params_car_windows(self):
        return get_vehicle_params_car_windows(self.id)

    @params_car_windows.setter
    def params_car_windows(self, param: tuple):
        try:
            driver, passenger, backleft, backright = param
        except ValueError:
            raise ValueError(
                "A tuple was expected: \
                    (driver, passenger, backleft, backright)"
            )
        else:
            return set_vehicle_params_car_windows(
                self.id, driver, passenger, backleft, backright
            )

    def set_to_respawn(self):
        return set_vehicle_to_respawn(self.id)

    def link_to_interior(self, interiorid):
        return link_vehicle_to_interior(self.id, interiorid)

    def add_component(self, componentid):
        return add_vehicle_component(self.id, componentid)

    def remove_component(self, componentid):
        return remove_vehicle_component(self.id, componentid)

    def change_color(self, color1, color2):
        return change_vehicle_color(self.id, color1, color2)

    def change_paintjob(self, paintjobid):
        return change_vehicle_paintjob(self.id, paintjobid)

    @property
    def health(self):
        return get_vehicle_health(self.id)

    @health.setter
    def health(self, health):
        return set_vehicle_health(self.id, health)

    def detach_trailer(self):
        return detach_trailer_from_vehicle(self.id)

    def is_trailer_attached(self):
        return is_trailer_attached_to_vehicle(self.id)

    @property
    def trailer(self):
        return get_vehicle_trailer(self.id)

    def set_number_plate(self, numberplate):
        return set_vehicle_number_plate(self.id, numberplate)

    @property
    def model(self):
        return get_vehicle_model(self.id)

    def get_component_in_slot(self, slot):
        return get_vehicle_component_in_slot(self.id, slot)

    def repair(self):
        return repair_vehicle(self.id)

    @property
    def velocity(self):
        return get_vehicle_velocity(self.id)

    @velocity.setter
    def velocity(self, vector: tuple):
        try:
            x, y, z = vector
        except ValueError:
            raise ValueError("Expected a tuple for x,y,z: (x,y,z)")
        else:
            return set_vehicle_velocity(self.id, x, y, z)

    def set_angular_velocity(self, x: float, y: float, z: float):
        return set_vehicle_angular_velocity(self.id, x, y, z)

    @property
    def damage_status(self):
        return get_vehicle_damage_status(self.id)

    @damage_status.setter
    def damage_status(self, param: tuple):
        try:
            panels, doors, lights, tires = param
        except ValueError:
            raise ValueError(
                "Expected a tuple for damage_status: \
                    (panels, doors, lights, tires)"
            )
        else:
            return update_vehicle_damage_status(
                self.id, panels, doors, lights, tires
            )

    @property
    def virtual_world(self):
        return get_vehicle_virtual_world(self.id)

    @virtual_world.setter
    def virtual_world(self, worldid):
        return set_vehicle_virtual_world(self.id, worldid)
