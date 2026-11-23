import enum
import random

class Suit(enum):
    SPADE=0, 
    CLUB=1, 
    HEART=2, 
    DIAMOND=3

class Rank(enum):
    ACE=14,
    KING=13,
    QUEEN=12,
    JACK=11,
    TEN=10,
    NINE=9,
    EIGHT=8,
    SEVEN=7,
    SIX=6,
    FIVE=5,
    FOUR=4,
    THREE=3,
    TWO=2



class Card:

    suit : Suit
    rank : Rank

    @staticmethod
    def random_rank():
        pass

    @staticmethod
    def random_suit():
        pass
    
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
        return self.suit + self.rank

    def __eq__(self, other):
        return self.rank == other.rank

    def __hash__(self):
        return hash((self.rank, self.suit))

    
class Deck:

    def __init__(self, exclude=()):
        self.cards = []

        for rank in Rank:
            for suit in Suit:

                card = Card(rank, suit)
                if card not in exclude:
                    self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, n):
        dealt = random.sample(self.cards, n)

        for c in dealt:
            self.cards.remove(c)

        return dealt

    def __len__(self):
        return len(self.cards)




class Table:

    def __init__(self, cards):
        self.player = []
        self.board = []
        self.opponents = []

    def known_cards(self):
        cards = list(self.player) + list(self.board)

        for hand in self.opponents:
            cards += hand

        return cards

    def remaining(self):
        return Deck(exclude=self.known_cards())

    def show(self):
        print(f" Table\n" )

        print(f" Player: {self.player}\n")

        print(f" Board:  {self.board}\n")

        for i, hand in enumerate(self.opponents, 1):
            print(f"Opponent {i}: {hand}")

        if not self.opponents:
            print(f"No Opponents")

        print(f"Unseen cards: {len(self.remaining())}")
        
        
       

        