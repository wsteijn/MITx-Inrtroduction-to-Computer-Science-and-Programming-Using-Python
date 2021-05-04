# -*- coding: utf-8 -*-
"""
Created on Sat May  1 15:54:52 2021

@author: Will
"""
#Assume 's' is a string of lowercase characters
s = 'azcbobobegghakobob'
#script for counting the number of times the string 'bob' occurs in string s

numBobs = 0
for i in range(len(s)):
    if s[i:i+3] == 'bob':
        numBobs += 1
print('Number of bobs: ' + str(numBobs))