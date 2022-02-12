import unittest
import blackjack


class TestBlackjack(unittest.TestCase):
    """[ 3, 12 ] → (13, 0)
    [ 5, 5, 10 ] → (20, 0)
    [ 11, 10, 1 ] → (21, 0)
    [ 1, 5 ] → (16, 1)
    [ 1, 1, 5 ] → (17, 1)
    [ 1, 1, 1, 7 ] → (20, 1)
    [ 7, 8, 10 ] → (25, 0)"""

    def test_get_card(self):
        self.assertTrue(1 <= blackjack.get_card() <= 13)

    def test_score_01(self):
        self.assertEqual(blackjack.score([3, 12]) == (13, 0))


unittest.main()
