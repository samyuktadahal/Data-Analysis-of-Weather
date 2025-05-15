#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[5]:


df = pd.read_csv(r"C:\Users\ASUS\OneDrive\Desktop\Python Data Analysis\Data Analysis of Weather\1. Weather Data.csv")
df


# In[6]:


df.info()


# In[7]:


#First 5 Rows
df.head()


# In[8]:


df.columns


# In[9]:


df.dtypes


# In[10]:


df.shape


# In[11]:


df.index


# In[12]:


#Last 5 Rows
df.tail()


# In[14]:


df.nunique()
# it shows that Data/Time has 8784 values, Temp_c has 533 and so on.


# In[15]:


df['Weather'].unique()
#it shows all unique weathers


# In[16]:


df['Weather'].nunique()
# it has 50 unique weather values from 8K entries.


# In[17]:


df['Weather'].value_counts()


# In[18]:


df.count()
#it shows non of the columns has empty cells


# In[19]:


df.isnull().sum()
#if there is any null value in any column


# In[20]:


df


# In[21]:


df.describe()


# In[22]:


#FIND ALL UNIQUE "WIND SPEED" VALUES FROM THE DATA.

df['Wind Speed_km/h'].unique()


# In[23]:


df['Wind Speed_km/h'].nunique()
#There are 34 unique values in wind speed column


# In[24]:


df['Wind Speed_km/h'].value_counts()
# 830 times, the wind speed is 9 km/h


# In[26]:


#FIND THE NUMBER OF TIMES WHEN THE WEATHER IS EXACTLY CLEAR
df[df['Weather']=='Clear']


# In[27]:


df[df['Weather']== 'Clear'].count()


# In[28]:


df[df['Weather']== 'Clear'].nunique()


# In[29]:


#FIND OUT THE NUMBER OF TIMES WHEN THE WIND SPEED WAS EXACTLY 4km/h

df[df['Wind Speed_km/h']== 4]


# In[32]:


df[df['Wind Speed_km/h']== 4].nunique()


# In[33]:


df.groupby('Wind Speed_km/h').get_group(4)


# In[34]:


#MIN, MAX, MEAN AND OTHERS

#Minimum Temperature
df['Temp_C'].min()


# In[35]:


#Maximum Temperature
df['Temp_C'].max()


# In[36]:


#Mean Temperature
df['Temp_C'].mean()


# In[37]:


df.groupby('Weather').agg({'Temp_C':['min', 'max', 'mean', 'std']})


# In[39]:


g1= df.groupby(['Weather', 'Wind Speed_km/h']).agg({'Temp_C':['min', 'max', 'mean', 'std']})
g1
# It groups table on basis of Weather, then Wind speed and showed min, max, mean and std bases on grouped result.


# In[40]:


df.describe()
# describe() return all the aggregate function values like min, max, mean, std etc


# In[41]:


#RENAME THE COLUMN NAME 'Weather' OF THE DATAFRAME TO 'Weather Condition'

df1= df.rename(columns={'Weather':'Weather Condition'})
df1
# renaming column name 'Weather' to 'Weather Condition'


# In[42]:


#FIND ALL THE INSTANCES WHEN 'Wind Speed is above 24 and visibility is 25.'
df[(df['Wind Speed_km/h']>24) & (df['Visibility_km']==25)]


# In[43]:


df[(df['Wind Speed_km/h']>24)& (df['Visibility_km']==25)].describe()


# In[45]:


#FIND THE MIN, MAX, MEAN VALUE OF EACH COLUMN AGAINST EACH 'Weather'

df.groupby('Weather').min(numeric_only= True)


# In[46]:


df.groupby('Weather').max(numeric_only= True)


# In[47]:


df.groupby('Weather').mean(numeric_only= True)


# In[48]:


df.groupby('Weather').describe()


# In[50]:


#SHOW ALL THE RECORDS WHERE 'Weather' IS Fog.
df[df['Weather']== 'Fog'] 


# In[51]:


df[(df['Weather']=='Fog') | (df['Weather']=='Rain') ]


# In[52]:


#FIND ALL THE INSTANCE WHERE 'Weather is Clear' OR 'Visibility is above 35'
df[(df['Weather']=='Clear') | (df['Visibility_km']>35)]


# In[54]:


#FIND INSTANCES WHEN 'Weather is Clear' and 'Relative Humidity is greater than 50' and 'Visibility is above 40'

df[((df['Weather']=='Clear')& (df['Rel Hum_%']>50)) | (df['Visibility_km']>40)]


# In[55]:


df


# In[59]:


#TEMPERATURE TRENDS

#Convert 'Date/Time' column to datetime format.
df['Date/Time']= pd.to_datetime(df['Date/Time'])

#plot temperature trends over time
plt.plot(df['Date/Time'], df['Temp_C'])
plt.title('Temperature Trends Over Time')
plt.xlabel('Date/Time')
plt.ylabel('Temperature(Celcius)')


# In[60]:


df.dtypes


# In[62]:


#WEATHER CONDITIONS

df['Weather'].value_counts()


# In[64]:


#Count frequency of each weather condition
Weather_counts= df['Weather'].value_counts()

Weather_counts.plot(kind= 'bar', color= 'green')
plt.title('Distribution of Weather Conditions')
plt.xlabel('Weather')
plt.ylabel('Frequency')
#plt.figure(figsize=(20,7))


# In[66]:


#EXTREME EVENTS

extreme_events= df[df['Temp_C']>30]
print("Extreme Temperature Events: ")
print(extreme_events[['Date/Time','Temp_C']])


# In[67]:


df[df['Temp_C']>30]


# In[68]:


df['Temp_C'].max()


# In[69]:


df


# In[ ]:




