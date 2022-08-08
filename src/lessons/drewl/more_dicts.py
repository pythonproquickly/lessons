def validate_name():
    print("i'm validating name")
    return

def validate_age():
    print("i'm validating age")
    return

def validate_fc():
    print("i'm validating fc")
    return


hrdata = {
    'name': {'prompt': 'enter your name', 'field_value': None, 'val': validate_name},
    'age': {'prompt': 'enter your age', 'field_value': None, 'val': validate_age},
    'fav_color': {'prompt': 'enter your fc', 'field_value': None, 'val': validate_fc},
}


def get_data(template):
    for key, value in template.items():
        value['field_value'] = input(value['prompt'])
    return template


def validate_data(template):
    for key, value in template.items():
        value['val']()
    return template


entered_data = get_data(hrdata)
validated = validate_data(entered_data)
