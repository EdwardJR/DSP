import sympy
import math
import os
import sys
import matplotlib.pyplot as plt
from scipy import integrate
import numpy as np


t = np.arange(-10, 10.1, 0.1)
dt = 0.1


def f(x):
    f = lambda x: x**2
    return f(x)


def F(x):
    int = 0
    points = []
    iterations = 0
    temp = t[0]
    for j in range(len(t)):
        for i in range(iterations):
            int += f(t[i])*0.1
        iterations += 1
        points.append(int)
        int = 0
    return points


plt.plot(t, F(t), linewidth = 3)
plt.show()
