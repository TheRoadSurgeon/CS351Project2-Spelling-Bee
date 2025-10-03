# -*- coding: utf-8 -*-

from __future__ import annotations
from typing import Optional, List

"""
Created on Mon Sep 15 15:22:23 2025

@author: troy
"""

class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.isWord = False



class Trie:
    """ A class for the Trie """
    def __init__ (self):
        self.insertDataMember = 0
        self.root: TrieNode = TrieNode()

    def getFromFile(self, fname: str) -> bool:
        

        try:
            with open(fname, "r", encoding="utf-8") as f:
                for line in f.readline():
                    self.insert(line)

        except FileNotFoundError:
            print(f"File was not found: {fname}")

        return False
    
    def insert(self, word: str) -> bool:
        curr = self.root
        
        for ch in word:
            
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
                self.insertDataMember+=1

            if ch in curr.children:
                return False        
            
            curr = curr.children[ch]

        curr.isWord = True
        return True

    def search(self, word: str) -> bool:
        curr = self.root

        for ch in word:
            
            if ch not in curr.children:
                return False
            
            curr = curr.children[ch]
            
        return curr.isWord
            


    def remove(self, word: str):
        pass
    
    def clear(self):
        pass
    
    def wordCount(self):
        pass
    
    def words(self):
        
        # Go down each level store each char in a string
        # Ones reaching isWord = True store string in list
        # Recusive call
        # while curr.children:
        #     for ch in curr.children:
        def helper(root: TrieNode, allWords: List, seq: str):
            
            if root.isWord == True:
                allWords.append(seq)
                return
            
            helper(root.children[])

        curr = self.root
        allWords = []
        seq = ""
        helper(curr, allWords, seq)

        pass