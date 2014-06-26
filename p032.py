"""We shall say that an n-digit number is pandigital if it makes use
of all the digits 1 to n exactly once; for example, the 5-digit
number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254,
containing multiplicand, multiplier, and product is 1 through 9
pandigital.

Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.

Notes:

"""
from itertools import permutations

DIGITS = "123456789"

def pandigitalProducts(perm):
    products = (int("".join(perm[:i])) * int("".join(perm[i:]))
                for i in range(1, len(perm)//2 + 1))
    for p in products:
        if sorted(str(p) + "".join(perm)) == list(DIGITS): yield p

ans = sum(set(p for ps in map(pandigitalProducts, (permutations(DIGITS, r=5))) for p in ps))

print(ans)
