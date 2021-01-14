# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 11:48:04 2020

@author: slb
"""
#The next two lines clears the workspace
from IPython import get_ipython
get_ipython().magic('reset -sf')

import re

import os
file_path = os.path.join(os.path.curdir, "Dec4.txt")

with open(file_path) as f:  
     data = f.readlines()
         
passports = []    
item = []
for i in range(len(data)):
    data1 = data[i]
    data1 = data1.split()
    if len(data1) == 0:
        passports.append(item)
        passports[-1] = [j for i in passports[-1] for j in i] #Flattens the list of lists to one list (of strings)
        item = []
        continue
    item.append(data1)
passports.append(item) #In order to not loose the last passport in the list
passports[-1] = [j for i in passports[-1] for j in i]
    
    
invalid = 0 #Counting the number of invalid passports and subtracting it from the total
for i in passports:
    if len(i)<7:
        invalid += 1 #All passports with less than 7 fields are invalid
    if len(i)==7:
        for j in i:
            if j[:3]=='cid': #If the cid field is there another field must be missing, and thus the passport is invalid
                invalid += 1
                

valid = len(passports)-invalid               
                
print('The number of valid passports is ', valid,)
                
#%% Second part of the task
valid2 = 0

for i in range(len(passports)):
    line = ''.join(passports[i]) #Combines the items in the list passports[i] into one string
    byr = re.findall("byr:(19[2-9][0-9]|200[0-2])", line) #These are empty if there is not match and contains the match if there is one.
    iyr = re.findall("iyr:(201[0-9]|2020)", line)
    eyr = re.findall("eyr:(202[0-9]|2030)", line)    
    hgt = re.findall("hgt:(1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in)", line)
    hcl = re.findall("hcl:#([0-9a-f]{6})", line)
    ecl = re.findall("ecl:(amb|blu|brn|gry|grn|hzl|oth)", line)
    pid = re.findall(r"(?<!\d)\d{9}(?!\d)", line) #This finds instances of exactly 9 digits after eachother
    
    if (len(byr)*len(iyr)*len(eyr)*len(hgt)*len(hcl)*len(ecl)*len(pid))==1: #If there was a match for all, all lengths are 1
       valid2 += 1
        
print('the new number of valid passports is ', valid2)
    
    
        
    
    
            
