
def calculate(length, height, multipler, thing):
    x = length * height
    y = x * multipler
    return y


result = calculate(10, 12, 5, 999)

print(result)


class Person:
    pass


class Employee:
    def __init__(self, ssn):
        self.ssn = ssn

    def say_hello(self, message):
        self.x = "abd" + self.ssn
        print(message)



accountant = Employee('1122333333')
accountant.say_hello("xxxxxxxxx")
print(accountant.ssn)
print(accountant.x)

cleaner = Employee('72772828')
cleaner.say_hello("pppppp")
print(cleaner.ssn)
print(cleaner.x)
