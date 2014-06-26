"""

It can be seen that n=6 produces a maximum n/tot(n) for n # 10.

Find the value of n <= 1,000,000 for which n/tot(n) is a maximum.

"""
import heapq
from math import sqrt
from itertools import count, accumulate, takewhile
from operator import mul

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

ans = max(takewhile(lambda n: n <= 10**6,
                    accumulate(primes(), mul)))

print(ans)
