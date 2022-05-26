import numpy as np
import copy


def is_need_to_complete(x_old, x_new, eps):
    for i in range(len(x_new)):
        if abs(x_old[i] - x_new[i]) > eps:
            return False

    return True


def seidel(A, B, eps):
    count = len(B)
    x = np.array([0.0] * count)

    number_of_iter = 0

    while number_of_iter < 100000:

        x_prev = copy.deepcopy(x)

        for i in range(count):
            s = 0
            for j in range(count):
                number_of_iter += 1
                if j != i:
                    s = s + A[i, j] * x[j]
            x[i] = B[i] / A[i, i] - s / A[i, i]

        if is_need_to_complete(x_prev, x, eps):
            break

    return x, number_of_iter
