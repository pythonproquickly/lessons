"""name = "101"
name2 = "2"

if name > name2:
    print("I am true")
    # end of if
elif name == name2:
    #
else:
    print("i am else")

print("I am not part of if")"""


dothings = {'1': 'option 1', '2': 'option 2'}


def menu():
    print("1. do this")
    print("2. do that")
    print("3. do that")
    result = input()
    if result in "123":
        return result
    else:
        print("ERROR")

option = menu()
print(dothings[option])
