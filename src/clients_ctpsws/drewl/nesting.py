names = ["aa", "bb", "ccc"]
assert names[0] == "aa"
people = [
    ["aa", 10],
    ["bb", 20],
    ["dd", 40, 10],
]
assert people[1] == ["bb", 20]
assert people[1][1] == 20
person = {"name": "andy", "age": 42}
assert person["name"] == "andy"
people = [
    {"ssn": "111111111", "name": "andy", "age": 42},
    {"ssn": "222222222", "name": "fred", "age": 60},
    {"ssn": "333333333", "name": "sue", "age": 22},
]
assert people[1]["age"] == 60

people = {
    "1111111111": {"name": ["Andy", "Miles"], "age": 56},
    "2222222222": {"name": "fred", "age": 60},
    "3333333333": {"name": "sue", "age": 22},
}

for ssn, person_details in people.items():
    print(ssn)
    for key, value in person_details.items():
        if key == "name":
            print(value[0] + " " + value[1])


assert (
    people["1111111111"]["name"][0] + " " + people["1111111111"]["name"][1]
    == "Andy Miles"
)


# name == fred, get age

assert people["3333333333"]["age"] == 22

people_by_name = {
    "andy": {"ssn": "1111111111", "age": 42},
}
assert people_by_name["andy"]["age"] == 42
