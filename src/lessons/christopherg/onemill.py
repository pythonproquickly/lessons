import random

my_list = [random.randrange(1, 10, 1) for _ in range(1000000)]
freq = {}
for item in my_list:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1
for key, value in freq.items():
    print(f"{key}: {value}")
