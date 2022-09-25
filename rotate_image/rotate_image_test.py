import unittest
from rotate_image import rotate_image


class RotateImageTest(unittest.TestCase):

    def test_3_x_3_matrix(self):
        result = rotate_image([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual([[7, 4, 1], [8, 5, 2], [9, 6, 3]], result)

    def test_4_x_4_matrix(self):
        result = rotate_image([[1, 2, 3, 4], [5, 6, 7, 8], [
                              9, 10, 11, 12], [13, 14, 15, 16]])
        self.assertEqual([[13, 9, 5, 1], [14, 10, 6, 2], [
                         15, 11, 7, 3], [16, 12, 8, 4]], result)
