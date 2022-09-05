"""
5! = 5 * 4 * 3 * 2 * 1 == 120
"""

"""results = 1
factorial = 8

for number in range(1, factorial + 1):
    results = results * number

print(results)
"""


def calculate_factorial(n):
    # part 1 - "stop condition
    if n == 1:
        return n
    # part 2 - recursive call
    return n * calculate_factorial(n - 1)


print(calculate_factorial(5))


calculate : n is 1
#-----------------------------#
calculate : n is 2
#-----------------------------#
calculate : n is 3
#-----------------------------#
calculate : n is 4
#-----------------------------#
calculate : n is 5
#-----------------------------#
n == 5
