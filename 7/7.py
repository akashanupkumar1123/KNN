#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:





# In[3]:


df = pd.read_csv("Classified Data",index_col=0)


# In[4]:


df.head()


# In[ ]:





# In[5]:


from sklearn.preprocessing import StandardScaler


# In[6]:


scaler = StandardScaler()


# In[ ]:





# In[7]:


scaler.fit(df.drop('TARGET CLASS',axis=1))


# In[ ]:





# In[8]:


scaled_features = scaler.transform(df.drop('TARGET CLASS',axis=1))


# In[ ]:





# In[9]:


df_feat = pd.DataFrame(scaled_features,columns=df.columns[:-1])
df_feat.head()


# In[ ]:





# In[10]:


from sklearn.model_selection import train_test_split


# In[11]:


X_train, X_test, y_train, y_test = train_test_split(scaled_features,df['TARGET CLASS'],
                                                    test_size=0.30)


# In[ ]:





# In[12]:


from sklearn.neighbors import KNeighborsClassifier


# In[ ]:





# In[13]:


knn = KNeighborsClassifier(n_neighbors=1)


# In[ ]:





# In[14]:


knn.fit(X_train,y_train)


# In[ ]:





# In[15]:


pred = knn.predict(X_test)


# In[ ]:





# In[16]:


from sklearn.metrics import classification_report,confusion_matrix


# In[ ]:





# In[17]:


print(confusion_matrix(y_test,pred))


# In[ ]:





# In[18]:


print(classification_report(y_test,pred))


# In[ ]:





# In[20]:


error_rate = []

# Will take some time
for i in range(1,40):
    
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train,y_train)
    pred_i = knn.predict(X_test)
    error_rate.append(np.mean(pred_i != y_test))


# In[ ]:





# In[21]:


plt.figure(figsize=(10,6))
plt.plot(range(1,40),error_rate,color='blue', linestyle='dashed', marker='o',
         markerfacecolor='red', markersize=10)
plt.title('Error Rate vs. K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')


# In[ ]:





# In[22]:


# FIRST A QUICK COMPARISON TO OUR ORIGINAL K=1
knn = KNeighborsClassifier(n_neighbors=1)

knn.fit(X_train,y_train)
pred = knn.predict(X_test)

print('WITH K=1')
print('\n')
print(confusion_matrix(y_test,pred))
print('\n')
print(classification_report(y_test,pred))


# In[ ]:





# In[ ]:





# In[23]:


# NOW WITH K=23
knn = KNeighborsClassifier(n_neighbors=23)

knn.fit(X_train,y_train)
pred = knn.predict(X_test)

print('WITH K=23')
print('\n')
print(confusion_matrix(y_test,pred))
print('\n')
print(classification_report(y_test,pred))


# In[ ]:




