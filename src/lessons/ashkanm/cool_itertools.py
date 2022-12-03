from itertools import count
from itertools import cycle
from itertools import islice

counter = count(start=6)
assert next(counter) == 6

people = ['andy', 'sue', 'fred', 'pete']
colors = cycle(people)

explain_cycle = []
for n in range(5):
    explain_cycle.append(next(colors))

assert explain_cycle == ['andy', 'sue', 'fred', 'pete', 'andy']

assert islice(people, 1, 3) == ['sue', 'fred']
