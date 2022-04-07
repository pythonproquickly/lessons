from itertools import islice


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


series1 = Fibonacci()
result1 = list(islice(series1, 10, 14)).copy()
assert result1 == [89, 144, 233, 377]


def fibonacci():
    previous, current = 0, 1
    while True:
        yield current
        previous, current = current, previous + current


series2 = fibonacci()
result2 = list(islice(series2, 10, 14)).copy()
assert result2 == result1
