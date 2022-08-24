# TreyEngine
### A 2D python game engine

This is a ***work-in-progress***. However, most of basic functionalities should work. If you find any bugs (assuming anyone actually views this), please report them.  

Currently supports:
 - rendering basic sprites
 - animated sprites 
 - rendering rectangles
 - Spritesheets
 - keyboard input detections

To install pypi package:

    pip install TreyEngine

Note: This is built on top of [pysdl2](https://github.com/py-sdl/py-sdl2)

## Current Work Focus
 - Debugging animated sprites
 - Removing game_globals file (increase modularity)
 - Removing image.load() requirement 
    - create_sprite() will accept path instead of image object
    - Sprite constructor will support optional sub-image region
 - Adding tests for easy debugging of changes
 - Adding FPS limiting
 - Adding audio module
 - add collision calculation module 
    - will support only circle and rectangular collisions at first
    - want to add support of collider object creation of all polygons
        - this would probably require automatic creation of collider based on image shape
    - visualization of colliders (easy)
Currently working on writing engine in C/C++ with SDL2, with wrapper for Python to be used by user






