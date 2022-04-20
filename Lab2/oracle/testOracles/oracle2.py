import numpy as np
from firstOrderOracle import FirstOrderOracle


class Oracle2(FirstOrderOracle):

    def function(self, arguments):
        return arguments[0] * np.exp(-(arguments[0] ** 2 + arguments[1] ** 2))

    def gradient(self, arguments):
        return np.array([(1 - 2 * (arguments[0] ** 2)) * np.exp(-arguments[0] ** 2 - arguments[1] ** 2),
                         -2 * arguments[0] * arguments[1] * np.exp(-arguments[0] ** 2 - arguments[1] ** 2)])
