class AClass:
    def __new__(cls, *args, **kwargs):
        print('constructing')
        return super().__new__(cls)

    def __init__(self, value):
        print('initializing')
        self.value = value


print(AClass(1).value)

input()

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(radius=diameter / 2)


print(Circle(5).radius)

print(Circle.from_diameter(10).radius)



class Thingy:
    def __init__(self, data=None):
        # set attributes based on data

    @classmethod
    def data_from_txtfile(cls, file):
        # validate file exists
        # data = data read from file
        # return instance of class created from data
        return cls(data=data)

    @classmethod
    def data_from_excelfile(cls, file):
        # validate file exists
        # parse file / create pandas dataframe
        # data = some data from parse or dataframe
        # return instance of class created from data
        return cls(data=data)

    @classmethod
    def data_from_csvfile(cls, file):
        # validate file exists
        # do stuff to the csv
        # data = some data from csv file
        # return instance of class created from data
        return cls(data=data)
