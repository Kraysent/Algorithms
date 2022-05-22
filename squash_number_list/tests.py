import unittest

from squash_number_list.main import squash_number_list


class ProgramTests(unittest.TestCase):
    def test_run(self):
        a = [1, 2, 3, 5, 6, 9, 11, 12, 13]

        expected = "1-3,5-6,9,11-13"
        actual = squash_number_list(a)

        self.assertEqual(expected, actual)

    def test_no_squash(self):
        a = [1, 3, 6, 8, 11, 21, 35]

        expected = "1,3,6,8,11,21,35"
        actual = squash_number_list(a)

        self.assertEqual(expected, actual)

    def test_empty_list(self):
        a = []

        expected = ""
        actual = squash_number_list(a)

        self.assertEqual(expected, actual)

    def test_no_last_squash(self):
        a = [1, 2, 4, 5, 7, 11, 32, 33, 34, 45]

        expected = "1-2,4-5,7,11,32-34,45"
        actual = squash_number_list(a)

        self.assertEqual(expected, actual)

    def test_squash_all(self):
        a = [5, 6, 7, 8, 9, 10, 11, 12]

        expected = "5-12"
        actual = squash_number_list(a)

        self.assertEqual(expected, actual)
