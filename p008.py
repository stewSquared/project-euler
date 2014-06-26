"""Find the greatest product of five consecutive digits in the 1000-digit number.

[p008.txt]

"""
from functools import reduce
from operator import mul
def product(a): return (reduce(mul, a))

digits = [int(digit) for line in open("p008.txt") for digit in line.rstrip()]

ans = max(product(seq5) for seq5 in (digits[i:i+5] for i in range(len(digits) - 4)))

print(ans)
