# -*- coding: utf-8 -*-
"""
Created on Mon May  3 16:51:24 2021

@author: Will
"""

#exception to force user to input an integer
while True:
    try:
        n = input("Please enter an integer: ")
        n = int(n)
        break
    except ValueError:
        print("Input not an integer; try again")
    print("Correct input of an integer!")

#example: control input
data = []
file_name = input("Provide a name of a file of data")
try:
    fh = open(file_name, 'r')
except IOError:
    print("Cannot open ", file_name)
else:
    for new in fh:
        if new != '\n':
            addIt = new[:-1].split(',')
            data.append(addIt)
finally:
    fh.close()
    
#example: file is a list of names and grades - want to add an empty list to students that do not have a grade
#name could be 1 element, or 2 elements, or 3 elements... grade is always the last element of the list
gradesData = []
if data:
    for x in data:
        try:
            name = x[0:-1]
            grades = int(x[-1])
            gradesData.append([name, [grades]])
        except ValueError: #if student does not havea  grade, this will throw a value error
            gradesData.append([x[:],[]])
            
#exceptions as control flow
def get_ratios(L1, L2):
    """Assumes L1 and L2 are lists of equal length of numbers. Returns a
        List containing L1[i] / L2[i] """
    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/float(L2[index]))
        except ZeroDivisionError:
            ratios.append(float('NaN')) #NaN = not a number
        except:
            raise ValueError('get_ratios called with bad arg')
    return ratios


#giving a return to an exception
def avg(grades):
    try:
        return sum(grades)/len(grades)
    except ZeroDivisionError:
        print('no grades data')#flags the error
        return 0.0 #returns an output that is more in line with the data structure we want

#helper function for fancy divide (shown below)
#do not raise exception if there is a divide by zero error
#when dividing by 0, this should returna  list with all 0 elements
def simple_divide(item, denom):
    try:
        return item / denom
    except ZeroDivisionError:
        return 0

def fancy_divide(list_of_numbers, index):
    denom = list_of_numbers[index]
    return[simple_divide(item, denom) for item in list_of_numbers]


#function to normalize a list of numbers
def normalize(numbers):
    max_number = max(numbers)
    assert(max_number != 0), "Cannot divide by 0" #asserts that max_number is not equal to 0
    for i in range(len(numbers)):
        numbers[i]  /= float(max_number)
        assert(0.0 <= numbers[i] <= 1.0), "output not between 0 and 1"
    return numbers       

    
