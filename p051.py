"""By replacing the 1st digit of the 2-digit number *3, it turns out that six
of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
number is the first example having seven primes among the ten generated
numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and
56993. Consequently 56003, being the first member of this family, is the
smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily
adjacent digits) with the same digit, is part of an eight prime value family.

"""

from math import sqrt, floor
from itertools import dropwhile

def primesUntil(n):
    composite = [False for _ in range(n)]
    for m in range(2, int(sqrt(n))+1):
        if not composite[m]:
            for i in range(m**2, n, m):
                composite[i] = True
    return [i for (i, m) in enumerate(composite) if (not m)][2:]

def prime(n):
    if n < 2: return False
    for m in range(2, floor(sqrt(n))+1):
        if n%m == 0: return False
    else: return True

primes = primesUntil(10**6)

def eightPrimeFamily(p):
    return 8 in (len(list(filter(lambda n: prime(n) and n >= p,
                                 (int(str(p).replace(c, str(digit)))
                                  for digit in range(10)))))
                 for c in set(str(p)))

ans = next(dropwhile(lambda p: not eightPrimeFamily(p), primes))

print(ans)
