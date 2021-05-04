# -*- coding: utf-8 -*-
"""
Created on Sat May  1 17:36:49 2021

@author: Will
"""

#Exercises for using recursion

#use recrusion to check if a string is a palendrome
def isPal(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isPal(s[1:-1])

#use recursion to find greatest common divisor of two numbers
def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if (b==0):
        return(a)
    else:
       return gcdRecur(b, a%b)

#use recursion to print the nth number in the fibonacci sequence
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

#use recursion to find if a character is in a string   
#input of function is a character, and a string
#returns true or false
def isIn(char, aStr):
    if len(aStr) == 0:
        return False
    midpoint = int(len(aStr)//2)
    midchar = aStr[midpoint]  
    if aStr == char:
        return True
    if len(aStr) <= 1:
        return False
    if midchar == char:
        return True
    if char > midchar:
        return isIn(char, aStr[midpoint+1:])
    else:
        return isIn(char, aStr[:midpoint])
isIn("m", "abcdefgjklmmmmmnopqr")

        
    