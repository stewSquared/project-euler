import java.lang.Long.parseLong

val primes: List[Int] = List(2,3,5,7,11,13,17)

def divProperty(pandigital: String) =
  (1 to 8) map (i => pandigital.slice(i, i+3)) map parseLong zip primes forall
    Function.tupled(_ % _ == 0)

val ans = ("0123456879".permutations filter divProperty map parseLong).sum

println(ans)
