import numpy as np
import algorithms.stepSizeAlgorithms as algos
from algorithms.gradientDescent import gradient_descent
from oracle.testOracles.oracle1 import Oracle1
from algorithms.fletcherReevesAlgorithm.fletcherReeves import FletcherReeves


o = Oracle1()
t1 = algos.ConstStep()
t2 = algos.GoldenRatioStep()
t3 = algos.FibonacciStep()


print(gradient_descent(o, np.array([-8, 4]), t1, 0.0001, max_iter=1000, max_alpha=1)[0])
print(gradient_descent(o, np.array([-5, 3]), t2, 0.0001, max_iter=1000, max_alpha=1)[0])
print(gradient_descent(o, np.array([7, -13]), t3, 0.0001, max_iter=1000, max_alpha=1)[0])
# print(FletcherReeves.execute(o, find_min, FletcherReeves.Params(np.array([0.5, 1]), 0.1, 0.15, 10)))
