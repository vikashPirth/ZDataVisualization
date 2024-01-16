#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 13:00:20 2024

@author: vikashpirthiani
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pickle 

with open('iris.pickle', 'rb') as f :
    iris = pickle.load(f)
    

sepal_length = iris['data'][:, 0]
sepal_width = iris['data'][:, 1]
petal_length = iris['data'][:, 2]
petal_width = iris['data'][:, 3]
classes = iris['target']

fig, axes = plt.subplots(2,2)
sns.scatterplot(x=sepal_length, y=sepal_width, hue=classes, legend=False, ax=axes[0,0])
axes[0,0].set_xlabel('Sepal length (cm)')
axes[0,0].set_ylabel('Sepal width (cm)')

sns.scatterplot(x=petal_length, y=petal_width, hue=classes, legend=False, ax=axes[0,1])
axes[0,1].set_xlabel('Petal length (cm)')
axes[0,1].set_ylabel('Petal width (cm)')

sns.scatterplot(x=sepal_length, y=petal_length, hue=classes, legend=False, ax=axes[1,0])
axes[1,0].set_xlabel('Sepal length (cm)')
axes[1,0].set_ylabel('Petal length (cm)')

sns.scatterplot(x=sepal_width, y=petal_width, hue=classes, legend=False, ax=axes[1,1])
axes[1,1].set_xlabel('Sepal width (cm)')
axes[1,1].set_ylabel('Petal width (cm)')


fig.suptitle('Iris Datase')
plt.show()