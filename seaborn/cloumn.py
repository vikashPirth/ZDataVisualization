#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 00:40:13 2024

@author: vikashpirthiani
"""

import matplotlib.pyplot as plt
import seaborn as sns

import pickle

with open('fruit-sales.pickle','rb') as f:
    data = pickle.load(f)
    

fruit, num_sold = zip(*data)
fruit = list(fruit)
num_sold= list(num_sold)

axes = sns.barplot(x = fruit, y=num_sold)
axes.set_title("Number of fruilts solid (2017)")
axes.set_ylabel("Number of Fruit (millions")


plt.show()