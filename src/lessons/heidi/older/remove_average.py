def remove_average_six(numbers):
    result = numbers.copy()
    for number_string in numbers:
        candidate = [int(n) for n in number_string]
        if sum(candidate) / len(candidate) == 6:
            result.remove(number_string)
    return result


print(remove_average_six(["66", "75", "286"]))
print(remove_average_six(["22", "1887", "91"]))
