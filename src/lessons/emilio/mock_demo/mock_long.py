import examples.mocks.sut


def test_big_long_func(mocker):
    mocker.patch("examples.mocks.sut.big_long_func", return_value=True)
    done = examples.mocks.sut.do_something()
    assert examples.mocks.sut.do_something() is True
