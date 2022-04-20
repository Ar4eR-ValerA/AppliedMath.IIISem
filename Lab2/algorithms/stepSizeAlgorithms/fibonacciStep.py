from algorithms.stepSizeFunction import StepSizeFunction
import fibonacci_algorithm


class FibonacciStep(StepSizeFunction):
    split_step: bool

    def __init__(self):
        super().__init__()

    def calc_step(self, function, left_bound, right_bound, eps):
        return fibonacci_algorithm.find_min(function, left_bound, right_bound, eps)[0]
