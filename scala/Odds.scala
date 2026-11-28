import scala.collection.mutable


def odds_make_combo() : Unit = {
    var board: List[Card] = List()
    var done = false

    while (!done) {
        try {
            val hand = get_cards(playerHand=true)
            Table.add_player_hand(hand)

            val board = get_cards(board=true)
            Table.set_board(board)

            done = true

        } catch {
            case e: Exception => ()
        }
    }

    Table.show()

    print("\nCalculating... Please be patient...\n")

    val remaining = Table.remaining().cards
    val counts = Array.fill(9)(0)
    var total = 0

    val need = 5 - Table.board.length

    for (runout <- remaining.combinations(need)) {
        val cards = Table.community() ++ runout
        val result = evaluate(cards)

        counts(result.handType) += 1
        total += 1
    }

    for (h <- 8 to 0 by -1) {
        val percent = counts(h).toDouble / total * 100
        println(f"${HAND_LABELS(h)}%-16s$percent%8.3f%%")
    }
}

def odds_make_comb() : Unit = {}

def odds_beat_other() : Unit = {}

def outs_calculator() : Unit = {}

def run_game() : Unit = {}