import random
import sys
import csv
from collections import namedtuple
from collections import defaultdict
    

def default_value():
    return 0


def get_card():
    return random.randint(1, 13)


def score(cards):
    total = 0
    soft_ace_count = 0
    eleven = False
    for i in cards:
        if i == 11:
            soft_ace_count -= 1
            continue
        elif i == 1 and not eleven:
            total += 11
            soft_ace_count += 1
            eleven = True
        elif i > 11:
            total += 10
        elif i == 1 and eleven:
            total += 1
        else:
            total += i
    Score = namedtuple("Score", "score ace")
    result = Score(total, soft_ace_count)
    return result


def stand(stand_on_value, stand_on_soft, cards):
    total, soft_ace_count = score(cards)
    Stand = namedtuple("Stand", "stand total")
    if (total >= stand_on_value) or (soft_ace_count > 0 and stand_on_soft):
        return Stand(True, total)
    return Stand(False, total)


def print_arg_error():
    print(
        "usage: blackjack.py <num-simulations> <stand-on-value (1-20)>"
        " <'soft'|'hard'>'"
    )


def play_hand(stand_on_value, stand_on_soft):
    cards = []
    total = 0
    while total <= stand_on_value:
        card = get_card()
        total += card
        cards.append(card)
        result = score(cards)
        if result.soft_ace_count > 0:
            return total
    return total


def main(args):
    try:
        num_simulations = int(args[0])
    except ValueError:
        print_arg_error()

    results = defaultdict(default_value)
    for stand_on_value in range(13, 21):
        for strategy in ["hard", "soft"]:
            for _ in range(num_simulations):
                results[strategy + str(stand_on_value)] += play_hand(
                    stand_on_value, strategy
                ).total
    with open("blackjack.csv", "w") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(results)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_arg_error()
        exit()
    main(sys.argv[1:])
