import math
import numpy as np
from algorithms.stepSizeFunction import StepSizeFunction
from oracle.firstOrderOracle import FirstOrderOracle


# TODO: add momentum
def gradient_descent(
        oracle: FirstOrderOracle,
        start_x: np.array,
        step_size_func: StepSizeFunction,
        eps: float, max_iter=-1, max_alpha=0.5, refresh_each=100,
        exit_clause="both"):  # argument/function/both

    if max_alpha <= 0:
        max_alpha = 1

    steps = [start_x]
    iteration = 0

    prev_x = start_x + 2 * eps
    curr_x = start_x
    prev_f = oracle.function(start_x) + eps * 2
    curr_f = oracle.function(start_x)
    alpha = max_alpha

    while (iteration < max_iter or max_iter < 0) \
            and check_exit_clause(prev_x, curr_x, prev_f, curr_f, eps, exit_clause):
        prev_x, prev_f = curr_x, curr_f
        grad = oracle.gradient(prev_x)

        if np.all(np.abs(grad) <= eps / 100):
            break

        def func(a):
            return oracle.function(prev_x - a * grad)

        alpha = step_size_func.calc_step(func, 0, alpha, eps, oracle, prev_x)

        # refresh
        if alpha <= eps / 100 or iteration == refresh_each:
            alpha = max_alpha

        curr_x = prev_x - alpha * grad
        curr_f = oracle.function(curr_x)

        while step_size_func.split_step and curr_f >= prev_f:
            alpha /= 2
            alpha = step_size_func.calc_step(func, 0, alpha, eps, oracle, prev_x)
            curr_x = prev_x - alpha * grad
            curr_f = oracle.function(curr_x)

        steps.append(curr_x)
        iteration += 1

    return curr_x, steps


def check_exit_clause(prev_x, curr_x, prev_f, curr_f, eps, condition):
    if condition == "argument":
        return math.dist(prev_x, curr_x) >= eps
    elif condition == "function":
        return math.fabs(curr_f - prev_f) >= eps
    return math.dist(prev_x, curr_x) >= eps and math.fabs(curr_f - prev_f) >= eps
