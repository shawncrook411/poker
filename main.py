from cards import *
import itertools

GAME_TABLE = None

def odds_make_combo():
    print()
    playerHand = get_hand()

    try: 
        GAME_TABLE= Table(
            playerHand=playerHand
        )
    except TypeError:
        print("Invalid input, please try again")
        return

    print("Odds with any random 5 community cards")

    need = 5 - len(GAME_TABLE.board)
    possible_7 = (list(option) + playerHand + GAME_TABLE.board
                   for option in itertools.combinations(GAME_TABLE.remaining().cards, need))


    possible_5 = ()
        


def outs_calculator():
    pass





def odds_beat_other():
    print()
    playerHand = get_hand()

    opps = []

    while True:
        try:
            num_opp = int(input("How many opponents are you up against?: "))
            if num_opp > 6 or num_opp < 0: raise ValueError
            break

        except ValueError:
            print("Sorry that is an invalid opponent count, please try again")

    
    for i in range(num_opp):
        print(f"Please input for Opponent {i+1}")
        opps.append(get_hand())

    GAME_TABLE = Table(playerHand=playerHand, opponentsHands=opps)

def run_game():
    pass

def get_card():
    suit = None
    rank = None

    while True:
        print(f"Please input suit information")
        print("You may also use S/C/H/D for input")
        print("1. Spade")
        print("2. Club")
        print("3. Heart")
        print("4. Diamond")

        val = input(f"SUIT: ").upper()

        match val:
            case "1" | "S":
                suit = Suit.SPADE
                break

            case "2" | "C":
                suit = Suit.CLUB
                break

            case "3" | "H":
                suit = Suit.HEART
                break

            case "4" | "D":
                suit = Suit.DIAMOND
                break

            case _:
                print("Invalid suit inputted, please try again")
                continue


    while True:
        print("Please input rank information")
        print("If typing a number card, just type the number")
        print("For royals, please use either 11/12/13/14 OR J/Q/K/A")

        val = input("RANK: ").upper()

        match val:
            case "1" | "A" | "14":
                rank = Rank.ACE
                break

            case "J" | "11":
                rank = Rank.JACK
                break

            case "Q" | "12":
                rank = Rank.QUEEN
                break

            case "K" | "13":
                rank = Rank.KING
                break

            case _:
                try:
                    rank = Rank(int(val))
                    break

                except KeyError:
                    print("Invalid rank inputted, please try again")
                    continue

    return Card(rank=rank, suit=suit)
            
def get_hand(num=2):

    while True:
        print("Is this a random hand, or would you like to one?")
        print("1. Random")
        print("2. Input")
        val = int(input("Option: "))

        if val in [1,2]:
            break

        print("Invalid option selected, please try again")

    cards = []

    if val == 1:
        for i in range(num):
            while True:
                card = Card()

                if card not in cards:
                    cards.append(card)
                    break

    if val == 2:
        for i in range(num):
            print(f"Card {i+1}\n")
            card = get_card()

            if card not in cards:
                cards.append(card)


    return cards

def print_menu():

    while True:
        print("\tMenu\n")
        print("1. Get odds of making a certain combination")
        print("2. Get odds of beating another hand")
        print("3. Outs calculator")
        print("4. Run simulated game")
        print("0. Quit")
        val = input("Option: ")


        if int(val) in [1,2,3]:
            return int(val)

        print("Invalid option selected, please try again")


def main():
    print("Welcome to the Command Line Poker odds calculator\n")
    
    try: 
        while True:
            match int(print_menu()):
                case 1:
                    odds_make_combo()
                case 2:
                    odds_beat_other()
                case 3:
                    outs_calculator()
                case 4:
                    run_game()
                case 0:
                    break

    except (KeyboardInterrupt, EOFError):
        print()


if __name__ == "__main__":
    main()