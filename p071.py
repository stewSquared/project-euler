"""By listing the set of reduced proper fractions for d <= 1,000,000
in ascending order of size, find the numerator of the fraction
immediately to the left of 3/7"""


from fractions import Fraction as F

def floor(frac, denom):
    """greatest proper fraction less than f with denominator d"""
    n, d = frac.numerator, frac.denominator
    numer = (n*denom)//d
    numer = numer-1 if numer/denom == n/d else numer
    return F(numer, denom)

ans = max(floor(F(3,7), d) for d in range(2, 10**6+1)).numerator

print(ans)
