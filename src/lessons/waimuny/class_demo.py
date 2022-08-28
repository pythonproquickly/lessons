class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello from {self.name}")

    def __str__(self):
        return f"{self.name} is {self.age} years old"


class Employee(Person):
    pass


banker = Person("andy", 42)
banker.say_hello()
print(banker.name)
print(banker)

manager = Person("fred", 55)
manager.say_hello()
print(manager.name)
print(manager)
