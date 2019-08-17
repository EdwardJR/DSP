import numpy as np
import scipy
import math
import sys
import os
import matplotlib.pyplot as plt
from scipy import integrate
from sympy import var
from sympy import sympify
from sympy import Symbol



def f(x):
    res = np.sin(x)*np.exp(-x*np.pi)
    return res

t = np.arange(-10, 10, 0.01)

def F(x):
    res = np.zeros_like(x)
    for index, value in enumerate(x):
        y, err = integrate.quad(f, 0, value)
        res[index] = y
    return res



plt.plot(t, F(t), linewidth = 3)
plt.show()

# eval will execute the expression that is given to in the form of str
# res = lambda x: eval(input())
