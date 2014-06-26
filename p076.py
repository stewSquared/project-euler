"""It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

7
6 1
5 2
5 1 1
4 3
4 2 1
4 1 1 1
3 3 1
3 2 2
3 2 1 1
3 1 1 1 1
2 2 2 1
2 2 1 1 1
2 1 1 1 1 1
1 1 1 1 1 1 1

How many different ways can one hundred be written as a sum of at
least two positive integers?
"""

def countChangeWays(amount, *coins):
    return (0 if amount < 0 or not coins else
            1 if len(coins) == 1 and not amount%coins[0] else
            1 if amount == 0 else
            (countChangeWays(amount, *coins[1:])
             + countChangeWays(amount - coins[0], *coins)))

test = countChangeWays(7, *range(1,7))
ans = countChangeWays(100, *range(1,100))

print(ans)

def countChangeWays(amount, *coins):
    return (0 if amount < 0 or not coins else
            1 if amount == 0 else
            (countChangeWays(amount, *coins[1:])
             + countChangeWays(amount - coins[0], *coins)))

ans = countChangeWays(7,6,5,4,3,2,1)

print(ans)
