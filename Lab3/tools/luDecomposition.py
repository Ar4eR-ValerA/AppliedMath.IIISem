from scipy import sparse
import numpy as np


def lu_decomposition(a: sparse.csr_matrix):
    n = a.shape[0]
    u = sparse.lil_matrix(a)
    l = sparse.lil_matrix(np.eye(n))

    iteration_counter = 0
    for i in range(0, n):
        for j in range(i, n):
            l[j, i] = u[j, i] / u[i, i]
            iteration_counter += 1

    print(l.todense())

    for k in range(1, n):
        for i in range(k - 1, n):
            for j in range(i, n):
                l[j, i] = u[j, i] / u[i, i]
                iteration_counter += 1

        for i in range(k, n):
            for j in range(k - 1, n):
                u[i, j] = u[i, j] - l[i, k - 1] * u[k - 1, j]
                iteration_counter += 1

    return sparse.csr_matrix(l), sparse.csr_matrix(u), iteration_counter
