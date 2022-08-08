from collections import defaultdict
from collections import OrderedDict

ints_r = dict()
try:
    a = ints_r[1]
except KeyError as e:
    assert isinstance(e, KeyError)


ints_d = defaultdict(int)

a = ints_d[1]
assert a == 0

ints_o = OrderedDict()

ints_o[0] = 'a'
ints_o[1] = 'b'
assert ints_o == {0: 'a', 1: 'b'}

ints_o.move_to_end(0, True)
assert ints_o == {1: 'b', 0: 'a'}

ints_o[2] = 'c'
assert ints_o == {1: 'b', 0: 'a', 2: 'c'}

ints_o.move_to_end(2, False)
assert ints_o == {2: 'c', 1: 'b', 0: 'a'}

chars = OrderedDict.fromkeys("abcdef")
assert chars == OrderedDict([
    ('a', None), ('b', None), ('c', None), ('d', None), ('e', None), ('f', None)
])
