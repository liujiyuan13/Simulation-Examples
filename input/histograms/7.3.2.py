import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt

plt.rcParams[u'font.sans-serif'] = ['simhei']
plt.rcParams['axes.unicode_minus']=False

# 读取xls（绝对路径）
data = pd.read_excel('./input/datas/arrivals.xls')
#查看所有的值
print(data.values)

a = plt.bar(data['Arrivals per Period'].values,data['Frequency'].values)

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
# 添加x轴和y轴标签
plt.xlabel('到达数量',fontsize=20)
plt.ylabel('频数',fontsize=20)
# 添加标题
plt.title('到达数量直方图',fontsize=20)
# 显示图形
plt.show()

