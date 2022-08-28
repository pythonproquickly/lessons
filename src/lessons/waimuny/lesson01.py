"""numbers = (4, 2, 6, 8)
print(numbers)

double_numbers = []
for number in numbers:
    double_numbers.append(number * 2)

print(double_numbers)

treble_numbers = tuple([number * 3 for number in numbers])
print(treble_numbers)"""

# ---------

person = {
    'name': 'andy',
    'age': 22,
    'state': 'wa'
}

print(person.items())

people = {
    ('andy', 'miles'): {'age': 22, 'state': 'wa'},
    ('fred', 'blogs'): {'age': 55, 'state': 'or'},
}

for key, value in people.items():
    print(f"{key=}")
    for k2, v2 in value.items():
        print(f"{k2=}: {v2=}")

print(people[('andy', 'miles')]['state'])
