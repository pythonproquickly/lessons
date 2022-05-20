import pysnooper


def addup(lhs, rhs):
    return lhs + rhs


def subtract(lhs, rhs):
    return lhs - rhs


@pysnooper.snoop(depth=3)
def calculate(f, lhs, rhs):
    return f(lhs, rhs)


print(calculate(subtract, 7, 3))

data = {"quantity": addup}

data["quantity"](1, 2)
