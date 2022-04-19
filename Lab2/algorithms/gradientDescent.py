import math
import numpy as np
from algorithms.stepSizeFunction import StepSizeFunction
from oracle.firstOrderOracle import FirstOrderOracle


# TODO: add momentum
# TODO: change '==' to fabs()
def gradient_descent(
        oracle: FirstOrderOracle,
        start_x: np.array,
        step_size_func: StepSizeFunction,
        eps: float, max_iter=-1, default_alpha=1):

    if default_alpha <= 0:
        default_alpha = 1

    steps = [start_x]
    iteration = 0

    prev_x = start_x + 2 * eps
    curr_x = start_x
    prev_f = oracle.function(start_x) + eps * 2
    curr_f = oracle.function(start_x)

    # TODO: decompose exit clause to it's own class
    while (iteration < max_iter or max_iter < 0)\
            and math.dist(prev_x, curr_x) >= eps and math.fabs(curr_f - prev_f) >= eps:
        prev_x, prev_f = curr_x, curr_f
        grad = oracle.gradient(prev_x)

        # if we reached extremum (maybe need to add check if extremum is min)
        if np.all(grad == 0):
            break

        def func(a):
            # TODO: check function
            return oracle.function(prev_x - a * grad) + eps

        # TODO: how to choose bounds to find min
        alpha = step_size_func.calc_step(func, 0, 100, eps)

        # refresh
        if alpha == 0:
            alpha = default_alpha

        curr_x = prev_x - alpha * grad
        curr_f = oracle.function(curr_x)
        steps.append(curr_x)

        iteration += 1

    return curr_x, steps
