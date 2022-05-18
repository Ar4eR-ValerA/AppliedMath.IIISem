from scipy import sparse
from scipy.sparse import linalg


def linear_equations_system_solve(a: sparse.csr_matrix, v: sparse.csr_matrix):
    x = []
    n = v.shape[1]

    for i in range(0, n):
        ans_vector = linalg.spsolve(a, v.getcol(i))
        x.append(ans_vector)

    matrix_x = sparse.lil_matrix(x)
    return matrix_x.transpose()
