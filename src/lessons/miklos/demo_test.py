def addup(first, second):
    first = first / 2
    return first + second


def test_addup():
    assert addup(5, 6) == 11


def test_subber():
    assert subber(6, 5) == 1
