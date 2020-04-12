""" Make random sample from police written exam results
"""

import pandas as pd

n = 50
desired = 91.2
df = pd.read_csv('nyc_police_exam_feb_2019.csv')
for i in range(1000):
    sample = df.sample(n, replace=True)
    stat = sample['Adj. FA'].mean()
    if stat > desired:
        break
print('Statistic', stat, 'at iteration', i)
sample.to_csv('nyc_police_exam_2019_sample.csv', index=None)
