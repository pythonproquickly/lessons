"""
implement a stack
demo using it

implement a class called Stack
takes a list on initialization
implement push method
 - single parameter, add to end
implement pop mtheod
 - no parameter, remove from end and return
"""


class Stack:
    def __init__(self, stack):
        self.__the_stack = stack

    def push(self, stack_item):
        self.__the_stack.append(stack_item)

    def pop(self):
        if len(self.__the_stack) < 1:
            raise ValueError
        result = self.__the_stack[-1]
        del self.__the_stack[-1]
        return result


s = Stack([0, 1, 3])
s.pop()  # remove 3
s.push(999)
s.push(998)
# print(s.__the_stack)
# stack is 0,1,999,998
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()


A - B _ C
push D
A - B C-D
pop
A - B _ C
