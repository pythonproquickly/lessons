import unittest
import autompgNEWESTFINALDRAFT2

# Test case for Part 1 the class AutoMPG:
class TestAutoMPG(unittest.TestCase):
    def test_autompg_create(self):
        # initializes the class for __init__.
        autompg = autompgNEWESTFINALDRAFT2.AutoMPG(make = 'ford', model = 'toyota', year = '1975', mpg = '20.0')
        self.assertEqual(autompg.make, 'ford')
        self.assertEqual(autompg.model, 'toyota')
        self.assertEqual(autompg.year, '1975')
        self.assertEqual(autompg.mpg, '20.0')

    # initializes the class for __str__.
    def test_string_autompg(self):
        autompg = autompgNEWESTFINALDRAFT2.AutoMPG(make = 'ford', model = 'toyota', year = '1975', mpg = '20.0')
        self.assertEqual(str(autompg), f'A vehicle: {autompg.make}, {autompg.model}, {autompg.year}, {autompg.mpg}') # expected when autompg is passed to string function.

    # initializes the class for __repr__.

    def test_repr_autompg(self):
        autompg = autompgNEWESTFINALDRAFT2.AutoMPG(make = 'ford', model = 'toyota', year = '1975', mpg = '20.0')
        self.assertEqual(repr(autompg), f'Vehicle({autompg.make}, {autompg.model}, {autompg.year}, {autompg.mpg})') # expected when autompg is passed to string function.

    # initializes the class for __eq__.
    # Checking equality of autompg1 and autompg2.
    def test_eq_autompg_eq(self):
        autompg1 = autompgNEWESTFINALDRAFT2.AutoMPG(make = 'ford', model = 'toyota', year = '1975', mpg = '20.0')
        autompg2 = autompgNEWESTFINALDRAFT2.AutoMPG(make = 'ford', model = 'toyota', year = '1975', mpg = '20.0')
        self.assertTrue(autompg1 == autompg2)

    # Check when autompg1 and 42 are NOT equal.
    def test_eq_autompg_ne(self):
        autompg1 = autompgNEWESTFINALDRAFT2.AutoMPG(make = 'ford', model = 'toyota', year = '1975', mpg = '20.0')
        self.assertFalse(autompg1 == 42)

    # initializes the class for __lt__.
    def test_lt_autompg(self):
        autompg1 = autompgNEWESTFINALDRAFT2.AutoMPG(make = ' ', model = ' ', year = ' ', mpg = ' ')
        autompg2 = autompgNEWESTFINALDRAFT2.AutoMPG(make = 'ford', model = 'toyota', year = '1975', mpg = '20.0')
        self.assertTrue(autompg1 < autompg2)

    # initializes the class for __hash__.
    def test_hash_autompg(self):
        autompg = autompgNEWESTFINALDRAFT2.AutoMPG(make = 'ford', model = 'toyota', year = '1975', mpg = '20.0')
        self.assertEqual(hash(autompg), hash((autompg.make, autompg.model, autompg.year, autompg.mpg)))

# This is important in what we use to implement the above functionality and confirm that these tests are running successfully.
if __name__ == '__main__':
    unittest.main()

    '''
    # Check when autompg1 and 42 are NOT equal.
    def test_eq_autompg(self):
        autompg1 = autompgNEWESTFINALDRAFT2.AutoMPG(make = 'ford', model = 'toyota', year = '1975', mpg = '20.0')
        #autompg2 = autompgNEWESTFINALDRAFT2.AutoMPG(make = 'chevrolet', model = 'camry', year = '1975', mpg = '20.0')
        self.assertFalse(autompg1, 42)


    # initializes the class for __lt__.
    def test_lt_autompg(self, autompg1):
        autompg1 = autompgNEWESTFINALDRAFT2.AutoMPG(make = 'ford', model = 'toyota', year = '1975', mpg = '20.0')
        autompg2 = autompgNEWESTFINALDRAFT2.AutoMPG(make = 'ford', model = 'toyota', year = '1975', mpg = '20.0')
        self.assertEqual(tuple(autompg1), tuple(autompg2))
    '''
