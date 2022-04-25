def factorial(n):
    if n == 1:
        return n
    return n * factorial(n - 1)


result = factorial(4)
print(result)
# 9! == 9 * 8 * 7 ....

"""
4 * (4-1 | 3) * (3-1 | 2) * (2-1 | 1)

"""


def recurse(n):
    if n == 2:
        return n
    return n + recurse(n - 1)


result = recurse(6)
print(result)

"""
5. recurse n = 2
4. recurse n = 3
3. recurse n = 4
2. recurse n = 5
1. recurse n = 6 
"""
