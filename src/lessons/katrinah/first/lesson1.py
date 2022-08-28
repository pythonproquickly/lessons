name = "andy"
name1 = "sue"
name2 = "fred"

names = ['andy', 'sue', 'fred']


for name in names:
    print(name)


more_names = []
while True:
    name = input("Enter a name, 99 to quit: ")
    if name == '99':
        break
    more_names.append(name)

print(more_names)
print("goodbye")
