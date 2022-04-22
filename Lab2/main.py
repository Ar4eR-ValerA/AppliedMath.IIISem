import numpy as np
import algorithms.stepSizeAlgorithms as algos
from algorithms.gradientDescent import gradient_descent
from oracle.testOracles.oracle1 import Oracle1
from oracle.testOracles.oracle2 import Oracle2
from oracle.testOracles.oracle3 import Oracle3
from oracle.testOracles.oracle4 import Oracle4
from algorithms.fletcherReevesAlgorithm.fletcherReeves import fletcher_reeves


o1 = Oracle1()
o2 = Oracle2()
o3 = Oracle3()
o4 = Oracle4()
t1 = algos.ConstStep()
t2 = algos.SplittingStep(0.3)
t3 = algos.GoldenRatioStep()
t4 = algos.FibonacciStep()


#print(gradient_descent(o1, np.array([-8, 4]), t1, 0.0001, max_iter=1000, max_alpha=1, exit_clause="argument")[0])
#print(gradient_descent(o1, np.array([-8, 4]), t2, 0.0001, max_iter=1000, max_alpha=1, exit_clause="function")[0])
#print(gradient_descent(o1, np.array([-5, 3]), t3, 0.0001, max_iter=1000, max_alpha=1, exit_clause="both")[0])
#print(gradient_descent(o1, np.array([7, -13]), t4, 0.0001, max_iter=1000, max_alpha=1)[0])

#print(fletcher_reeves(o1, np.array([0.5, 1]), t3, 0.00001, 0.00015, 10, 10)[0])
#print(fletcher_reeves(o2, np.array([0, -2]), t3, 0.00001, 0.00015, 10, 10)[1])

#print(fletcher_reeves(o3, np.array([-3, 4]), t3, 0.001, 0.015, 1000, 100)[1])

