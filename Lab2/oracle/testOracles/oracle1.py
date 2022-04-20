import numpy as np
from oracle.firstOrderOracle import FirstOrderOracle


class Oracle1(FirstOrderOracle):

    def function(self, arguments):
        return 2 * arguments[0] ** 2 + arguments[0] * arguments[1] + arguments[1] ** 2

    def gradient(self, arguments):
        return np.array([4 * arguments[0] + arguments[1], arguments[0] + 2 * arguments[1]])
