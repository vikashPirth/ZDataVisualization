#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 23:30:01 2024

@author: vikashpirthiani
"""

import matplotlib.pyplot as plt 
import seaborn as sns
import pickle

with open('coding-exp-by-dev-type.pickle', 'rb') as f:
    
    data = pickle.load(f)
    
dev_types, years_exp = zip(*data)
dev_types = list(dev_types)
years_exp = list(years_exp)


sns.barplot(x=years_exp, y=dev_types)



plt.xlabel('Years')
plt.title('Years of Coding Experience by Developer Type')
plt.tight_layout()

plt.show()