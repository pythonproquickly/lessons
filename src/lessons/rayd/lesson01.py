#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
factorial 5
5 * 4 * 3 * 2 * 1

"""


def ixyz(n):
    return n * ixyz(n - 1)


print(ixyz(5))
"""








                           n : 1
                     n : 2
               n : 3
         n : 4
n : 5 cf


1, 1, 2, 3, 5, 8, 13, 21

"""
