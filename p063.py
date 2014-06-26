"""The 5-digit number, 16807=7^5, is also a fifth power. Similarly,
the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?

"""
from itertools import count, chain, takewhile as tw

ans = len(list(chain.from_iterable(tw(lambda x: len(x) > 0,
                                      (list(filter(lambda x: len(str(x)) == n,
                                                   (m**n for m in range(1,10))))
                                       for n in count(1))))))

print(ans)
