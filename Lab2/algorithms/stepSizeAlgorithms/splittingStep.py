from stepSizeFunction import StepSizeFunction
import firstOrderOracle


class SplittingStep(StepSizeFunction):
    split_step: bool
    delta: float

    def __init__(self, delta=0.5):
        super().__init__()
        self.delta = delta if 0 < delta < 1 else 0.5

    def calc_step(self, function, left_bound, right_bound, eps, oracle: firstOrderOracle, curr_x):
        alpha = right_bound
        while oracle.function(curr_x) - oracle.function(
                curr_x - alpha * oracle.gradient(curr_x)) < eps * alpha * (sum(curr_x ** 2) ** 0.5):
            alpha *= self.delta

        return alpha
    