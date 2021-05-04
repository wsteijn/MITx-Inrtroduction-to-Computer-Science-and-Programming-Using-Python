# -*- coding: utf-8 -*-
"""
Created on Sat May  1 16:16:27 2021

@author: Will
"""

#Assume 's' is a string of lower case characters
s = 'aberichoeridhijklawern'

#Script for printing the longest substring of 's' where the letters appear in
#alphabetical order. In case of a tie, print the first string that appears

current_string = s[0]
longest = s[0]

#iterate through the string indices
for i in s[1:]:
    #if the character at index i is equal or larger than the previous character, add this
    #character to the string current_longest
    if i >= current_string[-1]:
        current_string += i
        #if the length of the current_string string is greater than the length
        #of the previous longest string, designate the current_string as the longest
        if len(current_string) > len(longest):
            longest = current_string
    else:
        #if character at index i is smaller than previous character, then set 
        #the current_string equal to this character
        current_string = i
    
print('Longest substring in alphabetical order is: ' + str(longest))
