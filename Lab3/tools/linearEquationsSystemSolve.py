import numpy as np
from scipy import sparse
from tools.luDecomposition import lu_decomposition


def linear_equations_system_solve(a: sparse.csr_matrix, v: sparse.csr_matrix):
    l, u, iteration_count = lu_decomposition(a)

    t, new_iteration_count = lower(l, v)
    iteration_count += new_iteration_count

    answer, new_iteration_count = upper(u, t)
    return answer, iteration_count + new_iteration_count


def linear_equations_system_solve_triangle(a: sparse.csr_matrix, v: sparse.csr_matrix, is_lower: bool):
    if is_lower:
        return lower(a, v)
    else:
        return upper(a, v)


def lower(a: sparse.csr_matrix, v: sparse.csr_matrix):
    x = []
    iteration_counter = 0
    n = v.shape[1]
    m = v.shape[0]

    for k in range(0, m):
        vector_v = v.getrow(k).toarray()[0]
        vector_x = []
        for i in range(0, n):
            for j in range(0, i):
                iteration_counter += 1
                vector_v[i] -= a[i, j] * vector_x[j]

            iteration_counter += 1
            vector_x.append(vector_v[i] / a[i, i])
        x.append(vector_x)

    matrix_x = sparse.csr_matrix(x)
    return matrix_x.transpose(), iteration_counter


def upper(a: sparse.csr_matrix, v: sparse.csr_matrix):
    n = v.shape[0]
    m = v.shape[1]

    x = np.empty(m, dtype=np.dtype)
    iteration_counter = 0

    for k in range(0, m):
        vector_v = v.getcol(m - 1 - k).transpose().toarray()[0]
        vector_x = np.empty(n, dtype=float)
        for i in range(0, n):
            for j in range(n - i, n):
                iteration_counter += 1
                vector_v[n - 1 - i] -= a[n - 1 - i, j] * vector_x[j]

            iteration_counter += 1
            vector_x[n - 1 - i] = (vector_v[n - 1 - i] / a[n - 1 - i, n - 1 - i])
        x[m - 1 - k] = vector_x

    matrix_x = sparse.csr_matrix(x.tolist())
    return matrix_x.transpose(), iteration_counter
