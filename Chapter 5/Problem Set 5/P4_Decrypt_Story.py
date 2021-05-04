# -*- coding: utf-8 -*-
"""
Created on Mon May  3 19:22:39 2021

@author: Will
"""
#Now that you have all the pieces to the puzzle, please use them to decode the file story.txt.
#Create a CipherTextMessage object using the story string and use decrypt_message to return the 
#appropriate shift value and unencrypted story string.

def decrypt_story():
    story = CiphertextMessage(get_story_string())
    return story.decrypt_message()
