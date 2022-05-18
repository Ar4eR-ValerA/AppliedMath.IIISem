from scipy import sparse
from scipy.sparse import linalg


def linear_equations_system_solve(a: sparse.lil_matrix, v: sparse.lil_matrix):
    x = []
    n = a.shape[0]

    for i in range(0, n):
        ans_vector = linalg.spsolve(a, v.getcol(i))
        x.append(ans_vector)

    matrix_x = sparse.lil_matrix(x)
    return matrix_x.transpose()
