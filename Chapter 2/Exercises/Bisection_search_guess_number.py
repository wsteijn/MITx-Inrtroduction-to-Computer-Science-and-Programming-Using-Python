# -*- coding: utf-8 -*-
"""
Created on Sat May  1 17:18:31 2021

@author: Will
"""
#Script for using bisection search to find a specific number between 0 and 1--
#Get input: c = correct, l = guess is too low, h = guess is too high
#g = the guess from bisection search
print("Please think of a number between 0 and 100!")
high = 100
low = 0
g = int((high+low)//2)
x = ''
#while loop - while input is not c (meaning the guess is not correct)
while x != 'c':
    print("Is your secret number " + str(g) +"?")
    x = input("Enter 'h' to indicate the guess is too high. Enter 'l', to indicate the guess is too low. Enter, 'c', to indicate I guessed correctly. ")
    if x == 'h':
        #update high - know the secret number cannot be higher than the previous guess
        high = g
        g=int(high + low)//2
    elif x == 'l':
        #update low - know the secret number cannot be lower than the previous guess
        low = g
        g = int(high + low)//2
    #input is not h or l or c - print statment indicating input is incorrect
    elif x != 'c': 
        print("Sorry, I did not understand your input.")
print("Game over. Your secret number was: " + str(g)) 
