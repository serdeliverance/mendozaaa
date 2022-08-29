import unittest
from pascal import pascal

class PascalTest(unittest.TestCase):

    # The following tests are testing the "get_roman_numeral()" method
    def test_first_row(self):
        result = pascal(1, 0)
        self.assertEqual(1, result)

    def test_second_row(self):
        result = pascal(2, 0)
        self.assertEqual(1, result)

    def test_second_row_intermediate_element(self):
        result = pascal(2, 1)
        self.assertEqual(1, result)
    
    def test_n_level_element(self):
        result = pascal(5, 2)
        self.assertEqual(6, result)
