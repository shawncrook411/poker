from enum import IntEnum
from itertools import combinations

from cards import *

class HandType(IntEnum):
    STRAIGHT_FLUSH=8
    FOUR_KIND=7
    FULL_HOUSE=6
    FLUSH=5
    STRAIGHT=4
    THREE_KIND=3
    TWO_PAIR=2
    PAIR=1
    HIGH=0

    @property
    def label(self) -> str:
        return HAND_LABELS[self]

HAND_LABELS = {
    HandType.STRAIGHT_FLUSH: "Straight Flush",
    HandType.FOUR_KIND: "Four of a Kind",
    HandType.FULL_HOUSE: "Full House",
    HandType.FLUSH: "Flush",
    HandType.STRAIGHT: "Straight",
    HandType.THREE_KIND: "Three of a Kind",
    HandType.TWO_PAIR: "Two Pair",
    HandType.PAIR: "Pair",
    HandType.HIGH: "High Card",
}    

def get_groups(cards: list[Card]):
    counts = {}

    for card in cards:
        counts[card.rank] = counts.get(card.rank, 0) + 1

    groups = sorted(counts.items(), key=lambda x: (x[1], x[0]), reverse=True)

    ranks = [rank for rank, kind in groups]
    kinds = [kind for rank, kind in groups]

    return (ranks, kinds)

def is_straight_flush(cards: list[Card]):

    suits = {}
    suits.setdefault(0)

    for suit in Suit:
        suited = [card for card in cards if card.suit == suit]
        
        if len(suited) >= 5:
            return is_straight(suited)
    
    return None


def is_straight(cards : list[Card]):

    unique = sorted(set([card.rank.value for card in cards]), reverse=True)

    if unique[0] == 14:
        unique.append(1)

    run = 1

    for i in range(len(unique) - 1):
        if unique[i] == unique[i+1] + 1:

            run += 1

            if run == 5:
                return [unique[i-4]]
            
        else:
            run = 1

    return None

def is_flush(cards: list[Card]):

    suits = {}
    suits.setdefault(0)

    for suit in Suit:
        suited = [card.rank for card in cards if card.suit == suit]
        
        if len(suited) >= 5:
            return sorted(suited, reverse=True)[:5]
    
    return None


def is_four_kind(cards: list[Card]):
    ranks, kinds = get_groups(cards)

    if kinds[0] == 4:
        return [ranks[0], max(ranks[1:])]

    return None

def is_full_house(cards: list[Card]):
    ranks, kinds = get_groups(cards)

    if kinds[0] == 3 and kinds[1] >= 2:
        return [ranks[0], ranks[1]]
    
    return None

def is_three_kind(cards: list[Card]):
    ranks, kinds = get_groups(cards)

    if kinds[0] == 3:
        return ranks[:3]
    
    return None

def is_two_pair(cards: list[Card]):
    ranks, kinds = get_groups(cards)

    if kinds[0] == 2 and kinds[1] == 2:
        return [ranks[0], ranks[1], max(ranks[2:])]

    return None
    

def is_pair(cards: list[Card]):
    ranks, kinds = get_groups(cards)

    if kinds[0] == 2:
        return ranks[:4]

    return None


def evaluate(cards: list[Card]):

    if result := is_straight_flush(cards):
        return (HandType.STRAIGHT_FLUSH, result)
    
    if result := is_four_kind(cards):
        return (HandType.FOUR_KIND, result)
    
    if result := is_full_house(cards):
        return (HandType.FULL_HOUSE, result)
    
    if result := is_flush(cards):
        return (HandType.FLUSH, result)
    
    if result := is_straight(cards):
        return (HandType.STRAIGHT, result)
    
    if result := is_three_kind(cards):
        return (HandType.THREE_KIND, result)
    
    if result := is_two_pair(cards):
        return (HandType.TWO_PAIR, result)
    
    if result := is_pair(cards):
        return (HandType.PAIR, result)

    ranks, kinds = get_groups(cards)

    return (HandType.HIGH, ranks[:5])


def main():

    hand_types = []
    

    while True:
    
        deck = Deck()
        cards = Card.sort(deck.deal(7))

        hand_type, sort = evaluate(cards)

        if hand_type not in hand_types:
            hand_types.append(hand_type)

            print(f"Hand Type: {HandType(hand_type)}")

            for card in cards:
                print(f"Card: {card}")

            print("-----")

        if len(hand_types) >= 9:
            break


if __name__ == "__main__":
    main()
