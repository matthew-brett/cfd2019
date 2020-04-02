""" Make random sample from Havana mathematics results
"""

import pandas as pd

df = pd.read_csv('havana_math_2019.csv')
sample = df.sample(50, replace=True)
sample.to_csv('havana_math_2019_sample.csv', index=None)
