import unittest
from copy import deepcopy
from src.cards_game import *

class CardsGameTestCase(unittest.TestCase):
    def test_deck_getter(self):
        deck = Deck()
        king = Card('K', 'clubs')
        self.assertEqual(king, deck['K', 'clubs'])

    def test_deck_shuffles(self):
        deck = Deck()
        shuffled_deck = deepcopy(deck)
        shuffled_deck.shuffle()
        self.assertNotEqual(deck.cards, shuffled_deck.cards, "Baralhos diferentes não devem ser afetados pelo shuffle")

    def test_deck_draws_until_run_out(self):
        deck = Deck()
        self.assertEqual(52, len(deck), "O baralho completo deve conter 52 cartas")

        deck.draw_cards(6)
        self.assertEqual(46, len(deck), "Deveria restar 46 cartas no baralho")

        deck.draw_cards(46)
        self.assertEqual(0, len(deck), "Deveria restar 0 cartas no baralho")

        self.assertRaises(IndexError, deck.draw_cards, 1)
        self.assertEqual(0, len(deck))

    def test_card_str(self):
        self.assertEqual('🂡', str(Card('A', 'spades')))
        self.assertEqual('🂱', str(Card('A', 'hearts')))

    def test_card_repr(self):
        self.assertEqual('A of diamonds', repr(Card('A', 'diamonds')))
        self.assertEqual('A of clubs', repr(Card('A', 'clubs')))
