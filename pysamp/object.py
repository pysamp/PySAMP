from pysamp import (
    create_object,
    get_object_pos,
    set_object_pos,
    set_object_rot,
    get_object_rot,
    set_object_no_camera_col,
    is_valid_object,
    destroy_object,
    move_object,
    stop_object,
    is_object_moving,
    set_object_material,
    set_object_material_text,
    set_objects_default_camera_col,
)


class Object:
    """Class that creates and handles global objects.

    For player objects, check out ``pysamp.PlayerObject``.

    Objects are world objects represented by what object they are (model), and
    where they are created. They can be moved, rotated and customized with
    non-default textures. The parameter ``draw_distance`` controls the
    behaviour of how far away the object appears for a player.

    It is recommended to use a streamer if you need more than 1000 objects.
    SA-MP has a limit if approximately 1000 objects. Bypassing this limit will
    cause all objects to disappear.

    For a list of models, you can utilize tools like here:
    https://dev.prineside.com/en/gtasa_samp_model_id/
    """
    def __init__(
        self,
        model,
        x: float,
        y: float,
        z: float,
        rotation_x: float,
        rotation_y: float,
        rotation_z: float,
        draw_distance: float,
    ):
        self.model = model
        self.id = create_object(
            model, x, y, z, rotation_x, rotation_y, rotation_z, draw_distance
        )

    def set_postition(self, x: float, y: float, z: float) -> bool:
        """Set a new position for the object using world coordinates.

        For rotation, check out ``Object.set_rotation``.
        """
        return set_object_pos(self.id, x, y, z)

    def get_position(self) -> tuple[float, float, float]:
        """Retrieve the coordinates for where the object is right now."""
        return get_object_pos(self.id)

    def set_rotation(
        self,
        rotation_x: float,
        rotation_y: float,
        rotation_z: float
    ) -> bool:
        """Set the new rotation the object should have. Values are absolute."""
        return set_object_rot(self.id, rotation_x, rotation_y, rotation_z)

    def get_rotation(self) -> tuple[float, float, float]:
        """Get the rotation the object have."""
        return get_object_rot(self.id)

    def get_model(self) -> int:
        """Get the model of the object."""
        return self.model

    def set_no_camera_collision(self) -> bool:
        """Disable camera collision on the object.

        Makes the camera freely pass through it.

        .. note:: This only works outside the map boundaries (past -3000/3000).
        """
        return set_object_no_camera_col(self.id)

    def is_valid(self) -> bool:
        """Check if the object exists."""
        return is_valid_object(self.id)

    def destroy(self) -> bool:
        """Destroy the object.

        This removes the object from the world, and will no longer be 
        available. It's occupied object id gets free'd up.
        """
        return destroy_object(self.id)

    def move(
        self,
        x: float,
        y: float,
        z: float,
        speed: float,
        rotation_x: float = -1000.0,
        rotation_y: float = -1000.0,
        rotation_z: float = -1000.0,
    ) -> int:
        """Move and rotate the object to given values.

        Rotation values should be -1000 if you don't want to modify the object
        rotation.

        Returns the time in seconds it takes to move the object.
        """
        return move_object(
            self.id, x, y, z, speed, rotation_x, rotation_y, rotation_z
        )

    def stop(self) -> bool:
        """Stop moving the object."""
        return stop_object(self.id)

    def is_moving(self) -> bool:
        """Check if the object is currently moving."""
        return is_object_moving(self.id)

    def set_material(
        self,
        material_index: int,
        model_id: int,
        txd_name: str,
        texture_name: str,
        material_color: int = 0
    ) -> bool:
        """Change the object materials.

        The material can be from another object model in the game.

        .. note:: Vertex lighting of the object will disappear if material\
            color is changed.

        .. warning:: You MUST use ARGB color format, not RGBA.
        """
        return set_object_material(
            self.id,
            material_index,
            model_id,
            txd_name,
            texture_name,
            material_color,
        )
