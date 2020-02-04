# Our usual imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
plt.style.use('fivethirtyeight')

# Our data is from this book:
#
# > Samuel P. Oliner and Pearl M. Oliner (1992) "The Altruistic Personality:
# > Rescuers of Jews in Nazi Europe". Free Press, New York. ISBN 0-02923829-3.

# Load the table
party_tab = pd.read_csv('oliner_tab6_8a_1.csv')
party_tab

# Replace the numerical index with the party_yn labels.
party_tab = party_tab.set_index('party_yn')

# ## Cleaning up the table
#
# We start by selecting the data we need from the original table.

bystander_tab = party_tab.loc[['Yes', 'No'], ['rescuers', 'bystanders']]
bystander_tab

# Make the 290 respondent labels.
respondent = np.repeat(['rescuer', 'bystander'], bystander_tab.sum())
# Show the first 10.
print('First 10:', respondent[:10])
# Show the last 10.
print('Last 10:', respondent[-10:])

# Make the 290 Yes No labels.
party_yn = np.repeat(['Yes', 'No'], bystander_tab.transpose().sum())
# Show the first 10.
print('First 10:', party_yn[:10])
# Show the last 10.
print('Last 10:', party_yn[-10:])

# Next we shuffle the Yes, No labels randomly:

np.random.shuffle(party_yn)

# We need more random samples to see if the fake value is often as small as the real value.  If so, then the ideal world, where the association between rescuer / bystander and Yes / No is random, is a reasonable explanation of what we see, and we might not want to investigate these data much further.
#
# Unfortunately, `pd.crosstab` is horribly slow, so we need to drop our usual number of iterations to 1000 to keep the run-time down.

counts = np.zeros(1000)
for i in np.arange(1000):
    np.random.shuffle(party_yn)
    fake_tab = pd.crosstab(party_yn, respondent)
    counts[i] = fake_tab.loc['Yes', 'bystander']
counts[:10]

# Here is our *sampling distribution* from sampling in the ideal world:

plt.hist(counts);

# How unusual is the actual value, in this ideal world?

# Proportion of times we see ideal world sample >= actual value.
actual_y_by = bystander_tab.loc['Yes', 'bystanders']
p_lte = np.count_nonzero(counts <= actual_y_by) / len(counts)
print(p_lte)
