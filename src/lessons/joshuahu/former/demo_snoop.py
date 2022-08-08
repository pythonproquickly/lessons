import pysnooper


@pysnooper.snoop()
def addup(number1, number2):
    total = number1 + number2
    total = total * 1.05
    return round(total, 4)


print(addup(34, 100))
