# -*- coding: utf-8 -*-
"""
Created on Mon May  3 17:22:45 2021

@author: Will
"""

# Problem #1: Scoring a word
#Assume input word is a string of lowercase letters or the empty string ""
#SCRABBLE_LETTER_VALUES dictionary is defined in another file and can be used here
#Do not always assume that there are always 7 letters in a hand. The parameter n
#is the number of letters required for a bonus score.
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    scoreLetters = []
    score = 0
    #if the the length of the word = n, give 50 point bonus
    if len(word) == n:
        score += 50
    for letter in word:
        #create array of scores of the letters in the word
          scoreLetters.append(SCRABBLE_LETTER_VALUES.get(letter))
    #calculate the score of the word
    score += len(word) * sum(scoreLetters)
    return score
