"""Take the number 192 and multiply it by each of 1, 2, and 3:

    192 x 1 = 192
    192 x 2 = 384
    192 x 3 = 576

By concatenating each product we get the 1 to 9 pandigital,
192384576. We will call 192384576 the concatenated product of 192 and
(1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2,
3, 4, and 5, giving the pandigital, 918273645, which is the
concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be
formed as the concatenated product of an integer with (1,2, ... , n)
where n > 1?

"""

from itertools import count, dropwhile

DIGITS = sorted("123456789")
LIMIT = 10**4

def cps(base):
    """cps - Concatenated Product Series"""
    cp = str(base)
    for n in count(2):
        yield cp
        cp += str(base*n)

def pandigital(n):
    return sorted(str(n)) == DIGITS

def longEnough(base):
    return next(dropwhile(lambda n: len(n) < len(DIGITS), cps(base)))

ans = max(filter(pandigital, (map(longEnough, range(1, LIMIT)))))

print(ans)
