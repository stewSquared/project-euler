"""145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the
factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

NOTES:

9! = 362880 ==> 
9! * 8 = 7 digits ==>
max of 7 digits or 10000000 bound
or 9! ** 7

"""

from math import factorial as f

def curious(n):
    return n == sum(f(int(d)) for d in str(n))

ans = sum(filter(curious, range(3, f(9)*6)))

print(ans)
