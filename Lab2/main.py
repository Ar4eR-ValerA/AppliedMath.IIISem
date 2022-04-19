import math
import numpy as np
from algorithms.gradientDescent import gradient_descent
from algorithms.stepSizeAlgorithms.constStep import ConstStep
from oracle.testOracles.oracle1 import Oracle1
from algorithms.fletcherReevesAlgorithm.fletcherReeves import FletcherReeves

o = Oracle1()
t = ConstStep()
t.set_step_size(0.2)

#TODO: выпилить нахер, мне нужно было для тестирования, а lab1 подключать было долго <3
def find_min(function, left_bound, right_bound, eps):
    golden_ratio = (math.sqrt(5) + 1) / 2
    segments = []
    calls = 0

    left_point = right_bound - (right_bound - left_bound) / golden_ratio
    right_point = left_bound + (right_bound - left_bound) / golden_ratio
    calls += 2

    left_result = function(left_point)
    right_result = function(right_point)

    while right_bound - left_bound > eps:
        segments.append((left_bound, right_bound))

        if left_result < right_result:
            right_bound = right_point
            right_result = left_result

            right_point = left_point
            left_point = right_bound - (right_bound - left_bound) / golden_ratio

            left_result = function(left_point)
            calls += 1

        else:
            left_bound = left_point
            left_result = right_result

            left_point = right_point
            right_point = left_bound + (right_bound - left_bound) / golden_ratio

            right_result = function(right_point)
            calls += 1

    segments.append((left_bound, right_bound))
    return (right_bound + left_bound) / 2, calls, segments


print(gradient_descent(o, np.array([-2, 7]), t, 0.001, max_iter=100, default_alpha=0.2)[0])
print(FletcherReeves.execute(o, find_min, FletcherReeves.Params(np.array([0.5, 1]), 0.1, 0.15, 10)))
