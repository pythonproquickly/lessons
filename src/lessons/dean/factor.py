"""
Factorials: 
    3: 3 * 2 * 1 = 6
    4: 4 * 3 * 2 * 1 = 25
    5: 5 * 4 * 3 * 2 * 1 = 120

3 4 and 5 here we call n. Factorial is all the values of n to 1
multiplied by each other.

"""

n = 5
result = 5
while n > 1:
    n -= 1
    result = result * n

#print(result)

n = 5
result = 1
for number in range(n, 0, -1):
    result = result * number
# print(result)


def factorial(n):
    if n == 1:
        return n
    return n * factorial(n - 1)

print(factorial(6))




factorial(1) - n == 1
#---------------------#
factorial(2) - n == 2
#---------------------#
factorial(3) - n == 3
#---------------------#
factorial(4) - n == 4
#---------------------#
factorial(5) - n == 5
#---------------------#
factorial(6) - n == 6
#---------------------#

def b():
    return 999


def a(k):
    x = k * 10
    y = b(x)
    return y


number1 = a(8)

mumber2 = b()


b(90)
#---------------------#
