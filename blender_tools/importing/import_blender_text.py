import bpy as b


def import_text_as_mod(file_name):
    data = b.data.texts[f"{file_name}.py"]
    data.name = f"{file_name}.py"
    data.use_module = True
    return data.as_module()
