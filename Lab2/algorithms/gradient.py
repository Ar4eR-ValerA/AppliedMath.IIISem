import inspect

import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def gradient_descent(function, gradient, delta_function, params, init=0):
    curr_point = np.array(init)
    if init == 0:
        curr_point = np.array([0] * params.dimensions)
        print(curr_point)
    x = [curr_point]
    f = [function(curr_point)]
    i = 0

    while i in range(0, params.maxIter):
        def func(x):
            return abs(function(curr_point) - function(curr_point - x * np.array(gradient(curr_point))))

        rate = delta_function(func, 0, 100, 0.05)

        delta = -rate[0] * np.array(gradient(curr_point))
        curr_point = curr_point + delta

        x.append(curr_point)
        f.append(function(curr_point))
        if abs(f[-2] - f[-1]) < params.eps:
            break
    return x, f
