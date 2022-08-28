class Queue:
    def __init__(self):
        self.__queuelist = []

    def enqueue(self, data):
        self.__queuelist.append(data)

    def remove(self):
        removed = self.peek()
        del self.__queuelist[0]
        return removed

    def peek(self):
        return self.__queuelist[0]


q = Queue()
q.enqueue(1)
q.enqueue(2)
a = q.remove()
q.enqueue(3)
b = q.remove()
print(a, b)
