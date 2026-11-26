
from itertools import combinations
from collections import Counter

from cards import *
from util import get_cards
from evaluations import *


def odds_make_combo():
    while True:
        try: 
            hand = get_cards(playerHand=True)
            Table.add_player_hand(hand)

            board = get_cards(board=True)
            Table.set_board(board)
            break

        except TypeError:
            print("Invalid input, please try again")
            continue

    Table.show()

    print("\nCalculating... Please be patient...\n")

    remaining = Table.remaining().cards
    counts = Counter()
    total = 0

    need = 5 - len(board) 

    for board in combinations(remaining, need):
        cards = Table.community() + list(board)
        hand_type, _ = evaluate(cards)

        counts[hand_type] += 1
        total += 1

    for hand_type in list(HandType):
        print(f"{hand_type.label:<16}{counts[hand_type] / total:8.3%}")


def odds_beat_other():
    while True:
        try: 
            hand = get_cards(playerHand=True)
            Table.add_player_hand(hand)

            board = get_cards(board=True)
            Table.set_board(board)

            opponents = get_cards(opponents=True)
            Table.add_opponents(opponents)
            
            break

        except TypeError:
            print("Invalid input, please try again")
            continue


    print("\nCalculating... Please be patient...\n")
    
    Table.show()


    remaining = Table.remaining().cards

    need = 5 - len(board)

    wins = 0
    chops = 0
    losses = 0

    for runout in combinations(remaining, need):

        cards = Table.community() + list(runout)
        player = evaluate(cards)

        opponent_best = None

        for opponent in Table.opponents:
            opponent_cards = Table.community(opponent) + list(runout)

            result = evaluate(opponent_cards)

            if opponent_best is None or result > opponent_best:
                opponent_best = result

        if player > opponent_best:
            wins += 1

        elif player < opponent_best:
            losses += 1

        else:
            chops += 1

    total = wins + chops + losses

    print()
    print(f"Total Wins:   {wins:<16} %: {wins/total:8.3%}")
    print(f"Total Losses: {losses:<16} %: {losses/total:8.3%}")
    print(f"Total Draws   {chops:<16} %: {chops/total:8.3%}")


def outs_calculator():
    while True:
        try: 
            hand = get_cards(playerHand=True)
            Table.add_player_hand(hand)

            while True:
                board = get_cards(board=True)

                if len(board) < 3: 
                    print("Can only calculate outs after the Flop (first three cards), Sorry!")
                    print("Please input cards for the board")
                    continue

                Table.set_board(board)
                break

            opponents = get_cards(opponents=True)
            Table.add_opponents(opponents)
            
            break

        except TypeError:
            print("Invalid input, please try again")
            continue

    Table.show()

    print("\nCalculating... Please be patient...\n")

    remaining = Table.remaining().cards

    need = 5 - len(board)

    outs = set()
    runners = set()

    player = evaluate(Table.community())

    opponent_best = None

    for opponent in Table.opponents:
        opponent_cards = Table.community(opponent)

        result = evaluate(opponent_cards)

        if opponent_best is None or result > opponent_best:
            opponent_best = result

    for_player = True

    if player > opponent_best:
        print("Player is already ahead, calculating outs for opponents instead")
        for_player = False


    # Calculate single card outs
    for runout in combinations(remaining, 1):
        cards = Table.community() + list(runout)
        player = evaluate(cards)

        opponent_best = None

        for opponent in Table.opponents:
            opponent_cards = Table.community(opponent) + list(runout)

            result = evaluate(opponent_cards)

            if not for_player and result > player:
                outs.add(runout)

            if opponent_best is None or result > opponent_best:
                opponent_best = result

        if for_player and player >= opponent_best:
            outs.add(runout[0])

    if need == 2:
        # Calculate double card runner outs, need 2 good cards in a row
        for runout in combinations(remaining, 2):
            if runout[0] in outs or runout[1] in outs:
                continue
            
            cards = Table.community() + list(runout)
            player = evaluate(cards)

            opponent_best = None

            for opponent in Table.opponents:
                opponent_cards = Table.community(opponent) + list(runout)

                result = evaluate(opponent_cards)

                if not for_player and result > player:
                    runners.add(runout)

                if opponent_best is None or result > opponent_best:
                    opponent_best = result

            if for_player and player >= opponent_best:
                runners.add(runout)

    outs, runners

    if for_player:
        print("\t**** Outs for Player to become ahead ****")

    else:
        print("\t**** Outs for Player to become behind ****")

    for card in outs:
        print(f"{card}", end=' ')

    if need == 2:
        if for_player:
            print("\n\t**** Running outs for Player to become ahead ****")
        else:
            print("\n\t**** Running outs for Player to become behind ****")

        for runout in runners:
            str = f"["
            for card in runout:
                str += f"{card} "
            str += f"]\t"
            print(str)

            

def run_game():
    while True:
        try: 
            hand = get_cards(playerHand=True)
            Table.add_player_hand(hand)

            while True:
                board = get_cards(board=True)

                if len(board) < 3: 
                    print("Can only calculate outs after the Flop (first three cards), Sorry!")
                    print("Please input cards for the board")
                    continue

                Table.set_board(board)
                break

            opponents = get_cards(opponents=True)
            Table.add_opponents(opponents)
            
            break

        except TypeError:
            print("Invalid input, please try again")
            continue

    print("Let the game begin!\n")

    need = 5 - len(board)
    
    Table.board += Table.deal(need)
    cards = Table.community()

    player = evaluate(cards)

    win = True
    draw = False
    result = None

    for opponent in Table.opponents:
        opponent_cards = Table.community(opponent)

        result = evaluate(opponent_cards)

        if result == player:
            draw = True

        if result > player:
            win = False
            draw = False

            break

    Table.show()

    if draw:
        print(f"Player has chopped the pot with a {player[0].label}")
        return

    if win:
        print(f"Congrats! You have won! You had a {player[0].label}")
        return

    print(f"Sorry, you have lost... Your opponent had a {result[0].label} and you only had a {player[0].label}")
    return


    

def main():
    pass

if __name__ == "__main__":
    main()