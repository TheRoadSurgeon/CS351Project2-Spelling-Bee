# -*- coding: utf-8 -*-
"""
Due: Tuesday, October 7th, 2025 @ 11:59PM

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
        self.seenFirstLetter: set[str] = set()

    def getLetters(self) -> str:
        letters = ""

        letters += self.central + "".join(self.others)

        return letters
    
    # TODO Check if this is correct
    def isNewSBWord(self, word: str) -> int:
        wrd = word.lower()

        if len(wrd) < 4:
            return -1
        
        if self.central not in wrd:
            return -2
        
        if not wrd.isalpha():
            return -3

        gameLatters = set(self.getLetters())
        for ch in wrd:
            if ch not in gameLatters:
                return -3
        
        if not self.search(wrd):
            return -4
         
        if self.found.search(wrd):
            return -5
        

        base = 1 if len(wrd) == 4 else len(wrd)
        points = base + (7 if self.isPangram(wrd) else 0)
        
        return points

    def isPangram(self, word: str) -> bool:
        # Make sure to get non repeating game letters that are used for the game.
        # When a word is guessed we extract all the unique letters.
        gameLetters = set(self.getLetters()) # The 7 letters choosen by user
        wordSet = set(word.lower()) # The letters of the inputed word to guess

        # We check if all the unique letters in 
        # the guest word and the allowed letters match.
        return wordSet == gameLetters

    
    def hasBingo(self) -> bool:
        # If word has been found that STARTS with each possible letter
        # from our choosen game letters check the set of those first letter words.
        # If we have 7 unique letters in that set we have a bingo.
        return len(self.seenFirstLetter) == 7
    
    def getFoundWord(self) -> list[str]:


        return []
    

    def sbWords(self, centralLetter: str, otherLetters: str) -> list[str]:

        return []
    

    # This was not in directions implament when you come to it if needed.
    def addFoundWord(self, word: str):
      
        return self.found.insert(word)



   
    
