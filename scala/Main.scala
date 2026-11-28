@main def Main(): Unit = {

    println("\n\n\tWelcome to the Command Line Poker odds calculator\n")

    var running = true
    
    while (running) {
        try {
            Table.clear()

            printMenu() match {
                case 1 => odds_make_combo()
                case 2 => odds_beat_other()
                case 3 => outs_calculator()
                case 4 => run_game()
                case 5 => display_random()
                case 9 => testing()
                case 0 => running = false
                case _ => println("Invalid option selected, please try again")
            }

            if (running) {
                Thread.sleep(2000)
                println("\n\n")
            }

        } catch {
            case e: IllegalArgumentException =>
                println("Something went wrong, please try again")
                running = false
        }
    }
}

def testing(): Unit = {

    var continue = true

    while (continue) {
        val deck = Deck()
        val cards = deck.deal(7)

        val result = evaluate(cards)


        if (result.handType == HandType.STRAIGHT_FLUSH) {
            println(result)
            println(cards)

            continue = false
        }
    }
}