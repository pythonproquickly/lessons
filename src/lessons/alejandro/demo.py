class Person:
    def __init__(self, name):
        self.name = name
        self.items = [1, 2, 3]

    def say_hello(self):
        print("hello from person")

    def walk(self, direction):
        print("i am moving " + direction)
        return 99

    def print_list(self):
        print(self.items)


andy = Person("Andy")
print(andy.name)
andy.print_list()

andy.say_hello()

value = andy.walk("forward")

print(value)

fred = Person("Fred")
