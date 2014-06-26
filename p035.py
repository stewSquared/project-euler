""""The number, 197, is called a circular prime because all rotations
of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31,
37, 71, 73, 79, and 97.

How many circular primes are there below one million?

"""

from math import sqrt

def primesUntil(n):
    composite = [False for _ in range(n)]
    for m in range(2, int(sqrt(n))):
        if not composite[m]:
            for i in range(m**2, n, m):
                composite[i] = True
    return [i for (i, m) in enumerate(composite) if (not m)][2:]

primes = primesUntil(10**6)

def prime(n):
    if n < 2: return False
    for m in range(2, int(sqrt(n)) + 1):
        if n%m == 0: return False
    else: return True

def circular(p):
    rotations = (int(str(p)[i:] + str(p)[:i]) for i in range(len(str(p))))
    return all(prime(n) for n in rotations)

ans = sum(1 for p in primes if circular(p))

print(ans)
