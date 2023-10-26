import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import numpy as np
import math

plt.rcParams[u'font.sans-serif'] = ['simhei']
plt.rcParams['axes.unicode_minus'] = False

def event(t, y):
    r = y[0]
    b = y[1]
    return b - 5

event.terminal = True
event.direction = -1

def fun(t, y):
    c = 0.2
    k = 0.8
    r = y[0]
    b = y[1]
    dR = -c * b
    dB = -k * r
    dydt = [dR, dB]
    return dydt

y0 = [30,60]
yy = solve_ivp(fun, (0, 20), y0, method='RK45',t_eval=np.linspace(0, 20, 100),events=(event))
#yy = solve_ivp(fun, (0, 20), y0, method='RK45',t_eval=np.linspace(0, 20, 100))

t = yy.t
data = yy.y
print(yy.t_events)
#print(yy.y_events)
print(yy)
#print(data)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.plot(t,data[0, :],label='红方兵力')
plt.plot(t,data[1, :],label='蓝方兵力')
plt.xlabel("时间",fontsize=20)
plt.ylabel("兵力数量",fontsize=20)
plt.title("红蓝兵力变化",fontsize=20)
plt.legend(loc='best', frameon=False,fontsize=20)
plt.show()