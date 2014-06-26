"""It can be seen that the number, 125874, and its double, 251748,
contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and
6x, contain the same digits.

"""

def shuffleCheck(n):
    digits = sorted(str(n))
    return all(sorted(str(m * n)) == digits for m in range(2,7))

def shuffleNumbers():
    for exp in range(10):
        for n in range(10**exp, 10**(exp+1)//6+1):
            if shuffleCheck(n): yield n

ans = next(shuffleNumbers())

print(ans)
