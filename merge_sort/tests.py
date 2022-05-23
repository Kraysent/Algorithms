import unittest

from merge_sort.main import merge_sort


class ProgramTests(unittest.TestCase):
    def test_run(self):
        a = [2, 5, 3, 1]

        expected = [1, 2, 3, 5]
        actual = merge_sort(a)

        self.assertEqual(expected, actual)

    def test_empty(self):
        a = []

        expected = []
        actual = merge_sort(a)

        self.assertEqual(expected, actual)

    def test_sorted(self):
        a = [1, 2, 3, 7, 10]

        expected = [1, 2, 3, 7, 10]
        actual = merge_sort(a)

        self.assertEqual(expected, actual)

    def test_uniform(self):
        a = [5, 5, 5, 5, 5, 5, 5]

        expected = [5, 5, 5, 5, 5, 5, 5]
        actual = merge_sort(a)

        self.assertEqual(expected, actual)
