import random
from typing import Callable
import matplotlib.pyplot as plt
import numpy as np


class UnfittedError(Exception):
    pass


class KNN_classificator:
    def __init__(
        self, n_neighbours: int, metric: Callable[[np.ndarray, np.ndarray], np.ndarray]
    ):
        self.k = n_neighbours
        self.metric = metric

    def fit(self, x: np.ndarray, y: np.ndarray):
        self.train_set = x
        self.train_markers = y

    def predict(self, x: np.ndarray) -> np.ndarray:
        if not hasattr(self, "train_set") or not hasattr(self, "train_markers"):
            raise UnfittedError()

        predictions = []

        for i in range(x.shape[0]):
            distances = self.metric(self.train_set, x[i, :])
            permutation = distances.argsort()[: self.k]
            sorted_markers: np.ndarray = self.train_markers[permutation]
            uniques, counts = np.unique(sorted_markers, return_counts=True)
            predictions.append(uniques[counts.argmax()])

        return np.array(predictions)


def minkovsky_distance(
    p: int, axis: int = 1
) -> Callable[[np.ndarray, np.ndarray], np.ndarray]:
    def distance_func(start: np.ndarray, end: np.ndarray) -> np.ndarray:
        return (np.abs((start - end)) ** p).sum(axis=axis) ** (1 / p)

    return distance_func


def generate_point(
    groups_number: int, left: float, right: float, bottom: float, top: float
) -> tuple[float, float, int]:
    x = left + random.random() * (right - left)
    group = random.randrange(0, groups_number)
    y = bottom + (group + random.random()) / groups_number * (top - bottom)

    return x, y, group


if __name__ == "__main__":
    GROUPS_NUMBER = 4
    N = 150
    K = 5
    TRAINT_ON_TEST = False
    LEFT, RIGHT = 0, 1
    BOTTOM, TOP = 0, 1
    COLORS = "bgrcmykw"

    fig = plt.figure()
    plt.xlim(LEFT, RIGHT)
    plt.ylim(TOP, BOTTOM)
    plt.ion()
    plt.show()

    points = np.ndarray(shape=(N, 2))
    markers = np.ndarray(shape=(N))

    for i in range(N):
        x, y, marker = generate_point(GROUPS_NUMBER, LEFT, RIGHT, BOTTOM, TOP)
        points[i, :] = np.array([x, y])
        markers[i] = marker

        plt.scatter(x, y, marker="o", color=COLORS[marker % len(COLORS)])

    classificator = KNN_classificator(K, minkovsky_distance(2))
    classificator.fit(points, markers)

    def onclick(event):
        x, y = event.xdata, event.ydata
        data = np.ndarray(shape=(2, 2))
        data[0, :] = [x, y]
        markers = classificator.predict(data)

        for i, marker in enumerate(markers):
            clr = COLORS[int(marker) % len(COLORS)]
            plt.scatter(data[i, 0], data[i, 1], marker="o", color=clr)
            fig.canvas.draw()

    cid = fig.canvas.mpl_connect("button_press_event", onclick)
    while True:
        plt.pause(0.0001)
