#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 23:48:52 2024

@author: vikashpirthiani
"""

import matplotlib.pyplot as plt 
import seaborn as sns
import pickle 

with open('prog-langs-popularity.pickle', 'rb') as f:
    data = pickle.load(f)
    
    
languages, rankings = zip(*data)

java_years, java_ranks = zip(*rankings[0])

java_years = list(java_years)
java_ranks= list(java_ranks)
sns.lineplot(x=java_years, y=java_ranks)

plt.xticks(java_years)
plt.xlabel('year')
plt.ylabel('ranking')
plt.title('Java Ranking')
plt.show()
