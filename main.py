import time
import argparse

from itertools import combinations
from math import comb

from cards import *
from odds import *
from util import *

import itertools

def main():

    print("\n\n\tWelcome to the Command Line Poker odds calculator\n")
    
    while True:    
        try: 
            Table.clear()

            match int(print_menu()):
                case 1:
                    odds_make_combo()
                case 2:
                    odds_beat_other()
                case 3:
                    outs_calculator()
                case 4:
                    run_game()
                case 5:
                    display_random()
                case 0:
                    break
                case _:
                    print("Invalid option selected, please try again")


        except (KeyboardInterrupt, EOFError):
            break

        except ValueError:
            print("Something went wrong, please try again")
            continue

        time.sleep(5)
        print('\n\n')

    print("Thank you! Have a good day :)")
    return

if __name__ == "__main__":
    main()