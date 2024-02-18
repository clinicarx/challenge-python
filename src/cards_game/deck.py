import collections


class Card(collections.namedtuple('Card', ['rank', 'suit'])):
    def __str__(self):
        """
        Retorna o simbolo unicode da respectiva carta
        https://en.wikipedia.org/wiki/Playing_Cards_(Unicode_block)
        https://www.unicode.org/charts/PDF/U1F0A0.pdf
        """
        suits = dict(spades=0, diamonds=2, clubs=3, hearts=1)
        ranks = Deck.ranks.copy()
        ranks.insert(-3, 'C')
        return chr(0x1F0A1 + (0x10 * suits[self.suit]) + ((0x1 + ranks.index(self.rank)) % 0xE))

    def __repr__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    suits = 'spades diamonds clubs hearts'.split()
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')

    def __init__(self):
        self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, position):
        rank, suit = position
        return next(card for card in self.cards
                    if card.rank == rank and card.suit == suit)

    def __deepcopy__(self, memo):
        deck = Deck()
        deck.cards = self.cards
        return deck

    def shuffle(self):
        pass

    def draw_cards(self, count):
        pass
