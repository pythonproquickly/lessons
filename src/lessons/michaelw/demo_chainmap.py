from collections import ChainMap

person0 = {"name": 'andy', 'age': 42}
person1 = {"another_name": 'fred', 'another_age': 22}
person2 = {"color": 'blue', "size": 'small'}
person3 = {"name": 'bill', 'age': 55}

cm = ChainMap(person0, person1)
assert cm['name'] == 'andy'
assert cm['another_age'] == 22
cm.maps.append(person2)  # can mutate
assert cm['color'] == 'blue'
cm = cm.new_child(person3)  # must reassign; can't mutate with new_child
assert cm['name'] == 'bill'
