# -*- coding: utf-8 -*-
"""
Created on Mon May  3 17:41:55 2021

@author: Will
"""
#Allow the user to play out a single hand

#Helper function to calculate the number of letters in the current hand
def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    return sum(hand.values())


#Note: do not assume that there will always be 7 letters in a hand! The parameter n
    #represents the size of the hand.
def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    #keep track of the total score
    totalScore = 0
    #while there are still letters left in the hand
    while calculateHandlen(hand) > 0:
        #Display the hand using the displayHand function
        print('Current Hand:', end=' '); displayHand(hand)
        #Ask user for a word as input
        a_word = str(input('Enter word, or a "." to indicate that you are finished: ' ))
        #If the input is a single period:
        if a_word == '.':
            #break out of the loop, game is over
            break
        #otherwise the input is not a single period
        else:
            #check to see if the input entered is a valid word
            #if the input is not a valid word:
            if isValidWord(a_word, hand, wordList) == False:
                #reject the invalid word and print a message
                print("Invalid word, please try again")
                print("\n")
            #if the input is a valid word
            elif isValidWord(word, hand, wordList) == True:
                #update the total score using the getWordScore function and print it out to the user
                totalScore += getWordScore(a_word, n)
                print('"' + a + '" earned ' + str(getWordScore(a_word, n)) + " points. Total: "+ str(totalScore) + " points.")
                #update the hand using updateHand function
                hand = updateHand(hand, a_word)
    #Game is over: tell the user the total score
    if a_word == '.':
        print ("Goodbye! Total score: " + str(totalScore) + " points.")
    else:
        print("Run out of letters. Total score: " + str(totalScore) + " points.")
        