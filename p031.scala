/**In England the currency is made up of pound, f, and pence, p, and
there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, 1f (100p) and 2f (200p).

How many different ways can 2f be made using any number of coins?

*/


def countChangeWays(amount: Int, coins: Array[Int]): Int =
  if (amount < 0 || coins.length == 0) 0
  else if (amount == 0) 1
  else (countChangeWays(amount, coins.drop(1)) +
    countChangeWays(amount - coins(0), coins))

val ans = countChangeWays(200, Array(200, 100, 50, 20, 10, 5, 2, 1))

println(ans)
