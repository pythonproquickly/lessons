
n = int(input("Enter n: "))
numbers_to_print = n ** 2

for number in range(1, numbers_to_print + 1):
    if number % n == 1:
        print()
    print(number, end=" ")
