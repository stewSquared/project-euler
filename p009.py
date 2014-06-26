"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which, a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = ^25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.  Find
the product abc.

"""

def isTriplet(a,b,c): return a*a + b*b == c*c

ans = next(a*b*c
           for a in range(1, 350)
           for b in range(a, 500)
           for c in [1000 - a - b]
           if isTriplet(a, b, c))

print(ans)
