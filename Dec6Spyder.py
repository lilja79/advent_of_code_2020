# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 21:07:02 2021

@author: slb
"""
#The next two lines clears the workspace
from IPython import get_ipython
get_ipython().magic('reset -sf')

import os
file_path = os.path.join(os.path.curdir, "C:/Users/slb/Documents/AdventOfCode2020/Dec6.txt")

with open(file_path) as f:  
     data = f.readlines()
     
groups = []    
item = []
for i in range(len(data)):
    data1 = data[i]
    data1 = data1.split()
    if len(data1) == 0:
        groups.append(item)
        groups[-1] = [j for i in groups[-1] for j in i] #Flattens the list of lists to one list (of strings)
        item = []
        continue
    item.append(data1)
groups.append(item) #In order to not loose the last passport in the list
groups[-1] = [j for i in groups[-1] for j in i]

yes = 0
yes2 = 0
for item in groups:
    t = len(item) #I.e. t is the number of people in each group
    liste = [j for i in item for j in i] #Splits the list of strings into a list of characters
    yes += len(set(liste)) #set(liste)) gives the number of unique elements in liste
    how_many = {} #Creates an empty dictionary
    for n in liste:
        how_many[n] = how_many.get(n, 0) + 1 #Calculates the occurence of each element and stors it in the dictionary
    yes2 += sum(x == t for x in how_many.values()) #Counts how many elements of the dictionary occurred t times and adds it to the counter
    
print(yes)    
print(yes2)