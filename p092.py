"""A number chain is created by continuously adding the square of the
digits in a number to form a new number until it has been seen before.

For example,

44 -> 32 -> 13 -> 10 -> 1 -> 1
85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89

Therefore any chain that arrives at 1 or 89 will become stuck in an
endless loop. What is most amazing is that EVERY starting number will
eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?

"""

LIMIT = 10**7

def addSquareDigits(n): return sum(int(d)**2 for d in str(n))

def chainLimit(n, cache={1:False, 89:True}):
    if n not in cache:
        cache[n] = chainLimit(addSquareDigits(n))
    return cache[n]

ans = sum(1 for _ in (filter(None, map(chainLimit, range(1, LIMIT)))))

print(ans)
