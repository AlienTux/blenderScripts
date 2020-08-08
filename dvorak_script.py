# Copyright 2015 Julian Sivertsen
#
# original post in BlenderArtists: https://blenderartists.org/t/dvorak-key-configration-transformer/630922

# Modified by AlienTux from the Norweigan Dvorak to US Dvorak
# Also added a part to modify addon keymaps

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation. See &lt;http://www.gnu.org/licenses/&gt;.


import bpy


# Mapping between the Qwerty keys, and what keys they are replaced with
# when using Dvorak. In other words. Label of the key on the keyboard
# is on the left, and the key that is registered when pressing that key is
# on the right.

# This map has been converted for English Dvorak using an English (US) keyboard
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


wm = bpy.context.window_manager


# Transform the user keys using the conversion_map
for km in wm.keyconfigs.user.keymaps:
    for kmi in km.keymap_items:
        if kmi.key_modifier in conversion_map:
            kmi.key_modifier = conversion_map[kmi.key_modifier]
        
        if kmi.type in conversion_map:
            kmi.type = conversion_map[kmi.type]

# Transform the addon keys using the conversion_map
for km in wm.keyconfigs.addon.keymaps:
    for kmi in km.keymap_items:
        if kmi.key_modifier in conversion_map:
            kmi.key_modifier = conversion_map[kmi.key_modifier]
        
        if kmi.type in conversion_map:
            kmi.type = conversion_map[kmi.type]


# Ask the user for a name to save the preset as
#bpy.ops.wm.keyconfig_preset_add('INVOKE_DEFAULT')
