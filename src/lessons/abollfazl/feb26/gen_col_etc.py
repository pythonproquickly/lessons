from itertools import islice
from collections import deque
from collections import Counter
from collections import namedtuple
from functools import cache  # use @cache to decorate a function
from functools import partial
import itertools as it


# generators


def fibonacci():
    previous, current = 0, 1
    while True:
        # next line makes me a generator
        yield current
        previous, current = current, previous + current


fibonacci_series = fibonacci()
print(fibonacci_series)
print(next(fibonacci_series))
print(next(fibonacci_series))
print(next(fibonacci_series))
print(next(fibonacci_series))
print(next(fibonacci_series))

fibonacci_series = fibonacci()
result = list(islice(fibonacci_series, 0, 5)).copy()
print(result)

fibonacci_series = fibonacci()
result = list(islice(fibonacci_series, 100, 145)).copy()
print(result)


class Fibonacci:
    def __init__(self):
        self.previous_number = 0
        self.current_number = 1

    def __iter__(self):
        return self

    def __next__(self):
        current_number = self.current_number
        self.previous_number, self.current_number = (
            self.current_number,
            self.previous_number + self.current_number,
        )
        return current_number


another_series = Fibonacci()
print(next(another_series))
print(next(another_series))
print(next(another_series))
print(next(another_series))
print(next(another_series))

# Deque

names = deque()
names.append("andy")
names.appendleft("fred")
names.append("fred")
print(names)

# Counter

counter = Counter(names)
print(counter)
counter += Counter(["andy", "bill", "pete", "fred"])
print(counter)

print(sorted(counter.elements()))

print(counter.most_common())

# ---- Named tuple

Location = namedtuple("Location", ["lat", "long"])
loc = Location(lat=23.0012, long=80.98)
print(loc.lat, loc.long)


def big_ugly_function(origin, destination, weight, volume):
    print(f"going to {destination} from {origin} weighs {weight} size {volume}")


from_seattle = partial(big_ugly_function, origin="seattle")
to_london_from_chicago = partial(
    big_ugly_function, origin="chicago", destination="london"
)

from_seattle(destination="Houston", weight=10, volume=23.4)
to_london_from_chicago(weight=99, volume=56.34)

# itertools

x = [1, 2, 3, 4, 5]
y = ["a", "b", "c"]
print(list(zip(x, y)))
print(list(it.zip_longest(x, y)))

# combinations - set of each of 3 values
print(list(it.combinations(["a", "b", "c", "e", "f"], 3)))
