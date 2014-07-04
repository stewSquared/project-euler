val LIMIT = math.pow(10, 6).toInt

def merge (a: Stream [Int], b: Stream [Int]): Stream [Int] = 
  if (a.head<b.head) a.head #:: merge(a.tail, b)
  else b.head #:: merge(b.tail, a)

def decimalPalindromes(): Stream[Int] = merge (
  Stream from 1 map (n =>
    Integer.parseInt((n/10).toString + n.toString.reverse)),
  Stream from 1 map (n =>
    Integer.parseInt(n.toString + n.toString.reverse)))

def binIsPali(n: Int) = {
  val binstr = Integer.toBinaryString(n)
  binstr equals binstr.reverse
}

val ans = decimalPalindromes.takeWhile(_ < LIMIT).filter(binIsPali(_)).sum

println(ans)
