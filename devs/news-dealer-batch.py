import NewsDealer
import matplotlib.pyplot as plt

profitsData = []
for i in range(400):
    profitsData.append(NewsDealer.MonthProfit()[1])

plt.rcParams[u'font.sans-serif'] = ['simhei']
plt.rcParams['axes.unicode_minus']=False

hist = plt.hist(x = profitsData, # 指定绘图数据
    bins = 10, # 指定直方图中条块的个数
    range = (min(profitsData),max(profitsData)),
    color = 'steelblue', # 指定直方图的填充色
    edgecolor = 'black' # 指定直方图的边框色
)
interval = (hist[1][1] - hist[1][0]) / 2

for i in range(len(hist[0])):
    plt.annotate(s=int(hist[0][i]), xy=(hist[1][i] + interval / 2, hist[0][i]),fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
# 添加x轴和y轴标签
plt.xlabel('利润',fontsize=20)
plt.ylabel('发生次数',fontsize=20)
# 添加标题
plt.title('利润分布直方图（批量运行次数400）',fontsize=20)
# 显示图形
plt.show()