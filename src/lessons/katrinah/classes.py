class Person:
    def __init__(self, name):
        self.name = name

    def talk(self, message):
        print(message)

    def say_goodbye(self):
        print("goodbye")


person1 = Person("andy")
print(person1.name)
person1.talk("hello from me")
person1.say_goodbye()


person2 = Person("fred")
print(person2.name)
person2.talk("abc")
