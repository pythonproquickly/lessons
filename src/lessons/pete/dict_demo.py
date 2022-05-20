people = {
    'fred': {'prompt': 'Enter freds full name: ', 'value': None},
    'andy': {'prompt': 'Enter andys full name: ', 'value': None},
    'sue': {'prompt': 'Enter sues full name: ', 'value': None},
    'sue2': {'prompt': 'Enter sue2s full name: ', 'value': None},
}


for name, person_details in people.items():
    people[name]['value'] = input(person_details['prompt'])

print(people)
