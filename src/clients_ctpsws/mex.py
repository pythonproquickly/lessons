import math


def f(x):
    return math.sqrt(math.log(x))


def f2(x):
    return math.log(x) ** 0.5


print(Derivative(f(3)))
print(f2(3))


# ---

def f(x):
    if x < 1:
        return (x ** 2) - 2
    return (x * -1) ** 2


print(f(-1))
import random

results = []
for _ in range(1, 401):
    result = random.uniform(-5.0, 5.0)
    results.append(result)

for result in results:
    # calc derivative of result
    print(result)


# -----
def u(x):
    return (x ** 2) - (3 * x)


def v(x):
    return math.sqrt(math.log(x) + x)


def f(x):
    u_value = u(x)
    v_value = v(x)
    return u_value * v_value


# calc derivatives here

print(f(10))
# print derivative of f

myarray = [9, 3, 5, 2, 5]
print(myarray[0: 5])
print(myarray[0: 2])
