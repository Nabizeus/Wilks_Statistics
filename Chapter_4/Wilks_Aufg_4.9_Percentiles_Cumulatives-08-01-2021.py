#!/usr/bin/env python
# coding: utf-8

# In[49]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.style.use('classic')
from scipy.stats import norm
from scipy import special
import numpy as np


# Ithaca July precipitation data from Wilks, Newyork, 1951-1980 (inches)
data_series = np.array([4.17,5.61,3.88,1.55,2.30,5.58,5.58,5.14,4.52,1.53,4.24,1.18,3.17,
        4.72,2.17,2.17,3.94,0.95,1.48,5.68,4.25,3.66,2.12,1.24,3.64,8.44,5.20,2.33,2.18,3.43])
years = np.arange(1951,1981,1)


mean_data=np.mean(data_series)
standard_dev_data=np.std(data_series)
log_data=np.log(data_series)
mean_log_data=np.mean(log_data)
standard_dev_log_data=np.std(log_data)
median_log_data=np.median(log_data)


print('Raw Data:', data_series)
print('Mean of Raw Data:', mean_data)
print('Stdev of Raw Data:', standard_dev_data)
print('Logarithmic transformation of Raw Data:', log_data)
print('Mean of Log of Raw Data:', mean_log_data)
print('Stdev of Log of Raw Data:', standard_dev_log_data)
print('Median of Log of Raw Data:', median_log_data)


# In[50]:


np.percentile(log_data,2.5)
np.percentile(data_series,2.5)


# In[46]:


#from statistics import quantiles
#In [25]: quants=quantiles(data_series,n=100)

#In [26]: pd.Series(quants)


# In[34]:


plt.hist(log_data,bins=6)


# In[52]:


z = (7 - mean_data) / standard_dev_data

print('7 inch z-score:', z)

# We'll bring in scipy to do the calculation of probability from the Z-table
import scipy.stats as st
print('z-score cumulative probability:',st.norm.cdf(z))

# We need the probability from the right side, so we'll flip it!
print('1-(cumulative probability of z-score):',1 - st.norm.cdf(z))


# In[53]:


z = (np.log(7) - mean_log_data) / standard_dev_log_data

print('log(7) inch z-score:', z)

# We'll bring in scipy to do the calculation of probability from the Z-table
import scipy.stats as st
print('z-score cumulative probability:',st.norm.cdf(z))

# We need the probability from the right side, so we'll flip it!
print('1-(cumulative probability of z-score):',1 - st.norm.cdf(z))


# In[ ]:




