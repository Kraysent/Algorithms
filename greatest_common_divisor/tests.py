import unittest

from greatest_common_divisor.main import gcd


class ProgramTests(unittest.TestCase):
    def tests(self):
        self.assertEqual(gcd(1, 1), 1)
        self.assertEqual(gcd(9, 3), 3)
        self.assertEqual(gcd(11, 5), 1)
        self.assertEqual(gcd(100, 50), 50)
        self.assertEqual(gcd(11, 13), 1)
        self.assertEqual(gcd(999, 666), 333)