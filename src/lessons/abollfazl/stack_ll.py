class Stack:
    # LIFO
    def __init__(self, the_stack):
        self.__the_stack = the_stack

    def push(self, item):
        self.__the_stack.append(item)

    def pop(self):
        popped = self.__the_stack[-1]
        del self.__the_stack[-1]
        return popped

    def __repr__(self):
        return "|".join(self.__the_stack)


s = Stack(["1", "2", "3"])
s.push("999")
s.pop()
s.pop()
print(repr(s))


class Queue:
    # FIFO
    pass
