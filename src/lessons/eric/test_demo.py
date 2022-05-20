import demo


def test_booking_simple():
    assert demo.booking(description="books", weight=8, height=10, height=5) == "BKG1"


def test_get_address():
    assert demo.get_address("Fred") == "main st, sumner"
