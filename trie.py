# -*- coding: utf-8 -*-

from __future__ import annotations
from typing import List

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
        self.insertDataMember: int = 0
        self.root: TrieNode = TrieNode()

    def getFromFile(self, fname: str) -> bool:
        

        try:
            with open(fname, "r", encoding="utf-8") as f:
                for line in f:
                    toInsert = line.strip().lower()
                    if toInsert:
                        self.insert(toInsert)
            return True
        except FileNotFoundError:
            print(f"File was not found: {fname}")

        return False
    
    def insert(self, word: str) -> bool:
        curr = self.root
        
        for ch in word:
            
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
                    
            
            curr = curr.children[ch]

        curr.isWord = True
        self.insertDataMember+=1 
        return True

    def search(self, word: str) -> bool:
        curr = self.root

        for ch in word:
            
            if ch not in curr.children:
                return False
            
            curr = curr.children[ch]

             
        return curr.isWord
            

    def remove(self, word: str) -> bool:
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        
        if not curr.isWord:
            return False
        
        curr.isWord = False
        self.insertDataMember-=1

        return True
    
    def clear(self):
        self.root = TrieNode()
        self.insertDataMember = 0
    
    def wordCount(self):
        return self.insertDataMember
    
    def words(self):
        
        allWords: List[str] = []
        def helper(root: TrieNode, seq: str):
            
            if root.isWord == True:
                allWords.append(seq)
                
            
            for ch in sorted(root.children.keys()):
                helper(root.children[ch], seq + ch)

        curr = self.root
        
        seq = ""
        helper(curr, seq)

        return allWords