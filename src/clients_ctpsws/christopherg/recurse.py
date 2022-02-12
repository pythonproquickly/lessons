import pysnooper


@pysnooper.snoop()
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
    if n == -4:
        return n
    return n + recurse(n - 1)


print(recurse(6))
