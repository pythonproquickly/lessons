# display menu
option = 1


def addup(number1, number2):
    return number1 + number2


def subtract(number1, number2):
    return number1 - number2


def calculate(f, number1, number2):
    return f(number1, number2)


options = {
    1: addup,
    2: subtract
}

print(options[option](10, 7))
