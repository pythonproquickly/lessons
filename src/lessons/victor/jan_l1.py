


people = {'andy': {'age': 22, 'favortite_color': 'green', 
        'message': "enter town", 'data_value': None},
          'sue': {'age': 61, 'favorite_color': 'red', 'message': "enter town",
                  'data_value': None}}

print(people['andy']['age'])


for key, value in people.items():
    value['data_value'] = input(value['message'])

print(people
