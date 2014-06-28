/**The decimal number, 585 = 10010010012 (binary), is palindromic in
both bases.

Find the sum of all numbers, less than one million, which are
palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not
include leading zeros.)*/

val LIMIT = math.pow(10, 6).toInt


def decimalPalindromes(): Stream[Int] = {
  def powersOfTen: Stream[Int] = Stream.cons(1, powersOfTen map (_*10))
  def palindromesByMagnitude(mag: Int): Stream[String] = {
    def evenLenPali(n: Int) = n.toString + n.toString.reverse
    def oddLenPali(n: Int) = n.toString + n.toString.reverse.substring(1)
    val nums = (mag until mag*10).toStream

    (nums map oddLenPali) ++ (nums map evenLenPali)
  }

  (powersOfTen map palindromesByMagnitude).flatten map Integer.parseInt
}


def binIsPali(n: Int) = {
  val binstr = Integer.toBinaryString(n)
  binstr equals binstr.reverse
}


val ans = decimalPalindromes.takeWhile(_ < LIMIT).filter(binIsPali(_)).sum

println(ans)
