"""If p is the perimeter of a right angle triangle with integral
length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?

"""

from itertools import product, groupby
from math import sqrt

p_vals = map(int, filter(lambda p: p % 1 ==0 and p < 1000, (a + b + sqrt(a**2 + b**2)
                                                            for a in range(500)
                                                            for b in range(a))))

def groupSize(group):
    return len(list(group[1]))

ans, _ = max(groupby(sorted(p_vals)), key=lambda group: len(list(group[1])))

print(ans)
