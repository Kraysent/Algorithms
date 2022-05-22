import unittest

from binary_search.main import binary_search


class ProgramTests(unittest.TestCase):
    def test_run(self):
        a = [1, 2, 3, 4, 5, 7, 10, 35]
        value = 3

        expected = 2
        actual = binary_search(a, value)

        self.assertEqual(expected, actual)

    def test_no_value_present(self):
        a = [1, 2, 3, 4, 5, 6, 7]
        value = 10

        expected = -1
        actual = binary_search(a, value)

        self.assertEqual(expected, actual)

    def test_empty_array(self):
        a = []
        value = 6

        expected = -1
        actual = binary_search(a, value)

        self.assertEqual(expected, actual)

    def test_first_value(self):
        a = [6, 10, 32, 54]
        value = 6

        expected = 0
        actual = binary_search(a, value)

        self.assertEqual(expected, actual)

    def test_last_value(self):
        a = [30, 40, 50]
        value = 50

        expected = 2
        actual = binary_search(a, value)

        self.assertEqual(expected, actual)
