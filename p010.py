from itertools import takewhile
from cust import primes

ans = sum(takewhile(lambda p: p < 2000000, primes()))

print(ans)
