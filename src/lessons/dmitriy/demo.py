person = {}

person['name'] = 'Fred'
person['age'] = 42

person['name'] = 'Andy'
print(person)

if person.get('shoe_size', None) is None:
    person['shoe_size'] = "x"
print(person['shoe_size'])

"""def x():
    return "abc"


print(x())"""
