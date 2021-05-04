# -*- coding: utf-8 -*-
"""
Created on Mon May  3 17:57:26 2021

@author: Will
"""

#A game consists of playing multiple hands. Implement one final function to complete the game. 
#Write the code that implements the playGme function. For the game, you should use the HAND_SIZE
#constant to determine the number of cards in a hand.

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    while True:
        #Ask user to give an input for what they want to do
        user_input = str(input("Enter n to deal a new hand, r to replay the last hand, or e to end game: "))
        #user wants to deal a new hand
        if user_input == 'n':
            #deal a hand the size of the HAND_SIZE parameter
            hand = dealHand(HAND_SIZE)
            #play the hand
            playHand(hand, wordList, HAND_SIZE)
        #user wants to end the game
        elif user_input == 'e':
            break
        #user wants to replay the last hand
        elif user_input == 'r':
            #account for no previous hand having been played
            try:
                playHand(hand, wordList, HAND_SIZE)
            except:
                print("You have not played a hand yet. Please play a new hand first!")
        #if user inputs anything else, tell them their input is invalid
        else:
            print("Invalid command.")