import unittest
import blackjack


class TestBlackjack(unittest.TestCase):
    def test_get_card(self):
        self.assertTrue(1 <= blackjack.get_card() <= 13)

    def test_score_01(self):
        self.assertEqual(blackjack.score([3, 12]), (13, 0))

    def test_score_02(self):
        self.assertEqual(blackjack.score([5, 5, 10]), (20, 0))

    def test_score_03(self):
        self.assertEqual(blackjack.score([11, 10, 1]), (21, 0))

    def test_score_04(self):
        self.assertEqual(blackjack.score([1, 5]), (16, 1))

    def test_score_05(self):
        self.assertEqual(blackjack.score([1, 1, 5]), (17, 1))

    def test_score_06(self):
        self.assertEqual(blackjack.score([1, 1, 1, 7]), (20, 1))

    def test_score_07(self):
        self.assertEqual(blackjack.score([7, 8, 10]), (25, 0))


unittest.main()
