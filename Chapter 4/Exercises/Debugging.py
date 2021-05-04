# -*- coding: utf-8 -*-
"""
Created on Mon May  3 16:49:46 2021

@author: Will
"""

#UnboundLocalError
def integerDivision(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    while x >= a:
        count += 1
        x = x - a
    return count
print(integerDivision(5, 3))
#get error: UnboundLocalError: local variable 'count' referenced before assignment
#fix error:
def integerDivision(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    count = 0
    while x >= a:
        count += 1
        x = x - a
    return count
print(integerDivision(9, 3))















