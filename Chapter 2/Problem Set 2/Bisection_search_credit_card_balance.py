# -*- coding: utf-8 -*-
"""
Created on Sun May  2 12:51:54 2021

@author: Will
"""

#Function for calculating the lowest monthly payment that will pay off all debt
#in under 1 year using bisection search
#input is the total balance (outstanding balance on the credit card) 
#and the annual interest rate (annual interest rate as a decimal)
#assume interest is compounded monthly according to the balance at the end of the month
#the monthly payment is the same for all months

def payDebt(balance, annualInterestRate):
    originalBalance = balance
    monthlyInterestRate = annualInterestRate/12.0
    monthlyPaymentLowerBound = balance/12.0
    monthlyPaymentUpperBound = (balance * ((1+ monthlyInterestRate)**12))/12.0
    while abs(balance) > .001:
        fixedMonthlyPayment = (monthlyPaymentLowerBound + monthlyPaymentUpperBound)/2.0
        balance = originalBalance
        month = 1
        while month <=12:   
            monthlyUnpaidBalance = balance - fixedMonthlyPayment
            updatedBalance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
            balance = updatedBalance
            month += 1
        if balance > .001:
            monthlyPaymentLowerBound = fixedMonthlyPayment
        if balance < -.001:
            monthlyPaymentUpperBound = fixedMonthlyPayment
        else:
            break
    print("Lowest Payment:", round(fixedMonthlyPayment, 2))