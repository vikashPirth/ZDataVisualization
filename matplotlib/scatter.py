#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 13:00:20 2024

@author: vikashpirthiani
"""

import matplotlib.pyplot as plt
import pickle 

with open('iris.pickle', 'rb') as f :
    iris = pickle.load(f)
    

sepal_length = iris['data'][:, 0]
sepal_width = iris['data'][:, 1]
petal_length = iris['data'][:, 2]
petal_width = iris['data'][:, 3]
classes = iris['target']

fig, axes = plt.subplots(2,2)
axes[0,0].scatter(sepal_length, sepal_width, c=classes)
axes[0,0].set_xlabel('Sepal length (cm)')
axes[0,0].set_ylabel('Sepal width (cm)')

axes[0,1].scatter(petal_length, petal_width, c=classes)
axes[0,1].set_xlabel('Petal length (cm)')
axes[0,1].set_ylabel('Petal width (cm)')

axes[1,0].scatter(sepal_length, petal_length, c=classes)
axes[1,0].set_xlabel('Sepal length (cm)')
axes[1,0].set_ylabel('Petal length (cm)')

axes[1,1].scatter(sepal_width, petal_width, c=classes)
axes[1,1].set_xlabel('Sepal width (cm)')
axes[1,1].set_ylabel('Petal width (cm)')


fig.suptitle('Iris Datase')
plt.show()