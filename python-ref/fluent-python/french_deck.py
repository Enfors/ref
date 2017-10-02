#!/usr/bin/env python3

"Example 1-1 from Fluent Python."

import collections
from random import choice

from demo import headline

Card = collections.namedtuple("Card", ["rank", "suit"])

class FrenchDeck:
    "A deck of cards."

    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit)
                       for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


def demo():
    "Demo FrenchDeck."
    
    deck = FrenchDeck()
    print(headline("General"))
    print("deck.suits:", deck.suits)
    print("deck.ranks:", deck.ranks)
    print("Length of deck:", len(deck))

    print(headline("Random"))
    print("choice(deck):", choice(deck))
    print("choice(deck):", choice(deck))
    print("choice(deck):", choice(deck))

    print(headline("Index access"))
    print("deck[0]:", deck[0])
    print("deck[0:2]:", deck[0:2])
    print("deck[-1]:", deck[-1])
    print("deck[::13]:", deck[::13])


if __name__ == "__main__":
    demo()
