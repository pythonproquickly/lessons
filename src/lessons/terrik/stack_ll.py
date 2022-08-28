import array as arr
MAX_SIZE = 100

class StackAndQueue:
    def __init__(self, size):
        if size > MAX_SIZE:
            raise ValueError
        self.size = 0
        # self.the_sq = []
        self.the_sq = arr.array('i')


    def push(self, item):
        if self.size > MAX_SIZE:
            raise ValueError
        self.size += 1
        self.the_sq.append(item)

    def pop(self):
        if self.size > 0:
            self.size -= 1
            popped = self.the_sq.pop(-1)
            return popped
        else:
            return -1

    def enqueue(self, data):
        if self.size > MAX_SIZE:
            raise ValueError
        self.size += 1
        self.the_sq.append(data)

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            popped = self.the_sq.pop(0)
            return popped
        else:
            return -1


s = StackAndQueue(100)
s.push(10)
s.push(11)
s.push(12)
print(s.the_sq)
s.enqueue(80)
print(s.the_sq)
s.dequeue()
print(s.the_sq)
s.pop()
print(s.the_sq)
s.pop()
s.pop()
s.pop()
print(s.pop())
