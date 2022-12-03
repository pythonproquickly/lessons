#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Two:

    def __init__(self2):
        self2.a = 0

    def call_me(self, x):
        print(self.b)
        print(self2.a)
        return "x"


class One:

    def __init__(self):
        self.b = 9

    def belongs_to_class(x):
        print("hello from class")

    def say_hello(self):
        """two = Two()
        two.call_me(99)"""
        ret = Two.call_me(self, 77)
        print(f"return value from call on class = {ret}")


two = Two()
print(two.a)

one = One()
one.say_hello()
