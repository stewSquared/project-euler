/**A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which, a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = ^25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.  Find
the product abc.

*/

def isTriplet(a:Int, b:Int, c:Int) = a*a + b*b == c*c
  
val ans = (for {
  a <- 1 until 350
  b <- a until 500
  c = 1000 - a - b
  if isTriplet(a,b,c)
} yield a*b*c).head

println(ans)
