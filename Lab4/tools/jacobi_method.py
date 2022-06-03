import copy

import numpy as np
import math
from scipy import sparse


def find_max(A):
    n = len(A)
    max_i, max_j = 0, 1;
    max = A[0, 1]
    for i in range(n):
        for j in range(i + 1, n):
            if (abs(A[i, j]) > abs(max)):
                max_i = i
                max_j = j
                max = A[i, j]

    return max_i, max_j


def find_rotation(A, i, j):
    k = len(A)
    if (A[i, i] == A[j, j]):
        return math.pi / 4

    return math.atan(2.0 * A[i, j] / (A[j, j] - A[i, i])) / 2.0


def stop_criteria(A, eps):
    n = len(A)
    norma = 0
    for i in range(n):
        for j in range(i + 1, n):
            norma += A[i, j] ** 2

    return math.sqrt(norma) < eps


def jacobi_solve(matrix: np.array, eps):
    n = len(matrix)
    iters = 0
    vectors = np.eye(n, n);

    if (n <= 1):
        return matrix, matrix, iters

    while (not stop_criteria(matrix, eps)):
        max_i, max_j = find_max(matrix)
        deg = find_rotation(matrix, max_i, max_j)
        rotate = np.eye(n, n);

        rotate[max_i, max_i] = rotate[max_j, max_j] = math.cos(deg)
        rotate[max_i, max_j] = -math.sin(deg)
        rotate[max_j, max_i] = -rotate[max_i, max_j]

        rotateT = rotate.transpose()

        matrix = np.dot(np.dot(rotateT, matrix), rotate)
        vectors = np.dot(vectors, rotate)

        iters += 1

    answer = [matrix[i, i] for i in range(n)]

    return answer, vectors, iters