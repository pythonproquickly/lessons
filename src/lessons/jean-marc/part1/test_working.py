import working

# # import pytest
# # Type 9 AM to 5 PM, followed by Enter. Your program should output 09:00 to 17:00.
# # Type 9:00 AM to 5:00 PM, followed by Enter. Your program should again output 09:00 to 17:00.
# # Type 10 PM to 8 AM, followed by Enter. Your program should output 22:00 to 08:00.
# # Type 10:30 PM to 8:50 AM, followed by Enter. Your program should again output 22:30 to 08:50.

# def test_valid():
#     # assert (convert("9 AM to 5 PM") == "09:00 to 17:00")
#     # assert (convert("9:00 AM to 5:00 PM") == "09:00 to 17:00")
#     # assert (convert("10 PM to 8 AM") == "22:00 to 08:00")
#     # assert (convert("10:30 PM to 8:50 AM") == "22:30 to 08:50")
#     assert convert("9 AM to 5 PM") == "09:00 to 17:00"
#     assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
#     assert convert("10 PM to 8 AM") == "22:00 to 08:00"
#     assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

# # ValueError by typing 9:60 AM to 5:60 PM, followed by Enter. Your program should indeed raise a ValueError.
# # ValueError by typing 9 AM - 5 PM, followed by Enter. Your program should indeed raise a ValueError.
# # ValueError by typing 09:00 AM - 17:00 PM, followed by Enter. Your program should indeed raise a ValueError.

# def test_raise1():
#     with pytest.raises(ValueError):
#         convert("9:60 AM to 5:60 PM")
#     with pytest.raises(ValueError):
#         convert("9 AM - 5 PM")
#     with pytest.raises(ValueError):
#         convert("09:00 AM - 17:00 PM")


def test_convert():
    assert working.convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

    # DON'T UNDERSTAND
    # assert (convert("1:09 AM to 5:00 PM") == "01:09 to 17:00")
    # assert (convert("10:30 PM to 8:50 AM") == "22:30 to 08:50")
    # assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    # assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    # with pytest.raises(ValueError):
    #     convert("9AM to 5PM")
    # with pytest.raises(ValueError):
    #     convert("9 AM - 5 PM")
    # with pytest.raises(ValueError):
    #     convert("13:00 AM to 5:00 PM") #Hours > 12
    # with pytest.raises(ValueError):
    #     convert("9:61 AM to 5:00 PM") #Minutes > 60
    # with pytest.raises(ValueError):
    #     convert("9:00 AM 5:00 PM") #Omits to
    # with pytest.raises(ValueError):
    #     convert("26:00 AM to 5:00 PM")
