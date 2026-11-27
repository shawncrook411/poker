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
}

def get_groups(cards: List[Card]) : (List[Int], List[Int])  = { 
    val counts = scala.collection.mutable.Map[Int, Int]()

    for (card <- cards) {
        counts(card.rank) = counts.getOrElse(card.rank, 0) + 1
    }

    val groups = counts.toList.sortBy(group => (group._2, group._1)).reverse

    val ranks = groups.map(group => group._1)
    val kinds = groups.map(group => group._2)
    
    return (ranks, kinds)
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

def is_four_kind(cards: List[Card]): Option[List[Int]] = { 
    val (ranks, kinds) = get_groups(cards)

    if (kinds(0) == 4) { 
        return Some(List(ranks(0), ranks.drop(1).max))   
    }

    return None
}

def is_full_house(cards: List[Card]): Option[List[Int]] = { 
    val (ranks, kinds) = get_groups(cards)

    if (kinds(0) == 3 && kinds(1) >= 2) { 
        return Some(List(ranks(0), ranks(1)))
    }

    return None
}

def is_three_kind(cards: List[Card]): Option[List[Int]] = { 
    val (ranks, kinds) = get_groups(cards)

    if (kinds(0) == 3) { 
        return Some(ranks.take(3))
    }

    return None

}

def is_two_pair(cards: List[Card]): Option[List[Int]] = { None }

def is_pair(cards: List[Card]): Option[List[Int]] = { None }

def evaluate(cards: List[Card]): (HandType.Value, List[Card]) = { (HandType(1), List()) }