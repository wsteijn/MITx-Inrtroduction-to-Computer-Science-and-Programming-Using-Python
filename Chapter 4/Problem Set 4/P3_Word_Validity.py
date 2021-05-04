# -*- coding: utf-8 -*-
"""
Created on Mon May  3 17:38:46 2021

@author: Will
"""
#Verify that the word entered is a valid word from the word list and is composed
#of letters in the hand
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    wordDict = {}
    if word not in wordList:
        return False
    elif word in wordList:
        for letter in word:
            wordDict[letter] = wordDict.get(letter,0) + 1
        for x in wordDict.keys():
            if x not in hand or wordDict[x] > hand[x]:
                return False
        else:
            return True
