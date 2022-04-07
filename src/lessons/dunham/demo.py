import surfshop
import unittest
class TestSurfers(unittest.TestCase):
    def __init__(self): self.cart=surfshop.ShoppingCart() def test_add_surfboards1(self): self.assertEqual(self.cart.add_surfboards(1), 'Successfully added 1 surfboard to cart!') def test_add_surfboards2(self): self.assertEqual(self.cart.add_surfboards(2), 'Successfully added 2 surfboards to cart!') def test_add_too_many(self): with self.assertRaises(self.cart.TooManyBoardsError): self.cart.add_surfboards(5) def test_add_check_truth(self): self.assertTrue(self.cart.apply_locals_discount()) unittest.main()