import numpy as np
import pandas as pd
from scipy import stats

data = pd.read_excel('./input/datas/life.xls')
samp = data['life'].values

d = {'a': list(range(8)),'b': list(range(8)), 'O': list(range(8)),'E':list(range(8))}
df = pd.DataFrame(d)
print(df)

u = data['life'].mean()
print(u)
expon = stats.expon(scale=u)

df['E'] = 1 / 8 * 50
startX = 0
df.iloc[0,0] = 0
for index in range(len(df['E'])):
    df.iloc[index,0] = startX
    if(index == 7):
        df.iloc[index,1] = float('inf')
    else:
        df.iloc[index,1] = expon.ppf((index + 1) * 0.125)
    startX = df.iloc[index,1]
    df.iloc[index,2] = 0
print(df)
for index in range(len(data['life'])):
    sample = data.iloc[index,0]
    for index2 in range(len(df['E'])):
        if(sample >= df.iloc[index2,0] and sample <= df.iloc[index2,1]):
            df.iloc[index2,2] += 1
print(df)

print(stats.chisquare(df['O'], df['E'], ddof=6))