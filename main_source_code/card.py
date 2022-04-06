class Card:
    """ A card object with a suit and rank."""

    # RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
    RANKS = (2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2)

    SUITS = ('Spades', 'Hearts', 'Diamonds', 'Clubs')

    BACK_NAME = 'img/cards/1b.gif'

    def __init__(self, rank, suit):
        """Creates a card with the given rank and suit."""
        self.rank = rank
        self.suit = suit
        self._filename = 'img/cards/' + str(rank) + suit[0].lower() + '.gif'

    def getFilename(self):
        """Returns the card's image filename if it is face up or the backside filename if it is face down."""
        return self._filename

    def get_shortcut(self):
        """Returns the string representation of a card in Shortcuts."""
        if self.rank == 10:
            rank = 'T'
        elif self.rank == 11:
            rank = 'J'
        elif self.rank == 12:
            rank = 'Q'
        elif self.rank == 13:
            rank = 'K'
        elif self.rank == 14:
            rank = 'A'
        elif self.rank == 0:
            rank = 0
            suit = 's'
        else:
            rank = self.rank

        if self.suit == 'Spades':
            suit = 's'
        elif self.suit == 'Hearts':
            suit = 'h'
        elif self.suit == 'Diamonds':
            suit = 'd'
        elif self.suit == 'Clubs':
            suit = 'c'

        return str(rank) + str(suit)

    def __str__(self):
        """Returns the string representation of a card."""
        if self.rank == 14:
            rank = 'Ace'
        elif self.rank == 11:
            rank = 'Jack'
        elif self.rank == 12:
            rank = 'Queen'
        elif self.rank == 13:
            rank = 'King'
        else:
            rank = self.rank
        return str(rank) + ' of ' + self.suit