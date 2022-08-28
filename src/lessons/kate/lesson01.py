person = {
    'name': 'fred',
    'favorite_number': 76,
    'age': 42,
    'favorite_color': 'white'
}

print(person['name'])

people = {
    ('fred', 'blogs'): {'age': 42, 'size': 'L'},
    ('andy', 'miles'): {'age': 42, 'size': 'L'},
}

print(people[('fred', 'blogs')]['age'])
people_by_town = {
    'sumner': {},
}

for key, value in people.items():
    print(f"{key=}")
    for k2, v2 in value.items():
        print(f"{k2=}, {v2=}")
