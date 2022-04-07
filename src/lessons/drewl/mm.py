# 3/14/2022
# lesson concept review after Andy Lesson
import random

even_numbers = [i for i in range(2, 52, 2)]
odd_numbers = [i for i in range(1, 52, 2)]
# print(even_numbers)
# print(odd_numbers)
# output:
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51]

random_evens = random.sample(even_numbers, 5)
random_odds = random.sample(odd_numbers, 5)
sorted_odds = sorted(random_odds)
sorted_evens = sorted(random_evens)

print(f"\n5 random odd numbers: {random_odds}")
print(f"5 sorted odd numbers: {sorted_odds}")
print(
    "\nHere the methods: sum(), min(), and max() are used in a for loop on 4/5 of the lowest odd numbers.\n"
    "The loop is then repeated for 4/5 highest odd numbers. ")
odds_lowest = sorted_odds[0:4]
odds_highest = sorted_odds[1:]

for nums in [odds_lowest, odds_highest]:
    print(f'Sum: {sum(nums)}')
    print(f'Min: {min(nums)}')
    print(f'Max: {max(nums)}')

print(f"\n5 random even numbers: {random_evens}")
print(f"5 sorted even numbers: {sorted_evens}")

print(
    "\nHere the methods: sum(), min(), and max() are used in a for loop on 4/5 of the lowest even numbers.\n"
    "The for loop is then repeated for 4/5 highest even numbers. ")
evens_lowest = sorted_evens[0:4]
evens_highest = sorted_evens[1:]

for nums in [evens_lowest, evens_highest]:
    print(f'Sum: {sum(nums):>4}')
    print(f'Min: {min(nums):>4}')
    print(f'Max: {max(nums):>4}')

# This is cool because you can keep re-running the program
# and it will select a new group of numbers to work on.
