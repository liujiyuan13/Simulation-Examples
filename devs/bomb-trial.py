import Bomb

data = Bomb.Bomb()

import matplotlib.pyplot as plt

plt.rcParams[u'font.sans-serif'] = ['simhei']
plt.rcParams['axes.unicode_minus'] = False

plt.axis("equal")
plt.scatter(data[0],data[1],color = 'red',label='落点',s=100,marker='o')
plt.scatter(Bomb.boundary[0],Bomb.boundary[1],color = 'steelblue',s=150,marker=',')
plt.plot(Bomb.boundary[0],Bomb.boundary[1],color = 'steelblue',linewidth=3.0,label='弹药库建筑')

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
# 添加x轴和y轴标签
plt.xlabel('Y',fontsize=20)
plt.ylabel('X',fontsize=20)
# 添加标题
plt.title('命中次数' + str(data[2]),fontsize=20)
plt.legend(loc='best', frameon=False,fontsize=20)
# 显示图形
plt.show()