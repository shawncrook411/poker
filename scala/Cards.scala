import scala.collection.mutable.ArrayBuffer
import scala.util.Random

object Suit extends Enumeration {
    val SPADE = 0
    val CLUB = 1
    val HEART = 2
    val DIAMOND = 3

    val all = List(SPADE, CLUB, HEART, DIAMOND)

    def str(suit: Int): String = {
        suit match {
            case 0 => "♠"
            case 1 => "♣"
            case 2 => "♥"
            case 3 => "♦"
        }
    }
}

object Rank extends Enumeration {
    val ACE=14
    val KING=13
    val QUEEN=12
    val JACK=11
    val TEN=10
    val NINE=9
    val EIGHT=8
    val SEVEN=7
    val SIX=6
    val FIVE=5
    val FOUR=4
    val THREE=3
    val TWO=2

    val all = List(ACE, KING, QUEEN, 
        JACK, TEN, NINE, EIGHT, SEVEN, 
        SIX, FIVE, FOUR, THREE, TWO
    )

    def str(rank: Int): String = {
        rank match {
            case 14 | 1 => "A"
            case 13 => "K"
            case 12 => "Q"
            case 11 => "J"
            case 10 => "T"
            case other => other.toString
        }
    }
}

case class Card(rank: Int, suit: Int) {

    override def toString: String = {
        val color = if (suit == Suit.HEART || suit == Suit.DIAMOND) "31" else "30"
        val rankText = Rank.str(rank)
        "\u001b[" + color + ";107m " + f"$rankText%2s" + Suit.str(suit) + " \u001b[0m"
    }

    def sort(cards: List[Card]) : List[Card] = {
        cards.sortBy(c => c.rank).reverse
    }
}

class Deck() {

    var cards = ArrayBuffer[Card]()

    for (rank <- Rank.all) {
        for (suit <- Suit.all) {
            cards += Card(rank, suit)
        }
    }

    def shuffle(): Unit = {
        cards = Random.shuffle(cards)
    }

    def deal(n: Int): List[Card] = {
        val dealt = Random.shuffle(cards.toList).take(n)

        for (c <- dealt) {
            cards -= c
        }

        return dealt
    }

    def length: Int = cards.length

    def contains(card: Card): Boolean = cards.contains(card)

}