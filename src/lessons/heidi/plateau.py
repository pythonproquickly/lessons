def find_plateaus(numbers):
    new_data = []
    for index, number in enumerate(numbers[1:-1]):
        if (number, number) == (numbers[index + 1], numbers[index - 1]):
            new_data.append(number)
    return new_data


# tests - you need to show as input
print(find_plateaus([10, 2, 20, 4, 4, 4, 5, 8, 5, 5, 5, 5]))
print(find_plateaus([1, 2, 2, 2, 1]))
print(find_plateaus([2, 2, 2, 2, 2, 2]))
