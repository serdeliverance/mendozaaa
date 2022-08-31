import unittest
from num_ways import num_ways

class NumWaysTest(unittest.TestCase):

    def test_basic_scenario(self):
        result = num_ways(2)
        self.assertEquals(2, result)

    def test_complex_scenario(self):
        result = num_ways(4)
        self.assertEquals(5, result)