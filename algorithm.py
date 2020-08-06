#!/usr/bin/env python
# coding: utf-8

# In[6]:


import requests, json, time

import numpy
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense


# In[55]:


f = open('data.json')

data = json.load(f)

arr = data['data']

mat = numpy.array(arr)

numpy.random.shuffle(mat)

endpoint = int(len(mat) * 0.9)
test = mat[endpoint:]

mat = mat[1:endpoint]

features = mat[:, 0:10]
results = mat[:,10]


featureTest = test[:, 0:10]
resultTest = test[:, 10]



                            


# In[56]:


#Create Model
model = Sequential()
model.add(Dense(20, input_dim=10, activation='relu'))
model.add(Dense(20, activation='relu'))
model.add(Dense(20, activation='relu'))
model.add(Dense(1, activation='sigmoid'))


# In[57]:


#compile
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


# In[58]:


#fit model and evaluate
model.fit(features, results, epochs=200, batch_size=32, validation_split = 0.2)
_, taccuracy = model.evaluate(features, results)
print('Accuracy: %.2f' % (taccuracy*100))
_, accuracy = model.evaluate(featureTest, resultTest)
print('Accuracy: %.2f' % (accuracy*100))


# In[ ]:





# In[ ]:




