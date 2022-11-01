class PersonPythonic:

    def __init__(self):
        self.age = 23

    def do_something(self):
        pass


class PersonNotPythonic:
    def __init__(self):
        self._age = 55

    # function to get value of age
    def get_age(self):
        print("i did something in a get")
        return self.age

    # function to set value of age
    def set_age(self, a):
        print("i did something in a set")
        self.age = a


class PersonSgPythonic:
    def __init__(self):
        self._age = 0

    @property
    def age(self):
        print("getter method called")
        return self._age

    # a setter function
    @age.setter
    def age(self, set_age):
        if set_age < 18:
            raise ValueError("Sorry you age is below eligibility criteria")
        print("setter method called")
        self._age = set_age


fred1 = PersonPythonic()
print(f"fred 1 is {fred1.age} years old")

fred2 = PersonNotPythonic()
fred2.set_age(45)
print(fred2.get_age())

fred3 = PersonSgPythonic()
fred3.age = 99
print(fred3.age)
