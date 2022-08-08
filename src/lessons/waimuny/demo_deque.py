from collections import deque

ints_deq = deque(range(10))

ints_deq.append(999)
ints_deq.appendleft(-999)

assert isinstance(ints_deq, deque)
assert ints_deq == deque([-999, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 999])

ints_deq.extend([0, 2, 4, 3, 2, 6])
assert ints_deq.count(2) == 3

ints_deq.extendleft([2, 5, 3, 1])
assert ints_deq.count(2) == 4

assert ints_deq == deque([
    1, 3, 5, 2, -999, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 999, 0, 2, 4, 3, 2, 6])

removed = ints_deq.popleft()
assert removed == 1
assert ints_deq == deque([
    3, 5, 2, -999, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 999, 0, 2, 4, 3, 2, 6])

ints_deq.rotate(10)
assert ints_deq == deque([
    7, 8, 9, 999, 0, 2, 4, 3, 2, 6, 3, 5, 2, -999, 0, 1, 2, 3, 4, 5, 6])
