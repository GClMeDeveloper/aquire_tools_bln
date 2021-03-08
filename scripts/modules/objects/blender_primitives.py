import bpy as b


class BlendObject:
    def __init__(self, **object_type):
        self.object_type = dict(object_type)
        self.possible_types = ["cube", "uv_sphere"]

        if self.object_type.get(self.possible_types[0]):
            self.initialize = b.ops.mesh.primitive_cube_add()
        if self.object_type.get(self.possible_types[1]):
            self.initialize = b.ops.mesh.primitive_uv_sphere_add()

        self.__name__ = b.context.active_object

    def __repr__(self):
        print(self.__name__)

    def scale_evenly(self, scale_modifier):
        self.__name__.scale = [scale_modifier, scale_modifier, scale_modifier]

    def position_self(self, x, y):
        self.__name__.location = [x, y, 0.5]
