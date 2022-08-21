person = {'name': 'andy', 'age': 42, 'fav_color': 'green'}

people = {
    'andy': {'age': 42, 'fav_color': 'green'},
    'fred': {'age': 22, 'fav_color': 'red'},
}

people['andy']['age']

booking = {
    'customer': {'prompt': "enter customer number", 'value': None},
    'weight': {'prompt': "enter shipment weight", 'value': None},
    'volume': {'prompt': "enter shipment volume", 'value': None},
}

for field_name, properties in booking.items():
    properties['value'] = input(properties['prompt'])
    
print(booking)
