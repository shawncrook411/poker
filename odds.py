
from itertools import combinations
from collections import Counter

from cards import *
from util import get_hand, get_board
from evaluations import *

GAME_TABLE = None

def odds_make_combo():
    print()
    playerHand = get_hand()

    print()
    board = get_board(taken=playerHand)

    try: 
        GAME_TABLE= Table(
            playerHand=playerHand,
            board=board
        )
    except TypeError:
        print("Invalid input, please try again")
        return

    GAME_TABLE.show()

    print("Calculating... Please be patient...\n")

    remaining = GAME_TABLE.remaining().cards
    counts = Counter()
    total = 0

    need = 5 - len(board) 

    for board in combinations(remaining, need):
        cards = list(playerHand) + list(board) + list(GAME_TABLE.board)

        hand_type, _ = evaluate(cards)

        counts[hand_type] += 1
        total += 1

    for hand_type in sorted(counts, reverse=True):
        print(f"{hand_type.label:<16}{counts[hand_type] / total:8.3%}")


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


def main():
    pass

if __name__ == "__main__":
    main()