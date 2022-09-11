import unittest
from partition_equal_subset_sum import partition_equal_subset_sum

class PartitionEqualSubsetSum(unittest.TestCase):

    def test(self):
        result = partition_equal_subset_sum([1, 5, 11, 5])
        self.assertEqual(True, result)

    def another_test(self):
        result = partition_equal_subset_sum([1, 2, 3, 5])
        self.assertEqual(False, result)