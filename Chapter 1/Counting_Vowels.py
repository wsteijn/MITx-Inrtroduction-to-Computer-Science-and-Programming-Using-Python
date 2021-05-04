# -*- coding: utf-8 -*-
"""
Created on Sat May  1 15:39:05 2021

@author: Will
"""

#assume 's' is a string of lower case characters
s = 'acbeiekjdf'
#script that counts the number of vowels in string s (vowels = a, e, i, o, u)  
numVowels = 0
for char in s:
    if char in ['a','e','i','o','u']:
        numVowels += 1
print('Number of vowels: ' + str(numVowels))