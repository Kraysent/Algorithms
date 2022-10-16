import unittest

import numpy as np

from ml_metrical_classificator.main import KNN_classificator, minkovsky_distance


class ProgramTests(unittest.TestCase):
    def _get_classificator(self) -> KNN_classificator:
        return KNN_classificator(5, metric=minkovsky_distance(2))

    def _get_data(self, N: int) -> tuple[np.ndarray, np.ndarray]:
        return np.zeros(shape=(N, 2)), np.zeros(shape=(N))

    def test_single_group(self):
        classificator = self._get_classificator()
        data, markers = self._get_data(2)

        data[0] = [0, 0]
        data[1] = [1, 0]
        markers[:] = [0, 0]

        classificator.fit(data, markers)

        test_data = np.zeros(shape=(1, 2))
        test_data[0] = [0, 1]

        actual = classificator.predict(test_data)
        expected = 0

        self.assertEqual(expected, actual)

    def test_two_groups_obvious(self):
        classificator = self._get_classificator()
        N = 3
        data, markers = self._get_data(N)

        data[:, 0] = list(range(N))
        data[:, 1] = 0
        markers[:2] = 0
        markers[2:] = 1

        classificator.fit(data, markers)

        test_data = np.zeros(shape=(1, 2))
        test_data[0] = [0, 1]

        actual = classificator.predict(test_data)
        expected = 0

        self.assertEqual(expected, actual)

    def test_two_groups_nonobvious(self):
        classificator = self._get_classificator()
        N = 10
        data, markers = self._get_data(N)

        data[:, 0] = list(range(N))
        data[:, 1] = 0
        markers[:6] = 0
        markers[6:] = 1

        classificator.fit(data, markers)

        test_data = np.zeros(shape=(1, 2))
        test_data[0] = [15, 1]

        actual = classificator.predict(test_data)
        expected = 1

        self.assertEqual(expected, actual)
