# LIFO
# deque
# queue


class Stack:
    def __init__(self, the_stack):
        self.the_stack = the_stack

    def push(self, item):
        self.the_stack.append(item)

    def pop(self):
        popped = self.the_stack[-1]
        del self.the_stack[-1]
        return popped


s = Stack([1, 2, 3])

print(s.the_stack)
s.push(999)
s.push(998)
print(s.the_stack)
s.pop()
print(s.the_stack)
s.pop()
s.pop()
print(s.the_stack)

"""
4 + 3 + 2

4 3 2 +

"""
