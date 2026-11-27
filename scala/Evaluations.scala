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

def get_groups(cards: List[Card]) : (List[Int], List[Int])  = { (List(), List()) }

def is_straight_flush(cards: List[Card]): Boolean = { true }

def is_straight(cards: List[Card]): Boolean = { true }

def is_flush(cards: List[Card]): Boolean = { true }

def is_four_kind(cards: List[Card]): Boolean = { true }

def is_full_house(cards: List[Card]): Boolean = { true }

def is_three_kind(cards: List[Card]): Boolean = { true }

def is_two_pair(cards: List[Card]): Boolean = { true }

def is_pair(cards: List[Card]): Boolean = { true }

def evaluate(cards: List[Card]): (HandType.Value, List[Card]) = { (HandType(1), List()) }