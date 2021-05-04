# -*- coding: utf-8 -*-
"""
Created on Mon May  3 18:47:37 2021

@author: Will
"""

def genFib():
    fibn_1 = 1
    fibn_2 = 0
    while True:
        next = fibn_1 + fibn_2
        yield next
        fibn_2 = fibn_1
        fibn_1 = next
        
fib = genFib()
fib.__next__()
        
#generator that returns the sequence of prime numbers on successive calls to its next method
def genPrimes():
    prime_1 = 1
    primeList = []
    while True:
        prime_1 += 1
        for x in primeList:
            if prime_1 % x == 0:
                break
        else:
            primeList.append(prime_1)
            yield primeList
       
    

prime = genPrimes()
prime.__next__()