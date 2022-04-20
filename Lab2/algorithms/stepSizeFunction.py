from oracle import firstOrderOracle


class StepSizeFunction:
    split_step: bool
    
    def __init__(self):
        self.split_step = False
    
    def calc_step(self, function, left_bound, right_bound, eps, oracle: firstOrderOracle, curr_x):
        pass
