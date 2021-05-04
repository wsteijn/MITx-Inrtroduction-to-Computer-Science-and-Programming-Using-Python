# -*- coding: utf-8 -*-
"""
Created on Sat May  1 17:04:50 2021

@author: Will
"""

#Calculate the credit card balance after one year if a person only pays the minimum
#monthly payment required
#balance = outstanding balance on the credit card
#annualInterestRate = annual interest rate as a decimal
#monthlPaymentRate = the minimum required monthly payment rate as a decimal
#Function should print out the remaining balance after one year of minimum payments, rounded to two decimal places

balance = 1000
annualInterestRate = .67 
monthlyPaymentRate = .0359

def calc_balance (balance, annual_interest_rate, monthly_payment):
    month = 0
    monthly_interest_rate = annual_interest_rate/12.0
    while month<12:
        min_monthly_payment = monthly_payment * balance
        unpaid = balance - min_monthly_payment
        balance = round(unpaid + (monthly_interest_rate * unpaid),2)
        month +=1
    return balance

print(calc_balance(balance, annualInterestRate, monthlyPaymentRate))