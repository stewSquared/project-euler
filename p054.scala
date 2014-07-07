import Function.tupled

class PokerHand (val cards: Array[String]) extends Ordered[PokerHand] {

  val HAND_RANKS = Array {
    "HighCard"
    "OnePair"
    "TwoPair"
    "ThreeKind"
    "Straight"
    "Flush"
    "FullHouse"
    "FourKind"
    "StraightFlush"
  }

  val CARD_VALUES = "23456789TJQKA".toArray

  val values = for (c <- cards) yield (CARD_VALUES.indexOf(c(0)) + 1)
  val suits = for (c <- cards) yield c(1)

  lazy val rank = HAND_RANKS.indexOf {
    val distinctValues = values.toSet.size
    lazy val largestGroupSize = (
      for ((_, group) <- values.groupBy(identity)) yield group.length
    ).max

    distinctValues match {
      case 2 => if (largestGroupSize == 4) "FourKind" else "FullHouse"
      case 3 => if (largestGroupSize == 3) "ThreeKind" else "TwoPair"
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

  def compare(that: PokerHand) = {
    def tieBreakers(values: Array[Int]): Array[Int] = {
      def groupScore(value: Int, group: Array[Int]) =
        value * math.pow(CARD_VALUES.length+1, group.length-1).toInt

      (values groupBy identity map tupled(groupScore)).toArray.sorted.reverse
    }

    if (this.rank - that.rank == 0) {
      val (thisTieBreaker: Int, thatTieBreaker: Int) =
        (tieBreakers(this.values) zip tieBreakers(that.values)
          dropWhile tupled(_ == _)).head

      thisTieBreaker - thatTieBreaker
    } else {
      this.rank - that.rank
    }
  }
}

def roundHands(round: String) = {
  val cards = round.split(' ')
  (new PokerHand(cards.slice(0,5)), new PokerHand(cards.slice(5,10)))
}

val ans = (
  io.Source.fromFile("p054.txt").getLines
    map roundHands
    filter tupled(_ > _)
).length

println(ans)
