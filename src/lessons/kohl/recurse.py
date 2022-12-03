# calculate

"""
5! 5 * 4 * 3 * 2 * 1
- the product of all values from n to 1
"""

n = 80
result = 1
for value in range(1, n + 1):
    result = result * value

print(result)


def calculate_factorial(n):
    if n == 1:
        return n
    return n * calculate_factorial(n - 1)


answer = calculate_factorial(20)
print(answer)

"""
                cf n is 1
            cf n is 2
        cf n is 3
    cf n is 4
cf n is 5

"""
