import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card1 = Card("Clubs", 8)
        self.card2 = Card("Diamonds", 2)
        self.card_game = CardGame()

    def test_check_for_ace(self):
        self.check_for_ace = self.card_game.check_for_ace(self.card1)
        self.assertEqual(False, self.check_for_ace)

    def test_get_highest_card(self):
        self.highest_card = self.card_game.highest_card(self.card1, self.card2)
        self.assertEqual(self.card1, self.highest_card)

    def test_get_cards_total(self):
        self.cards_list = [self.card1, self.card2]
        self.cards_total = self.card_game.cards_total(self.cards_list)
        self.assertEqual("You have a total of 10", self.cards_total)