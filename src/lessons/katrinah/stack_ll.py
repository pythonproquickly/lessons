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


s = Stack([1, 2, 3])
s.push(999)
x = s.pop()
y = s.pop()
x = s.pop()
y = s.pop()
x = s.pop()
y = s.pop()


