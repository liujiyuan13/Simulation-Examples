import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import numpy as np
import math

plt.rcParams[u'font.sans-serif'] = ['simhei']
plt.rcParams['axes.unicode_minus'] = False

def nextY(t, y):
    return 0.9 * y + 0.1 * t

y = []
t = []
lastY = 0
y.append(lastY)
t.append(0)
for i in range(10):
    lastY = nextY(0.1 * (i + 1),lastY)
    y.append(lastY)
    t.append(0.1 * (i + 1))

print(y)
print(t)

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.plot(t,y,label='Y')
plt.xlabel("T",fontsize=20)
plt.ylabel("Y",fontsize=20)
plt.title("dy = t - y",fontsize=20)
plt.legend(loc='best', frameon=False,fontsize=20)
plt.show()