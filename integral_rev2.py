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


x2 = lambda x: x**2

y, err = integrate.quad(x2, 0, 10)

print(y)
