import numpy as np
from oracle.firstOrderOracle import FirstOrderOracle


class Oracle3(FirstOrderOracle):

    def function(self, arguments):
        return arguments[0] ** 2 + (arguments[0] - 1) * (arguments[1] - 2) + 5 * (arguments[1] + 1) ** 2

    def gradient(self, arguments):
        return np.array([2 * arguments[0] + arguments[1] - 2,arguments[0] + 10 * arguments[1] + 9])
