""" Make random sample from police written exam results
"""

import pandas as pd

df = pd.read_csv('nyc_police_exam_feb_2019.csv')
df['Adj. FA'] = df['Adj. FA'].round()
med = 0
while med < 92:
    sample = df.sample(50, replace=True)
    med = sample['Adj. FA'].median()
print('Median', sample['Adj. FA'].median())
sample.to_csv('nyc_police_exam_2019_sample.csv', index=None)
