import unittest

from fibonacci_sequence.main import get_fibonacci_number


class ProgramTests(unittest.TestCase):
    def test_run_low(self):
        index = 5

        expected = 3
        actual = get_fibonacci_number(index)

        self.assertEqual(expected, actual)

    def test_run_high(self):
        index = 50

        expected = 20365011074

    def test_zero(self):
        index = 0

        expected = 0
        actual = get_fibonacci_number(index)

        self.assertEqual(expected, actual)

    def test_one(self):
        index = 1

        expected = 1
        actual = get_fibonacci_number(index)

        self.assertEqual(expected, actual)
