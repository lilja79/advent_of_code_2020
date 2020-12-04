# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 19:00:31 2020

@author: slb
"""
#%%
with open('C:/Users/slb/Documents/AdventOfCode2020/Dec1.txt') as f:
    dec1_data = [int(i) for i in f]
t = 0
tt = 0
for i in range(199):
    for j in range(i,200):
        if (dec1_data[i] + dec1_data[j]) == 2020:
            result = dec1_data[i] * dec1_data[j]
            first_number = dec1_data[i]
            second_number = dec1_data[j]
            print(result)
            print(first_number)
            print(second_number)



#%%
