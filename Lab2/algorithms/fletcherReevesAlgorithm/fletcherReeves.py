import math

import numpy as np


class FletcherReeves:
    class Params:
        def __init__(self, start_point, eps1, eps2, max_iter):
            self.start_point = start_point
            self.eps1 = eps1
            self.eps2 = eps2
            self.max_iter = max_iter

    @staticmethod
    def execute(oracle, optimisation, params):
        points = [params.start_point]
        directions = []
        counter = 0
        end_condition_counter = 0

        while counter < params.max_iter:
            current_gradient_value = oracle.gradient(points[counter])
            if np.linalg.norm(current_gradient_value) < params.eps1:
                return points[counter], points

            if counter == 0:
                directions.append(-current_gradient_value)
            else:
                prev_gradient_value = oracle.gradient(points[counter - 1])
                prev_B = (np.linalg.norm(current_gradient_value) / np.linalg.norm(prev_gradient_value)) ** 2
                directions.append(-current_gradient_value + prev_B * directions[counter - 1])

            def func(t):
                return oracle.function(points[counter] + t * directions[counter])

            #TODO: офк надо извне границы и точность прокидывать. Да и саму функцию бы вынести.
            step_size = optimisation(func, -10, 100, 0.00005)[0]
            points.append(points[counter] + step_size * directions[counter])

            current_point_result = oracle.function(points[counter])
            next_point_result = oracle.function(points[counter + 1])
            if np.linalg.norm(points[counter + 1] - points[counter]) < params.eps2 and \
                    math.fabs(next_point_result - current_point_result) < params.eps2:
                end_condition_counter += 1
                if end_condition_counter == 2:
                    return points[counter], points
            else:
                end_condition_counter = 0

            counter += 1
