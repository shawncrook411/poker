
object Suit {
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

object Rank {
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