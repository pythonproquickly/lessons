results = []

while True:
    number = int(input("Enter a number (999 to quit): "))
    if number == 999:
        break
    results.append(number)

results.sort()
print(results)

print(sum(results))
print(sum(results) / len(results))


print(max(results))
print(min(results))


person = ['andy', 24, 23.1, 'green']

person = {'name': 'andy', 'age': 24, 'shoe_size': 23.2. 'fav_col': 'green'}

person[2]

person['shoe_size']

