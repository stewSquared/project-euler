"""The decimal number, 585 = 10010010012 (binary), is palindromic in
both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)


NOTES:

there are fewer palindromes in decimal than binary

iterate through all decimal palindromes (not all integers, testing for palindromes)

and test if the binary version is also palindromic

"""

from itertools import count, takewhile
LIMIT = 10**6

def decimalPalindromes():
    for i in count(1):
        for n in range(10**(i-1), 10**i):
            yield int(str(n) + str(n)[-2::-1])
        for n in range(10**(i-1), 10**i):
            yield int(str(n) + str(n)[::-1])

def palindrome(s): return s == s[::-1]

ans = sum(p for p in takewhile(lambda n: n < LIMIT, decimalPalindromes())
          if palindrome(bin(p)[2:]))

print(ans)
