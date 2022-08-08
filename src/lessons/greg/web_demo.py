
from pywebio.input import *


def check_age(p):
    if p < 25:
        return 'Too young!!'
    if p > 60:
        return 'Too old!!'

data = input_group(
    "User data",
    [
        # value keeps track of the "current" value, allowing us to edit
        input("What is your Name?", name="name", type=TEXT, value="ABC"),
        # validate points to a function to verify the data is entered correctly
        input("Input your age", name="age", type=NUMBER, value="22", validate=check_age),
        radio(
            "Which Continent?",
            name="continent",
            options=[
                "Africa",
                "Asia",
                "Australia",
                "Europe",
                "North America",
                "South America",
            ],
        ),
        checkbox(
            "User Term", name="agreement", options=["I agree to terms and conditions"]
        ),
    ],
)
