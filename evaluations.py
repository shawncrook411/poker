from enum import Enum

import cards

class HandType(Enum):
    STRAIGHT_FLUSH=8
    FOUR_KIND=7
    FULL_HOUSE=6
    FLUSH=6
    STRAIGHT=5
    THREE_KIND=4
    TWO_PAIR=3
    PAIR=2
    HIGH=1


def evaluate(cards):
    values = sorted(cards, reverse=True)

    print(values)



def main():
    pass



if __name__ == "__main__":
    main()
