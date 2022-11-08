from unittest.mock import mock_open
from unittest.mock import patch

import pytest


@pytest.fixture
def file_data():
    return "abc\n123\nxyz"


def test_read_file(file_data):
    with patch("builtins.open", mock_open(read_data=file_data)) as mock_file:
        assert open("/home/andy/myfile").read() == file_data
    mock_file.assert_called_with("/home/andy/myfile")


def test_write_file(file_data):
    test_data = file_data
    with patch('builtins.open',
               mock_open(read_data=test_data), create=True) as mock_file:
        assert open("/home/andy/myfile", "w").write() is None
    mock_file.assert_called_with("/home/andy/myfile", 'w')
