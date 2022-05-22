import unittest

from array_merge.main import array_merge

class ProgramTests(unittest.TestCase):
    def test_run(self):
        a = [1, 5, 8, 12, 16]
        b = [2, 3, 6, 10, 17, 21]

        expected = [1, 2, 3, 5, 6, 8, 10, 12, 16, 17, 21]
        actual = array_merge(a, b)

        self.assertEqual(expected, actual)

    def test_one_array_empty(self):
        a = []
        b = [1, 2, 3]

        expected = [1, 2, 3]
        actual = array_merge(a, b)

        self.assertEqual(expected, actual)

    def test_both_empty(self):
        a, b = [], []

        expected = []
        actual = array_merge(a, b)

        self.assertEqual(expected, actual)

    def test_equal(self):
        a = [1, 2, 3]
        b = [1, 2, 3]

        expected = [1, 1, 2, 2, 3, 3]
        actual = array_merge(a, b)

        self.assertEqual(expected, actual)
        