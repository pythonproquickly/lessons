"""some representative examples"""

from itertools import chain
print(chain([1,2,3], [4,5,6]))

from itertools import permutations
assert list(permutations('ABCD', 2)) == [
    ('A', 'B'), ('A', 'C'), ('A', 'D'),
    ('B', 'A'), ('B', 'C'), ('B', 'D'),
    ('C', 'A'), ('C', 'B'), ('C', 'D'),
    ('D', 'A'), ('D', 'B'), ('D', 'C')]

from itertools import islice

assert list(islice('ABCDEFG', 2, 4)) == ['C', 'D']

from itertools import product

assert list(product('ABCD', 'xy')) == [
    ('A', 'x'), ('A', 'y'), ('B', 'x'), ('B', 'y'),
    ('C', 'x'), ('C', 'y'), ('D', 'x'), ('D', 'y')]
