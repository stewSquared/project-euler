import sys, time
from itertools import *

CARD_VALUES = list("23456789TJQKA")
HAND_RANKS = [
    "HighCard",
    "OnePair",
    "TwoPair",
    "ThreeKind",
    "Straight",
    "Flush",
    "FullHouse",
    "FourKind",
    "StraightFlush"]


class Hand:
    def __init__(self, cards):
        self.cards = cards
        self.values = [CARD_VALUES.index(c[0])+1 for c in cards]
        self.suits = [c[1] for c in cards]

    @property
    def rank(self):
        distinct = len(set(self.values))
        longest = max(len(list(g)) 
                      for k, g in groupby(sorted(self.values)))
        if distinct == 2:
            rank = "FourKind" if longest == 4 else "FullHouse"
        elif distinct == 3:
            rank = "ThreeKind" if longest == 3 else "TwoPair"
        elif distinct == 4:
            rank = "OnePair"
        else:
            flush = len(set(self.suits)) == 1
            straight = max(self.values) - min(self.values) == 4
            rank = ("StraightFlush" if straight and flush
                    else "Straight" if straight 
                    else "Flush" if flush
                    else "HighCard")
        return HAND_RANKS.index(rank)
 
    def trumps(self, other):
        def tiebreakers(values):
            def group_score(value, group):
                return (value * (len(CARD_VALUES)+1) ** (len(list(group))-1))

            return reversed(sorted(starmap(group_score,
                                           groupby(sorted(values)))))
        if self.rank == other.rank:
            selfTiebreaker, otherTiebreaker = next(dropwhile(
                lambda tup: tup[0] == tup[1],
                zip(tiebreakers(self.values), tiebreakers(other.values))
            ))
            return selfTiebreaker > otherTiebreaker
        else:
            return self.rank > other.rank


if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else "p054.txt"

    t0 = int(time.time()*1000)
    ans = list(starmap(lambda left, right: left.trumps(right),
                       map(lambda cards: (Hand(cards[0:5]), Hand(cards[5:10])),
                           (line.split() for line in open(filename))))).count(1)
    t1 = int(time.time()*1000)

    print(t1 - t0)

    print(ans)
