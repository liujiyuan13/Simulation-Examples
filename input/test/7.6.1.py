import numpy as np
import pandas as pd
from scipy import stats

d = {'arrivals': list(range(12)), 'frequency':[12,10,19,17,10,8,7,5,5,3,3,1]}
df = pd.DataFrame(d)
print(df)

df.iloc[7,1]=17
df=df[:8]
print(df)

df.iloc[1,1]=22
df=df[1:]

print(df)

Poiss = stats.poisson(mu=3.64)
df['prop']=Poiss.pmf(df['arrivals'])
df.iloc[0, 2] = Poiss.cdf(1)
# 修正大于7对应的概率
df.iloc[6, 2] = 1 - Poiss.cdf(6)

print(df)

df['t_frequency']=100*df['prop']
print(df)

print(stats.chisquare(df['frequency'], df['t_frequency'], ddof=5))