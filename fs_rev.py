
import numpy as np
import math
import cmath
import matplotlib.pyplot as plt
from scipy import signal

# NOTE: Not working properly
# probably has indexing issues

time = np.linspace(0, 10000, 10000, endpoint = True, retstep=False, dtype=None)
period = 12
x = [i for i in range(10000)]
def my_square():
    s = []
    temp = 0
    for i in range(len(x)):
        if temp <= 6:
            s.append(1)
        else:
            s.append(0)
            if temp == 12:
                temp = 0
        temp += 1
    return s
s = my_square()

# for i, n in enumerate(s):
#     if n == -1:
#         s[i] = 0

print(s)

new_s = np.delete(s, 0)

def get_ak(k):
    ak = []
    result = 0
    for i in range(k):
        for t in range(period):
            result += s[t+1]*np.sin((i+1)*np.pi*t/period)/period
            print(result)
        ak.append(result)
    print(ak)
    return ak
def get_fs():
    fs = []
    result = 0
    ak = get_ak(10)
    print("Total number of coefficients : {} ".format(len(ak)))
    for t in range(len(time)):
        for i in range(len(ak)):
            result += ak[i]*np.sin((i+1)*np.pi*t/(period))
        fs.append(result)
        result = 0
    plt.plot(x, fs, linewidth = 3)
    plt.xlim(0,100)
    plt.show()

get_fs()

######################################################
#plots only a single harmonic
def one_ak(k):
    ak = 0
    for t in range(len(time)):
        ak += s[t]*np.cos(k*np.pi*t/period)*1/period
    return ak

def one_fs(k):
    fs = []
    result = 0
    ak = one_ak(k)
    for t in range(len(time)):
        result = ak*np.cos(k*np.pi*t/period)
        fs.append(result)
    # plt.plot(x, fs, linewidth = 3)
    # plt.show()
    return fs



#Lambda func
# def func_maker(n):
#     return lambda x:x**n
# pow2 = func_maker(2)
# print(pow2(2))

# list_a = []
# list_b = []
# list_c = []
# list_d = []
#


# Finds items and their indexes inside lists
# for n, i in enumerate(list_a):
#     print("i : ",i)
#     print("n : ",n)


# list_a = one_fs(1)
# list_b = one_fs(2)
# list_c = one_fs(3)
# list_d = one_fs(4)
#
# list_e = [sum(i) for i in zip(list_c, list_a)]
#
#
# plt.figure(1)
# plt.subplot(311)
# plt.plot(x, list_c, linewidth = 3)
#
# plt.subplot(312)
# plt.plot(x, list_a, linewidth = 3)
#
# plt.subplot(313)
# plt.plot(x, list_e, linewidth = 3)
#
# plt.show()

# def f(t):
#     return np.exp(-t) * np.cos(2*np.pi*t)
# t1 = np.arange(0, 5, 0.1)
# t2 = np.arange(0, 5, 0.02)
# t3 = np.arange(-5, 5, 0.1)
#
# plt.figure(1)
# plt.subplot(311)
# plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
#
# plt.subplot(312)
# plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
#
# plt.subplot(313)
# plt.plot(t3, np.sin(2*np.pi*t3), 'r--')
# plt.show()
