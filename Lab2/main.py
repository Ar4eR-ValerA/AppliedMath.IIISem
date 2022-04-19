import inspect

import algorithms.gradient as gd
import abstarctions.gradientparams as gp
import algorithms.generate_plot as gen
import numpy as np

# algos for finding the minimum
from Lab1.algorithms.brent_algorithm import find_min as brent
from Lab1.algorithms.dichotomy_algorithm import find_min as dichotomy


# def function(args):
#     x = args[0]
#     y = args[1]
#     return (x - 15) ** 2 + y ** 2


def gradient(args):
    x = args[0]
    y = args[1]
    return [2 * (x - 15), 2 * y]


def function(args):
    x = args[0]
    y = args[1]
    return (x - 15) ** 2 + y ** 2 + 8


gen.visualize_fw()
params = gp.GradientParams(dimensions=2)
gd.gradient_descent(function, gradient, dichotomy, params)
