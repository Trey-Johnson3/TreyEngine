'''none of this is currently functional'''
import trey.game_globals as game_globals


def set_scene(new_scene):
    game_globals.CUREENT_SCENE = new_scene
    '''add ability to destory old scene'''


class Scene:
    def __init__(self):
        pass

    def start(self):
        pass

    def update(self):
        pass

    def render(self):
        pass
