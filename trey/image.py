import sdl2
import sdl2.ext

images = {}


def load(name, path, x=None, y=None, width=None, height=None):
    '''add option to load without a name, so that the path is just placed as the name'''
    if x == None:
        images[name] = sdl2.ext.load_img(path)
        print(images)
    else:
        if x and y and width and height:
            temp_image = sdl2.ext.load_img(path)
            images[name] = sdl2.ext.surface.subsurface(
                temp_image, (x, y, width, height))
        else:
            '''print error'''
            pass


def get(name):
    if name in images.keys():
        return images[name]
    else:
        print("name of image does not exist")
        '''print error'''
        pass
