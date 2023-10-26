from scipy import stats
import random

random.seed(12345)

Ws = []
for i in range(100):
    X = random.normalvariate(100,10)
    Y = random.normalvariate(300,15) 
    Z = random.normalvariate(40,8) 
    W = (X+Y)/Z
    Ws.append(W)

import matplotlib.pyplot as plt

plt.rcParams[u'font.sans-serif'] = ['simhei']
plt.rcParams['axes.unicode_minus'] = False

hist = plt.hist(x = Ws, # 指定绘图数据
#    bins = int((max(Ws) - min(Ws)) / 3), # 指定直方图中条块的个数
#    range = (min(Ws),max(Ws)),
    color = 'steelblue', # 指定直方图的填充色
    edgecolor = 'black' # 指定直方图的边框色
)

interval = (hist[1][1] - hist[1][0]) / 2

for i in range(len(hist[0])):
    plt.annotate(s=int(hist[0][i]), xy=(hist[1][i] + interval / 2, hist[0][i]),fontsize=20)

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
# 添加x轴和y轴标签
plt.xlabel('W',fontsize=20)
plt.ylabel('发生次数',fontsize=20)
# 添加标题
plt.title('W=(X+Y)/Z',fontsize=20)
plt.legend(loc='best', frameon=False,fontsize=20)
# 显示图形
plt.show()