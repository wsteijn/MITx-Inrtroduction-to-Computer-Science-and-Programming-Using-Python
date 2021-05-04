# -*- coding: utf-8 -*-
"""
Created on Sun May  2 23:21:31 2021

@author: Will
"""
#function that returns every other element of a tuple, starting with the first one
def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup
    
    '''
    b = len(aTup)
    a = aTup[0:b:2]
    return a

oddTuples(('I', 'am', 'a', 'test', 'tuple'))


#Write a function that applies a function to each elemetn in a list
def applyToEach(L, f):
    '''
    L: a list of integers
    
    f: a function that will be applied to each element in L
    '''
    for i in range(len(L)):
        L[i] = f(L[i])
testList = [1, -4, 8, -9]

def absoluteValue(a):
    return abs(a)

applyToEach(testList, absoluteValue)
print(testList)


#function for appling a list of functions to an integer
def applyEachTo(L, x):
    '''
    L: a list of functions

    x: an integer that will have the list of functions applied to it
    
    '''
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result

def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1

applyEachTo([inc, square, halve, abs], 3.0)


#MAP
#find minimum of the two functions at each position (min of L1 at place 0 and l2 at place 0, then place 1...)
L1 = [1, 28, 36]
L2 = [2, 57, 9]
for elt in map(min, L1, L2):
    print (elt)





