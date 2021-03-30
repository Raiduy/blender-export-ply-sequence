bl_info = {
    "name": "Export multiple frames as .ply files",
    "category": "Export",
    "blender": (2, 80, 0),
}

import bpy
import os

class frameExportMesh(bpy.types.Operator):
    """Export animation frames as mesh files."""
    bl_idname = "frame.export_mesh"
    bl_label = "Export multiple frames as .ply files"
    bl_options = {'REGISTER'}

    @classmethod
    def poll(cls, context):
        return bpy.data.is_saved is True
    
    def execute(self, context):
        scene = context.scene

        for frame in range(scene.frame_start, scene.frame_end + 1):
            scene.frame_set(frame)
            path = bpy.path.abspath('//PLY_Animation_frames/')

            if not os.path.exists(path):
                os.makedirs(path)

            file = scene.name + str(scene.frame_current).zfill(3) + ".ply"
            bpy.ops.export_mesh.ply(filepath = path + file)
            self.report({'INFO'}, file + " has been saved")
        
        return {'FINISHED'}

def menu_func_export(self, context):
    self.layout.operator(frameExportMesh.bl_idname, text="Export multiple frames as PLY files - Ridu")
 
def register():
    bpy.utils.register_class(frameExportMesh)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)
    
def unregister():
    bpy.utils.unregister_class(frameExportMesh)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)
 
if __name__ == "__main__":       
    register() 