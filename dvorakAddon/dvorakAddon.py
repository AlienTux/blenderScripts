# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
#
# Managed to make this very small addon to change the keymap of all my addons 
# from QWERTY to Dvorak.
# Originally I just the script once and the keymaps would be saved. However
# there were issues with the addon keymaps that prompted me to actually
# finish this addon. I didn't write the originalscript. Found it here
# https://blenderartists.org/t/dvorak-key-configration-transformer/630922
#
# The addon doesn't have an interface. You have to run everything from the
# F3 menu and then search for
# "Dvorak". There are 2 commands:
# 1) To change from the default blender keymap to Dvorak
# 2) To revert everything back to the default


import bpy
 
bl_info = {
    'name': 'Dvorak Layout',
    'category': 'Interface',
    'author': 'AlienTux',
    'version': (0, 0, 2),
    'blender': (2, 80, 0),
    'location': 'Blender Icon (next to File) -> System',
    'description': 'Change all keybindings to Dvorak Layout'
}

# This is the conversion map for all keys. QWERTY on the left, Dvorak on the
# right. If you wish to modify this structure just change the keys and
# re-install the addon.
conversion_map = {
    'A': 'A',
    'B': 'X',
    'C': 'J',
    'D': 'E',
    'E': 'PERIOD',
    'F': 'U',
    'G': 'I',
    'H': 'D',
    'I': 'C',
    'J': 'H',
    'K': 'T',
    'L': 'N',
    'M': 'M',
    'N': 'B',
    'O': 'R',
    'P': 'L',
    'Q': 'QUOTE',
    'R': 'P',
    'S': 'O',
    'T': 'Y',
    'U': 'G',
    'V': 'K',
    'W': 'COMMA',
    'X': 'Q',
    'Y': 'F',
    'Z': 'SEMI_COLON',
    'MINUS': 'LEFT_BRACKET',
    'EQUAL': 'RIGHT_BRACKET',
    'LEFT_BRACKET': 'SLASH',
    'RIGHT_BRACKET': 'EQUAL',
    'SEMI_COLON': 'S',
    'QUOTE': 'MINUS',
    'COMMA': 'W',
    'PERIOD': 'V',
    'SLASH': 'Z',
}


# This message box I got from here: 
# https://blender.stackexchange.com/questions/109711/how-to-popup-simple-message-box-from-python-console
def showMessageBox(message = "", title = "Message Box", icon = 'INFO'):

    def draw(self, context):
        self.layout.label(text = message)

    bpy.context.window_manager.popup_menu(draw, title = title, icon = icon)

 
class dvorakLayout(bpy.types.Operator):
    bl_idname = 'dvorak.dvorak_layout'
    bl_label = 'Change all unmodified keyboard bindings to Dvorak Layout'
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):

        wm = bpy.context.window_manager

    # Transform the user keys using the conversion_map
        for km in wm.keyconfigs.user.keymaps:
            # get the active version of the keymap, dont alter the oiginal
            # Addon keymap
            km = km.active()
            for kmi in km.keymap_items:
                # check if keymap has already been changed, don't alter if
                # already changed
                if kmi.is_user_modified == False:
                    if kmi.key_modifier in conversion_map:
                        kmi.key_modifier = conversion_map[kmi.key_modifier]
                    
                    if kmi.type in conversion_map:
                        kmi.type = conversion_map[kmi.type]
                        
    # Transform the addon keys using the conversion_map
    # This section has been commented out and is not required. It is here
    # for historical purposes. If you uncomment this and run the addon your
    # addon keymaps will get messed up (basically the keymaps will be changed
    # twice.
#        for km in wm.keyconfigs.addon.keymaps:
#           for kmi in km.keymap_items:
#               if kmi.key_modifier in conversion_map:
#                   kmi.key_modifier = conversion_map[kmi.key_modifier]
#        
#               if kmi.type in conversion_map:
#                   kmi.type = conversion_map[kmi.type]


    # Ask the user for a name to save the preset as
    # This was in the original script. It is really not needed since the addon
    # provides a means to return to the default blender config.
#        bpy.ops.wm.keyconfig_preset_add('INVOKE_DEFAULT')
                        
        showMessageBox("Layout converted to Dvorak", "Dvorak Keyboard")
            
        return {"FINISHED"}

class dvorakLayoutRestore(bpy.types.Operator):
    bl_idname = 'dvorak.dvorak_layout_restore'

    bl_label = 'Restore ALL keymays to default (usually from Dvorak Addon)'
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):

        wm = bpy.context.window_manager
        
        # Transform the user keys using the conversion_map
        for km in wm.keyconfigs.user.keymaps:
            # get the active version of the keymap, don't alter the oiginal
            # Addon keymap
            km.restore_to_default()
            
        showMessageBox("Layout reverted to QWERTY")
        
        return {"FINISHED"}
 
def dvorakMenuOne(self, context):
    self.layout.operator(dvorakLayout.bl_idname)

def dvorakMenuTwo(self, context):
    self.layout.operator(dvorakLayoutRestore.bl_idname)
    
def register():
    bpy.utils.register_class(dvorakLayout)
    bpy.utils.register_class(dvorakLayoutRestore)
    bpy.types.TOPBAR_MT_app_system.append(dvorakMenuOne)
    bpy.types.TOPBAR_MT_app_system.append(dvorakMenuTwo)
 
def unregister():
    bpy.utils.register_class(dvorakLayoutRestore)
    bpy.utils.unregister_class(dvorakLayout)
    
if __name__ == '__main__':
    register()
