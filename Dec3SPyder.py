# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 09:12:06 2020

@author: slb
"""
#The next two lines clears the workspace
from IPython import get_ipython
get_ipython().magic('reset -sf')

import math

with open('C:/Users/slb/Documents/AdventOfCode2020/Dec3.txt') as f:
    geology = f.readlines()
 
k = 0
count_trees2 = 0
for i in range(len(geology)):
    yty = list(geology[i])
    if yty[k] == '#':
        count_trees2 += 1
    k += 3
    if k > 30:
        k = (k%31)
print(count_trees2)

k = 0
count_trees1 = 0
for i in range(len(geology)):
    yty = list(geology[i])
    if yty[k] == '#':
        count_trees1 += 1
    k += 1
    if k > 30:
        k = (k%31)

k = 0
count_trees3 = 0
for i in range(len(geology)):
    yty = list(geology[i])
    if yty[k] == '#':
        count_trees3 += 1
    k += 5
    if k > 30:
        k = (k%31)
    
k = 0
count_trees4 = 0
for i in range(len(geology)):
    yty = list(geology[i])
    if yty[k] == '#':
        count_trees4 += 1
    k += 7
    if k > 30:
        k = (k%31)
    
k = 0
count_trees5 = 0 
for i in range(math.ceil(len(geology)/2)):
    yty = list(geology[2*i])
    if yty[k] == '#':
        count_trees5 += 1
    k += 1
    if k > 30:
        k = (k%31)

result = count_trees1 * count_trees2 * count_trees3 * count_trees4 * count_trees5
print(result)
