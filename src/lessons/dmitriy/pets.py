import os
from datetime import date

from peewee import *

os.remove("people.db")

db = SqliteDatabase('people.db')


class Person(Model):
    name = CharField()
    # name = PrimaryKeyField...
    birthday = DateField()

    class Meta:
        database = db  # This model uses the "people.db" database.


class Pet(Model):
    owner = ForeignKeyField(Person, backref='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db  # this model uses the "people.db" database


def main():
    db.connect()
    db.create_tables([Person, Pet])

    uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15))
    uncle_bob.save()  # bob is now stored in the database

    # alt
    grandma = Person.create(name='Grandma', birthday=date(1935, 3, 1))
    herb = Person.create(name='Herb', birthday=date(1950, 5, 5))
    grandma.save()
    herb.save()

    grandma.name = 'Grandma L.'
    grandma.save()  # Update grandma's name in the database.

    Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
    Pet.create(owner=herb, name='Fido', animal_type='dog')
    herb_mittens = Pet.create(owner=herb, name='Mittens', animal_type='cat')
    Pet.create(
        owner=herb, name='Mittens Jr', animal_type='cat')
    herb_mittens.delete_instance()

    # queries 1

    for person in Person.select():
        print(person.name)

    # 2
    query = (Pet
             .select(Pet, Person)
             .join(Person)
             .where(Pet.animal_type == 'cat'))

    for pet in query:
        print(pet.name, pet.owner.name)

    # 3
    for pet in Pet.select().join(Person).where(Person.name == 'Bob'):
        print(pet.name)
    db.close()


if __name__ == "__main__":
    main()
