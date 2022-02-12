class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self, size):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


block_1 = Rectangle(12, 5)
assert block_1.calculate_area("medium") == 60
assert block_1.calculate_perimeter() == 34
assert block_1.width == 12

block_2 = Rectangle(10, 4)
