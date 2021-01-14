# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 19:00:31 2020

@author: slb
"""
#%%
with open('C:/Users/slb/Documents/AdventOfCode2020/Dec1.txt') as f:
    dec1_data = [int(i) for i in f]

for i in range(199):
    for j in range(i,200):
        if (dec1_data[i] + dec1_data[j]) == 2020:
            result = dec1_data[i] * dec1_data[j]
print(result)

#%%

for k in range(198):
    for i in range(199):
        for j in range(i,200):
            if (dec1_data[i] + dec1_data[j] + dec1_data[k]) == 2020:
                result2 = dec1_data[i] * dec1_data[j] * dec1_data[k]
print(result2)