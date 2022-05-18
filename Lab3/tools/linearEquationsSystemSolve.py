from scipy import sparse
from scipy.sparse import linalg


def linear_equations_system_solve(a: sparse.csr_matrix, v: sparse.csr_matrix, is_lower: bool):
    if is_lower:
        return lower(a, v)
    else:
        return upper(a, v)

def lower(a: sparse.csr_matrix, v: sparse.csr_matrix):
    x = []
    iteration_counter = 0
    n = v.shape[1]

    for k in range(0, n):
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
    x = []
    n = v.shape[1]

    iteration_counter = 0
    for i in range(0, n):
        iteration_counter += 1
        ans_vector = linalg.spsolve(a, v.getcol(i))
        x.append(ans_vector)

    return sparse.csr_matrix(x).transpose(), 0
