import numpy as np


def linear_equations_system_solve(a: np.array, v: np.array):
    x = []
    n = len(a)
    a = a
    v = v.transpose()

    for i in range(0, n):
        ans_vector = np.linalg.solve(a, v[i])
        x.append(ans_vector)

    matrix_x = np.array(x)
    return matrix_x.transpose()