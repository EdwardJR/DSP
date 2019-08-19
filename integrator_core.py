import sympy
import math
import os
import sys
import matplotlib.pyplot as plt
from scipy import integrate
import numpy as np

dt = 0.1
t = np.arange(-100, 100, dt)



#in order to prevent users passing in arguments like os.remove we need to restrict their access to eval
# print(eval('dir()', {'pow':pow,'math':math,'t':t}))
# proper = eval(input(),{'pow':pow,'math':math,'t':t})


def f(x):
    f = lambda x: x
    return f(x)


def F(x):
    int = 0
    points = []
    iterations = 0
    temp = t[0]
    for j in range(len(t)):
        for i in range(iterations):
            int += f(t[i])*dt
        iterations += 1
        points.append(int)
        int = 0
    return points



plt.plot(t, F(t), linewidth = 3)
# plt.ylim(-2, 2)
# plt.xlim(-25, 25)
plt.show()
