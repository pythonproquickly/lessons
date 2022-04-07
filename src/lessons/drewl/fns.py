def another(a):
    return a + 3


def simple():
    b = another(3)
    return 1 + b


assert simple() == 7
