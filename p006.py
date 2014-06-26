"""Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.

"""

def square(x): return x * x

ans = square(sum(range(1, 101))) - (sum (square(n) for n in range(1, 101)))

print(ans)
