from enum import Enum
from itertools import combinations

from cards import *

class HandType(Enum):
    STRAIGHT_FLUSH=8
    FOUR_KIND=7
    FULL_HOUSE=6
    FLUSH=5
    STRAIGHT=4
    THREE_KIND=3
    TWO_PAIR=2
    PAIR=1
    HIGH=0

    def __eq__(self, other: HandType):
        return self.value == other.value

    def __lt__(self, other: HandType):
        return self.value < other.value

    def __gt__(self, other: HandType):
        return self.value > other.value


def is_straight(cards : list[Card]):
    cards = Card.sort(cards)

    for i, card in enumerate(cards):
        if i < len(cards) - 1:
            next = cards[i + 1]

            # Special Edge Case : Ace, 2, 3, 4, 5
            if i == 0 and card.rank.value == 14 and next.rank.value == 5:
                continue

            if card.rank.value != next.rank.value + 1:
                return False

    return True

def is_flush(cards: list[Card]):

    suit = cards[0].suit

    for curr in cards:
        if curr.suit != suit:
            return False

    return True

def get_groups(cards: list[Card]):
    cards = Card.sort(cards)

    counts = {}

    for c in cards:
        counts[c.rank.value] = counts.get(c.rank.value, 0) + 1

    groups = sorted(counts.items(), key=lambda x: (x[1], x[0]), reverse=True)
    ranks = [rank for rank, kind in groups]
    kinds = [kind for rank, kind in groups]

    return (ranks, kinds)



def is_four_kind(kinds: list[int]):
    return kinds == [4, 1]

def is_full_house(kinds: list[int]):
    return kinds == [3, 2]

def is_three_kind(kinds: list[int]):
    return kinds == [3, 1, 1]

def is_two_pair(kinds: list[int]):
    return kinds == [2, 2, 1]

def is_pair(kinds: list[int]):
    return kinds == [2, 1, 1, 1]


def evaluate(cards: list[Card]):
    values: list[Card] = sorted(cards, reverse=True)

    high: Card = values[0]

    ranks: list[Rank.value]
    kinds: list[int] 
    ranks, kinds = get_groups(cards)

    if is_straight(cards) and is_flush:
        return (HandType.STRAIGHT_FLUSH, [high])

    if is_four_kind(kinds):
        return (HandType.FOUR_KIND, ranks)

    if is_full_house(kinds):
        return (HandType.FULL_HOUSE, ranks)

    if is_flush(cards):
        return (HandType.FLUSH, ranks)

    if is_straight(cards):
        if high.rank == Rank.ACE and cards[1].rank == 5:
            return (HandType.STRAIGHT, [cards[1]])
        return (HandType.STRAIGHT, [high])

    if is_three_kind(kinds):
        return (HandType.THREE_KIND, ranks)

    if is_two_pair(kinds):
        return (HandType.TWO_PAIR, ranks)

    if is_pair(kinds):
        return (HandType.PAIR, ranks)

    return (HandType.HIGH, ranks)

def best_hand(cards):
    best = None

    for five in combinations(cards, 5):
        score = evaluate(five)

        if best is None or score > best:
            best = score

    return best



def main():


    deck = Deck()
    cards = Card.sort(deck.deal(52))

    eval = best_hand(cards)

    print(eval)



    



if __name__ == "__main__":
    main()
