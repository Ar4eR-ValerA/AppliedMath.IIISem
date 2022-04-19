from algorithms.stepSizeFunction import StepSizeFunction


class ConstStep(StepSizeFunction):
    _step_size = 1

    def calc_step(self, function, left_bound, right_bound, eps):
        return self._step_size

    def set_step_size(self, step_size):
        self._step_size = step_size if step_size > 0 else step_size
