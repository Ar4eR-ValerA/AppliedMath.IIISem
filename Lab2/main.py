import inspect

import algorithms.gradient as gd
import abstarctions.gradientparams as gp
import algorithms.generate_plot as gen
import numpy as np


def function(args):
    x = args[0]
    y = args[1]
    return (x - 15) ** 2 + y ** 2


def gradient(args):
    x = args[0]
    y = args[1]
    return [2 * (x - 15), 2 * y]


gen.visualize_fw()
params = gp.GradientParams(dimensions=2)
gd.gradient_descent(function, gradient, params)
