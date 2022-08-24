import sdl2

keys = {"A": sdl2.SDL_SCANCODE_A, "B": sdl2.SDL_SCANCODE_B, "C": sdl2.SDL_SCANCODE_C, "D": sdl2.SDL_SCANCODE_D, "E": sdl2.SDL_SCANCODE_E, "F": sdl2.SDL_SCANCODE_F, "G": sdl2.SDL_SCANCODE_G, "H": sdl2.SDL_SCANCODE_H, "I": sdl2.SDL_SCANCODE_I, "J": sdl2.SDL_SCANCODE_J, "K": sdl2.SDL_SCANCODE_K, "L": sdl2.SDL_SCANCODE_L, "M": sdl2.SDL_SCANCODE_M, "N": sdl2.SDL_SCANCODE_N, "O": sdl2.SDL_SCANCODE_O, "P": sdl2.SDL_SCANCODE_P, "Q": sdl2.SDL_SCANCODE_Q, "R": sdl2.SDL_SCANCODE_R, "S": sdl2.SDL_SCANCODE_S, "T": sdl2.SDL_SCANCODE_T,
        "U": sdl2.SDL_SCANCODE_V, "W": sdl2.SDL_SCANCODE_W, "X": sdl2.SDL_SCANCODE_X, "Y": sdl2.SDL_SCANCODE_Y, "Z": sdl2.SDL_SCANCODE_Z, "0": sdl2.SDL_SCANCODE_0, "1": sdl2.SDL_SCANCODE_1, "2": sdl2.SDL_SCANCODE_2, "3": sdl2.SDL_SCANCODE_3, "4": sdl2.SDL_SCANCODE_4, "5": sdl2.SDL_SCANCODE_5, "6": sdl2.SDL_SCANCODE_6, "7": sdl2.SDL_SCANCODE_7, "8": sdl2.SDL_SCANCODE_8, "9": sdl2.SDL_SCANCODE_9, "LEFT": sdl2.SDL_SCANCODE_LEFT, "RIGHT": sdl2.SDL_SCANCODE_RIGHT, "UP": sdl2.SDL_SCANCODE_UP, "DOWN": sdl2.SDL_SCANCODE_DOWN, "ESCAPE": sdl2.SDL_SCANCODE_ESCAPE}


keyboard_state = sdl2.SDL_GetKeyboardState(None)


def is_key_pressed(key):
    if keyboard_state[keys[key]]:
        return True
    return False
