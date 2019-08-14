import numpy as np
import math
import cmath
import matplotlib.pyplot as plt
from scipy import signal



time = np.linspace(0, 1000, endpoint = True, retstep=False, dtype=None)
period = 10
x = [i for i in range(50)]
def my_square():
    s = signal.square(2*np.pi*period*time)
    return s
s = my_square()
new_s = np.delete(s, 0)

def get_ak(k):
    ak = []
    result = 0
    for i in range(k):
        for t in range(len(time)):
            result += s[t]*np.cos(k*np.pi*t/period)*1/10
        ak.append(result)
    return ak
def get_fs():
    fs = []
    result = 0
    ak = get_ak(4)
    print(len(ak))
    for t in range(len(time)):
        for i in range(len(ak)):
            result += ak[i]*np.cos(i*np.pi*t/period)
        fs.append(result)
    plt.plot(x, fs, linewidth = 3)
    plt.show()

get_fs()
