def countChangeWays(amount: Int, coins: Array[Int]): Int =
  if (amount < 0 || coins.length == 0) 0
  else if (amount == 0) 1
  else (countChangeWays(amount, coins.drop(1)) +
    countChangeWays(amount - coins(0), coins))

val ans = countChangeWays(200, Array(200, 100, 50, 20, 10, 5, 2, 1))

println(ans)
