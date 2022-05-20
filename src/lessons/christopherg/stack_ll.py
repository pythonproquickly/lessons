class Stack:
    def __init__(self, the_stack):
        self.__the_stack = the_stack

    def push(self, item):
        self.__the_stack.append(item)

    def pop(self):
        if len(self.__the_stack) < 1:
            raise ValueError
        popped = self.__the_stack[-1]
        del self.__the_stack[-1]
        return popped


s = Stack([])

s.push(999)
s.push(998)
s.push(997)
s.push(996)

s.pop()
x = s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
print(x)


"""
def a():
    x = 9
    b()

def b():
    d = 9
    c()



a()

c
b
a
-

3 + 4 + 5 + 6 * 7

*
5
4
3
+
"""
