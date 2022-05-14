import numpy as np
from scipy import sparse


def linear_equations_system_solve(a: sparse.csr_matrix, v: sparse.csr_matrix):
    x = []
    n = a.shape[0]
    a = a.toarray()
    v = v.toarray().transpose()

    for i in range(0, n):
        ans_vector = np.linalg.solve(a, v[i])
        x.append(ans_vector)

    matrix_x = sparse.csr_matrix(x)
    return matrix_x.transpose()
