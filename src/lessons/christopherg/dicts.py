booking_data = {
    'description': {'value': None, 'prompt': "Describe what you want to ship"},
    'weight': {'value': None, 'prompt': 'Weight of you package in lbs'},
    'size': {'value': None, 'prompt': 'Size of you package in lbs'},
}
print(booking_data)

for _, details in booking_data.items():
    details['value'] = input(details['prompt'])

print(booking_data)
