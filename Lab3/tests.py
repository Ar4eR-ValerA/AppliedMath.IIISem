import random

import numpy as np
from scipy import sparse
from tools.luDecomposition import lu_decomposition
from tools.inverseMatrix import inverse_matrix
from tools.linearEquationsSystemSolve import linear_equations_system_solve
from tools.seidel import seidel
import pytest

eps = 0.01


def are_equal(matrix_a, matrix_b, delta=eps):
    delta_matrix = matrix_a - matrix_b
    for arr in delta_matrix.toarray():
        for item in arr:
            if abs(item) > delta:
                return False

    return True


def generate_matrix(size: int, pool: list):
    return generate_spread_matrix(size, pool, 1)


def generate_spread_matrix(size: int, pool: list, fullness: float = 0.5):
    matrix = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            if random.random() < fullness:
                matrix[i, j] = random.choice(pool)
    return matrix


def fill_diagonal(matrix, pool: list):
    for i in range(len(matrix)):
        matrix[i][i] = random.choice(pool)
    return matrix


class TestUM:
    def teardown_class(cls):
        print("class teardown")

    def setup_method(self, test_lu_decomposition):
        pool = list([1, 2, 9, 7])
        self.a = np.zeros((8, 8))
        while abs(np.linalg.det(self.a)) < eps:
            self.a = fill_diagonal(generate_spread_matrix(8, pool), pool)
        self.a = sparse.csr_matrix(self.a)

    def teardown_method(self, method):
        print("method teardown")

    def test_lu_decomposition(self):
        l, u, _ = lu_decomposition(self.a)
        assert are_equal(l.dot(u), self.a)

    def test_matrix_generating(self):
        assert True
