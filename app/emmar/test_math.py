import mathm


def test_adder_integers():
    booking = {...}
    assert mathm.addup(2, 4) == 6


def test_adder_string():
    assert mathm.addup("b", "a") == "ba"
