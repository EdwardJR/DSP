import numpy as np
import math
import cmath
import matplotlib.pyplot as plt
from midpoint import midpoint


time = np.arange(0, 50, 0.1)
period = 12


def my_square():
    s = []
    temp = 0
    for i in range(len(time)):
        if temp <= 6:
            s.append(1)
        else:
            s.append(0)
            if temp == 12:
                temp = 0
        temp += 1
    return s
s = my_square()

def get_ak(k):
    ak = []
    i = 0
    v = lambda t : np.sin((i+1)*2*np.pi*t/period)/period
    for i in range(k):
        ak.append(midpoint(v, 0, 6, 1000))
    print(ak)
    return ak



def get_fs(n):
    fs = []
    result = 0
    ak = get_ak(n)
    print("Total number of coefficients : {} ".format(len(ak)))
    for t in range(len(time)):
        for i in range(len(ak)):
            result += ak[i]*np.sin((i+1)*np.pi*t/(period))
        fs.append(result)
        result = 0
    plt.plot(time, fs, linewidth = 3)
    plt.xlim(0,10)
    plt.show()
get_fs(100)
