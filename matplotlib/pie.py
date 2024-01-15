#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 23:40:51
 2024

@author: vikashpirthiani
"""

import matplotlib.pyplot as plt 
import pickle


with open('devs-outside-time.pickle','rb') as f:
    data = pickle.load(f)
    
time, responses = zip(*data)


plt.pie(responses, labels=time, autopct='%d%%')


plt.axis("equal")

plt.title('Daily Time Developers Spend Outside')

plt.show()