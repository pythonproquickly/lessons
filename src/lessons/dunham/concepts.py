countries = {"uk", "france", "india", "belgium"}
people = ["andy", "sue", "fred", "pete"]
colors = {1: "red", 2: "blue", 3: "green"}
sizes = (3, 5, 6, 9, 12)
document = (
    "Sometimes, a simple algorithm can achieve drastic performance " "improvements."
)

assert isinstance(people, list)

name = iter(people)
assert str(type(name)) == "<class 'list_iterator'>"
assert next(name) == people[0]
assert next(name) == people[1]
