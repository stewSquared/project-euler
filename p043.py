from itertools import permutations

def div_property(pandigital, primes=(2,3,5,7,11,13,17)):
    substrings = (int(pandigital[i:i+3]) for i in range(1,8))
    return all(s % p == 0 for s, p in zip(substrings, primes))

pandigitals = map("".join, permutations("0123456789"))

ans = sum(map(int, filter(div_property, pandigitals)))

print(ans)
