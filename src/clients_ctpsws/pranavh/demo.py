def addup(lhs: int, rhs: int) -> int:
    return lhs + rhs


def subber(lhs, rhs):
    return lhs - rhs


def test_addup_happy():
    assert addup(1.1, 2.2) == 3


def calculate(f, lhs, rhs):
    return f(lhs, rhs)


print(calculate(addup, 3, 4))
