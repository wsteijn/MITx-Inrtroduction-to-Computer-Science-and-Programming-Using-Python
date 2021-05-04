# -*- coding: utf-8 -*-
"""
Created on Mon May  3 18:10:15 2021

@author: Will
"""

#Example of classes and inheritance through using coordinates
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    #function for all Coordinate objects
    def distance(self, other):
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5
    #define a print method
    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"
    #Getter method for a Coordinate object's c coordinate
    def getX(self):
        return self.x
    #Getter method for a Coordinate object's y coordinate
    def getY(self):
        return self.y
    def __eq__(self, other):
        assert type(other) == type(self)
        return self.getX()==other.getX() and self.getY() == other.getY()
    def __repr__(self):
        return 'Coordinate('+ str(self.getX()) + ',' + str(self.getY()) + ')'
    
    
    
c = Coordinate(3,4)
origin = Coordinate(0,0)
print(c.x)
c.distance(origin)
Coordinate.distance(c, origin)

#Clock example
class Clock(object):
    def __init__(self, time):
	    self.time = time
    def print_time(self, time):
	    print(time)

clock = Clock('5:30')
clock.print_time('10:30')

#Fraction example
class fraction(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
    def __str__(self):
        return str(self.numer) + " / " + str(self.denom)
    def getNumer(self):
        return self.numer
    def getDenom(self):
        return self.denom
    def __add__(self, other):
        numerNew = other.getDenom() * self.getNumer() + other.getNumer() * self.getDenom()
        denomNew = other.getDenom() * self.getDenom()
        return fraction(numerNew, denomNew)
    def __sub__(self, other):
        numerNew = other.getDenom() * self.getNumer() - other.getNumer() * self.getDenom()
        denomNew = other.getDenom() * self.getDenom()
        return fraction(numerNew, denomNew)
    def convert(self):
        return self.getNumer() / self.getDenom()
        
oneHalf = fraction(1,2)
twoThirds = fraction(2,3)
new = oneHalf + twoThirds
print(new)


#Your task is to define the following two methods for the intSet class:
#1. Define an intersect method that returns a new intSet containing elements that appear in both sets
#2. Add the appropriate method so that len(s) returns the number of elemetns in s
class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
    
    def intersect(self, other):
        assert type(self) == type(other)
        x = intSet()
        for val in self.vals:
            if other.member(val):
                x.insert(val)
        return x
    
    def __len__(self):
        return len(self.vals)
    
    
#gradebook example
class Grades(object):
    """A mapping from students to a list of grades"""
    def __init__(self):
        """Create empty grade book""" 
        self.students = [] #list of students
        self.grades = {} #id Num -> list of grades
        self.isSorted = True
        
    def addStudent(self, student):
        if student in self.student:
            raise ValueError("Duplicate sutdent")
        self.students.append(student)
        self.grades[student.getIdNumber()] = []
        self.isSorted = False








