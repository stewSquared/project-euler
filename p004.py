"""A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91x99

Find the largest palindrome made from the product of two 3-digit numbers.

"""
from itertools import dropwhile

def palindromes(): for n in range(999,99,-1): yield 1000*n + int(str(n)[::-1])

def desired(n):
    return any((lambda m: n%m == 0 and len(str(int(n/m))) == 3)(k) for k in range(100,1000))

ans = next(n for n in palindromes() if desired(n))

print(ans)

def palindrome(n): return n == int(str(n)[::-1])
ans = max(n*m for n in range(100, 1000) for  m in range(100, 1000) if palindrome(n*m))

print(ans)
