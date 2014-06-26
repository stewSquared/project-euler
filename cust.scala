package cust {

  object Primes {
    def apply(n: Int) = primesWN.drop(n-1).head

    def primes(): Stream[Int] = {
      def merge(a: Stream[Int], b: Stream[Int]): Stream[Int] = {
        def next = a.head min b.head
        Stream.cons(next, merge(if (a.head == next) a.tail else a,
          if (b.head == next) b.tail else b))
      }
      def test(n: Int, compositeStream: Stream[Int]): Stream[Int] = {
        if (n > compositeStream.head) throw new Exception()
        else if (n == compositeStream.head) test(n+1, compositeStream.tail)
        else Stream.cons(n, test(n+1, merge(Stream.from(n*n, n), compositeStream)))
      }
      test(2, Stream.from(4, 2))
    }

    def primesWN(): Stream[Int] = {
      def merge(a: Stream[Int], b: Stream[Int]): Stream[Int] = {
        def next = a.head min b.head
        Stream.cons(next, merge(if (a.head == next) a.tail else a,
          if (b.head == next) b.tail else b))
      }
      def test(n: Int, q: Int,
        compositeStream: Stream[Int],
        primesStream: Stream[Int]): Stream[Int] = {
        if (n == q) test(n+2, primesStream.tail.head*primesStream.tail.head,
          merge(compositeStream,
            Stream.from(q, 2*primesStream.head).tail),
          primesStream.tail)
        else if (n == compositeStream.head) test(n+2, q, compositeStream.tail,
          primesStream)
        else Stream.cons(n, test(n+2, q, compositeStream, primesStream))
      }
      Stream.cons(2, Stream.cons(3, Stream.cons(5,
        test(7, 25, Stream.from(9, 6), primesWN().tail.tail))))
    }
  }
}
