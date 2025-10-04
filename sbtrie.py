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
        self._seenFirstLetter: set[str] = set()

    def getLetters(self) -> str:
        letters = ""

        letters += self.central + "".join(self.others)

        return letters
    
    # TODO Check if this is correct
    def isNewSBWord(self, word: str) -> int:
    
        if len(word) < 4:
            return -1
        
        if self.central not in word:
            return -2
        
        for ch in word:
            if ch not in self.others and ch != self.central:
                return -3
        
        if not self.search(word):
            return -4
         
        if self.found.search(word):
            return -5
        
        self.score += len(word) - 3
        self.insert(word)
        
        if self.isPangram(word):
            self.score +=7
            return 1

        if self.hasBingo():
            self.score
        return 0

    def isPangram(self, word: str) -> bool:
        possibleLetters = self.getLetters()
        chSet = set()

        for ch in word:
            if ch in possibleLetters:
                chSet.add(ch)

        if len(chSet) >= 7:
            return True

        return False
    
    def hasBingo(self) -> bool:
        allWordsFound = self.found.words()
        if len(set(allWordsFound)) >= 7:
            return True
        
        return False
    
    def getFoundWord(self) -> list[str]:


        return []
    

    def sbWords(self, centralLetter: str, otherLetters: str) -> list[str]:

        return []
    

    # This was not in directions implament when you come to it if needed.
    def addFoundWord(self):
        pass



   
    
