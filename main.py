import sys
import argparse

from itertools import combinations
from math import comb

from cards import *
from odds import *
from util import *

import itertools


def main():

    # parser = argparse.ArgumentParser(description="")
    # parser.add_argument("")

    print("\n\n\tWelcome to the Command Line Poker odds calculator\n")
    
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