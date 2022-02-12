people = {'andy': {'last_name': 'miles', 'age': 23},
          'fred': {}}

assert people['andy']['last_name'] == 'miles'

for name, person_details in people.items():
    print(name, person_details)

print(people.items())
