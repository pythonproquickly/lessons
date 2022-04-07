def increment_by_one(number):
    return number + 1


assert (lambda x: x + 1)(2) == increment_by_one(2)

assert (lambda x, y: x + y)(10, 20) == 30

assert (lambda *args: sum(args))(1, 2, 9) == 12

sequences = [10, 2, 8, 7, 5, 4, 3, 11, 0, 1]
filtered_result = map(lambda x: x * x, sequences)
print(list(filtered_result))
