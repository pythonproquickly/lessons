import math


class Pizza:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    # conceptually, I "belong" to the class (but a subtle point)
    @staticmethod
    def compute_area(radius):
        return math.pi * (radius ** 2)

    # i can use properties of the class
    @classmethod
    def compute_volume(cls, height, radius):
        return height * cls.compute_area(radius)

    def get_volume(self):
        return self.compute_volume(self.height, self.radius)


another_pizza = Pizza.compute_area(6)
print(another_pizza)


pizza_volume = Pizza.compute_volume(3, 4)
print(pizza_volume)
