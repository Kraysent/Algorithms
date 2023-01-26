import numpy as np

def tdma(A, B, C, F) -> np.ndarray:
    A = [0.0] + A
    C = C + [0.0]
    n = len(B)
    x = np.zeros(shape=(n,))

    alpha = np.zeros(shape=(n,))
    beta = np.zeros(shape=(n,))
    alpha[0] = 0
    alpha[1] = -C[0] / B[0]
    beta[0] = 0
    beta[1] = F[0] / B[0]

    for i in range(1, n - 1):
        alpha[i + 1] = -C[i] / (A[i] * alpha[i] + B[i])
        beta[i + 1] = (F[i] - A[i] * beta[i]) / (A[i] * alpha[i] + B[i])

    x[-1] = (F[-1] - A[-1] * beta[-1]) / (A[-1] * alpha[-1] + B[-1])

    for i in range(n - 2, -1, -1):
        x[i] = alpha[i + 1] * x[i + 1] + beta[i + 1]

    return x
