class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []


q = Queue()
q.enqueue(1)
q.dequeue()
if not q.is_empty:
    q.dequeue()
else:
    print("cant pop")


