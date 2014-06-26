"""Find the first four consecutive integers to have four distinct
prime factors. What is the first of these numbers?

"""

NCN = 4 # Number of Consecutive Numbers
DPF = 4 # to have Distinct Prime Factors

from itertools import groupby, starmap, count
from math import floor, sqrt

def primeFactors(n):
    if n < 2: raise StopIteration
    for k in range(2, floor(sqrt(n)) + 1):
        while n % k == 0:
            yield k
            n = n / k
        if n == 1: break
    else: yield n

def dpf(n): # calculate the number of distinct prime factors of n
    return len(list(groupby(primeFactors(n))))

ans = next(filter(lambda group: len(group) >= NCN,
                  starmap(lambda k, g: list(g) if k == DPF else [],
                          groupby(count(), key=lambda n:
                                  len(list(groupby(primeFactors(n))))))))[0]

print(ans)

"""

from itertools import groupby, starmap, count
from math import floor, sqrt
from cust import primeFactors

print(next(filter(lambda group: len(group) >= 4,
                  starmap(lambda k, g: list(g) if k == 4 else [],
                          groupby(count(2*3*5*7), key=lambda n:
                                  len(list(groupby(primeFactors(n))))))))[0])

"""
