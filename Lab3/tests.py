import random

import numpy as np
from scipy import sparse
from tools.luDecomposition import lu_decomposition
from tools.inverseMatrix import inverse_matrix
from tools.linearEquationsSystemSolve import linear_equations_system_solve
from tools.seidel import seidel
import pytest

eps = 0.01


def output(out_file, matrix):
    for i in matrix.toarray():
        print(*i, file=out_file)


def decompose_matrix(matrix):  # returns L, D, U matrix from given
    n = len(matrix)
    L, D, U = np.zeros((n, n)), np.zeros((n, n)), np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i > j:
                L[i, j] = matrix[i, j]
            elif i < j:
                U[i, j] = matrix[i, j]
            else:
                D[i, j] = matrix[i, j]
    return L, D, U


def check_siedel(matrix):
    L, D, U = decompose_matrix(matrix)
    inv_matrix = -(np.linalg.inv(L + D)) * U
    val = np.linalg.norm(inv_matrix)
    return np.linalg.norm(inv_matrix) < 1


def generate_diagonal_matrix(k):
    values = [0, -1, -2, -3, -4, -5, -6]
    noise = 10 ** (-k)
    matrix = np.zeros((k, k))
    for i in range(k):
        for j in range(k):
            matrix[i][j] = random.choice(values)
    for i in range(k):
        matrix[i][i] = -(sum(matrix[i]) - matrix[i][i]) + noise
    return matrix


def generate_gilbert_matrix(k):
    matrix = np.zeros((k, k))
    for i in range(k):
        for j in range(k):
            matrix[i][j] = 1 / (i + j + 1)
    return matrix


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
    def setup_method(self, test_lu_decomposition):
        matrix_size = 8
        pool = list([1, 2, 9, 7])
        self.a = np.zeros((matrix_size, matrix_size))
        while abs(np.linalg.det(self.a)) < eps:
            self.a = fill_diagonal(generate_spread_matrix(matrix_size, pool), pool)
        self.a = sparse.csr_matrix(self.a)

    def setup_method(self, test_diagonal_matrix):
        matrix_size = 8
        self.a = generate_diagonal_matrix(matrix_size)
        self.arr = np.array([i for i in range(1, matrix_size + 1)])
        self.b = np.dot(self.a, self.arr)

        self.a = sparse.csr_matrix(self.a)
        self.out = open("out.txt", "w")
    
    def setup_method(self, test_gilbert_matrix):
        matrix_size = 8
        self.a = generate_gilbert_matrix(matrix_size)
        self.arr = np.array([i for i in range(1, matrix_size + 1)])
        self.b = np.dot(self.a, self.arr)

        self.a = sparse.csr_matrix(self.a)
        self.out = open("out.txt", "w")

    def test_lu_decomposition(self):
        l, u, _ = lu_decomposition(self.a)
        assert are_equal(l.dot(u), self.a)

    def test_diagonal_matrix(self):
        x, _ = seidel(self.a, self.b, eps, self.out)

        f = open("tmp.txt", "w")
        output(f, self.a)
        assert True

    def test_gilbert_matrix(self):
        x, _ = linear_equations_system_solve(self.a, sparse.csr_matrix(self.b))

        print("", *x.transpose().toarray()[0], sep="\n")
        f = open("tmp.txt", "w")
        output(f, self.a)
        assert True
