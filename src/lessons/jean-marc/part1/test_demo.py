import re
import pytest


def check_email_format(email):
    if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
        raise Exception("Invalid email format")
    else:
        return "Email format is ok"


def test_email_exception():
    with pytest.raises(Exception) as e:
        assert check_email_format("bademail.com")
    assert str(e.value) == "Invalid email format"
