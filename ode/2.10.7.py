import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import numpy as np
import math

plt.rcParams[u'font.sans-serif'] = ['simhei']
plt.rcParams['axes.unicode_minus'] = False

def dy(t, y):
    return  t + y

h = 0.1
y = []
t = []
lastY = 1
y.append(lastY)
t.append(0)

for i in range(9):
    k1 = dy(h * i,lastY)
    k2 = dy(h * i + h / 2,lastY + k1 * h / 2)
    k3 = dy(h * i + h / 2,lastY + k2 * h / 2)
    k4 = dy(h * i + h,lastY + k3 * h)
    lastY = lastY + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    y.append(lastY)
    t.append(h * (i + 1))

print(y)
print(t)

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.plot(t,y,label='Y')
plt.xlabel("T",fontsize=20)
plt.ylabel("Y",fontsize=20)
plt.title("dy = t + y",fontsize=20)
plt.legend(loc='best', frameon=False,fontsize=20)
plt.show()