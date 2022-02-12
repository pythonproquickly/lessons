"""
This program calculates the probability of going "bust" with different play
strategies.
"""
import random
import sys
import csv
from collections import namedtuple

"""
Function returns a random value between 1 - 13 (ends included).

Values of Cards:
Ace = 1 or 11 (An Ace will have a value of 11 unless that would give a player
or the dealer a score in excess of 21; in which case, it has a value of 1.)

Number cards = 2 - 10
Jack, Queen, King = 11, 12, 13

Returns:
Random integers 1 - 13 (integer)
"""


def get_card():
    return random.randint(1, 13)


"""
Score function converts integers representing the total value (tuple) of cards
in a Blackjack hand (soft aces are converted from 11 to 1 to keep the hand from
going bust.)
"""


def score(cards):
    # total = 0
    # soft_ace_count = 0
    # Conditions for when player's hand has an ace and total is equal to or
    # less than 21.
    # Example, hand is greater than 21 with ace card, convert from 11 to 1
    # (soft ace) add to total amount in hand without going bust.
    Score = namedtuple("Score", ["total", "soft_ace_count"])
    score = Score(0, 0)  # abstantiating a score 0,0
    """s = Score(15, 1)
    assert s.total == 1 #access properties of s, testing s
    assert s.soft_ace_count == 1
    """

    for x in cards:
        if x >= 11 and x <= 13:
            score = score._replace(total=score.total + 10)  # score.total += 10
            if score.total > 21 and score.soft_ace_count == 1:
                score = score._replace(total=score.total - 10)
                score = score._replace(soft_ace_count=0)

        elif x == 1:
            if score.total + 11 and score.total <= 21:
                score = score._replace(total=score.total + 11)
                score = score._replace(soft_ace_count=1)
            else:
                score = score._replace(total=score.total + 1)
            if score.total > 21 and score.soft_ace_count == 1:
                score = score._replace(total=score.total - 10)
                score = score._replace(soft_ace_count=0)

        else:
            score = score._replace(total=score.total + x)  # score.total += x
            if score.total > 21 and score.soft_ace_count == 1:
                score = score._replace(total=score.total - 10)
                score = score._replace(soft_ace_count=0)
    return score.total, score.soft_ace_count  # no () needed for tuple


"""
Stand function is the stand-on value (e.g., 17), a Boolean value (True/False)
indicating whether the player will stand on a "soft" hand or just on a "hard"
hand, and a list of integers representing the cards in a Blackjack hand.

Input:
'stand on value'
'stand on soft'
cards

Returns:
True or False (Boolean)
"""


def stand(stand_on_value, stand_on_soft, cards):
    total, soft_ace_count = score(cards)
    Stand = namedtuple("Stand", ["stand_on_value", "total"])
    if stand_on_soft == True:
        if total < stand_on_value:
            return Stand(False, total)
        else:
            return Stand(True, total)
    if stand_on_soft == False:
        if total < stand_on_value:
            return Stand(False, total)
        elif total == stand_on_value and soft_ace_count == 1:
            return Stand(False, total)
        else:
            return Stand(True, total)


def play_hand(stand_on_value, stand_on_soft):
    cards = [get_card()]
    cards.append(get_card())
    while stand(stand_on_value, stand_on_soft, cards).stand_on_value == False:
        cards.append(get_card())
    total = stand(stand_on_value, stand_on_soft, cards).total
    if total > 21:
        return 22
    else:
        return total


def main():
    s1 = int(sys.argv[1])
    if s1 <= 0:
        raise ValueError

    d = {}
    for count in range(13, 21):
        d[f"Hard{count}"] = [0 for k in range(10)]
        d[f"Soft{count}"] = [0 for k in range(10)]
        for i in range(s1):
            countHand = play_hand(count, False)
            d[f"Hard{count}"][countHand - 13] += 1
            countSoft = play_hand(count, True)
            d[f"Soft{count}"][countSoft - 13] += 1

    with open("blackjack2.csv", "w", encoding="utf8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            ["Strategy", "13", "14", "15", "16", "17", "18", "19", "20", "21", "Bust"]
        )
        for key in d.keys():
            writer.writerow([key] + d[key])


if __name__ == "__main__":
    print(main())
