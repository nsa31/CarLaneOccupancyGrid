import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
import numpy as np

sigx = 1
sigy = 1
vx = 80
vy = 0
alpha = 2


def f(x, y):
    #return np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)
    z1 = np.exp(-(((10-x)/sigx)**2 + ((30-y)/sigy)**2))
    z2 = 1 + np.exp(-alpha*((x-10)*vx + (y-30)*vy))
    return z1/z2*1000



x = np.linspace(0, 30, 100)
y = np.linspace(20, 40, 100)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)
plt.contour(X, Y, Z, colors='blue');
plt.show()

