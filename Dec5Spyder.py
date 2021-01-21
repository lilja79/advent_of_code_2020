# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 21:46:00 2021

@author: slb
"""
from IPython import get_ipython
get_ipython().magic('reset -sf')

import os
file_path = os.path.join(os.path.curdir, "Dec5.txt")

with open(file_path) as f:  
     data = f.readlines()

rows = []
columns = []    
seatID = []
for line in data:
    characters = list(line)
    lower = 0
    higher = 127
    lefter = 0
    righter = 7
    for i in range(7):
        if characters[i]=='B':
            lower += 128/(2**(i+1))
        elif characters[i]=='F':
            higher -= 128/(2**(i+1))
    rows.append(higher)        
    for j in range(3):
        if characters[j+7]=='R':
            lefter += 8/(2**(j+1))
        elif characters[j+7]=='L':
            righter -= 8/(2**(j+1))
    columns.append(righter)
    seatID.append(8*higher+righter)
    
seatIDmax = max(seatID)
print(seatIDmax)

yuy = []       
for r in range (len(seatID)): #Convert from float to int
    yuy.append(int(seatID[r]))

yuy1 = sorted(yuy)
missing = sorted(set(range(yuy1[0], yuy1[-1])) - set(yuy1))

print(missing)
