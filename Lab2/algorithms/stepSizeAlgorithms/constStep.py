from algorithms.stepSizeFunction import StepSizeFunction


class ConstStep(StepSizeFunction):
    split_step: bool

    def __init__(self):
        super().__init__()
        self.split_step = True

    def calc_step(self, function, left_bound, right_bound, eps):
        return right_bound
