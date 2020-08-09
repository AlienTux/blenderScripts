# Managed to make this very small addon to change the keymap of all my addons 
# from QWERTY to Dvorak.
# Originally I just this script once and the keymaps would be saved:
#
# (I didn't write the script. Found it here: https://blenderartists.org/t/dvorak-key-configration-transformer/630922 )

#import bpy
#
#
## Mapping between the Qwerty keys, and what keys they are replaced with
## when using Dvorak. In other words. Label of the key on the keyboard
## is on the left, and the key that is registered when pressing that key is
## on the right.
#
## This map has been converted for English Dvorak using an English (US) keyboard
#conversion_map = {
#    'A': 'A',
#    'B': 'X',
#    'C': 'J',
#    'D': 'E',
#    'E': 'PERIOD',
#    'F': 'U',
#    'G': 'I',
#    'H': 'D',
#    'I': 'C',
#    'J': 'H',
#    'K': 'T',
#    'L': 'N',
#    'M': 'M',
#    'N': 'B',
#    'O': 'R',
#    'P': 'L',
#    'Q': 'QUOTE',
#    'R': 'P',
#    'S': 'O',
#    'T': 'Y',
#    'U': 'G',
#    'V': 'K',
#    'W': 'COMMA',
#    'X': 'Q',
#    'Y': 'F',
#    'Z': 'SEMI_COLON',
#    'MINUS': 'LEFT_BRACKET',
#    'EQUAL': 'RIGHT_BRACKET',
#    'LEFT_BRACKET': 'SLASH',
#    'RIGHT_BRACKET': 'EQUAL',
#    'SEMI_COLON': 'S',
#    'QUOTE': 'MINUS',
#    'COMMA': 'W',
#    'PERIOD': 'V',
#    'SLASH': 'Z',
#}
#
#
#wm = bpy.context.window_manager
#
#
## Transform the user keys using the conversion_map
#for km in wm.keyconfigs.user.keymaps:
#    for kmi in km.keymap_items:
#        if kmi.key_modifier in conversion_map:
#            kmi.key_modifier = conversion_map[kmi.key_modifier]
#        
#        if kmi.type in conversion_map:
#            kmi.type = conversion_map[kmi.type]
#
## Transform the addon keys using the conversion_map
#for km in wm.keyconfigs.addon.keymaps:
#    for kmi in km.keymap_items:
#        if kmi.key_modifier in conversion_map:
#            kmi.key_modifier = conversion_map[kmi.key_modifier]
#        
#        if kmi.type in conversion_map:
#            kmi.type = conversion_map[kmi.type]

# However, if you run the script once then all the user keymaps do change and
# are seved, but the addon keymaps are just changed and not registered
# as changed. Therefore, the script must be run every single time Blender
# starts up.
# 
# The original addon was found here: https://blender.stackexchange.com/questions/135361/blender-2-8-startup-function-working-in-addon
#
# It was modified to suit my needs.

bl_info = {
    "name": "Dvorak Keymap",
    "author": "AlienTux",
    "version": (0, 0),
    "blender": (2, 80, 0),
    "description": "Sets addon keymap to Dvorak",
    "category": "User"}

import bpy
from bpy.app.handlers import persistent

@persistent
def dvorakKeymap(scene):
    wm = bpy.context.window_manager

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
    for km in wm.keyconfigs.addon.keymaps:
        for kmi in km.keymap_items:
            if kmi.key_modifier in conversion_map:
                kmi.key_modifier = conversion_map[kmi.key_modifier]
            if kmi.type in conversion_map:
                kmi.type = conversion_map[kmi.type]
    bpy.app.handlers.depsgraph_update_post.remove(dvorakKeymap)


def register():
    bpy.app.handlers.depsgraph_update_post.append(dvorakKeymap)

def unregister():
    bpy.app.handlers.depsgraph_update_post.remove(dvorakKeymap)

if __name__ == "__main__":
    register() 





