'''
Step 2: Unit Testing
Create a new program, test_compute_stats2.py, that contains the unit tests for the
compute_stats function described above. This code should use the unittest module as
described in lecture, import the compute_stats2 module, and make calls to the
compute_stats2.compute_stats function to test it. The core functionality should be tested with
a list containing an even number of elements and an odd number. Corner cases such as an
empty list (should return None for all the values) and a list with a single element should also be
tested.
'''

import unittest
import compute_stats2


class TestStats(unittest.TestCase):
    def test_even(self):
        self.assertEqual(compute_stats2.compute_stats([2, 4, 6, 18]), (2, 18, 7.5, 5))

    def test_odd(self):
        self.assertEqual(compute_stats2.compute_stats([2, 4, 6]), (2, 6, 4.0, 4))

    def test_non(self):
        self.assertEqual(compute_stats2.compute_stats([]), None)

    def test_one(self):
        self.assertEqual(compute_stats2.compute_stats([1]), (1, 1, 1, 1))

if __name__ == '__main__':
    unittest.main()
