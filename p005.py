"""2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?

"""

from functools import reduce

def lcm(m, n):
    for k in range(m, m*n + 1, m):
        if k%n == 0: return k

reduce(lcm, range(1, 21))
