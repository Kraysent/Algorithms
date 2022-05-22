import unittest

from to_binary_form.main import to_binary_form


class ProgramTests(unittest.TestCase):
    def test_run(self):
        number = 34

        expected = [1, 0, 0, 0, 1, 0]
        actual = to_binary_form(number)

        self.assertEqual(expected, actual)

    def test_zero(self):
        number = 0

        expected = [0]
        actual = to_binary_form(number)

        self.assertEqual(expected, actual)

    def test_all_ones(self):
        number = 127

        expected = [1, 1, 1, 1, 1, 1, 1]
        actual = to_binary_form(number)

        self.assertEqual(expected, actual)

    def test_power_of_two(self):
        number = 64

        expected = [1, 0, 0, 0, 0, 0, 0]
        actual = to_binary_form(number)

        self.assertEqual(expected, actual)
