#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 23:55:18 2024

@author: vikashpirthiani
"""


import matplotlib.pyplot as plt 
import pickle 

with open('prog-langs-popularity.pickle', 'rb') as f:
    data = pickle.load(f)
    
    
languages, rankings = zip(*data)


for i in range(len(languages)):
    years, ranks = zip(*rankings[i])

    plt.plot(years, ranks)

plt.xlabel('year')
plt.ylabel('ranking')
plt.title('Rankings of Programming languages')
plt.legend(languages)
plt.show()
