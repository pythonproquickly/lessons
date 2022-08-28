import sut


def test_big_long_func(mocker):
    mocker.patch("sut.big_long_func", return_value=True)
    done = sut.do_something()
    assert sut.do_something() is True
