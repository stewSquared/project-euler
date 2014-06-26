"""Find the sum of digits in the numerator of the 100th convergent of
the continued fraction for e.

"""

from fractions import Fraction
from itertools import count
from functools import reduce

def eSequence():
    yield 2
    for k in count(2,2):
        yield 1; yield k; yield 1

e = eSequence()

ans = sum(int(d) for d in str(reduce(lambda a, b: b + Fraction(1,a),
                                     [next(e) for _ in range(100)][::-1]).numerator))

print(ans)
