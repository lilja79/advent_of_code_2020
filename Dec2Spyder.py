# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 10:49:54 2020

@author: slb
"""
import pandas as pd
import re
#Read data
pswrds = pd.read_csv('C:/Users/slb/Documents/AdventOfCode2020/Dec2.txt', sep=' ')

#Separate the lowest and highest numbers acceptable in the password (split string)
orig = pswrds['number']
results = []
lower_values = []
higher_values = []
for i in range(len(orig)):
    results.append(re.split(r'\D+',orig[i])) #splits string
    tyt = (list(map(int, results[i]))) #converts to integer
    lower_values.append(tyt[0])
    higher_values.append(tyt[1])    

#Get rid of : 
letters = pswrds['letter']
character = []
for i in range(len(letters)):
    tyt = list(letters[i])
    character.append(tyt[0])

#Test what passwords are valid
correct = 0
data = pswrds['password']
for i in range(len(data)):
    data1 = list(data[i])
    ter = data1.count(character[i])
    if (ter >= lower_values[i]) and (ter <= higher_values[i]):
        correct += 1
print(correct)

correct2 = 0
#Test with new criteria
for i in range(len(data)):
    dummy = 0
    data1 = list(data[i])
    if data1[lower_values[i] - 1] == character[i]:
        dummy += 1
    if data1[higher_values[i] - 1] == character[i]:
        dummy += 1
    if dummy == 1:
        correct2 +=1
print(correct2)
