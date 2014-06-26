"""In the first one-thousand expansions, how many fractions contain a
numerator with more digits than denominator?"""

from fractions import Fraction
from itertools import islice

def rootTwoIterations():
    f = Fraction(1)
    while True:
        f = Fraction(1 + 1/(1 + f))
        yield f

ans = len(list(filter(lambda f: len(str(f.numerator)) > len(str(f.denominator)),
                      islice(rootTwoIterations(), 1000))))

print(ans)
