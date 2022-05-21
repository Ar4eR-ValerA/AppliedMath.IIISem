import numpy as np
from scipy import sparse


def seidel(a: sparse.csr_matrix, b: np.array, eps):
    n = a.shape[0]
    x = np.zeros(n)
    print(x)
    iteration_count = 0

    converge = False
    while not converge:
        x_new = np.copy(x)
        for i in range(n):
            s1 = sum(a[i, j] * x_new[j] for j in range(i))
            s2 = sum(a[i, j] * x[j] for j in range(i + 1, n))
            print (s1, s2)
            x_new[i] = (b[i] - s1 - s2) / a[i, i]
            iteration_count += 1

        converge = np.sqrt(sum((x_new[i] - x[i]) ** 2 for i in range(n))) <= eps
        x = x_new

    return x, iteration_count


def seidel_iteration(a: sparse.csr_matrix, b: np.array, x):
    n = a.shape[0]

    for j in range(0, n):
        d = b[j]

        for i in range(0, n):
            if j != i:
                d -= a[j, i] * x[i]
        x[j] = d / a[j][j]
    return x