import random

class Card:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    # how to recreate object
    # called by repr(obj)
    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"

    # human-friendly view of object
    # called by str(obj)
    def __str__(self):
        return f"{self.rank}/{self.suit}"



class CardDeck:  # object
    SUITS = 'Clubs Diamonds Hearts Spades'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __init__(self, dealer_name):
        self.dealer = dealer_name
        self._make_deck()

#   'self' == 'this'

    def _make_deck(self):
        self._cards = list()
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)


    def shuffle(self):
        random.shuffle(self._cards)

    def deal(self):
        return self._cards.pop()

    @property
    def cards(self):
        return self._cards

    @property  # read-only at first
    def dealer(self):  # getter property
        # print("GETTING dealer")
        return self._dealer

    # dealer = property(dealer)

    @dealer.setter  # read/write
    def dealer(self, dealer_name):
        if isinstance(dealer_name, str):
            # print("SETTING dealer")
            self._dealer = dealer_name
        else:
            raise TypeError("Dealer must be a string")
    # dealer = dealer.setter(dealer)


    def get_dealer(self):  # getter method
        return self._dealer

    def set_dealer(self, dealer): # setter
        self._dealer = dealer

    @classmethod
    def get_suits(cls):
        return cls.SUITS


    def __len__(self):
        return len(self.cards)

