import numpy as np
import pandas as pd

#Part1
df = pd.read_csv("Day2_input.csv",header = None, sep = ' ')
sum_rep = 0
safe_rep = np.zeros(len(df.values))
def is_rep_safe(rpt:np.array):
    return (np.all(np.diff(rpt) <= -1) and np.all(np.diff(rpt) >= -3)) \
        or (np.all(np.diff(rpt) >= 1) and np.all(np.diff(rpt) <= 3))

for i in range(0,len(df.values)):
    rpt = (df.values[i])[~np.isnan(df.values[i])]
    is_safe =is_rep_safe(rpt)
    sum_rep+= is_safe
    safe_rep[i] = is_safe
print(sum_rep) #442

#Part2
mis_df = df[safe_rep==0]
for i in range(0,len(mis_df.values)):
    rpt = (df.values[i])[~np.isnan(df.values[i])]
    for j in range(0,len(rpt)):
        cor_rpt = np.delete(rpt, j) #clear but slow, maybe possible to use diff_rpt to accelerate
        if is_rep_safe(cor_rpt):
            sum_rep+=1
            break
print(sum_rep)
