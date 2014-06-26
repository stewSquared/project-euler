from math import sqrt
from itertools import count, islice

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
    for m in range(2, int(sqrt(n))+1):
        if n%m == 0: return False
    else: return True

def rightTruncatable(p):
    return prime(p) and (True if p < 10 else rightTruncatable(int(str(p)[1:])))

def leftTruncatable(p):
    return prime(p) and (True if p < 10 else leftTruncatable(int(str(p)[:-1])))

ans = sum(filter(lambda p: (leftTruncatable(p)
                            and rightTruncatable(p) 
                            and p > 10), primes()))

print(ans)
