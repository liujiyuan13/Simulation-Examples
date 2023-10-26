from scipy.stats import kstest
import numpy as np
import pandas as pd
from scipy import stats

data = pd.read_excel('./input/datas/intervals.xls')
samp = data['Intervals'].values
print(samp)
u = data['Intervals'].mean()
print(u)
e = stats.expon(scale=u)
test_stat = kstest(samp, e.cdf)
print(test_stat)