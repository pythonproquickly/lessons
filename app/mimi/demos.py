import random


def throw_dice():
    return random.randrange(2, 13)


for result in range(20):
    print(throw_dice())
