person = {'name': 'andy', 'age': 42, 'last_name': 'miles'}


people =[{'name': 'andy', 'age': 42, 'last_name': 'miles'},
        {'name': 'fred', 'age': 42, 'last_name': 'miles'},
]

people = {
          ('andy', 'miles'): {'age': 42, 'last_name': 'miles'},
          ('fred', 'bloggs'): {'age': 42, 'last_name': 'miles'},

}
people_ages = {
               42: [{'name': 'andy'}, {'name': 'drew]'},   },
                43: {'name': 'fred'}
              }

for key, person_details in people.items():
    print("details for", key)
    for item, value in person_details.items():
        print(item, value)

