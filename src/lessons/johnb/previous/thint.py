from itertools import combinations


def find_pairs(nums, k):
    n = len(nums)
    return [pair for pair in combinations(nums, n) if sum(pair) == k]


print(find_pairs([1, 2, 3, 2, 4, 5, 6, 4], 5))
