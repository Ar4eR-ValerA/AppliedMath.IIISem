import numpy as np
from oracle.firstOrderOracle import FirstOrderOracle


class Oracle4(FirstOrderOracle):

    def function(self, arguments):
        return arguments[0] ** 2 + arguments[0] * (arguments[1] + 4) + 5 * (arguments[1] - 3) ** 2

    def gradient(self, arguments):
        return np.array([2 * arguments[0] + arguments[1] + 4, arguments[0] + 10 * (arguments[1] - 3)])
