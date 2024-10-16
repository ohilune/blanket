import bpy


class OHILUNE_MT_Menu(bpy.types.Menu):
    bl_label = "OHILUNE"
    bl_idname = "OHILUNE_MT_Menu"

    def draw(self, context):
        layout = self.layout
        layout.operator("mesh.primitive_cube_add", text="Add Cube")
        layout.operator("mesh.primitive_uv_sphere_add", text="Add Sphere")
        layout.operator("transform.translate", text="Translate")


def draw_custom_menu(self, context):
    self.layout.menu(OHILUNE_MT_Menu.bl_idname)


def register():
    bpy.utils.register_class(OHILUNE_MT_Menu)
    bpy.types.TOPBAR_MT_editor_menus.append(draw_custom_menu)


def unregister():
    bpy.types.TOPBAR_MT_editor_menus.remove(draw_custom_menu)
    bpy.utils.unregister_class(OHILUNE_MT_Menu)


if __name__ == "__main__":
    register()
