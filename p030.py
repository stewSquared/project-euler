"""Surprisingly there are only three numbers that can be written as
the sum of fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 163^4 + 8208 + 947^4 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

Notes:

9**5 = 5905

9**5 * 6 == 354294 => 6 digits maximum

"""

def sumFifthDigits(n):
    return n == sum(int(d)**5 for d in str(n))

ans = sum(filter(sumFifthDigits, range(10, 9**5*6)))

print(ans)
