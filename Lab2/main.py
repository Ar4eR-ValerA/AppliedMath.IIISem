import numpy as np
import algorithms.stepSizeAlgorithms as algos
from algorithms.gradientDescent import gradient_descent
from oracle.testOracles.oracle1 import Oracle1
from algorithms.fletcherReevesAlgorithm.fletcherReeves import fletcher_reeves


o = Oracle1()
t1 = algos.ConstStep()
t2 = algos.SplittingStep(0.3)
t3 = algos.GoldenRatioStep()
t4 = algos.FibonacciStep()


print(gradient_descent(o, np.array([-8, 4]), t1, 0.0001, max_iter=1000, max_alpha=1, exit_clause="argument")[0])
print(gradient_descent(o, np.array([-8, 4]), t2, 0.0001, max_iter=1000, max_alpha=1, exit_clause="function")[0])
print(gradient_descent(o, np.array([-5, 3]), t3, 0.0001, max_iter=1000, max_alpha=1, exit_clause="both")[0])
print(gradient_descent(o, np.array([7, -13]), t4, 0.0001, max_iter=1000, max_alpha=1)[0])

print(fletcher_reeves(o, np.array([0.5, 1]), t3, 0.00001, 0.00015, 10, 10)[0])
