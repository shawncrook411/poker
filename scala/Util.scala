import scala.io.StdIn

def print_input_info() : Unit = {}

def get_cards(playerHand: Boolean = false, board: Boolean = false, opponents : Boolean = false) : List[Card] = { List() }

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