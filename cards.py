from enum import IntEnum
import random

class Suit(IntEnum):
    SPADE=0
    CLUB=1
    HEART=2
    DIAMOND=3

class Rank(IntEnum):
    ACE=14
    KING=13
    QUEEN=12
    JACK=11
    TEN=10
    NINE=9
    EIGHT=8
    SEVEN=7
    SIX=6
    FIVE=5
    FOUR=4
    THREE=3
    TWO=2



class Card:

    suit : Suit
    rank : Rank

    @staticmethod
    def random_rank():
        return random.choice(list(Rank))

    @staticmethod
    def random_suit():
        return random.choice(list(Suit))

    @staticmethod
    def sort(cards: list[Card]):
        return sorted(cards, reverse=True)
    
    def __init__(self, rank=None, suit=None):
        if rank:
            self.rank = rank
        else:
            self.rank = Card.random_rank()

        if suit:
            self.suit = suit
        else:
            self.suit = Card.random_suit()


    def __str__(self):
        return f"{self.rank.name}  {self.suit.name}"

    def __eq__(self, other: Card):
        return self.rank.value == other.rank.value and self.suit == other.suit

    def __lt__(self, other: Card):
        return self.rank.value < other.rank.value

    def __gt__(self, other: Card):
        return self.rank.value > other.rank.value

    def __hash__(self):
        return hash((self.rank, self.suit))

    
class Deck:

    def __init__(self, shuffle=True, exclude: list[Card] = [] ):
        self.cards = []

        for rank in Rank:
            for suit in Suit:

                card = Card(rank, suit)

                if card not in exclude:
                    self.cards.append(card)

        if shuffle:
            self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, n):
        try:
            dealt = random.sample(self.cards, n)

        except ValueError:
            dealt = random.sample(self.cards, len(self.cards))

        for c in dealt:
            self.cards.remove(c)

        return dealt

    def __len__(self):
        return len(self.cards)


class Player:
    def __init__(self, hand):
        self.hand : list[Card] = hand

    def __str__(self):
        str = ""

        for c in self.hand:
            str += f"{c} "

        return str

class Table:

    def __init__(self, playerHand=None):

        self.board : list[Card] = []
        self.opponents : list[Player] = []

        if playerHand:

            if len(set(playerHand)) != 2:
                raise TypeError

            for card in playerHand:
                if not isinstance(card, Card):
                    raise TypeError

            self.player = Player(playerHand)
            deck = Deck(exclude=playerHand)

        else:
            deck = Deck()
            self.player = Player(deck.deal(2))

    def known_cards(self):

        cards = self.player.hand + list(self.board)

        for player in self.opponents:
            for card in player.hand:
                cards.append(card)

        return cards

    def remaining(self):
        return Deck(exclude=self.known_cards())

    def show(self):
        print(f"\tTable\n" )

        print(f"\tPlayer: {self.player}\n")

        print(f"\tBoard:  {self.board}\n")

        for i, hand in enumerate(self.opponents, 1):
            print(f"\tOpponent #{i}: {hand}")

        if not self.opponents:
            print(f"\tNo Opponents")

        print(f"Unseen cards: {len(self.remaining())}")

        
        
       
def main():

    table = Table()

    table.show()

    for c in table.known_cards():
        print(c)

if __name__ == "__main__":
    main()
        