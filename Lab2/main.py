import numpy as np
from algorithms.gradientDescent import gradient_descent
from algorithms.stepSizeAlgorithms.constStep import ConstStep
from oracle.testOracles.oracle1 import Oracle1

o = Oracle1()
t = ConstStep()
t.set_step_size(0.2)

print(gradient_descent(o, np.array([-2, 7]), t, 0.001, max_iter=100, default_alpha=0.2)[0])
