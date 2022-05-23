import numpy as np
import copy
from scipy import sparse


# def seidel(a: sparse.csr_matrix, b: np.array, eps):
#     n = a.shape[0]
#     x = np.zeros(n)
#     iteration_count = 0
#
#     converge = False
#     while not converge:
#         x_new = np.copy(x)
#         for i in range(n):
#             s1 = sum(a[i, j] * x_new[j] for j in range(i))
#             s2 = sum(a[i, j] * x[j] for j in range(i + 1, n))
#             x_new[i] = (b[i] - s1 - s2) / a[i, i]
#             iteration_count += 1
#
#         converge = np.sqrt(sum((x_new[i] - x[i]) ** 2 for i in range(n))) <= eps
#         x = x_new
#
#     return x, iteration_count

# def seidel(a: sparse.csr_matrix, b: np.array, eps, out):
#     n = a.shape[0]
#     x = np.zeros(n)
#     iteration_count = 0
#     converge = False
#     while not converge:
#         iteration_count += n ** 2 + n
#         new_x = copy.deepcopy(x)
#         x = seidel_iteration(a, b)
#         print(*x, file=out)
#         converge = np.sqrt(sum((new_x[i] - x[i]) ** 2 for i in range(n))) <= eps
#     return x, iteration_count
#
#
# def seidel_iteration(a: sparse.csr_matrix, b: np.array):
#     n = a.shape[0]
#     x = np.zeros(n)
#
#     for j in range(0, n):
#         d = 0
#
#         for i in range(0, n):
#             if j != i:
#                 d += a[i, j] * x[j]
#         x[j] = (b[j] - d) / a[j, j]
#     return x


def isNeedToComplete(x_old, x_new, eps):
    for i in range(len(x_new)):
        if abs(x_old[i] - x_new[i]) > eps:
            return False

    return True


def seidel(A, B, eps, out):
    count = len(B)
    x = np.array([0.0] * count)

    numberOfIter = 0

    while 1:
        x_prev = copy.deepcopy(x)

        for i in range(count):
            S = 0
            for j in range(count):
                if j != i:
                    S = S + A[i, j] * x[j]
            x[i] = B[i] / A[i, i] - S / A[i, i]

        numberOfIter += 1

        print(*x, file=out)
        if isNeedToComplete(x_prev, x, eps):
            break

    return x, numberOfIter
