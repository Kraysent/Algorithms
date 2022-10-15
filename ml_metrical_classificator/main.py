import math
from pprint import pprint
from random import random
from typing import Callable
import matplotlib.pyplot as plt
import numpy as np


def euclidean_metric(x1, y1, x2, y2) -> float:
    """
    Returns metric computed as physical distance between points.
    """
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def cosine_distance(x1, y1, x2, y2) -> float:
    return 1 - (x1 * x2 + y1 * y2) / (
        math.sqrt(x1**2 + y1**2) * math.sqrt(x2**2 + y2**2)
    )


def manhattan_distance(x1, y1, x2, y2) -> float:
    return abs(x1 - x2) + abs(y1 - y2)


def k_nearest(
    groups: list[list[tuple[float, float]]],
    current: tuple[float, float],
    K: int,
    metric: Callable[[float, float, float, float], float],
) -> list[float]:
    """
    Returns "importances" of the `current` point relative to points in each group from `groups`
    according to K nearest neighbours algorithm.
    """
    x, y = current
    dst_groups = [
        sorted([metric(currx, curry, x, y) for currx, curry in group])
        for group in groups
    ]

    indices = [0] * len(groups)
    importances = [0] * len(groups)

    while sum(indices) < K and all(
        index < len(dst_groups[i]) for i, index in enumerate(indices)
    ):
        curr_distances = [dst_groups[i][index] for i, index in enumerate(indices)]

        nearest_group_number = np.argmin(curr_distances)
        indices[nearest_group_number] += 1
        importances[nearest_group_number] += 1

    return importances


def generate_points(
    N: int, left: float, right: float, bottom: float, top: float
) -> list[tuple[float, float]]:
    res = []

    for _ in range(N):
        x = left + random() * (right - left)
        y = bottom + random() * (top - bottom)
        res.append((x, y))

    return res


GROUPS_NUMBER = 4
N = 30
K = 50
TRAINT_ON_TEST = False
LEFT, RIGHT = 0, 1
BOTTOM, TOP = 0, 10
COLORS = "bgrcmykw"

fig = plt.figure()
plt.xlim(LEFT, RIGHT)
plt.ylim(TOP, BOTTOM)
plt.ion()
plt.show()

groups = []

for i in range(GROUPS_NUMBER):
    curr_group = generate_points(
        N,
        LEFT,
        RIGHT,
        BOTTOM + i / GROUPS_NUMBER * (TOP - BOTTOM),
        BOTTOM + (i + 1) / GROUPS_NUMBER * (TOP - BOTTOM),
    )

    for x, y in curr_group:
        plt.scatter(x, y, marker="o", color=COLORS[i % len(COLORS)])

    groups.append(curr_group)


def onclick(event):
    x, y = event.xdata, event.ydata
    importances = k_nearest(groups, (x, y), K, euclidean_metric)

    print(f"Importances: {importances}")
    clr = COLORS[np.argmax(importances) % len(COLORS)]

    plt.scatter(x, y, marker="o", color=clr)
    fig.canvas.draw()


cid = fig.canvas.mpl_connect("button_press_event", onclick)
while True:
    plt.pause(0.001)
