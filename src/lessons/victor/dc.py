from dataclasses import dataclass


@dataclass
class Card:
    rank: str
    suit: str


card1 = Card("Q", "hearts")
card2 = Card("Q", "hearts")
print(card1 == card2)
print(card1.rank)

print(card1)
Card(rank="Q", suit="hearts")
