def get_max(numbers):
    if numbers:
        return sorted(numbers, reverse=True)[0]
    else:
        return -99999999


print(get_max([1, 2, 3]))
