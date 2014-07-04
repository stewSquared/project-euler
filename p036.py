from itertools import count, takewhile
LIMIT = 10**6


def decimal_palindromes():
    for i in count(1):
        for n in range(10**(i-1), 10**i):
            yield int(str(n) + str(n)[-2::-1])
        for n in range(10**(i-1), 10**i):
            yield int(str(n) + str(n)[::-1])


def bin_is_pali(n):
    binstr = bin(n)[2:]
    return binstr == binstr[::-1]


ans = sum(filter(bin_is_pali, takewhile(lambda n: n < LIMIT,
                                        decimal_palindromes())))

print(ans)
