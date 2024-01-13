#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 00:40:13 2024

@author: vikashpirthiani
"""

import matplotlib.pyplot as plt

import pickle

with open('fruit-sales.pickle','rb') as f:
    data = pickle.load(f)
    

fruit, num_sold = zip(*data)

bar_coords = range(len(fruit)) 

plt.bar(bar_coords, num_sold)

plt.show()
