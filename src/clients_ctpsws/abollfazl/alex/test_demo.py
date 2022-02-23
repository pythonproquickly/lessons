def addup(numbers_to_add):
    return sum(numbers_to_add)

def subtract(lhs, rhs):
    return lhs - rhs

def test_addup():
    assert addup([2, 5, 3]) == 10

def test_subtract():
    assert subtract(10, 7) == 3
