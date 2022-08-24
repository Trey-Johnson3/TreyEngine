import sdl2
import sdl2.ext


import sys
import time
# is it really necessary to import all of these?
import trey.image as image
import trey.colors as colors
import trey.keyboard as keyboard
import trey.maths as maths
import trey.graphics as graphics
import trey.game_globals as game_globals
# rename import as ... to make it simpler (globals vs game_globals)


CREATE_WINDOW = True
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_NAME = "Untitled Game"

FPS_LIMIT = None  # currently there is no limit capability
RENDER_QUALITY = "best"  # only use this until add more options


def initialize():
    '''Add ability to initialize or not initialize, depending on whether or not it affects performance'''
    '''if CREATE_WINDOW == True:'''
    window = sdl2.ext.Window(WINDOW_NAME, size=(WINDOW_WIDTH, WINDOW_HEIGHT))
    window.show()
    print("created and showed window")
    if "-hardware" in sys.argv:
        render_flags = (sdl2.SDL_RENDERER_ACCELERATED |
                        sdl2.SDL_RENDERER_PRESENTVSYNC)
    else:
        render_flags = sdl2.SDL_RENDERER_SOFTWARE
    renderer = sdl2.ext.Renderer(window, flags=render_flags)
    sdl2.ext.set_texture_scale_quality(method=RENDER_QUALITY)
    print("tried to assign renderer")
    assert renderer, "no renderer in trey"
    game_globals.RENDERER = renderer


def start(scene):
    _start(scene)
    old_time = 0
    running = True
    while running:
        print("fps: " + str(1/(time.time()-old_time)))
        dt = time.time()-old_time
        old_time = time.time()
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
        _update(scene, dt)
        _render(scene, dt)
    sdl2.ext.quit()
    return 0


def _start(scene):
    assert scene, "no scene"
    try:
        scene.start()
    except:
        print("no start function in active scene")


def _update(scene, dt):
    assert scene, "no scene"
    try:
        scene.update(dt)
    except:
        print("no update function in active scene")


def _render(scene, dt):
    assert scene, "no scene"
    assert game_globals.RENDERER, "no RENDERER, _render"
    game_globals.RENDERER.clear()
    try:
        scene.render(dt)
    except:
        print("no render function in active scene")
    game_globals.RENDERER.present()
    # sdl2.SDL_delay(10)


class Scene():
    def __init__(self):
        pass

    def start(self):
        pass

    def update(self):
        pass

    def render(self):
        pass
