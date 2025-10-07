# -*- coding: utf-8 -*-
"""
Due: Tuesday, October 7th, 2025 @ 11:59PM

The SBTrie file of Project 2 Spelling Bee.
    This file inherits form the Trie class. It is capable of building a trie
    tree that can be used to play the spelling bee game. The SBTrie class
    also has the ability to build a separate Trie tree that keeps track of
    correctly found words by the user, if they are Pangrams and if the user
    has score a bingo.


@author: Hristian Tountchev
"""
from trie import Trie

class SBTrie(Trie):
    """ A class for the Spelling Bee Trie """
    def __init__ (self):
        super().__init__()
        self.found = Trie()
        self.central: str = ""
        self.others: list[str] = []
        self.score: int = 0
        self.pangramFound: bool = False
        self.bingoFound: bool = False
        self.seenFirstLetter: set[str] = set() # This is a helper set for bingo

    # Simple function that returns the playable letters in the game.
    # The letters must be inputted by the player in the begging of the game.
    def getLetters(self) -> str:
        letters = ""

        letters += self.central + "".join(self.others)

        return letters
    
    # This function tries to find if the user's input word is correct
    # and that word exists in the Trie we create out of the file.
    def isNewSBWord(self, word: str) -> int:
        '''
        Command 5 Helper function
        '''
        wrd = word.lower()

        # Error 1 if the word is less than 4 characters long.
        if len(wrd) < 4:
            return -1
        
        # Error 2 if the word contains the central letter.
        if self.central not in wrd:
            return -2
        
        # Error 3 if the word is alphabetical characters only.
        if not wrd.isalpha():
            return -3

        # Error 3 And if every character in the user's word matches 
        # with the characters they declared as playable.
        gameLatters = set(self.getLetters())
        for ch in wrd:
            if ch not in gameLatters:
                return -3
        
        # Error 4 If the word exists in the Trie that was build in 
        # the begging of the game.
        if not self.search(wrd):
            return -4
         
        # Error 5 If the word was already guessed by the user
        # do not allow the word to be inputted again
        if self.found.search(wrd):
            return -5
        
        # If no errors were found in the user's input return the points
        # they have scored.
        base = 1 if len(wrd) == 4 else len(wrd)
        points = base + (7 if self.isPangram(wrd) else 0)
        
        return points

    # Function that helps with checking if the user's input was a pangram.
    def isPangram(self, word: str) -> bool:
        # Make sure to get non repeating game letters that are used for the game.
        # When a word is guessed we extract all the unique letters.
        gameLetters = set(self.getLetters()) # The 7 letters choosen by user
        wordSet = set(word.lower()) # The letters of the inputed word to guess

        # We check if all the unique letters in 
        # the guest word and the allowed letters match.
        return wordSet == gameLetters

    # Function that helps with finding out if the user has scored a bingo.
    def hasBingo(self) -> bool:
        # If word has been found that STARTS with each possible letter
        # from our choosen game letters check the set of those first letter words.
        # If we have 7 unique letters in that set we have a bingo.
        return len(self.seenFirstLetter) == 7
    

    # Return all the words the user has guessed correctly.
    def getFoundWord(self) -> list[str]:

        return self.found.words()
    
    # build and return a list of strings containing all of the words in the trie that 
    # meet the criteria of the Spelling Bee game: 
    #   - words must be at least 4 letters long
    #   - words must contain the centralLetter
    #   - in addition to the centralLetter, words may contain only the letters specified 
    #           in the otherLetters string.
    def sbWords(self, centralLetter: str, otherLetters: str) -> list[str]:
        '''
        Command 7 Helper function
        '''
        c = centralLetter.lower()
        other = ''.join(ch for ch in otherLetters.lower() if ch.isalpha())

        allowed = set(other)
        allowed.add(c)
        
        out = []

        def helper(root, pref: str):

            if root.isWord and len(pref) >= 4 and (c in pref):
                out.append(pref)

            for ch in sorted(root.children.keys()):
                if ch in allowed:
                   helper(root.children[ch], pref + ch)

        helper(self.root, "")

        return out
    

    # Helper function to add a found word by the user.
    def addFoundWord(self, word: str):
        
        return self.found.insert(word)



   
    
