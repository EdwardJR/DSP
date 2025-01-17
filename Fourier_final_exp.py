import numpy as np
import matplotlib.pyplot as plt

# NOTE: This script calculates the exponential fourier series for a given function
period = 1
time = np.linspace(0, 5, 1000)
y = np.sin(2*np.pi*time/period)
j = complex(0,1)

def cn(n):
    c = y*np.exp(-1*j*2*n*np.pi*time/period)
    return c.sum()/c.size

def f(x, Nh):
    f = np.array([2*(cn(i)*np.exp(1*j*2*i*np.pi*x/period)) for i in range(1, Nh + 1)])
    return f.sum()

y2 = np.array([f(t,50).real for t in time])


plt.plot(time, y2)
plt.show()
