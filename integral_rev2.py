import numpy as np
import scipy
import math
import sys
import os
import matplotlib.pyplot as plt
from sympy import integrate
from sympy import var
from sympy import sympify
from sympy import Symbol
from sympy.utilities.lambdify import lambdify

# x2 = lambda x: x**2
#
# y, err = integrate.quad(x2, 0, 10)
#
# print(y)
t = var('t')
dt = 0.001
def definite_integral(expr, t_min, t_max):
    function = sympify(expr)
    print("Integrating the following function : {}".format(function))
    int = integrate(function, t)
    func = lambdify(t, int)
    result = func(t_max-t_min)
    print(result)
    return result


definite_integral('t**2',0,10)
