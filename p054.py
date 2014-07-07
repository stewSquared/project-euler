from itertools import groupby, starmap, count

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

CARD_VALUES = list("23456789TJQKA")

class Hand:

    def __init__(self, cards):
        self.cards = cards
        self.values = [c[0] for c in cards]
        self.suits = [c[1] for c in cards]

    def rank(self):
        distinct = len(set(self.values))
        clumpSize = max(len(list(g)) 
                        for k, g in groupby(sorted(self.values)))
        if distinct == 2:
            rank = "FourKind" if clumpSize == 4 else "FullHouse"
        elif distinct == 3:
            rank = "ThreeKind" if clumpSize == 3 else "TwoPair"
        elif distinct == 4:
            rank = "OnePair"
        else:
            flush = len(set(self.suits)) == 1
            run = sorted(CARD_VALUES.index(c) for c in self.values)
            straight = run[-1] - run[0] == 4
            rank = ("StraightFlush" if straight and flush
                    else "Straight" if straight 
                    else "Flush" if flush
                    else "HighCard") 
        assert rank in HAND_RANKS
        return rank

    def trumps(self, other):
        def outranks(self, other):
            return (HAND_RANKS.index(self.rank()) > 
                    HAND_RANKS.index(other.rank()))

        def tiebreakers(self):
            """Return a list of cards values with which to break ties."""
            if self.rank() in ["HighCard", "Flush"]:
                return sorted(map(lambda c: CARD_VALUES.index(c),
                                  self.values),
                              reverse=True)
            else:
                groups = sorted([(CARD_VALUES.index(k), len(list(g)))
                                 for k, g in groupby(sorted(self.values,
                                                            reverse=True))],
                                key=lambda tup: tup[1], # tup = (value, size)
                                reverse=True)
                return list(starmap((lambda value, size: value), groups))

        return (self.outranks(other) or
                not other.outranks(self) and
                self.tiebreakers() > other.tiebreakers())

def matchHands(match):
    cards = match.split()
    return (Hand(cards[0:5]), Hand(cards[5:10]))

ans = len(list(filter(None, starmap(lambda left, right: left.trumps(right),
                                    map(matchHands, open("p054.txt"))))))

print(ans)
