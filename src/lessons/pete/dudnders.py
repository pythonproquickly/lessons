class Person:
    def __init__(self, name):
        self.name = name

    def __iter__(self):
        return

    def __str__(self):
        return f"name is {self.name}"

    def __repr__(self):
        return "{name='" + self.name + "'}"


developer = Person("andy")
print(developer.name)

print(developer)
print(repr(developer))

for person in Person:
