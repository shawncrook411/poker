import random
from itertools import combinations
from math import comb

from cards import *
from odds import *
import itertools


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


        if int(val) in [1,2,3,4,0]:
            return int(val)

        print("Invalid option selected, please try again")

