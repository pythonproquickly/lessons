import array as arr

numbers = arr.array('i', range(0, 50))

print(numbers)

numbers.insert(0, 99)
numbers.append(88)

for number in numbers:
    print(number, end = ',')

end = numbers.pop()

print()
print(end)
