#!/usr/bin/env python
# coding: utf-8

# In[166]:


print("Name : ")
print("We will be cleaning the big data and make a comparison to show who has a healthier heart smokers OR non smokers, uisng a line graph")
print("Also we will be deriviring which age group has the high chances of coronary heart disease in 10 years")


# # Task 1 - Plot a line graph to show the difference between heart rate of smokers and non smokers

# In[7]:


#Import libraries

#read the csv
import pandas as pd
import numpy as numpy
from matplotlib import pyplot as plt
df = pd.read_csv('framingham.csv')
df


# In[9]:


#Filter and make a new dataframe for non smokers
non_smokers = df.loc[df['currentSmoker']==0]
non_smokers


# In[11]:


#Group by age column and find average heart rate at different age
group_non_smokers = non_smokers.groupby('age')['heartRate'].mean().reset_index()
group_non_smokers


# In[12]:


#Filter and make a new dataframe for smokers
smokers = df.loc[df['currentSmoker']==1]
smokers


# In[13]:


#Group by age column and find average heart rate at different age
group_smokers = smokers.groupby('age')['heartRate'].mean().reset_index()
group_smokers


# In[21]:


#Plot a line graph to show the heart rate of smokers vs non smokers
label = group_age['age']
value = group_age['TenYearCHD']

fig = plt.subplots(figsize=(19,8))

plt.plot(label, value, label = "Chance of CHD in next ten years" , linewidth=3.0)
plt.xlabel('age')
plt.xticks(rotation='vertical')

plt.ylabel('Chance of CHD in next ten years')

plt.title('Chance of CHD in next ten years as per age ', fontsize=20)

plt.legend()

plt.show()


# Conslusion - 

# # Task 2 - Which age group have high chances of having coronary heart disease in 10 years

# In[14]:


#Read the csv

#Filter and make a new dataframe for those who has chances of having coronary heart disease in 10 years
coronary_heart_disease = df.loc[df['TenYearCHD']==1]
coronary_heart_disease


# In[15]:


#Group by age column and count the rows of TenYearCHD column
group_age = coronary_heart_disease.groupby('age')['heartRate'].mean().reset_index()
group_age


# In[9]:


#Plot a line graph to show total number of people having a chance of coronary heart disease in 10 years
label = group_by_date['acq_date']
value = group_by_date['confidence']

fig = plt.subplots(figsize=(19,8))

plt.plot(label, value, label = "Average confidence as per date" , linewidth=3.0)
plt.xlabel('Dates')
plt.xticks(rotation='vertical')

plt.ylabel('confidence')

plt.title('Average confidence as per date', fontsize=20)impport

plt.legend()

plt.show()


# Conslusion - 

# In[ ]:




