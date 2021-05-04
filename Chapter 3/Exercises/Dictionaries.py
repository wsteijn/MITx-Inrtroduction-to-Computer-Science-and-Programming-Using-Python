# -*- coding: utf-8 -*-
"""
Created on Mon May  3 00:44:37 2021

@author: Will
"""

#dictionaries
animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}


#creating a dictionary of frequencies where lyrics is a list of strings
def lyrics_to_frequencies (lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] +=1
        else:
            myDict[word] = 1
    return myDict

#find the most common word from the dictionary
def most_common_words(freqs):
    values = freqs.values()
    best = max(values)
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)


#find words that occur a minimum number of times
def words_often(freqs, minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w]) #remove word from dictionary
        else:
            done = True
    return result
            
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
animals

#length of values that correspond to a key in the dictionary
len(animals['d'])
count = 0
for i in animals:
    count += len(animals[i])
print(count)

#find the total number of values in the dictionary
def how_many(aDict):
    count = 0
    for i in aDict:
        count += len(aDict[i])
    return count

how_many(animals)


#find the key with the biggest number of values in the dictionary
def biggest(aDict):
    myDict1 = {}
    for i in aDict:
        myDict1[i] = len(aDict[i])
    return max((myDict1))

biggest(animals)
    
#fibonacci with a dictionary
def fib_efficient(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans
d = {1:1, 2:2}
print(fib_efficient(6, d))    
 #this does a lookup first in case already calculated value, then modifies the dictionary as it progresses through the function calls
