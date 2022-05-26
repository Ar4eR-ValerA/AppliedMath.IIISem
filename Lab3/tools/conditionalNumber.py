import numpy as np
from scipy import sparse
from tools.inverseMatrix import inverse_matrix


def norm(A: sparse.csr_matrix):
    result = 0
    k, n = A.shape
    for i in range(k):
        for j in range(n):
            result += A[i, j] ** 2
    return np.sqrt(result)


def get_conditional_number(a: sparse.csr_matrix):
    a_inverse = inverse_matrix(a)[0]
    return norm(a) * norm(a_inverse)
