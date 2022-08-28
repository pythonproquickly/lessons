class Queue:
    def __init__(self):
        self.__queuelist = []

    def enqueue(self, data):
        self.__queuelist.append(data)

    def dequeue(self):
        popped = self.__queuelist.pop(0)
        return popped


q = Queue()
q.enqueue(1)
q.enqueue(2)
a = q.dequeue()
q.enqueue(3)
b = q.dequeue()
print(a, b)
