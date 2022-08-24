import math

PI = 3.14159265358979


class Math():
    def __init__(self):
        PI = 3.141592653589793
        E = 2.718281828459045

    def dot(self, vector_1, vector_2):
        if isinstance(vector_1, Vector2) and isinstance(vector_2, vector_2):
            return vector_1.x*vector_2.x + vector_1.y*vector_2.y
        else:
            return False

    def Vector2(self, x, y):
        return Vector2(x, y)


class Vector2():
    def __init__(self, x=None, y=None):
        self.x = x or 0
        self.y = y or 0

    def magnitude(self):
        return math.sqrt(math.pow(x, 2)+math.pow(y, 2))

    def square_magnitude(self):
        return math.pow(x, 2) + math.pow(y, 2)

    def normalize(self):
        temp_magnitude = self.magnitude()
        self.x = self.x/temp_magnitude
        self.y = self.y/temp_magnitude

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y+other.y)

    def __sub__(self, other):
        return Vector2(self.x-other.x, self.y-other.y)

    def __mul__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return Vector2(self.x*other, self.y*other)

    def dot(self, other):
        if isinstance(other, Vector2):
            return self.x*other.x + self.y*other.y

    def cross(self, other):
        """returns scalar z component"""
        if isinstance(other, Vector2):
            return self.x*other.y + self.y*other.x
