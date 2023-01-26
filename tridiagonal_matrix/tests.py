import unittest
import numpy as np
from tridiagonal_matrix.main import tdma


class ProgramTests(unittest.TestCase):
    def test_run(self):
        A = [3, 1, 1]
        B = [5, 6, 4, -3]
        C = [3, 1, -2]
        F = [8, 10, 3, -2]

        xs = tdma(A, B, C, F)

        tridiag = np.diag(A, -1) + np.diag(B, 0) + np.diag(C, 1)
        np.testing.assert_array_equal(tridiag @ xs, F)
