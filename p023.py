"""A perfect number is a number for which the sum of its proper
divisors is exactly equal to the number. For example, the sum of the
proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means
that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is
less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
smallest number that can be written as the sum of two abundant numbers
is 24. By mathematical analysis, it can be shown that all integers
greater than 28123 can be written as the sum of two abundant
numbers. However, this upper limit cannot be reduced any further by
analysis even though it is known that the greatest number that cannot
be expressed as the sum of two abundant numbers is less than this
limit.

Find the sum of all the positive integers which cannot be written as
the sum of two abundant numbers.

"""
from math import ceil, sqrt
from itertools import takewhile
LIMIT = 100#28123

def divisors(n):
    if n < 1: raise StopIteration
    root = ceil(sqrt(n))
    if root**2 == n: yield root
    for k in range(1, root):
        if n % k == 0:
            yield k
            yield n // k

def d(n, cache={}): return sum(divisors(n)) - n

abundants = [n for n in range(LIMIT) if d(n) > n]

# _Writable_ as the _Sum_ of two _Abundants_
wsa = set(m+n for n in abundants 
          for m in takewhile(lambda m: m < (LIMIT - n),
                             abundants))

# sum(other numbers) - sum(wsa) = sum(non-wsa)
ans = ((LIMIT**2 + LIMIT) // 2 - LIMIT) - sum(wsa)

print(ans)
