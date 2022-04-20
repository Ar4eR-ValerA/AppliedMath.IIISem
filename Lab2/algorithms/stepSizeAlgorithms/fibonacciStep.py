from stepSizeFunction import StepSizeFunction
import fibonacci_algorithm
import firstOrderOracle


class FibonacciStep(StepSizeFunction):
    split_step: bool

    def __init__(self):
        super().__init__()

    def calc_step(self, function, left_bound, right_bound, eps, oracle: firstOrderOracle, curr_x):
        return fibonacci_algorithm.find_min(function, left_bound, right_bound, eps)[0]
