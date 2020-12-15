# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 10:28:30 2020

@author: slb
"""
#The next two lines clears the workspace
from IPython import get_ipython
get_ipython().magic('reset -sf')

#import numpy as np

import os
file_path = os.path.join(os.path.curdir, "C:/Users/slb/Documents/AdventOfCode2020/Dec13.txt")

with open(file_path) as f:
    notes = f.readlines()
    
departure = int(notes[0])
busses = notes[1].split(',') #Splits string at commas
while 'x' in busses: busses.remove('x') #Remove x's
busses = [int(i) for i in busses] #convert strings to int

waiting_time = [busses - departure%busses for busses in busses] #Calculate the waiting time for each bus when arriving at depature o'clock

for i in range(len(waiting_time)):
    if waiting_time[i] == min(waiting_time):
        bus = busses[i] #Determine the ID of the bus with least waiting time
result = bus * min(waiting_time)
print(result)


#%%
busses_with_x = notes[1].split(',')
busses_str = [str(i) for i in busses]
index = [busses_with_x.index(i) for i in busses_str]

r = 1
t = pow(10,14)
while r:
    tester = [(t+index[i])%busses[i] for i in range(len(index))] #If all conditions are fulfilled all elements of tester is 0
    if sum(tester) == 0:
        r = 0
        break
    t += 1
print(t)
