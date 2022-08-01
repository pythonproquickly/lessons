import random
from collections import Counter

random.seed(1)

randoms_to_count = [random.randint(0, 10) for _ in range(0, 100)]

count_nums = Counter(randoms_to_count)

assert count_nums == Counter({7: 13, 6: 12, 10: 11, 0: 11,
                              8: 10, 3: 9, 9: 8, 1: 8,
                              4: 7, 5: 6, 2: 5})


n1 = Counter(a=4, b=2, c=0, d=-2)
n2 = Counter(a=1, b=2, c=3, d=4)
n1.subtract(n2)
assert n1 == Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})

assert sum({n for _, n in n1.items()}) == -6