import random
from itertools import combinations
from math import comb

from cards import *
from odds import *
import itertools


def get_cards(num=1, taken=[]):
    suit = None
    rank = None

    cards = []
    print(f"Please input rank and suit information")

    if num > 1:
        print("\tYou may type multiple cards on a line at at time, seperated by spaces")

    print()
    print("For the rank, just type the number")
    print("\tFor royals, please use either 11/12/13/14 OR J/Q/K/A")
    print()
    print("You may also use S/C/H/D for the suit or the full name, or the following values")
    print("\t1. Spade\t2. Club\t3. Heart\t4. Diamond")
    print()
    print("Example: Ah - Ace of Hearts, 8D - Eight of Diamonds, 121 - Queen of Spades")

    while len(cards) < num:

        values = input(f"Card: ").upper().split()

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
                        continue

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
                    continue

            card = Card(rank=rank, suit=suit)

            if card in cards or card in taken:
                print("Duplicated card inputted, please try again")
                continue

            cards.append(card)
            print(f'Card added: {card}')

            if len(cards) >= num:
                return cards

    return cards
            
def get_hand(num=2):

    while True:
        print("Is this a random hand, or would you like to input one?")
        print("\t1. Random")
        print("\t2. Input")
        val = int(input("Option: "))

        if val in [1,2]:
            break

        print("Invalid option selected, please try again")

    if val == 1:
        deck = Deck()
        return deck.deal(num)

    if val == 2:
        print(f"\n\n\nPlease type the player hand")
        return get_cards(num=num)

    

def get_board(taken=[]):

    print("Would you like to calculate this from Pre-Flop, Flop, Turn, or after the River?")
    print("\t1. Pre-Flop [0 cards dealt, 5 remaining]")
    print("\t2. Flop     [3 cards dealt, 2 remaining]")
    print("\t3. Turn     [4 cards dealt, 1 remaining]")
    print("\t4. River    [All 5 cards dealt]")

    while True:

        try:
            val = int(input("Option: "))
        except ValueError:
            print('Invalid input, please try again')
            continue

        if val in [1,2,3,4]:
            break

        print("Invalid option selected, please try again")



    if val == 1:
        return []

    print("Please input the community cards")

    return get_cards(num= val+1, taken=taken)



def print_menu():

    while True:
        print("Menu\n")
        print("\t1. Get odds of making a certain combination")
        print("\t2. Get odds of beating another hand")
        print("\t3. Outs calculator")
        print("\t4. Run simulated game")
        print("\t0. Quit")
        val = input("Option: ")


        if int(val) in [1,2,3,4,0]:
            return int(val)

        print("Invalid option selected, please try again")

