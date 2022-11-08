def calculate_collatz(n):
    results = [n]
    while n != 1:
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = (3 * n) + 1
        results.append(n)
    return results


print(calculate_collatz(10))
print(calculate_collatz(24))
