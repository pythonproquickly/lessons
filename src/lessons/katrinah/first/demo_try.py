

def div(numerator, denominator):
    if denominator == 0:
        raise ZeroDivisionError
    result = numerator / denominator
    return result


try:
    answer = div(4, 0)
except ZeroDivisionError:
    print("dont divide by zero")

try:
    answer = div(4, 0)
except ZeroDivisionError:
    answer = div(4, 1)
