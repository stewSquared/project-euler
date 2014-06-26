"""Let d(n) be defined as the sum of proper divisors of n (numbers
less than n which divide evenly into n).  If d(a) = b and d(b) = a,
where a # b, then a and b are an amicable pair and each of a and b are
called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20,
22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284
are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

"""
from math import sqrt, ceil

def divisors(n):
    if n < 1: raise StopIteration
    root = ceil(sqrt(n))
    if root**2 == n: yield root
    for k in range(1, root):
        if n % k == 0:
            yield k
            yield n // k

def d(n, cache={}): 
    if n not in cache: cache[n] = sum(divisors(n)) - n
    return cache[n]

def amicable(n): return d(n) != n and d(d(n)) == n

ans = sum(n for n in range(10000) if amicable(n))

print(ans)
