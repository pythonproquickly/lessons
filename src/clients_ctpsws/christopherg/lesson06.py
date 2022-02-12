def play_with_numbers(numbers):
    largest = float("-inf")
    for number in numbers:
        if number > largest:
            largest = number

    return largest


def test_play_with_numbers_scenario1():
    assert play_with_numbers([0, -1, 4, 6]) == 6


def test_play_with_numbers_scenario2():
    assert play_with_numbers([999, 345, -4, 35]) == 999


def test_play_with_numbers_scenario3():
    assert play_with_numbers([-90, -70, -999]) == -70


def test_play_with_numbers_scenario4():
    assert play_with_numbers(["aa", "b", "xyz"]) == "xyz"
