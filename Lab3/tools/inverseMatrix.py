import numpy as np
from tools.luDecomposition import lu_decomposition


def inverse_matrix(a: np.array):
    n = len(a)
    e = get_identity_matrix(n)
    l, u = lu_decomposition(a)

    t = np.linalg.solve(l, e)
    return np.linalg.solve(u, t)


def get_identity_matrix(n: int):
    matrix = []
    for i in range(0, n):
        list = []
        for j in range(0, n):
            list.append(0)
        list[i] = 1
        matrix.append(list)

    return np.array(matrix)