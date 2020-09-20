from enum import Enum, auto
import random

class Denomination(Enum):
    ACE = auto()
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()
    EIGHT = auto()
    NINE = auto()
    TEN = auto()
    JACK = auto()
    QUEEN = auto()
    KING = auto()

class Suit(Enum):
    CLUBS = auto()
    DIAMONDS = auto()
    HEARTS = auto()
    SPADES = auto()

class Card:
    def __init__(self, d, s):
        self._d = d
        self._s = s
    
    @property
    def denomination(self):
        return self._d
    
    @property
    def suit(self):
        return self._s

def build_deck():
    deck = []

    for d in Denomination:
        for s in Suit:
            deck.append(Card(d, s))
    
    return deck

def check(cards):
    prev = None

    for i in range(len(cards)):
        if prev is not None and prev.denomination == Denomination.ACE and cards[i].denomination == Denomination.ACE:
            return True
        else:
            prev = cards[i]
    
    return False

if __name__ == "__main__":
    successes = 0
    trials = 0

    deck = build_deck()

    for i in range(1000000):
        trials += 1

        random.shuffle(deck)        
        result = check(deck)

        if result:
            successes += 1
        
        if trials % 1000 == 0:
            print(f"{trials} trials complete")

    print(f"successes, trials: {successes}, {trials}")
    print(f"success rate: {successes / trials}")