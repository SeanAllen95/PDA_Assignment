import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("Spades", 1)
        self.card2 = Card("Hearts", 2)
        self.game = CardGame("Simple Card Game")

        self.cards = (self.card1, self.card2)

    def test_check_for_ace(self):
        self.assertEqual(1, self.card1.value)
    
    def test_highest_card(self):
        result = self.game.highest_card(self.card1, self.card2)
        self.assertEqual(self.card2, result)

    def test_cards_total(self):
        result = self.game.cards_total(self.cards)
        self.assertEqual('You have a total of 3', result)