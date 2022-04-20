from stepSizeFunction import StepSizeFunction
import firstOrderOracle


class ConstStep(StepSizeFunction):
    split_step: bool

    def __init__(self):
        super().__init__()
        self.split_step = True

    def calc_step(self, function, left_bound, right_bound, eps, oracle: firstOrderOracle, curr_x):
        return right_bound
