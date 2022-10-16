from scipy import stats
import random
from typing import Callable
import matplotlib.pyplot as plt
import numpy as np


def minkovsky_distance(
    p: int, axis: int = 1
) -> Callable[[np.ndarray, np.ndarray], np.ndarray]:
    def distance_func(start: np.ndarray, end: np.ndarray) -> np.ndarray:
        return (np.abs((start - end)) ** p).sum(axis=axis) ** (1 / p)

    return distance_func


def cosine_distance(start: np.ndarray, end: np.ndarray) -> np.ndarray:
    return 1 - np.dot(start, end) / (np.linalg.norm(start) * np.linalg.norm(end))


def k_nearest(
    points: np.ndarray,
    markers: np.ndarray,
    current: np.ndarray,
    K: int,
    metric: Callable[[np.ndarray, np.ndarray], np.ndarray],
) -> int:
    distances = metric(points, current)
    permutation = distances.argsort()[:K]
    sorted_markers = markers[permutation]
    modes, _ = stats.mode(sorted_markers, keepdims=False)
    return modes


def generate_point(
    groups_number: int, left: float, right: float, bottom: float, top: float
) -> tuple[float, float, int]:
    x = left + random.random() * (right - left)
    group = random.randrange(0, groups_number)
    y = bottom + (group + random.random()) / groups_number * (top - bottom)

    return x, y, group


GROUPS_NUMBER = 4
N = 150
K = 5
TRAINT_ON_TEST = False
LEFT, RIGHT = 0, 1
BOTTOM, TOP = 0, 10
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


def onclick(event):
    x, y = event.xdata, event.ydata
    marker = k_nearest(points, markers, np.array([x, y]), K, minkovsky_distance(2))
    clr = COLORS[int(marker) % len(COLORS)]
    plt.scatter(x, y, marker="o", color=clr)
    fig.canvas.draw()


cid = fig.canvas.mpl_connect("button_press_event", onclick)
while True:
    plt.pause(0.001)
