class Person:
    """this is a comment"""

    def __init__(self, name, age):
        """blah"""
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name=} : {self.age=}"


tutor = Person("andy", 22)
print(tutor)
print(tutor.__init__.__doc__)
print(dir(tutor))
