"""How many, not necessarily distinct, values of nCr, for 1 <= n <= 100,
are greater than one-million?

"""

from math import factorial

def choose(n, r):
    return (0 if n < 0 or r < 0 or r > n else
            factorial(n)//(factorial(r) * factorial(n-r)))
            
ans = len(list(filter(lambda k: k > 10**6,
                      (choose(n,r)
                       for n in range(1, 101)
                       for r in range(n+1)))))

print(ans)

"""
from math import factorial as f

print(len(list(filter(lambda k: k > 10**6, (f(n)//(f(r) * f(n-r))
                                            for n in range(1, 101)
                                            for r in range(n+1))))))
"""
