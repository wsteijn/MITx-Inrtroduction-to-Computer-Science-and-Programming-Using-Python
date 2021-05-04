# -*- coding: utf-8 -*-
"""
Created on Mon May  3 19:01:11 2021

@author: Will
"""

#The Message class contains methods that could be used to apply a ciper to a string,
#either to encrypt or to decrypt a message. In this problem you will fill in two methods:
#1. the build_shift_dict(self, shift) method of the Message class. Be sure that your dictionary
#includes both lower and upper case letters, but that the shifted character for a lower case
#letter and its uppercase version are lower and upper case instances of the same letter.
#2. fill in the apply_shift(self, shift) method of the Message class. Remember that spaces and 
#punctuation should nto be changed by the cipher.


def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        assert 0 <= shift < 26, "shift must be greater than 0 and less than 26"
        listUpper = list(2*string.ascii_uppercase)
        listLower = list(2*string.ascii_lowercase)
        newDictUpper = dict(zip(listUpper[0:26], listUpper[0+shift:26+shift]))
        newDictLower = dict(zip(listLower[0:26], listLower[0+shift:26+shift]))
        newDictUpper.update(newDictLower)
        return(newDictUpper)


def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        listText = []
        for char in self.message_text:
            if char not in self.build_shift_dict(shift).keys():
                listText.append(char)
                continue
            else:
                listText.append(self.build_shift_dict(shift)[char])
        return ''.join(listText)