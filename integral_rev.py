import numpy as np
import scipy
import math
import sys
import os
import matplotlib.pyplot as plt
import scipy
from sympy import integrate
from sympy import var
from sympy import sympify
from sympy import Symbol
from sympy import sin
from sympy.utilities.lambdify import lambdify

# NOTE: Works like a charm

x = var('x')
t = np.arange(-10, 10, 0.1)

user_input = input("input the desired function : ")
expr = sympify(user_input)
print(expr)
int = integrate(expr, x)
print(int)
func = lambdify(x, int)

f_list = []

for i in t:
    f_list.append(func(i))

plt.plot(t, f_list)
plt.show()
# expr = sympify(user_input)
