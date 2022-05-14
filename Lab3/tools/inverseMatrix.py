import numpy as np
from tools.luDecomposition import lu_decomposition


def inverse_matrix(a: np.array):
    n = len(a)
    e = get_identity_matrix(n)
    l, u = lu_decomposition(a)

    t = linalg_smart_solve(l, e)
    return linalg_smart_solve(u, t)


def get_identity_matrix(n: int):
    matrix = []
    for i in range(0, n):
        list = []
        for j in range(0, n):
            list.append(0)
        list[i] = 1
        matrix.append(list)

    return np.array(matrix)


def linalg_smart_solve(a: np.array, v: np.array):
    x = []
    n = len(a)
    a = a
    v = v.transpose()

    for i in range(0, n):
        ans_vector = np.linalg.solve(a, v[i])
        x.append(ans_vector)

    matrix_x = np.array(x)
    return matrix_x.transpose()
