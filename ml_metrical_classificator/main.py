import math
from random import random
from typing import Callable

import matplotlib.pyplot as plt


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
    points1: list[tuple[float, float]],
    points2: list[tuple[float, float]],
    current: tuple[float, float],
    K: int,
    metric: Callable[[float, float, float, float], float],
) -> tuple[float, float]:
    """
    Returns "importance" of the `current` point relative to points in two lists accourding to "K nearest algorithm"
    """
    x, y = current
    dsts1 = [metric(currx, curry, x, y) for currx, curry in points1]
    dsts2 = [metric(currx, curry, x, y) for currx, curry in points2]

    i1, i2 = 0, 0
    imp1 = 0
    imp2 = 0

    while (i1 + i2 < K) and (i1 < len(dsts1)) and (i2 < len(dsts2)):
        if dsts1[i1] < dsts2[i2]:
            i1 += 1
            imp1 += 1
        else:
            i2 += 1
            imp2 += 1

    return imp1, imp2


def generate_points(
    N: int, left: float, right: float, bottom: float, top: float
) -> list[tuple[float, float]]:
    res = []

    for _ in range(N):
        x = left + random() * (right - left)
        y = bottom + random() * (top - bottom)
        res.append((x, y))

    return res


reds = generate_points(5, 0, 1, 0, 0.5)
blues = generate_points(5, 0, 1, 0.5, 1)

K = 5

fig = plt.figure()
plt.ion()
plt.show()

for x, y in reds:
    plt.scatter(x, y, marker="o", color="r")

for x, y in blues:
    plt.scatter(x, y, marker="o", color="b")


def onclick(event):
    x, y = event.xdata, event.ydata
    r_imp, b_imp = k_nearest(reds, blues, (x, y), K, manhattan_distance)

    print(f"red importance: {r_imp} | blue importance: {b_imp}")
    if r_imp > b_imp:
        reds.append((x, y))
        clr = "r"
    else:
        blues.append((x, y))
        clr = "b"

    plt.scatter(x, y, marker="o", color=clr)
    fig.canvas.draw()


cid = fig.canvas.mpl_connect("button_press_event", onclick)
while True:
    plt.pause(0.001)
