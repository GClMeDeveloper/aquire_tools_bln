import bpy as b


class PrimitiveMesh:
    def __init__(self, **object_type):
        self.object_type = dict(object_type)
        self.possible_primitives = [
            "cube", "uv_sphere",
            "circle", "cone",
            "gizmo_cube", "cylinder",
            "grid", "ico_sphere",
            "plane", "torus"
        ]
        # using **object_type to create the desired mesh
        if self.object_type.get(self.possible_primitives[0]):
            self.initialize = b.ops.mesh.primitive_cube_add()

        if self.object_type.get(self.possible_primitives[1]):
            self.initialize = b.ops.mesh.primitive_uv_sphere_add()

        if self.object_type.get(self.possible_primitives[2]):
            self.initialize = b.ops.mesh.primitive_circle_add()

        if self.object_type.get(self.possible_primitives[3]):
            self.initialize = b.ops.mesh.primitive_cone_add()

        if self.object_type.get(self.possible_primitives[4]):
            self.initialize = b.ops.mesh.primitive_cube_add_gizmo()

        if self.object_type.get(self.possible_primitives[5]):
            self.initialize = b.ops.mesh.primitive_cylinder_add()

        if self.object_type.get(self.possible_primitives[6]):
            self.initialize = b.ops.mesh.primitive_grid_add()

        if self.object_type.get(self.possible_primitives[7]):
            self.initialize = b.ops.mesh.primitive_ico_sphere_add()

        if self.object_type.get(self.possible_primitives[8]):
            self.initialize = b.ops.mesh.primitive_plane_add()

        if self.object_type.get(self.possible_primitives[9]):
            self.initialize = b.ops.mesh.primitive_torus_add()

        self.__name__ = b.context.active_object

    def __repr__(self):
        print(self.__name__)

    def even_scale(self, scale_modifier):
        self.__name__.scale = [scale_modifier, scale_modifier, scale_modifier]

    def odd_scale(self, x, y, z):
        self.__name__.scale = [float(x), float(y), float(z)]

    def position_self(self, x, y, z):
        self.__name__.location = [float(x), float(y), float(z)]
