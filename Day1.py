import numpy as np
import pandas as pd
#Part 1
df = pd.read_csv("Day1_input.csv",header = None,sep='   ')
a = np.array(df.iloc[:,0])
b = np.array(df.iloc[:,1])
a.sort()
b.sort()
print("Distance =",sum(abs(a-b))) #1970720

#Part 2
a_ele = set(a)
sim_list = [np.count_nonzero(a==i)*i*np.count_nonzero(b==i) for i in a_ele]
sim_count = sum(sim_list)
print("Similarity =",sim_count) #17191599