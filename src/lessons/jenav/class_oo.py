class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"hello {self.name} I see you are {self.age} years old")


manager = Person("andy", 42)
manager.say_hello()
print(manager.name)
worker = Person("fred", 76)
worker.say_hello()
print(worker.name)
