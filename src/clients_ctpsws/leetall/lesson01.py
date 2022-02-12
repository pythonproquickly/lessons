
def addup(lhs, rhs):
    result = lhs + rhs
    print(" result is")
    print(result)

print(addup(3, 4))
print(addup(45, 99))


class Person:
    def __init__(self, ssn, name):
        self.ssn = ssn
        self.name = name

    def say_hello(self):
        print("Hello")

age = 42

person1 = Person("999-99-9999", "andy")
person1.say_hello()
print(person1.ssn)

class A:
    b = 1

a= A()
c = A()
c.a = 9
print(a.b)
print(c.a)
