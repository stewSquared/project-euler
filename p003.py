"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

n = 600851475143

def primeFactors(n):
    k = 2
    while n != 1:
        while n % k == 0:
            yield k
            n = n / k
        k += 1

ans = max(primeFactors(n))

print(ans)
