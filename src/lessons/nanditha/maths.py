#!/usr/bin/env python
# -*- coding: utf-8 -*-


def addup(number1, number2):
    return number1 + number2


def subtract(n1, n2):
    return n1 - n2


def calculate(f, n1, n2):
    return f(n1, n2)


stuff = {'n1': 2, 'n2': 3, 'f': addup}

x = stuff['f']  # (stuff['n1'], stuff['n2'])

print(x)
