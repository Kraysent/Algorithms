import matplotlib.pyplot as plt
import numpy as np
from main import sample
from scipy import special


def inverse_exp():
    pdf = lambda x: np.exp(-x)
    inverse_cdf = lambda x: -np.log(1 - x)
    return pdf, inverse_cdf


def gauss():
    pdf = lambda x: 1 / np.sqrt(2 * np.pi) * np.exp(-0.5 * x**2)
    inverse_cdf = lambda x: np.sqrt(2) * special.erfinv(2 * x - 1)
    return pdf, inverse_cdf


LEFT, RIGHT = -5, 5

X = np.linspace(LEFT, RIGHT, 100)

pdf, inverse_cdf = gauss()

sampled = sample(inverse_cdf, 10000)
hist, edges = np.histogram(sampled, 101)
hist = hist / max(hist)
expected = pdf(X) / max(pdf(X))
edges = (edges[1:] + edges[:-1]) / 2

plt.plot(edges, hist, label="samples")
plt.plot(X, expected, label="pdf", color="r")
plt.legend()
plt.show()
