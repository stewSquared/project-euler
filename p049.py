"""The arithmetic sequence, 1487, 4817, 8147, in which each of the
terms increases by 3330, is unusual in two ways: (i) each of the three
terms are prime, and, (ii) each of the 4-digit numbers are
permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
primes, exhibiting this property, but there is one other 4-digit
increasing sequence.

What 12-digit number do you form by concatenating the three terms in
this sequence?

"""

from math import sqrt
from itertools import permutations

def primesUntil(n):
    composite = [False for _ in range(n)]
    for m in range(2, int(sqrt(n))):
        if not composite[m]:
            for i in range(m**2, n, m):
                composite[i] = True
    return [i for (i, m) in enumerate(composite) if (not m)][2:]

def prime(n):
    if n < 2: return False
    for m in range(2, int(sqrt(n))+1):
        if n%m == 0: return False
    else: return True

primes = list(filter(lambda n: n > 10**3, primesUntil(10**4)))

def primePermutations(p):
    primes = sorted(set(filter(prime, map(int, map("".join, permutations(str(p)))))))
    return primes if p == primes[0] else None

def seq3(seq):
    if len(seq) >= 3 and seq[1]*2 - seq[0] == seq[2]:
        return seq[0:3]
    elif len(seq) <= 3:
        return None
    else:
        return (seq3(seq[0:2] + seq[3:]) or
                seq3(seq[0:1] + seq[2:]) or
                seq3(seq[1:4]))

ans = list(filter(None, map(seq3, filter(None, map(primePermutations, primes)))))
ans = list(filter(lambda seq: not seq == [1487,4817,8147], ans))[0]
ans = "".join(map(str, ans))

print(ans)
