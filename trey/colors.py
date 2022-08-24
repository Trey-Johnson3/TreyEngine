import sdl2
import sdl2.ext

GREEN = sdl2.ext.Color(0, 255, 0)
RED = sdl2.ext.Color(255, 0, 0)
BLUE = sdl2.ext.Color(0, 0, 255)
BLACK = sdl2.ext.Color(0, 0, 0)
WHITE = sdl2.ext.Color(255, 255, 255)


def from_rgb(red, green, blue):
    return sdl2.ext.Color(red, green, blue)
