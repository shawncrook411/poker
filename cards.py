
from enum import IntEnum
import random
from functools import wraps

class Suit(IntEnum):
    SPADE=0
    CLUB=1
    HEART=2
    DIAMOND=3

    def __str__(self):
        return {
            Suit.SPADE: "♠",
            Suit.CLUB: "♣",
            Suit.HEART: "♥",
            Suit.DIAMOND: "♦",
        }[self]


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

    def __str__(self):
        if self < 10:
            return str(int(self))
        
        return {
            Rank.ACE: "A",
            Rank.KING: "K",
            Rank.QUEEN: "Q",
            Rank.JACK: "J",
            Rank.TEN: "T"
        }[self]

class Card:

    suit : Suit
    rank : Rank

    @staticmethod
    def sort(cards: list[Card]):
        return sorted(cards, reverse=True)
    
    def __init__(self, rank=None, suit=None):
        if rank is not None and suit is not None:
            self.rank = rank
            self.suit = suit
        else:
            self.rank = random.choice(list(Rank))
            self.suit = random.choice(list(Suit))
            
    def __str__(self):
        color = "31" if self.suit in (Suit.HEART, Suit.DIAMOND) else "30"   # red / black text
        return f"\033[{color};107m {str(self.rank):>2}{self.suit} \033[0m"

    def __eq__(self, other: Card):
        return self.rank.value == other.rank.value and self.suit == other.suit

    def __lt__(self, other: Card):
        return self.rank.value < other.rank.value

    def __gt__(self, other: Card):
        return self.rank.value > other.rank.value

    def __hash__(self):
        return hash((self.rank, self.suit))
   
class Deck:

    def __init__(self, shuffle=True, exclude=None):
        exclude = set(exclude or [])

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

    def __contains__(self, item):
        return item in self.cards

class Player:
    def __init__(self, hand=None):
        self.hand : list[Card] = hand or []

    def __str__(self):
        str = ""

        for c in self.hand:
            str += f"{c} "

        return str

class Table:

    board : list[Card] = []
    player : Player = None
    opponents : list[Player] = []
    deck : Deck = None
    burned : list[Card] = []

    @staticmethod
    def add_player_hand(hand):

        if len(set(hand)) != 2:
            raise TypeError

        for card in hand:
            if not isinstance(card, Card):
                raise TypeError

        Table.player = Player(hand)
        Table.claim(hand)


    @staticmethod
    def community(current : Player = None):

        if not current:
            return Table.player.hand + Table.board

        return current.hand + Table.board

    @staticmethod
    def add_opponents(opponents : list[Player]):

        Table.opponents = []

        for player in opponents:

            if len(set(player.hand)) != 2:
                raise TypeError
            
            for card in player.hand:
                if not isinstance(card, Card):
                    raise TypeError

            Table.opponents.append(player)

            Table.claim(player.hand)

    @staticmethod
    def set_board(board):

        if len(set(board)) > 5:
            raise TypeError

        if not isinstance(board, list):
            raise TypeError
        
        for card in board:
            if not isinstance(card, Card):
                raise TypeError

        Table.board = list(set(board)) # Removes duplicates by mistake
        Table.claim(board)

    
    @staticmethod
    def board_cards():
        return Table.board

    @staticmethod
    def known_cards():

        cards = Table.player.hand + Table.board + Table.burned

        for player in Table.opponents:
            for card in player.hand:
                cards.append(card)

        return cards
            
    @staticmethod
    def remaining():
        return Table.deck

    @staticmethod
    def deal(n=2):
        return Table.deck.deal(n)

    @staticmethod
    def claim(cards: list[Card]):
        for c in cards:
            if c in Table.deck:
                Table.deck.cards.remove(c)


    @staticmethod
    def show():
        print(f"\tTable\n" )

        print(f"\tPlayer: {Table.player}\n")

        str = "\tBoard:"
        for card in Table.board:
            str += f"{card} "
        print(str + '\n')

        for i, player in enumerate(Table.opponents, 1):
            print(f"\tOpponent #{i}: {player}")

        if not Table.opponents:
            print(f"\tNo Opponents")

        print(f"\tUnseen cards: {len(Table.remaining())}")

    @staticmethod
    def random():

        Table.deck = Deck()

        Table.add_player_hand(
            Table.deal()
        )

        Table.set_board(
            Table.deal(5)
        )

        Table.add_opponents([Player(Table.deal()) for _ in range(5)])

    @staticmethod
    def clear():

        Table.player = Player()
        Table.board = []
        Table.opponents = []
        Table.deck = Deck()


        
    
def main():
    pass

if __name__ == "__main__":
    main()
        