from datetime import date
# example - a person is acreated by default using their age
# an alternative constructore creates a Person instance using theor birth year

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, year):           # CONSTRUCTOR
        return cls(name, date.today().year - year)  # calls __init__

    def display(self):
        print("Name : ", self.name, "Age : ", self.age)


person1 = Person('mayank', 21)
person1.display()

person2 = Person.from_birth_year('mayank', 1996)
person2.display()
