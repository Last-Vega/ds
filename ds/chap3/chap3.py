#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 以下のライブラリを使うので、あらかじめ読み込んでおいてください
import numpy as np
import scipy as sp
import pandas as pd
from pandas import Series, DataFrame

# 可視化ライブラリ
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
sns.set()
get_ipython().run_line_magic('matplotlib', 'inline')

# 小数第3位まで表示
get_ipython().run_line_magic('precision', '3')


# In[2]:


from sklearn import linear_model


# In[3]:


student_data_math = pd.read_csv('student-mat.csv')


# In[4]:


cd chap3


# In[5]:


student_data_math = pd.read_csv('student-mat.csv')


# In[6]:


student_data_math.head()


# In[7]:


student_data_math.head(10)


# In[8]:


# データの読み込み
# 区切りに";"がついているので注意
student_data_math = pd.read_csv('student-mat.csv', sep=';')
student_data_math.head()


# In[9]:


student_data_math.groupby('sex')['age'].mean()


# In[10]:


student_data_math.groupby('sex')['G3'].mean()


# In[11]:


student_data_math.groupby('sex')['absences'].mean()


# In[13]:


student_data_math.groupby('address')['G3'].mean()


# In[14]:


plt.boxplot(student_data_math['G1'])
plt.grid(True)


# In[15]:


plt.boxplot([student_data_math['G1'], student_data_math['G2'], student_data_math['G3']])
plt.grid(True)


# In[16]:


student_data_math['absences'].std() / student_data_math['absences'].mean()


# In[17]:


student_data_math.std() / student_data_math.mean()


# In[18]:


data_por = pd.read_csv("student-por.csv")
data_por.head()


# In[19]:


data_por = pd.read_csv("student-por.csv", sep = ";")
data_por.head()


# In[20]:


print("平均値:", data_por.mean())


# In[21]:


print("中央値:", data_por.median())


# In[22]:


print("最頻値:", data_por.mode())


# In[23]:


print('最頻値：', student_data_math['absences'].mode())


# In[24]:


print("最頻値:", data_por["absences"].mode())


# In[25]:


print("中央値:", data_por.median())


# In[26]:


data_por.describe()


# In[27]:


pd.merge("sudent-mat.csv", "student-por.csv")


# In[41]:


student_data_por = pd.read_csv("student-por.csv", sep = ";")
student_dara_math = pd.read_csv("student-mat.csv", sep = ";")
student_data_merge = pd.merge(student_data_math
                            , student_data_por
                            , on = ['school','sex','age','address','famsize','Pstatus','Medu','Fedu','Mjob','Fjob','reason','nursery','internet']
                            , suffixes = ('_math', '_por')
                            )
student_data_merge.describe()


# In[42]:


sns.pairplot(student_data_merge[['Medu', 'Fedu', 'G3_math']])
plt.grid(True)


# In[ ]:
