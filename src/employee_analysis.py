#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# # Employee Data Analysis
# 
# ## 1. Introduction
# Analysis of employee data using Python.
# 
# ## 2. Data Loading
# Loading employee records using Pandas.
# 
# ## 3. Data Analysis
# Analyzing salaries and departments.
# 
# ## 4. Conclusion
# Summary of employee data findings.

# In[3]:


import pandas as pd
import numpy as np

df = pd.read_csv("../../task2/employees.csv")

print(df.head())
print("\nAverage salary:", df["salary"].mean())

print("\nDepartment counts:")
print(df["department"].value_counts())


# In[4]:


get_ipython().run_line_magic('timeit', 'df["salary"].mean()')


# In[ ]:




