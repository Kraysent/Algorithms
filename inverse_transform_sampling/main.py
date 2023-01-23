import numpy as np
from typing import Callable

def sample(inverse_cdf: Callable[[np.ndarray], np.ndarray], n: int):
    u = np.random.uniform(0, 1, n)

    return inverse_cdf(u)
    