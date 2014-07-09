import Function.tupled

object p054 {
  class Hand (val cards: Array[String]) extends Ordered[Hand] {
    val CARD_VALUES = "23456789TJQKA".toArray
    val HAND_RANKS = Array (
      "HighCard",
      "OnePair",
      "TwoPair",
      "ThreeKind",
      "Straight",
      "Flush",
      "FullHouse",
      "FourKind",
      "StraightFlush")

    val values = for (c <- cards) yield (CARD_VALUES.indexOf(c(0)) + 1)
    val suits = for (c <- cards) yield c(1)

    lazy val rank: Int = HAND_RANKS.indexOf {
      val distinct = values.toSet.size
      lazy val longest = (
        for ((_, group) <- values.groupBy(identity)) yield group.length
      ).max

      distinct match {
        case 2 => if (longest == 4) "FourKind" else "FullHouse"
        case 3 => if (longest == 3) "ThreeKind" else "TwoPair"
        case 4 => "OnePair"
        case 5 => {
          val straight = values.max - values.min == 4
          val flush = suits.toSet.size == 1
          if (straight && flush) "StraightFlush"
          else if (straight) "Straight"
          else if (flush) "flush"
          else "HighCard"
        }
      }
    }

    override def compare(that: Hand): Int = {
      def tiebreakers(values: Array[Int]) = {
        def groupScore(value: Int, group: Array[Int]) =
          value * math.pow(CARD_VALUES.length+1, group.length-1).toInt

        (values groupBy identity map tupled(groupScore)).toArray.sorted.reverse
      }
      if (this.rank == that.rank) {
        val (thisTiebreaker, thatTiebreaker) =
          (tiebreakers(this.values) zip tiebreakers(that.values)
            dropWhile tupled(_ == _)).head

        thisTiebreaker - thatTiebreaker
      } else {
        this.rank - that.rank
      }
    }
  }

  def main(args: Array[String]) {
    val filename = if (args.nonEmpty) args(0) else "p054.txt"

    val t0 = System.nanoTime / 1000000
    val ans = (io.Source.fromFile(filename).getLines map (_.split(' '))
      map (cards => (new Hand(cards.slice(0,5)), new Hand(cards.slice(5,10))))
      filter tupled(_ > _)).length
    val t1 = System.nanoTime / 1000000

    println(t1 - t0)

    println(ans)
  }
}
