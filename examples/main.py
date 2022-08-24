import trey


class BaseScene():
    def __init__(self):
        pass

    def start(self):
        print("start function called in base_scene")
        self.kitten = trey.graphics.create_sprite(
            trey.window.image.get("kitten"))
        self.rectangle = trey.graphics.Rectangle(
            100, 200, trey.colors.from_rgb(234, 90, 87))
        print(self.kitten)
        pass

    def update(self, dt):
        print("update")
        pass

    def render(self, dt):
        # z is defined by which object is drawn first
        trey.graphics.draw(self.kitten, 0, 0)
        trey.graphics.draw(self.rectangle, 200, 300)

        pass


base_scene = BaseScene()
trey.window.initialize()
trey.image.load("kitten", "resources/kitten.jpg")  # change path for yourself
print(trey.maths.PI)

trey.window.start(base_scene)
