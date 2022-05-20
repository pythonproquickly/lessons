def addup(lhs, rhs):
    return lhs + rhs


def subtract(lhs, rhs):
    return lhs - rhs


def calculate(f, lhs, rhs):
    return f(lhs, rhs)


print(calculate(addup, 1, 2))
