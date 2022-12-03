class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello", self.name)


programmer = Person("Andy")
programmer.say_hello()
print(programmer.name)

manager = Person("Fred")
manager.say_hello()
print(manager.name)
