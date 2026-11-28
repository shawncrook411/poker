object  HandType extends Enumeration {
    val STRAIGHT_FLUSH = 8
    val FOUR_KIND = 7
    val FULL_HOUSE = 6
    val FLUSH = 5
    val STRAIGHT = 4
    val THREE_KIND = 3
    val TWO_PAIR = 2
    val PAIR = 1
    val HIGH = 0
}

val HAND_LABELS = List(
    "High Card",
    "Pair",
    "Two Pair",
    "Three of a Kind",
    "Straight",
    "Flush",
    "Full House",
    "Four of a Kind",
    "Straight Flush"
)

case class HandResult(handType: Int, tiebreak: List[Int]) {

    def label : String = HAND_LABELS(handType)

    def compare(other: HandResult): Int = {
        if (handType != other.handType) {
            return handType - other.handType
        }

        var i = 0
        while (i < tiebreak.length && i < other.tiebreak.length) {
            if (tiebreak(i) != other.tiebreak(i)) {
                return tiebreak(i) - other.tiebreak(i)
            }
            i += 1
        }

        tiebreak.length - other.tiebreak.length
    }

    override def toString(): String = {
        HAND_LABELS(handType)
    }
}

def is_straight_flush(cards: List[Card]): Option[List[Int]] = { 
    var result : Option[List[Int]] = None

    for (suit <- Suit.all) {
        val suited = cards.filter(c => c.suit == suit)

        if (suited.length >= 5) {
            result = is_straight(suited)
        }
    }   

    return result
}

def is_straight(cards: List[Card]): Option[List[Int]] = { 
    var unique = cards.map(c => c.rank).distinct.sorted.reverse

    if (unique.head == 14) {
        unique = unique :+ 1
    }

    var run = 1
    var i = 0

    while (i < unique.length - 1) {
        if (unique(i) == unique(i+1) + 1) {
            run += 1

            if (run == 5) {
                return Some(List(unique(i - 3)))
            }
        } else {
            run = 1
        }
        i += 1
    }

    return None
 }

def is_flush(cards: List[Card]): Option[List[Int]] = {
    var result : Option[List[Int]] = None

    for (suit <- Suit.all) {
        val suited = cards.filter(c => c.suit == suit).map(c => c.rank)

        if (suited.length >= 5) {
            result = Some(suited.sorted.reverse.take(5))
        }
    }   

    return result
}


def evaluate(cards: List[Card]): HandResult = {
    val counts = scala.collection.mutable.Map[Int, Int]()

    for (card <- cards) {
        counts(card.rank) = counts.getOrElse(card.rank, 0) + 1
    }

    val groups = counts.toList.sortBy(group => (group._2, group._1)).reverse

    val ranks = groups.map(group => group._1)
    val kinds = groups.map(group => group._2)

    val straight_flush = is_straight_flush(cards)
    val flush = is_flush(cards)
    val straight = is_straight(cards)

    kinds match {
        case _ if straight_flush.isDefined => HandResult(HandType.STRAIGHT_FLUSH, straight_flush.get)

        case 4 :: _ => HandResult(HandType.FOUR_KIND, ranks.take(1) ++ ranks.drop(1).sorted.reverse.take(1))

        case 3 :: n :: _ if n >= 2 => HandResult(HandType.FULL_HOUSE, ranks.take(2)) // We do n >= 2 in case we pass 7 cards and there are 2 sets of 3, rare but happens

        case _ if flush.isDefined => HandResult(HandType.FLUSH, flush.get)

        case _ if straight.isDefined => HandResult(HandType.STRAIGHT, straight.get)

        case 3 :: _ => HandResult(HandType.THREE_KIND, ranks.take(3))

        case 2 :: 2 :: _ => HandResult(HandType.TWO_PAIR, ranks.take(2) ++ ranks.drop(2).sorted.reverse.take(1))

        case 2 :: _  => HandResult(HandType.PAIR, ranks.take(4))

        case _ => HandResult(HandType.HIGH, ranks.take(5))
    }
}