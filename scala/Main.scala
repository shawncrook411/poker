@main def Main(): Unit = {

    println("\n\n\tWelcome to the Command Line Poker odds calculator\n")

    var running = true
    
    while (running) {
        try {
            // Table.clear()

            printMenu() match {
                case 1 => println("odds make combo")
                case 2 => println("odds beat other")
                case 3 => println("outs calculator")
                case 4 => println("run game")
                case 5 => println("display random")
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
    val deck = Deck()

    for (i <- 1 to 5) {
        val cards = deck.deal(i)

        for (card <- cards) {
            println(card)
        }

        println("\n")    
    }
}