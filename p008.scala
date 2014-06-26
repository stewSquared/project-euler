/**Find the greatest product of five consecutive digits in the 1000-digit number.

[p008.txt]

*/
val nums = for (
  c <- io.Source.fromFile("p008.txt").mkString
  if c != '\n'
) yield c.asDigit

val products = for {
  i <- 0 to nums.length - 5;
  seq5 = nums.slice(i, i+5)
} yield seq5.product

val ans = products.max

println(ans)
