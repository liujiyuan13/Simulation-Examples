import NewsDealer
import matplotlib.pyplot as plt

profitsData = NewsDealer.MonthProfit()[0]

plt.rcParams[u'font.sans-serif'] = ['simhei']
plt.rcParams['axes.unicode_minus'] = False

plt.hist(x = profitsData, # 指定绘图数据
    bins = 10, # 指定直方图中条块的个数
    range = (min(profitsData),max(profitsData)),
    color = 'steelblue', # 指定直方图的填充色
    edgecolor = 'black' # 指定直方图的边框色
)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
# 添加x轴和y轴标签
plt.xlabel('利润',fontsize=20)
plt.ylabel('发生次数',fontsize=20)
# 添加标题
plt.title('利润分布直方图（20天）',fontsize=20)
# 显示图形
plt.show()