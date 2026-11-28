import scala.collection.mutable.ArrayBuffer
import scala.util.Random

object Suit extends Enumeration {
    type Suit = Value

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
    type Rank = Value

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
        print("dealing......")
        val dealt = Random.shuffle(cards.toList).take(n)

        for (c <- dealt) {
            cards -= c
        }

        return dealt
    }

    def length: Int = cards.length

    def contains(card: Card): Boolean = cards.contains(card)

}

class Player(var hand: List[Card] = List()) {

    override def toString: String = {
        var str = ""

        for (c <- hand) {
            str += s"$c "
        }

        return str
    }
}

object Table {

    var board: List[Card] = List()
    var player: Player = null
    var opponents: List[Player] = List()
    var deck: Deck = Deck()

    def add_player_hand(hand: List[Card]) : Unit = {
        if (hand.toSet.size != 2) {
            throw new IllegalArgumentException()
        }

        player = new Player(hand)
        claim(hand)
    }

    def community(current: Player = null): List[Card] = {
        if (current == null) {
            return player.hand ++ board
        } else {
            return current.hand ++ board
        }
    }

    def add_opponents(new_opponents: List[Player]): Unit = {
        opponents = List()

        for (p <- new_opponents) {
            if (p.hand.toSet.size != 2) {
                throw new IllegalArgumentException()
            }

            opponents = opponents :+ p
            claim(p.hand)
        }
    }

    def set_board(new_board: List[Card]) : Unit = {
        if (new_board.toSet.size > 5) {
            throw new IllegalArgumentException()
        }

        board = new_board.distinct
        claim(board)
    }

    def board_cards() : List[Card] = {
        return board
    }

    def known_cards() : List[Card] = { 
        var cards = player.hand ++ board

        for (player <- opponents) {
            for (card <- player.hand) {
                cards = cards :+ card
            }
        }

        return cards
    }

    def remaining(): Deck = deck

    def deal(n: Int = 2): List[Card] = {
        return deck.deal(n)
    }

    def claim(cards: List[Card]): Unit = {
        for (card <- cards) {
            if (deck.contains(card)) {
                deck.cards -= card
            }
        }
    }

    def show(): Unit = {
        println("\tTable\n")

        println(s"\tPlayer: ${player}\n")
        println(s"\t\tEvaluation: ${HAND_LABELS(evaluate(community()).handType)}")

        var str = "\tBoard: "
        for (card <- board) {
            str += s"$card "
        }
        println(str + '\n')

        var i = 0
        for (opponent <- opponents) {
            print(s"\tOpponent #$i: $opponent")
            print(s"\t\tEvaluation: ${HAND_LABELS(evaluate(community(opponent)).handType)}")
            i += 1
        }

        if (opponents.length == 0) {
            println("\t No Opponents")
        }

        println(s"\tUnseen cards: ${remaining().length}")

    }

    def random() : Unit = {

        deck = Deck()

        add_player_hand(deal())

        set_board(deal(5))

        var opponents = List[Player]()

        for (i <- 1 to 5) {
            opponents = opponents :+ new Player(deal())
        }

        add_opponents(opponents)
    }

    def clear() : Unit = {
        player = new Player()
        board = List()
        opponents = List()
        deck = new Deck()
    }
}