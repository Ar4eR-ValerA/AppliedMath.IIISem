from algorithms.stepSizeFunction import StepSizeFunction
import golden_ratio_algorithm


class GoldenRatioStep(StepSizeFunction):
    split_step: bool

    def __init__(self):
        super().__init__()

    def calc_step(self, function, left_bound, right_bound, eps):
        return golden_ratio_algorithm.find_min(function, left_bound, right_bound, eps)[0]
