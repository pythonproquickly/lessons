def factorial(n):
    if n == 1:
        return n
    return n * factorial(n - 1)


print(factorial(5))  # == 120

"""
                factorial : n 1 -|
            factorial : 2           1 * 2 -|
        factorial : n 3                         2 * 3
    factorial : n 4                                     6 * 4
factorial : n 5                                                 24 * 5 == 120
"""
