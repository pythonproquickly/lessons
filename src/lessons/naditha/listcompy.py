numbers = [6, 3, 7, 8, 3, 1, 7, 3]
"""squares = []

for number in numbers:
    if (number ** 2) % 2 ==0:
        squares.append(number ** 2)

print(squares)"""

"""squares = [number ** 2 for number in numbers if number **2 %2 == 0]

print(squares)"""

"""numbers = list(set(numbers))
print(numbers)"""

numbers2 = (6, 3, 7, 8, 3, 1, 7, 3)

squares2 = (number ** 2 for number in numbers2)  # generator expression
while True:
    value = next(squares2)
    print(value)

