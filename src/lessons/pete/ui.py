# windows
# 
import model
making_data = {
    'making_number': {'value': None, 'prompt': 'Enter making number'},
    'name': {'value': None, 'prompt': 'Enter making name'},
    'vineyard': {'value': None, 'prompt': 'Enter vineyard'},
    'pete': {'value': None, 'prompt': 'hello pete'},
    'weight': {'value': None, 'prompt': 'Enter weight'},
    'crush_date': {'value': None, 'prompt': 'Enter crush date'},
}

for field, item in making_data.items():
    item['value'] = input(item['prompt'] + ": ")
    making = model.Making()
    making.making_name = item['value']
    making.save()

print(making_data)

bin_data = {
    'making'['value'] = making_data['making_number']['value'],
    'gallons': {'value': None, 'prompt': 'Enter gallons in this bin'}
}
