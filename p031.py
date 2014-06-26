"""In England the currency is made up of pound, f, and pence, p, and
there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, 1f (100p) and 2f (200p).

How many different ways can 2f be made using any number of coins?

"""


def countChangeWays(amount, *coins):
    return (0 if amount < 0 or not coins else
            1 if amount == 0 else
            (countChangeWays(amount, *coins[1:])
             + countChangeWays(amount - coins[0], *coins)))

ans = countChangeWays(200, 200,100,50,20,10,5,2,1)

print(ans)
