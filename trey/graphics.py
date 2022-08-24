
import sys
import time
import sdl2
import sdl2.ext
import trey.maths as maths
import trey.game_globals as game_globals


CREATE_WINDOW = True
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_NAME = "Untitled Game"

FPS_LIMIT = None  # currently there is no limit capability
RENDER_QUALITY = "best"  # only use this until add more options

'''TODO:
    - add static color object, access colors via "trey.graphics.colors.GREEN"
    - add FPS limit capabilities
    - no need for image module now that renderer is part of the graphics module
      - sprite can have optional parameters that allow for sub-image regions
'''


def initialize():
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


def draw(thing, x, y):

    assert game_globals.RENDERER, "no renderer in graphics draw"
    if isinstance(thing, Sprite):
        game_globals.RENDERER.copy(src=thing.texture, dstrect=(
            x, y), angle=thing.rotation_angle, flip=1 if thing.flip else 0)

    elif isinstance(thing, Rectangle):
        game_globals.RENDERER.fill(
            (x, y, thing.width, thing.height), thing.color)

    else:
        print("not sprite")
    # center=thing.center_of_rotation
    '''draw rectangle'''  # RENDERER.fill((0, 0, 100, 100), (0, 1, 0, 0))


def create_sprite(image):
    assert game_globals.RENDERER, "no global renderer"

    return Sprite(image, game_globals.RENDERER)


class Sprite():
    def __init__(self, image, renderer):
        print(renderer)
        self.renderer = renderer
        self.texture = sdl2.ext.Texture(self.renderer, image)

        #self.width, self.height = self.texture.size()

        self.center_of_rotation = maths.Vector2(0, 0)
        self.rotation_angle = 0
        self.flip = False

    def set_image(self, image):
        self.texture = sdl2.ext.Texture(self.renderer, image)
        #self.width, self.height = self.texture.size()

    def set_center_of_rotation(self, x, y):
        self.center_of_rotation.x = x
        self.center_of_rotation.y = y

    def set_rotation_angle(self, angle):
        self.rotation_angle = angle

    def rotate(self, angle):
        self.rotation_angle += angle

    def set_flip(self, flip):
        self.flip = flip

    def flip(self):
        self.flip = not self.flip


class AnimatedSprite:
    def __init__(self, renderer=None):
        self.renderer = renderer

        self.texture = None

        self.animations = {}
        self.active_animation = None

        self.old_time = 0
        self.time = self.old_time

    def add_animation(self, name, animation_frames, loop, delay):
        self.animations[name] = Animation(
            name, self, animation_frames, loop, delay)

    def play(self, name, frame=0):
        # check for name?
        if self.active_animation != None:
            self.stop(self.active_animation.name)
        self.active_animation = self.animations[name]
        self.active_animation.frame = frame

    def stop(self, name):
        # check for name?
        self.active_animation = None

    def update_animation(self, delta):
        if self.active_animation != None:
            self.time += delta
            if self.time - self.old_time >= self.active_animation.delay:
                if self.active_animation.loop == False and self.active_animation.frame == len(self.active_animation.animation_frames)-1:
                    self.stop(self.active_animation.name)
                else:
                    if self.active_animation.frame == len(self.active_animation.animation_frames)-1:
                        self.active_animation.frame = 0
                    else:
                        self.active_animation.frame += 1
                    self.texture = self.active_animation.animation_frames[self.active_animation.frame]
                    self.old_time = self.time

    def draw(self, x=0, y=0):
        if self.texture != None:
            self.renderer.copy(self.texture, dstrect=(x, y))
        '''
        else:
            print("{}, texture is None").format(self)
            '''


class Animation:
    def __init__(self, name, sprite, animation_frames, loop=None, delay=None):
        self.name = name
        self.sprite = sprite
        self.animation_frames = animation_frames
        self.loop = loop or False
        self.delay = delay
        self.animation_frames = [sdl2.ext.Texture(
            self.sprite.renderer, frame) for frame in self.animation_frames]

        self.frame = 0


class Spritesheet():
    def __init__(self, image, renderer):
        self.image = image
        self.renderer = renderer

    def create_animation_frames(self, x, y, width, height, direction, length):
        '''creates an array of textures that can be drawn by an animated sprite'''
        frames = []
        for i in range(length):
            if direction == "right":
                frames.append(sdl2.ext.surface.subsurface(
                    self.image, (x + width*i, y, width, height)))
            elif direction == "down":
                frames.append(sdl2.ext.surface.subsurface(
                    self.image, (x, y + width*i, width, height)))
            elif direction == "left":
                frames.append(sdl2.ext.surface.subsurface(
                    self.image, (x-width*i, y, width, height)))
            elif direction == "up":
                frames.append(sdl2.ext.surface.subsurface(
                    self.image, (x, y-width*i, width, height)))
            else:
                print("Error, I don't know what direction that is")

        return frames


class Rectangle:
    def __init__(self, width, height, color=None):
        self.width = width
        self.height = height
        self.color = color or colors.WHITE
