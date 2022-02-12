class Person:
    pass


andy = Person()
assert str(type(andy)) == "<class '__main__.Person'>"


class Vehicle:
    def __init__(self, owner_name):
        self.owner_name = owner_name


my_car = Vehicle("andy's")
assert my_car.owner_name == "andy's"
my_car.owner_name = "Fred"
assert my_car.owner_name == "Fred"


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


block_1 = Rectangle(12, 5)
assert block_1.area() == 60
assert block_1.perimeter() == 34
