import numpy as np
import copy

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

        if isNeedToComplete(x_prev, x, eps):
            break

    return x, numberOfIter
