import unittest

from bubble_sort.main import bubble_sort


class ProgramTests(unittest.TestCase):
    def test_run(self):
        a = [2, 5, 3, 1]

        expected = [1, 2, 3, 5]
        actual = bubble_sort(a)

        self.assertEqual(expected, actual)

    def test_empty(self):
        a = []

        expected = []
        actual = bubble_sort(a)

        self.assertEqual(expected, actual)

    def test_sorted(self):
        a = [1, 2, 3, 7, 10]

        expected = [1, 2, 3, 7, 10]
        actual = bubble_sort(a)

        self.assertEqual(expected, actual)

    def test_uniform(self):
        a = [5, 5, 5, 5, 5, 5, 5]

        expected = [5, 5, 5, 5, 5, 5, 5]
        actual = bubble_sort(a)

        self.assertEqual(expected, actual)
