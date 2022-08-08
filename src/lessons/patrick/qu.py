class Queue:
    def __init__(self):
        self.queue = list()

    def addToQueue(self, value):
        # Insert method to add element
        if value not in self.queue:
            self.queue.insert(0, value)
            return True
        return False

    # Pop method to remove element
    def removefromQueue(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return "No elements in Queue!"


q = Queue()
q.addToQueue(1)
q.addToQueue(2)
print(q.removefromQueue())  # 1 because FIFO
