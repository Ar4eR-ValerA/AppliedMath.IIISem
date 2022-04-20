import numpy as np
from oracle.firstOrderOracle import FirstOrderOracle


class Oracle4(FirstOrderOracle):

    def function(self, arguments):
        x = arguments[0]
        y = arguments[1]
        return np.log(10000 * (x + 1) ** 8 + x ** 4 * y ** 4 + y ** 8 + 0.1) + 2

    def gradient(self, arguments):
        x = arguments[0]
        y = arguments[1]


        t = np.log10(x ** 4 * y ** 4 + 10000 * (x + 1) ** 8 + y ** 8 + 0.1)

        g1 = (4 * x ** 3 * y ** 4 + 80000 * (x + 1) ** 7) / t
        g2 = (4 * y ** 3 * (x ** 4 + 2 * y ** 4)) / t

        return np.array([g1, g2])
