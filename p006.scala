/**Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.

*/

def sum(a: Iterable[Int]) = a.reduce(_ + _)
def square(x: Int) = x * x

val ans = square(sum(1 to 100)) - sum((1 to 100) map square)

println(ans)
