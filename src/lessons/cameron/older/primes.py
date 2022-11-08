import math
while True:
    number = int(input("Enter a positive integer: "))
    if number < 1:
        continue

    isprime = True


    for candidate in range(2, int(number / 2)):
        if number % candidate == 0:
            isprime = False
            break
    if isprime:
        result = ""
    else:
        result = "not"
    print(f"{number} is {result} prime")


    for low in range(1, number + 1):
        low_square = low ** 2
        for high in range(number, 0, -1):
            lower_square = low + high
            higher_square = high - low
            if higher_square < 1:
                continue
            if (math.sqrt(lower_square) - int(math.sqrt(lower_square))) == 0 and \
                    (math.sqrt(higher_square) - int(math.sqrt(higher_square))) == 0:
                print(f"{low}\t{high}\t{lower_square}\t{higher_square}")

    yorn = input("Try again? y/n: ")
    if yorn.upper() != "Y":
        break

print("finished")