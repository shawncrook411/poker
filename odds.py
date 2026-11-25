
from itertools import combinations
from collections import Counter

from cards import *
from util import *
from evaluations import *

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

    remaining = GAME_TABLE.remaining().cards
    counts = Counter()
    total = 0

    for board in combinations(remaining, 5):
        hand_type, _ = evaluate(playerHand + list(board))
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
