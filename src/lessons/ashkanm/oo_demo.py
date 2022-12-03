#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Person:

    def __init__(self, name):
        self.name = name
        self.age = 0

    def say_hello(self):
        print(self.age)
        print("Hello from person")


class Male(Person):
    pass


andy = Person("andy miles")
andy.say_hello()
print(andy.age)
print(andy.name)
andy.age = 55
print(andy.age)

fred = Person("fred smith")
fred.say_hello()

age = 42

age = "zzz"

height = 9.1

numbers = [1, 3, 5, 2]
more_numbers = (5, 7, 7, 9, 1)
numbers.append(9999)
more_numbers = (2, 4)
