def isprime(number):
    if number == 2:
        return True
    elif number == 1:
        return False
    for candidate in range(2, int(number / 2) + 1):
        if number % candidate == 0:
            return False
    return True


print(isprime(13))
print(isprime(4))
