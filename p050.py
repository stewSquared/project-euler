"""The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime
below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to
a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?

"""
from math import sqrt
LIMIT = 10**6

def primesUntil(n):
    composite = [False for _ in range(n)]
    for m in range(2, int(sqrt(n))+1):
        if not composite[m]:
            for i in range(m**2, n, m):
                composite[i] = True
    return [i for (i, m) in enumerate(composite) if (not m)][2:]

primes = primesUntil(5000)

def prime(n):
    if n < 2: return False
    for m in range(2, int(sqrt(n))+1):
        if n%m == 0: return False
    else: return True

length = len(primes) - 1
ans = 0
while not ans:
    start = 0
    s = sum(primes[start:(start+length)])
    while (start+length) < len(primes) and s < LIMIT:
        if prime(s):
            ans = s
            break
        start += 1
        s = sum(primes[start:(start+length)])
    else:
        length -= 1
        start = 0

print(ans)

