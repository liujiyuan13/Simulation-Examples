import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

x = [(j + 1 / 2) / 40 for j in range(0,40)]
y = stats.norm.ppf(x, 0, 1)

data = pd.read_excel('./input/datas/cep.xlsx')
samp = data['落点偏差'].values
sorted_ = np.sort(samp)

plt.rcParams[u'font.sans-serif'] = ['simhei']
plt.rcParams['axes.unicode_minus']=False
fig = plt.figure()
plt.subplot(121)
plt.axis("equal")
plt.scatter(sorted_,y)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel("落点偏差",size=20)
plt.ylabel("标准正态分布",size=20)
plt.title("标准正态分布Q-Q图",size=20)

for i in range(len(y)):
    y[i] = 149.725 + 49.59 * y[i]
print(y)
print(sorted_)
plt.subplot(122)
plt.axis("equal")
plt.scatter(sorted_,y)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel("落点偏差",size=20)
plt.ylabel("拟合正态分布",size=20)
plt.title("拟合正态分布Q-Q图",size=20)

plt.show()
