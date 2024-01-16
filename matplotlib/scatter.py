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
classes = iris['target']


plt.scatter(sepal_length, sepal_width, c=classes)
plt.xlabel('Sepal length (cm)')
plt.ylabel('Sepal length (cm)')
plt.title('Iris data: Sepal length v. widthx')
plt.show()