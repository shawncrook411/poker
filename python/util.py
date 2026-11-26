import random
from itertools import combinations
from math import comb

from cards import *
from odds import *
import itertools


def print_input_info():
    print('\n')
    print('\t\t***** MANUALLY INPUT CARDS HERE *******\n')
    print("\tYou must type multiple cards on a line at at time, seperated by spaces")
    
    print()
    print("\tFor the rank, just type the number")
    print("\tFor royals, please use either 11/12/13/14 OR J/Q/K/A")
    print()
    print("\tYou may also use S/C/H/D for the suit or the full name, or the following values")
    print("\t1: Spade - 2: Club - 3: Heart - 4: Diamond")
    print()
    print("\tExample: Ah - Ace of Hearts, 8D - Eight of Diamonds, 121 - Queen of Spades")
    print("\tExample: Ah Kh Qh")
    print()


def get_cards(playerHand=False, board=False, opponents=False):
    suit = None
    rank = None

    cards = []

    assert playerHand or board or opponents

    print("********     ", end='')
    if playerHand:
        print("INPUT PLAYER HAND: You may leave blank for a random hand, MAX = 2", end='\t')

    if board:
        print("INPUT COMMUNITY BOARD: You may leave blank for an empty board\n Or type how many cards have been revealed, MAX = 5", end='')

    if opponents:
        print("INPUT OPPONENTS: You may leave blank to randomize 5 opponents\n Or you may type one opponents hand, MAX = 2", end='')
    
    print("     ********\n")

    while True:
        values = input(f"Input: ").upper().strip()

        try : 
            if playerHand and values == "":
                print("Randomizing player hand")
                cards = Table.deal(2)
                str = "Player Hand: " 
                for card in cards:
                    str += f"{card} "
                print(str + '\n')
                return cards

            if board and values == "":
                print("Community board is set to empty\n")
                return []

            try:
                num = int(values)

                if board and num in range(6):
                    print(f"Randomizing {num} community cards")

                    dealt = Table.deal(num)
                    str = "Board: " 
                    for card in dealt:
                        str += f"{card} "
                    print(str + '\n')
                    return dealt
                
            except ValueError, TypeError:
                pass

            if opponents and values == "":
                print(f"Randomizing 5 opponent hands")

                opps = []

                for i in range(5):
                    cards = Table.deal(2)
                    str = f"Opponent #{i+1} :"
                    for card in cards:
                        str += f"{card} "
                    print(str)

                    opps.append(Player(cards))

                return opps

            values = values.split(' ')

            for val in values:
                match val[:-1]:
                    case "1" | "A" | "14":
                        rank = Rank.ACE

                    case "J" | "11":
                        rank = Rank.JACK

                    case "Q" | "12":
                        rank = Rank.QUEEN

                    case "K" | "13":
                        rank = Rank.KING

                    case _:
                        try:
                            rank = Rank(int(val[:-1]))

                        except ValueError, KeyError:
                            print("Invalid rank inputted, please try again")
                            raise ValueError

                match val[-1]:
                    case "1" | "S":
                        suit = Suit.SPADE

                    case "2" | "C":
                        suit = Suit.CLUB

                    case "3" | "H":
                        suit = Suit.HEART

                    case "4" | "D":
                        suit = Suit.DIAMOND

                    case _:
                        print("Invalid suit inputted, please try again")
                        raise ValueError

                card = Card(rank=rank, suit=suit)

                if card in cards or card in Table.known_cards():
                    print("Duplicated card inputted, please try again")
                    raise ValueError

                cards.append(card)
                print(f'Card added: {card}')

            print('\n')
            if playerHand:
                return cards[:2]

            if board:
                return cards[:5]

            if opponents:
                return [Player(cards[:2])]
            
            return cards[:5] # Will only return first 5
        
        except ValueError:
            continue

def print_menu():

    print("Menu\n")
    print("\t1. Get odds of making a certain combination")
    print("\t2. Get odds of beating another hand")
    print("\t3. Outs calculator")
    print("\t4. Run simulated game")
    print("\t5. Show random board")
    print("\t0. Quit")
    print()
     
    val = int(input("Option: ")[0])

    if val in [1,2,3,4]:
        print_input_info()

    return val

def display_random():
    Table.random()
    Table.show()
    pass
