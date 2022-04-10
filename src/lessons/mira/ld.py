def validate_name(name):
    return len(name) > 5

other_fields = {
    'name': {'f': validate_name},
    'value': None
}


fields = {
    'person_name': {
        'validate': (lambda x: len(x) > 5)},
        'value': None,
        'prompt': "Enter value: "}
    'age':
}

assert fields['name']['f']("aa")
