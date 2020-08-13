# Simple Blender addons & scripts

This is a (very basic) collection of scripts I have written myself and find useful.

## Dvorak Keyboard Layout

The first and most important addon (for me) in here is the **Dvorak Keyboard Layout mapper**.

The whole addon is called: _dvorakAddon/dvorakAddon.py_

Blender Artists thread: [https://blenderartists.org/t/dvorak-keymap-add-on-actually-any-keyboard-layout-coleman-azerty-qwertz-etc/1246938](https://blenderartists.org/t/dvorak-keymap-add-on-actually-any-keyboard-layout-coleman-azerty-qwertz-etc/1246938)

### Installation

Download the .py file and install via de Blender Add-On preferences. Activate the add-on.

### Usage

There are only 2 commands (so far):

1. Change all unmodified keyboard bindings to Dvorak Layout
2. Restore from Dvorak Layout to Blender (QWERTY) default

To run this commands you have to press the F3 key and type the word **_Dvorak_**. Both options will show up. Select which one you want and press enter. There will be a small dialog poping up telling you what just happened.

### How the add-on works

If you look into the .py file you will see that the addon is extremely simple. There is a conversion map that has all the default keys on the left and the converted keys on the right. If you wish to modify this layout just change the letters and symbols on the right, save the file and re-install the addon.

```
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
```

## BPSRender script

This script was made to easily run the BPSRender addon for multithread rendering.

It is still very basic and works only if you configure the paths yourself.

Additional work is needed, but is provided here in case it gives people ideas =]


