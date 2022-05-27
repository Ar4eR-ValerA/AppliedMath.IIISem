from scipy import sparse
from tools.luDecomposition import lu_decomposition
from tools.linearEquationsSystemSolve import linear_equations_system_solve_triangle


def inverse_matrix(a: sparse.csr_matrix):
    n = a.shape[0]
    e = get_identity_matrix(n)
    l, u, iteration_count = lu_decomposition(a)

    t, new_iteration_count = linear_equations_system_solve_triangle(l, e, True)
    iteration_count += new_iteration_count

    inverse, new_iteration_count = linear_equations_system_solve_triangle(u, t, False)
    iteration_count += new_iteration_count
    return inverse, iteration_count


def get_identity_matrix(n: int):
    matrix = sparse.lil_matrix((n, n))
    for i in range(0, n):
        matrix[i, i] = 1

    return matrix
