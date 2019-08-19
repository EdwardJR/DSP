import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from PIL import Image
from math import sin
import cmath
import math

# Constructing a squarewave
T = 1
period = T
delta_t = 0.1
K = 50
t = 100

def square_gen(f):
    time = np.linspace(0, 1, 1000, endpoint = True)
    # plt.plot(t, signal.square(2*np.pi*f*t))
    # plt.title('{}Hz square wave'.format(f))
    # plt.xlabel('Time')
    # plt.ylabel('Amplitude')
    # plt.grid(True, which = 'both')
    # plt.axhline(y=0, color='k')
    # plt.ylim(-2, 2)
    # plt.show()
    return signal.square(2*np.pi*f*time)

def form_ak():
    ak = []
    result = 0
    for i in range(K):
        for j in np.arange(0, t, delta_t):
            result += square_gen(10)[math.trunc(j)]*math.cos(i*2*(np.pi/T)*delta_t)
        ak.append(result)
    # print(ak)
    return ak

def dc_val():
    value = 0
    for i in np.arange(0, t, delta_t):
        value += square_gen(10)[math.trunc(i)]
    return value

def form_fs():
    res = 0
    fs = []
    dc = dc_val()
    time = np.arange(0, t, 0.1)
    ak_list  = form_ak()
    for time in np.arange(0, t, 0.1):
        for x in range(K):
            res += ak_list[x]*math.cos(x*2*np.pi*time)
        fs.append(dc + res)

    return fs

def plot_fs():
    time = np.arange(0, t, 0.1)
    fs = form_fs()
    plt.plot(time, fs, linewidth = 3)
    plt.title("Fourier series of a 10Hz square wave")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.grid(True, which = 'both')
    plt.axhline(y=0, color='k')
    plt.xlim(0,10)
    plt.show()
def my_square():
    time = np.arange(0, 10.1, 0.1)
    signal = []
    for i in time:
        if i < 4:
            signal.append(0)
        elif 4 < i < 8:
            signal.append(1)
        else:
            signal.append(0)
    plt.plot(time, signal, linewidth = 3)
    plt.show()
    return signal


def get_sine():
    point_list = []
    point_list_real = []
    res = 0
    time = np.arange(0, 10.1, 0.1)
    for j in time:
        point_list.append((np.exp(complex(0,1)*j)-np.exp(complex(0,-1)*j))/(2*complex(0,1)))
        point_list_real.append(point_list[res].real)
        res += 1
    print(point_list_real)
    plt.plot(time, point_list_real, linewidth = 3)
    plt.show()

def form_cn(n):
    time = np.arange(0, 10.1, 0.1)
    cn = []
    res = 0
    count = 0
    signal = my_square()
    for k in range(n):
        for i in time:
            res += signal[count]*np.exp((-complex(0,1)*k*2*np.pi)*i/(8))*0.1/8
            count += 1
        count = 0
        cn.append(res.real)
        print(cn)
    return cn

def get_fs():
    time = np.arange(0, 10.1, 0.1)
    fs = []
    for k in range(len(form_cn(5))):
        for i time:
