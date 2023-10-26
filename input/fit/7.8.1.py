from scipy import stats
from fitter import Fitter
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('./input/datas/cep.xlsx')
samp = data['落点偏差'].values
# 拟合分布
#f = Fitter(samp)  # 创建Fitter类
f = Fitter(samp, distributions=['norm'], bins='auto')
f.fit()  # 调用fit函数拟合分布
print(f.summary())  # 输出拟合结果
print(f.fitted_param['norm'])
#f.get_best()
f.hist()
#f.plot_pdf()
plt.show()

