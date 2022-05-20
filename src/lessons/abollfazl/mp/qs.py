import threading
import queue
import time
from random import randrange

b = [randrange(20) for _ in range(30)]


class Worker(threading.Thread):
    def __init__(self, q, other_arg, *args, **kwargs):
        self.q = q
        self.other_arg = other_arg
        super().__init__(*args, **kwargs)

    def run(self):
        while True:
            try:
                work = self.q.get(timeout=3)  # 3s timeout
            except queue.Empty:
                return
            print("I do my work here...")
            work = randrange(20)
            time.sleep(work)
            print(f"I'm done: it took {work}")
            self.q.task_done()


q = queue.Queue()
for ptf in b:
    q.put_nowait(ptf)
for _ in range(20):
    Worker(q, ("a", 1, "ABC")).start()
q.join()  # blocks until the queue is empty.
