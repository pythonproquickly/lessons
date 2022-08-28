import pysnooper

# @pysnooper.snoop()


def factorial(n):
    if n == 1:
        return n
    return n * factorial(n - 1)


result = factorial(4)
print(result)
# 9! == 9 * 8 * 7 ....
