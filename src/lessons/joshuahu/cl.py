class Person:
    def __init__(self, name):
        self.name: str = name

    def say(self):
        print("hello")

    def get_name(self):
        return self.name

andy = Person()

andy.say()

myname = andy.name
andy.name = 999


print(myname)
