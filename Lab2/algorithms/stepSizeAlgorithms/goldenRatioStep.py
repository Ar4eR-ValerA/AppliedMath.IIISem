from algorithms.stepSizeFunction import StepSizeFunction
import golden_ratio_algorithm
from oracle import firstOrderOracle


class GoldenRatioStep(StepSizeFunction):
    split_step: bool

    def __init__(self):
        super().__init__()

    def calc_step(self, function, left_bound, right_bound, eps, oracle: firstOrderOracle = 0, curr_x=0):
        return golden_ratio_algorithm.find_min(function, left_bound, right_bound, eps)[0]
