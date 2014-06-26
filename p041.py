"""We shall say that an n-digit number is pandigital if it makes use
of all the digits 1 to n exactly once. For example, 2143 is a 4-digit
pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

"""
from itertools import permutations, chain
from math import sqrt

def prime(n):
    if n < 2: return False
    for m in range(2, int(sqrt(n))+1):
        if n%m == 0: return False
    else: return True

pandigitals = chain.from_iterable((sum(p * (10**i) for i, p in enumerate(list(perm)[::-1]))
                                   for perm in permutations(range(n, 0, -1)))
                                  for n in range(7,0,-1))

ans = next(filter(prime, pandigitals))
