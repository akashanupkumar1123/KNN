#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[ ]:





# In[3]:


df = pd.read_csv('gene_expression.csv')


# In[4]:


df.head()


# In[ ]:





# In[5]:


sns.scatterplot(x='Gene One', y='Gene Two', hue='Cancer Present', data=df, alpha=0.7)


# In[ ]:





# In[8]:


sns.scatterplot(x='Gene One', y='Gene Two', hue='Cancer Present', data=df)
plt.xlim(2,6)
plt.ylim(3,10)
plt.legend(loc=(1.1,0.5))


# In[ ]:





# In[10]:


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


# In[ ]:





# In[11]:


X = df.drop('Cancer Present', axis=1)
y = df['Cancer Present']


# In[ ]:





# In[12]:


X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3,random_state=42)


# In[ ]:





# In[13]:


scaler = StandardScaler()


# In[ ]:





# In[14]:


scaled_X_train = scaler.fit_transform(X_train)
scaled_X_test = scaler.transform(X_test)


# In[ ]:





# In[15]:


from sklearn.neighbors import KNeighborsClassifier


# In[ ]:





# In[16]:


knn_model = KNeighborsClassifier(n_neighbors=1)


# In[ ]:





# In[17]:


knn_model.fit(scaled_X_train,y_train)


# In[ ]:





# In[18]:


full_test = pd.concat([X_test,y_test],axis=1)


# In[ ]:





# In[19]:


len(full_test)


# In[ ]:





# In[20]:


sns.scatterplot(x='Gene One',y='Gene Two',hue='Cancer Present',
                data=full_test,alpha=0.7)


# In[ ]:





# In[21]:


y_pred = knn_model.predict(scaled_X_test)


# In[ ]:





# In[22]:


from sklearn.metrics import classification_report,confusion_matrix,accuracy_score


# In[ ]:





# In[23]:


accuracy_score(y_test,y_pred)


# In[ ]:





# In[24]:


confusion_matrix(y_test,y_pred)


# In[ ]:





# In[25]:


print(classification_report(y_test,y_pred))


# In[ ]:





# In[26]:


test_error_rates = []


for k in range(1,30):
    knn_model = KNeighborsClassifier(n_neighbors=k)
    knn_model.fit(scaled_X_train,y_train) 
   
    y_pred_test = knn_model.predict(scaled_X_test)
    
    test_error = 1 - accuracy_score(y_test,y_pred_test)
    test_error_rates.append(test_error)


# In[ ]:





# In[27]:


plt.figure(figsize=(10,6),dpi=200)
plt.plot(range(1,30),test_error_rates,label='Test Error')
plt.legend()
plt.ylabel('Error Rate')
plt.xlabel("K Value")


# In[ ]:





# In[ ]:





# In[28]:


scaler = StandardScaler()


# In[ ]:





# In[29]:


knn = KNeighborsClassifier()


# In[ ]:





# In[30]:


knn.get_params().keys()


# In[ ]:





# In[31]:


# Highly recommend string code matches variable name!
operations = [('scaler',scaler),('knn',knn)]


# In[ ]:





# In[32]:


from sklearn.pipeline import Pipeline


# In[ ]:





# In[33]:


pipe = Pipeline(operations)


# In[ ]:





# In[34]:


from sklearn.model_selection import GridSearchCV


# In[ ]:





# In[35]:


k_values = list(range(1,20))


# In[36]:


k_values


# In[38]:


param_grid = {'knn__n_neighbors': k_values}


# In[39]:


full_cv_classifier = GridSearchCV(pipe,param_grid,cv=5,scoring='accuracy')


# In[ ]:





# In[40]:


# Use full X and y if you DON'T want a hold-out test set
# Use X_train and y_train if you DO want a holdout test set (X_test,y_test)
full_cv_classifier.fit(X_train,y_train)


# In[ ]:





# In[41]:


full_cv_classifier.best_estimator_.get_params()


# In[ ]:





# In[42]:


full_cv_classifier.cv_results_.keys()


# In[43]:


len(k_values)


# In[ ]:





# In[44]:


full_cv_classifier.cv_results_['mean_test_score']


# In[ ]:





# In[45]:


len(full_cv_classifier.cv_results_['mean_test_score'])


# In[ ]:





# In[46]:


scaler = StandardScaler()
knn14 = KNeighborsClassifier(n_neighbors=14)
operations = [('scaler',scaler),('knn14',knn14)]


# In[ ]:





# In[47]:


pipe = Pipeline(operations)


# In[48]:


pipe.fit(X_train,y_train)


# In[ ]:





# In[49]:


pipe_pred = pipe.predict(X_test)


# In[ ]:





# In[50]:


print(classification_report(y_test,pipe_pred))


# In[51]:


single_sample = X_test.iloc[40]


# In[ ]:





# In[52]:


single_sample


# In[ ]:





# In[53]:


pipe.predict(single_sample.values.reshape(1, -1))


# In[ ]:





# In[54]:


pipe.predict_proba(single_sample.values.reshape(1, -1))


# In[ ]:




