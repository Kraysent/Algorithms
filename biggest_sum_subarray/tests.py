import unittest

from biggest_sum_subarray.main import biggest_sum_subarray


class ProgramTests(unittest.TestCase):
    def test_run(self):
        a = [-1, 2, 6, -2, 0, 4, 7, 9, -11]

        expected = 26
        actual = biggest_sum_subarray(a)

        self.assertEqual(expected, actual)

    def test_empty(self):
        a = []

        expected = 0
        actual = biggest_sum_subarray(a)

        self.assertEqual(expected, actual)

    def test_negatives(self):
        a = [-1, -2, -1, -5, -6, -11, -5]

        expected = 0
        actual = biggest_sum_subarray(a)

        self.assertEqual(expected, actual)

    def test_positives(self):
        a = [1, 3, 5, 7, 4, 2, 11]

        expected = 33
        actual = biggest_sum_subarray(a)

        self.assertEqual(expected, actual)

    def test_zeros(self):
        a = [0, 0, 0, 0, 0, 0]

        expected = 0
        actual = biggest_sum_subarray(a)

        self.assertEqual(expected, actual)
