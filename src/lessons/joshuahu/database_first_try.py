import os
from datetime import date

from peewee import *

db = SqliteDatabase("Educational institute")


class University(Model):
    name = CharField()
    school_ID = AutoField()
    founding_date = DateField()

    class Meta:
        database = db


class Faculty(Model):
    university = ForeignKeyField(University, backref="university")
    name = CharField()
    numer_of_students = AutoField()

    class Meta:
        database = db


class Student(Model):
    university = ForeignKeyField(University, backref="student")
    faculty = ForeignKeyField(Faculty, backref="student")
    student_ID = AutoField()
    name = CharField()
    age = AutoField()

    class Meta:
        database = db


class Professor(Model):
    university = ForeignKeyField(University, backref="professor")
    faculty = ForeignKeyField(Faculty, backref="professor")  # is there a way to allow a professor to teach in
    # multiple faculties?
    name = CharField()
    professor_ID = AutoField()

    class Meta:
        database = db


def create_tables(database):
    database.create_tables([University, Faculty, Student, Professor])


def add_data():
    harvard_university = University(name="Harvard", school_ID=1, founding_date=date(1636, 8, 9))
    oxford_university = University(name="Oxford", school_ID=2, founding_date=date(1096, 0, 0))
    faculty_philosophy_harvard = Faculty(university=harvard_university, name="Philosophy",
                                         number_of_students=22947)
    faculty_cs_oxford = Faculty(university=oxford_university, name="Computer Science", number_of_students=25820)
    joshua_hu = Student(university=oxford_university, faculty=faculty_cs_oxford, student_ID=983, name="Joshua Hu",
                        age=21)
    professor_blunsom = Professor(university=oxford_university, faculty=faculty_cs_oxford, name="Phil Blunsom",
                                  professor_ID=54)
    harvard_university.save()
    oxford_university.save()
    faculty_philosophy_harvard.save()
    faculty_cs_oxford.save()
    joshua_hu.save()
    professor_blunsom.save()


def delete_university(harvard_university):
    harvard_university.delete_instance()


def show_faculty_students():
    Faculty.select(Faculty.name == "Computer Science")
    for faculty in Faculty.select():
        print(f"{Faculty.name}")

        query = (Student
                 .select(Student, Faculty, University)
                 .join(Faculty, University)
                 .where(University.name == "Oxford", Faculty.name == "Computer Science"))
        for student in query:
            print(Student.name, Faculty.name, University.name)


if __name__ == "__main__":
    db.connect()
    create_tables(db)
    add_data()
    """delete_university(harvard_university)"""  #What's wrong here?
    show_faculty_students()
    db.close()



# can I use Datefield() if I only know the year?
    # I noticed that Pycharm does not provide support when you're typing in the parameters. Why is this?
    # Why do I have to type in the name of the variable as well?
