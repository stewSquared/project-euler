"""An irrational decimal fraction is created by concatenating the
positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value
of the following expression.

d1 x d10 x d100 x d1000 x d 10000 x d100000 x d1000000

"""

from functools import reduce
from itertools import count
from operator import mul

def product(args): return reduce(mul, args)

def d():
    for n in count(1):
        for d in str(n):
            yield int(d)

def drop(iterable, amount):
    for _ in range(amount): next(iterable)
    return next(iterable)

ans = product(drop(d(), (10**n)-1) for n in range(7))

print(ans)
