"""The fraction 49/98 is a curious fraction, as an inexperienced
mathematician in attempting to simplify it may incorrectly believe
that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction,
less than one in value, and containing two digits in the numerator and
denominator.

If the product of these four fractions is given in its lowest common
terms, find the value of the denominator.

"""

from functools import reduce
from operator import mul
from itertools import starmap
from fractions import Fraction

rawFracs = [(num, denom)
            for denom in range(12, 100) if denom % 10
            for num in range(11, denom) if num % 10]

def curious(rawFrac):
    num, denom = rawFrac
    return (str(num)[1] == str(denom)[0] and
            (num // 10) / (denom % 10) == num/denom)

ans = reduce(mul, starmap(Fraction, filter(curious, rawFracs))).denominator

print(ans)
