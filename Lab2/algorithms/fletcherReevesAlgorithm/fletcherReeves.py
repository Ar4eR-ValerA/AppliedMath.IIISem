import math
import numpy as np
from algorithms.stepSizeFunction import StepSizeFunction
from oracle.firstOrderOracle import FirstOrderOracle


def fletcher_reeves(
        oracle: FirstOrderOracle,
        start_point: np.array,
        step_size_func: StepSizeFunction,
        eps1, eps2, max_iter, max_step):
    points = [start_point]
    directions = []
    counter = 0
    end_condition_counter = 0

    while counter < max_iter:
        current_gradient_value = oracle.gradient(points[counter])
        if np.linalg.norm(current_gradient_value) < eps1:
            return points[counter], points

        if counter == 0:
            directions.append(-current_gradient_value)
        else:
            prev_gradient_value = oracle.gradient(points[counter - 1])
            prev_B = (np.linalg.norm(current_gradient_value) / np.linalg.norm(prev_gradient_value)) ** 2
            directions.append(-current_gradient_value + prev_B * directions[counter - 1])

        def func(t):
            return oracle.function(points[counter] + t * directions[counter])

        step_size = step_size_func.calc_step(func, 0, max_step, eps1, oracle, 0)
        points.append(points[counter] + step_size * directions[counter])

        current_point_result = oracle.function(points[counter])
        next_point_result = oracle.function(points[counter + 1])
        if np.linalg.norm(points[counter + 1] - points[counter]) < eps2 and \
                math.fabs(next_point_result - current_point_result) < eps2:
            end_condition_counter += 1
            if end_condition_counter == 2:
                return points[counter], points
        else:
            end_condition_counter = 0

        counter += 1

    return points[counter], points
