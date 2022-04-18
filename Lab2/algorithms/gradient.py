import inspect

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#примитивный градиентный спуск
def gradient_descent(function, gradient, params, init=0): #1:сама функ 2:ее градиент 3: см. gradient_params 4: начальная точка
    curr_point = np.array(init)
    if init is 0:
        curr_point = np.array([0] * params.dimensions)
        print(curr_point)
    x = [curr_point]
    f = [function(curr_point)]

    i = 0
    while i in range(0, params.maxIter):
        delta = -params.rate * np.array(gradient(curr_point)) #см .md (1)
        curr_point = curr_point + delta
        x.append(curr_point)
        f.append(function(curr_point))
        if abs(f[-1] - f[-2]) < params.eps:
            break
    return x, f
