import numpy as np
from scipy import sparse
from tools.luDecomposition import lu_decomposition
from tools.inverseMatrix import inverse_matrix
from tools.linearEquationsSystemSolve import linear_equations_system_solve
from tools.seidel import seidel
import pytest


def are_equal(matrix_a, matrix_b, delta=0.01):
    if matrix_a.getnnz() != matrix_b.getnnz():
        return False

    delta_matrix = matrix_a - matrix_b
    for arr in delta_matrix.toarray():
        for item in arr:
            if abs(item) > delta:
                return False

    return True


class TestUM:
    def setup_class(cls):
        cls.a = sparse.csr_matrix([
            [1, 0, 0, 0, 0],
            [0, 2, 1, 0, 1],
            [0, 0, 9, 0, 0],
            [0, 0, 1, 3, 0],
            [0, 7, 0, 3, 2],
        ])

    def teardown_class(cls):
        print("class teardown")

    def setup_method(self, method):
        print("method setup")

    def teardown_method(self, method):
        print("method teardown")

    def test_lu_decomposition(self):
        l, u, _ = lu_decomposition(self.a)
        assert are_equal(l.dot(u), self.a)

    def test_strings_b_2(self):
        print("test b*2")
        assert 'b' * 2 == 'bb'
