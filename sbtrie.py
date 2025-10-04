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
        self.central: str | None = None
        self.others: list[str] = []
        self.score: int = 0
        self.pangramFound: bool = False
        self.bingoFound: bool = False
        self._seenFirstLetter: set[str] = set()

    def getLetter(self) -> str:
        


        return ""
    
    # TODO Check if this is correct
    def isNewSBWord(self, word: str) -> int:
        toRet: int = 0

        for ch in word:
            pass
        
        return toRet

    def isPangram(self, word: str) -> bool:

        return False
    
    def hasBingo(self) -> bool:


        return False
    
    def getFoundWord(self) -> list[str]:


        return []
    

    def sbWords(self, centralLetter: str, otherLetters: str) -> list[str]:

        return []
    

    # This was not in directions implament when you come to it if needed.
    def addFoundWord(self):
        pass



   
    
