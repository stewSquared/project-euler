from functools import reduce
from itertools import repeat

ans = reduce(lambda m, n: m*n % 10**10, repeat(2, 7830457), 28433) + 1

print(ans)
