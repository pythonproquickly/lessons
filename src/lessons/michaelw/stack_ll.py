

class Stack:
    def __init__(self, the_stack):
        self.__the_stack = the_stack

    def push(self, item):
        self.__the_stack.append(item)

    def pop(self):
        popped = self.__the_stack[-1]
        del self.__the_stack[-1]
        return popped


s = Stack([1, 2, 3])
print(s.__the_stack)
s.push(999)
print(s.__the_stack)
x = s.pop()
y = s.pop()
print(s.__the_stack)
