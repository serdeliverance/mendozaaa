import unittest
from is_permutation import is_permutation

class IsPermutationTest(unittest.TestCase):

    def test_is_permutation(self):
        result = is_permutation("12jitu23", "31tjui22")
        self.assertEqual(True, result)

    def test_not_permutation(self):
        result = is_permutation("casa", "lolo")
        self.assertEqual(False, result)

    def test_different_lengths(self):
        result = is_permutation("asd", "bbbfeef")
        self.assertEqual(False, result)