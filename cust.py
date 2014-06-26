import heapq
from math import sqrt
from itertools import count
def primes():
    compositeQueue = []
    nextComposite = 4
    for n in count(2):
        if n < nextComposite:
            yield n
            heapq.heappush(compositeQueue, (n**2, n))
        else:
            while n == nextComposite:
                nextComposite, p = compositeQueue[0]
                heapq.heapreplace(compositeQueue,
                                  (nextComposite + (2*p if p > 2 else p), p))

from math import sqrt
def primesUntil(n):
    composite = [False for _ in range(n)]
    for m in range(2, int(sqrt(n))+1):
        if not composite[m]:
            for i in range(m**2, n, m):
                composite[i] = True
    return [i for (i, m) in enumerate(composite) if (not m)][2:]

from math import sqrt, floor
def prime(n):
    if n < 2: return False
    for m in range(2, floor(sqrt(n))+1):
        if n%m == 0: return False
    else: return True

# simple, O(n) implementation.
def oldPrimeFactors(n):
    k = 2
    while n != 1:
        while n % k == 0:
            yield k
            n = n / k
        k += 1

from math import sqrt, floor
def primeFactors(n):
    if n < 2: raise StopIteration
    for k in range(2, floor(sqrt(n)) + 1):
        while n % k == 0:
            yield k
            n = n / k
        if n == 1: break
    else: yield n

# Euler's totient function
def tot(n):
    if n < 2: raise ValueError
    pfs = list(primeFactors(n))
    def relPrime(m):
        if m < 1: raise ValueError
        if m == 1: return True
        for p in pfs:
            if m%p == 0: return False
        else:
            return True
    return len(list(filter(relPrime, range(1,n))))
