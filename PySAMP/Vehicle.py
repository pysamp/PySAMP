from Player import Player
from PySAMP import (
    add_vehicle_component,
    change_vehicle_color,
    change_vehicle_paintjob,
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
    """
    Create a vehicle by using this class.

    Properties:
    --------
    - id
    - pos
    - z_angle
    - rotation_quat
    - params_ex
    - params_siren_state
    - params_car_doors
    - params_car_windows
    - health
    - trailer
    - model
    - velocity
    - damage_status
    - virtual_world
    __________________
    Methods:
    ---------
    - is_valid()
    - get_distance_from_point(x, y, z)
    - destroy()
    - is_streamed_in(forplayerid)
    - set_to_respawn()
    - link_to_interior(interiorid)
    - add_component(componentid)
    - remove_component(componentid)
    - change_color(color1, color2)
    - change_paintjob(paintjobid)
    - detach_trailer()
    - is_trailer_attached()
    - set_number_plate(text)
    - get_component_in_slot(slot)
    - repair()
    - set_angular_velocity(x, y, z)

    """

    def __init__(
        self,
        vehicletype,
        x,
        y,
        z,
        rotation,
        color1,
        color2,
        respawn_delay,
        addsiren=False,
    ):
        self.vehicletype = vehicletype
        self.x = x
        self.y = y
        self.z = z
        self.rotation = rotation
        self.color1 = color1
        self.color2 = color2
        self.respawn_delay = respawn_delay
        self.addsiren = addsiren

        self.id = create_vehicle(
            vehicletype, x, y, z, rotation, color1, color2, respawn_delay, addsiren
        )

    def is_valid(self):
        return is_valid_vehicle(self.id)

    def get_distance_from_point(self, x: float, y: float, z: float):
        return get_vehicle_distance_from_point(self.id, x, y, z)

    def destroy(self):
        return destroy_vehicle(self.id)

    def is_streamed_in(self, forplayerid):
        return is_vehicle_streamed_in(self.id, forplayerid)

    @property
    def pos(self):
        return get_vehicle_pos(self.id)

    @pos.setter
    def pos(self, pos: tuple):
        try:
            x, y, z = pos
        except:
            raise ValueError("Pass position as a tuple: xx.pos = (x,y,z)")
        else:
            return set_vehicle_pos(self.id, x, y, z)

    @property
    def z_angle(self):
        return get_vehicle_z_angle(self.id)

    @z_angle.setter
    def z_angle(self, z_angle: float):
        return set_vehicle_z_angle(self.id, z_angle)

    @property
    def rotation_quat(self):
        return get_vehicle_rotation_quat(self.id)

    def set_params_for_player(self, player: Player, objective, doorslocked):
        return set_vehicle_params_for_player(self.id, player.id, objective, doorslocked)

    @property
    def params_ex(self):
        return get_vehicle_params_ex(self.id)

    @params_ex.setter
    def params_ex(self, param: tuple):
        try:
            engine, lights, alarm, doors, bonnet, boot, objective = param
        except:
            raise ValueError(
                "A tuple was expected: (engine, lights, alarm, doors, bonnet, boot, objective)"
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
        except:
            raise ValueError(
                "A tuple was expected: (driver, passenger, backleft, backright)"
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
        except:
            raise ValueError(
                "A tuple was expected: (driver, passenger, backleft, backright)"
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
            X, Y, Z = vector
        except:
            raise ValueError("Expected a tuple for x,y,z: (x,y,z)")
        else:
            return set_vehicle_velocity(self.id, X, Y, Z)

    def set_angular_velocity(self, x: float, y: float, z: float):
        return set_vehicle_angular_velocity(self.id, X, Y, Z)

    @property
    def damage_status(self):
        return get_vehicle_damage_status(self.id)

    @damage_status.setter
    def damage_status(self, param: tuple):
        try:
            panels, doors, lights, tires = param
        except:
            raise ValueError(
                "Expected a tuple for damage_status: (panels, doors, lights, tires)"
            )
        else:
            return update_vehicle_damage_status(self.id, panels, doors, lights, tires)

    @property
    def virtual_world(self):
        return get_vehicle_virtual_world(self.id)

    @virtual_world.setter
    def virtual_world(self, worldid):
        return set_vehicle_virtual_world(self.id, worldid)
