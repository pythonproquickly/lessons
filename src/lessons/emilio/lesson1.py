#!/usr/bin/env python
# -*- coding: utf-8 -*-

employees = {
    1: {
        'name': 'andy',
        'age': 43,
        'shoe_size': 9.1
    },
}


def update(mydict):
    mydict[1]['age'] = 99


update(employees)

data = {
    'first_name': {
        "Value": None,
        'prompt': "Enter first name: "
    },
    'last_name': {
        "Value": None,
        'prompt': "Enter last name: "
    },
}

for field_name, attributes in data.items():
    attributes['Value'] = input(attributes['prompt'])

print(data)


def addup(number1, number2):
    return number1 + number2


def subtract(number1, number2):
    return number1 - number2


print(subtract)


def calculate(f, x, y):
    return f(x, y)


print(calculate(addup, 5, 6))

xyz = print

xyz(9999)
