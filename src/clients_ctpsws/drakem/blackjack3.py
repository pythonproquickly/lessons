import random
import sys
import csv
from collections import namedtuple
from collections import defaultdict


class Hand:
    """Class that encapsulates a blackjack hand."""

    total = 0
    soft_ace_count = 0

    def __init__(self, cards=None):

        if cards is None:
            self.cards = []
            self.total = 0
            self.soft_ace_count = 0
            return
        self.cards = cards
        self.total = self.score().Final
        self.soft_ace_count = self.score().score_ace

    def score(self):
        self.total = 0
        self.soft_ace_count = 0
        eleven = False
        for i in self.cards:
            print(i)
            if i == 11:
                self.soft_ace_count -= 1
                continue
            elif i == 1 and not eleven:
                self.total += 11
                self.soft_ace_count += 1
                eleven = True
            elif i > 11:
                self.total += 10
            elif i == 1 and eleven:
                self.total += 1
            else:
                self.total += i
        Score = namedtuple("Score", ("Final", "score_ace"))
        result = Score(self.total, self.soft_ace_count)
        return result

    def __str__(self):
        return str(self.cards)

    def add_card(self):
        self.cards.append(random.randint(1, 13))
        self.score()

    def is_blackjack(self):
        if 10 in self.cards or 11 in self.cards:
            if self.soft_ace_count > 0:
                return True
        return False

    def is_bust(self):
        return self.score().Final > 21


class Strategy:
    def __init__(self, stand_on_value, stand_on_soft):
        self.stand_on_value = stand_on_value
        self.stand_on_soft = stand_on_soft

    def __repr__(self):
        return str(self.stand_on_value) + " " + str(self.stand_on_soft)

    def __str__(self):
        if self.stand_on_soft:
            return "S" + str(self.stand_on_value)
        else:
            return "H" + str(self.stand_on_value)

    def stand(self, hand):
        total, soft_ace_count = hand.score()

        Stand = namedtuple("Stand", "game total")
        if (total >= self.stand_on_value) or (self.stand_on_soft):
            print(hand)
            return Stand(True, total)
        return Stand(False, total)

    def play(self):
        calc = 0
        hand = Hand()

        while calc < self.stand_on_value:

            if self.stand(hand).game:

                hand.cards.append(hand.add_card())
                calc = self.stand(hand).total
        return hand


def main(simulations):

    book = []
    suit = []

    for i in range(13, 21):
        strategy = Strategy(i, True)

        book.append(0)
        suit.append(0)
        for j in range(simulations):
            player = strategy.play()

            if Hand(player).is_bust():
                suit[-1] += 1
                continue
            if Hand(player).is_blackjack():
                book[-1] += 1
                continue
        print(book[-1] / simulations)
    with open("player.csv", "w") as file:

        csvwriter = csv.writer(file)

        csvwriter.writerow(book)

    for i in range(13, 21):
        strategy = Strategy(i, True)
        for j in range(simulations):
            dealer = strategy.play()
            if Hand(dealer).is_bust():
                book[-1] += 1
                continue
            if Hand(dealer).is_blackjack():
                suit[-1] += 1
                continue
        print(suit[-1] / simulations)

    with open("dealer.csv", "w") as csvfile:

        csvwriter = csv.writer(csvfile)

        csvwriter.writerow(suit)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(
            "usage: blackjack.py <num-simulations> <stand-on-value (1-20)>"
            " <'soft'|'hard'>'"
        )
        exit()
    print(sys.argv[1])
    main(int(sys.argv[1]))
