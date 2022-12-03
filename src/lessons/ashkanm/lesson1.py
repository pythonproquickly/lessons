#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

#Write a package that exports a class "Variable"

#Call it as

# from assignment import Expression, Variable
# import assignment
# reference as assignment.Expression
# assignment.Variable


# these go in separate file called assignment
class Stack:

    def __init__(self):
        self.the_stack = []

    def push(self, stack_item):
        pass

    def pop(self):
        pass


class Expression:

    def __init__(self):
        self.assembly = Stack()


class Variable(Object):

    def __init__(self, variable_name):
        if str(variable_name).isdigit():
            self.value = variable_name
        else:
            self.variable_name = variable_name
            self.value = None
        self.tree = Expression()
    def __add_(self, ...):
        return ...


# end of separate file

#Then provide below functionalities :

a = Variable('a')
b = Variable('b')
c = Variable('c')
a.value = 1
b.value = 2
c.value = 3

z = (a + b) * c + Variable(7)

# z.tree.assembly.eval()) --> evaluate z

assert z.tree.assembly.eval() == 16

print(z.tree)
#                   +
#                   |\
#                   * 7
#                  /|
#                 + c
#                /|
#               a b

print(z.tree.assembly)
#   PUSH a
#   PUSH b
#   ADD
#   PUSH c
#   MULT
#   PUSH 7
#   ADD
