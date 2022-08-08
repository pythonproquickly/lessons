from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'favorite_color'])
person = Person('andy', 42, 'green')

assert person.name == 'andy'
assert person.age == 42
assert person.favorite_color == 'green'

assert person._fields == ('name', 'age', 'favorite_color')

assert person._replace(name='fred', age=55)  # !!! note age
assert person.name == 'andy'

person_new = person._replace(name='fred')
assert person_new.name == 'fred'
assert person is not person_new

assert person == Person(name='andy', age=42, favorite_color='green')
assert person_new == Person(name='fred', age=42, favorite_color='green')  # !!!

person_dict = {'name': 'andy', 'age': 40, 'favorite_color': 'blue'}
person_list = ['andy', 40, 'blue']

nt_from_dict = Person._make(person_dict)
assert nt_from_dict == Person(name='name', age='age',
                              favorite_color='favorite_color')

nt_from_list = Person(**person_dict)
assert nt_from_list == Person(name='andy', age=40, favorite_color='blue')

assert person == Person(name='andy', age=42, favorite_color='green')
person = person._replace(name='fred', age=55)
assert person == Person(name='fred', age=55, favorite_color='green')  # !!!
