import unittest
from find_longest_sub_array_by_sum import find_longest_sub_array_by_sum

class FindLongestSubArrayBySumTest(unittest.TestCase):
    def test_find_longest_sub_array(self):
        result = find_longest_sub_array_by_sum([1, 2, 3, 7, 5], 12)
        self.assertEqual([2, 3, 7], result)

    def test_another_case(self):
        result = find_longest_sub_array_by_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15)
        self.assertEqual([1, 2, 3, 4, 5], result)

    def test_with_trailing_zeros(self):
        result = find_longest_sub_array_by_sum([1, 2, 3, 0, 0, 7, 0, 5], 12)
        self.assertEqual([2, 3, 0, 0, 7, 0], result)