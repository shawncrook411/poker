import scala.io.StdIn
import scala.collection.mutable.ArrayBuffer

def print_input_info() : Unit = {
    println('\n')
    println("\t\t***** MANUALLY INPUT CARDS HERE *******\n")
    println("\tYou must type multiple cards on a line at at time, seperated by spaces")

    println()
    println("\tFor the rank, just type the number")
    println("\tFor royals, please use either 11/12/13/14 OR J/Q/K/A")
    println()
    println("\tYou may also use S/C/H/D for the suit or the full name, or the following values")
    println("\t1: Spade - 2: Club - 3: Heart - 4: Diamond")
    println()
    println("\tExample: Ah - Ace of Hearts, 8D - Eight of Diamonds, 121 - Queen of Spades")
    println("\tExample: Ah Kh Qh")
    println()

}

def get_cards(playerHand: Boolean = false, board: Boolean = false, opponents : Boolean = false) : List[Card] = { 
    var suit = None
    var rank = None

    var cards = ArrayBuffer[Card]()

    if (!(playerHand || board || opponents)) { return List() }

    print("********    ")

    if (playerHand) {
        print("INPUT PLAYER HAND: You may leave blank for a random hand, MAX = 2")
    }

    if (board) {
        print("INPUT COMMUNITY BOARD: You may leave blank for an empty board\n Or type how many cards have been revealed, MAX = 5")
    }

    if (opponents) {
        print("INPUT OPPONENTS: You may leave blank to randomize 5 opponents\n Or you may type one opponents hand, MAX = 2")
    }
    
    print("     ********\n")

    while (true) {
        var result : List[Card] = null

        val values = StdIn.readLine("Input: ").toUpperCase.trim

        try {
            
            if (playerHand && values == "") {
                println("Randomizing player hand")
                val cards = Table.deal(2)
                println("test")
                
                var str = "Player Hand: "
                for (card <- cards) {
                    str += s"$card "
                }
                println(str + '\n')
                return cards
            }

            val num = values.toIntOption

            if (board && values == "") {
                println("Community board is set to empty\n")
                return List()
            } 
            else if (board && num.isDefined) {
                if (num.get <= 5 && num.get >= 1) {
                    println(s"Randomizing ${num.get} community cards")

                    val dealt = Table.deal(num.get)

                    var str = "Board: "

                    for (card <- dealt) {
                        str += s"$card "
                    }
                    println(str + '\n')


                    return dealt
                }
            }

            if (opponents && values == "") {
                println("Randomizing 5 opponent hands")

                var opps = List[Card]()

                for (i <- 1 to 5) {
                    val cards = Table.deal(2)

                    var str = s"Opponent #$i :"
                    for (card <- cards) {
                        str += s"$card "
                        opps = opps :+ card
                    }
                    println(str)
                }

                return opps // Return 2x cards, will break into players later
            }

            val words = values.split("\\s+")

            for (word <- words) {
                if (word.length < 2) {
                    println("Invalid card inputted, please")
                    throw new IllegalArgumentException()
                }

                val rankText = word.dropRight(1)
                val suitText = word.last.toString

                val rank = rankText match {
                    case "1" | "A" | "14" => 14
                    case "J" | "11"       => 11
                    case "Q" | "12"       => 12
                    case "K" | "13"       => 13
                    case other =>
                        val number = other.toIntOption
                        if (number.isDefined && number.get >= 2 && number.get <= 10) {
                            number.get
                        } else {
                            println("Invalid rank inputted, please try again")
                            throw new IllegalArgumentException()
                        }
                }
                

                val suit = suitText match {
                    case "1" | "S" => Suit.SPADE
                    case "2" | "C" => Suit.CLUB
                    case "3" | "H" => Suit.HEART
                    case "4" | "D" => Suit.DIAMOND
                    case _ => 
                        println("Invalid suit inputted, please try again")
                        throw new IllegalArgumentException
                }

                val card = Card(rank, suit)

                if (cards.contains(card) || Table.known_cards().contains(card)) {
                    println("Duplicated card inputted, please try again")
                    throw new IllegalArgumentException()
                }

                cards += card
                println(s"Card added: $card")
            }

            return cards.toList.take(5)
            
        } catch {
            case e: Exception => ()
        } 
    }

    ??? // this is cute, I haven't seen this before
}

def printMenu() : Int = {
    println("Menu\n")
    println("\t1. Get odds of making a certain combination")
    println("\t2. Get odds of beating another hand")
    println("\t3. Outs calculator")
    println("\t4. Run simulated game")
    println("\t5. Show random board")
    println("\t0. Quit")
    println()
     
    val input = StdIn.readLine("Option: ")

    if (input == null) {
        println("\nThank you! Have a good day :)")
        sys.exit(0)
    }

    val option = input.trim.take(1).toInt

    option match {
        case 1 | 2 | 3 | 4 => "Print Input Info"
        case _ => ""
    }

    return option
}

def display_random() : Unit = {}