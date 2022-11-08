import os

import pytest


def read_file(filename):
    with open(filename, 'r') as f:
        return f.readlines()



def test_fileops(mocker):
    mocker.patch("open")
    read_file("xxxxxx")
    open.assert_called_once_with('filename')
    assert isinstance(read_file(filename), list)


@pytest.fixture
def get_test_data_valid():
    return [
        "one",
        "two",
    ]

def test_read_file(get_test_data):
