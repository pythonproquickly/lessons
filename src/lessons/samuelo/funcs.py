#!/usr/bin/env python
# -*- coding: utf-8 -*-

numbers = [1, 2, 3]

more_numbers = numbers.copy()

print(numbers)
print(more_numbers)

more_numbers.append("abc")

print(numbers)
print(more_numbers)


def addup(x, y):
    return x + y


def subtract(x, y):
    return x - y


print(addup(2, 3))

print(subtract(7, 2))


def calculate(f, x, y):
    return f(x, y)


print(calculate(subtract, 9, 10))

action = 2
actions = {1: addup, 2: subtract}

print(f"my actions is {actions[action](2, 3)}")

action = 1
if action == 1:
    addup(9, 8)
elif action == 2:
    subtract(8, 7)

import pysnooper


#@pysnooper.snoop()
def calculate_factorial(n):
    if n == 1:
        return n
    return n * calculate_factorial(n - 1)


print(calculate_factorial(5))

print("-" * 30)
xyz = print

xyz("xyz")
