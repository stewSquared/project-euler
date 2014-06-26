/**The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

*/

val n = 600851475143L

def primeFactors(n: Long): Stream[Int] = {
  def test(n: Long, k: Int): Stream[Int] = 
    if (n == 1) Stream.empty
    else if (n % k == 0) Stream.cons(k, test(n/k, k))
    else test(n, k+1)
  test(n, 2)
}

val ans = primeFactors(n).reduce(_ max _)

println(ans)
