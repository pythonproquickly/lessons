class Teacher:
    def __init__(self, subject):
        self.subject_taught = subject

    def grade_homework(self):
        return "A"

    def shout(self):
        return "Stop talking"


fred = Teacher("math")
andy = Teacher("computers")

home_grade = fred.grade_homework()
fred.shout()
print(fred.subject_taught)
print(andy.subject_taught)
