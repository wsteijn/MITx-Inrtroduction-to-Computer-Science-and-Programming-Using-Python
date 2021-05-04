# -*- coding: utf-8 -*-
"""
Created on Sun May  2 12:49:51 2021

@author: Will
"""
#Write a program that calculates the minimum fixed monthly payment needed to pay off a balance w/in 12 months
#balance = outstanding balance on the credit card
#annualInterestRate = annual insterest rate as a decimal
#Assume interest is compounded monthly according to the balance at the end of the month
#monthly payment must be a multiple of 10

balance = 12000
annualInterestRate = 0.33


def calc_min_payment(balance, annual_interest_rate):
    monthly_interest_rate = annual_interest_rate/12.0
    min_monthly_payment = 10
    while True:
        month = 0
        bal = balance
        while month < 12:
            unpaid_balance = bal - min_monthly_payment
            bal = unpaid_balance + (monthly_interest_rate * unpaid_balance)
            month += 1
        if bal <= 0:
            return min_monthly_payment
        min_monthly_payment += 10
 
print(calc_min_payment(balance, annualInterestRate))




