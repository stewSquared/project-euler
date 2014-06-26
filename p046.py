"""It was proposed by Christian Goldbach that every odd composite
number can be written as the sum of a prime and twice a square.

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum
of a prime and twice a square?

"""
from math import sqrt, ceil

LIMIT = 10000

def primesUntil(n):
    composite = [False for _ in range(n)]
    for m in range(2, int(sqrt(n))):
        if not composite[m]:
            for i in range(m**2, n, m):
                composite[i] = True
    return [i for (i, m) in enumerate(composite) if (not m)][2:]

primes = primesUntil(LIMIT)
twiceSquares = list(map(lambda x: 2*x*x, range(0, ceil(sqrt(LIMIT//2)))))[::-1]
odds = (2*n + 1 for n in range(1, LIMIT//2))

def writeable(n):
    ps, ss = iter(primes), iter(twiceSquares)
    s, p = next(ss), next(ps)
    while True:
        try:
            if s+p == n:
                return True
            elif s+p > n:
                s = next(ss)
            elif s+p < n:
                p = next(ps)
        except StopIteration: return False
            

ans = next(filter(lambda n: not writeable(n), odds))

print(ans)
