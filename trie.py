# -*- coding: utf-8 -*-

from __future__ import annotations
from typing import List

"""
Due: Tuesday, October 7th, 2025 @ 11:59PM

The Trie file of Project 2 Spelling Bee.
    This file is the core of this project. It contains the Trie class
    This class helps with building and checking if a Trie tree has specific
    words. It uses a dictionary for all the children and isWord Boolean to 
    tell us if the word that was guessed is actually a word or not.

@author: Hristian Tountchev
"""

# TrieNode class that builds each character of our Trie tree.
class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.isWord = False


# The Trie class helps us build and validate a tree.
# It can build, seach in, remove nodes, clear in the Trie structure.
class Trie:
    """ A class for the Trie """
    def __init__ (self):
        self.insertDataMember: int = 0 # Keep track of all the words inserted.
        self.root: TrieNode = TrieNode()

    # This function is used to get words from a predefined file.
    def getFromFile(self, fname: str) -> bool:
        

        try:
            with open(fname, "r", encoding="utf-8") as f:
                for line in f:
                    # toInsert = line.strip().lower()
                    for tok in line.split():
                        c = tok.lower()
                        if c.isalpha():
                            self.insert(c)
            return True
        except OSError:
            return False

    # This function is used to insert nodes in the Trie Tree.
    def insert(self, word: str) -> bool:
        curr = self.root
        
        # Check if the word is composed of characters.
        # Check if the string is not empty.
        if not word or not word.isalpha():
            return False
        
        word = word.lower()

        # If the character does not exist in the current children of
        # the parent node's children dictionary - insert it.
        for ch in word:
            
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
                    
            
            curr = curr.children[ch]

        if curr.isWord:
            return False


        curr.isWord = True
        self.insertDataMember+=1 
        return True

    # Search the Trie to see if a word exists in there.
    def search(self, word: str) -> bool:
        curr = self.root

        # Check if the character in the word parameter is in the children 
        # of the parent node. If not, stop, its not a word break from the function.
        for ch in word:
            
            if ch not in curr.children:
                return False
            
            curr = curr.children[ch]

             
        return curr.isWord
            
    # Remove a word from the Trie.
    # IE set the node's isWord (if it exists) to false.
    def remove(self, word: str) -> bool:
        curr = self.root

        # Check each character in the word parameter. If the character does
        # not exists break out of the function.
        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        
        # If the word is not complete than the last letter we get to
        # will have a Boolean of isWord set to false. IE not a word
        # only partial word.
        if not curr.isWord:
            return False
        
        curr.isWord = False
        self.insertDataMember-=1

        return True
    
    # Clear the whole Trie tree.
    # IE set the root node to a new TrieNode 
    # let the garbage collector deal with it.
    def clear(self):
        self.root = TrieNode()
        self.insertDataMember = 0
        return True
    
    # Return the count of all the words in the Trie.
    def wordCount(self):
        return self.insertDataMember
    
    # Returns all the words that are stored in the Trie.
    # This list can get VERY large.
    def words(self):
        
        allWords: List[str] = []

        # Helper function that uses DFS (depth first search)
        # It visits every child node of the parent node. 
        # Does that for all the nodes. 
        # Every recursive call it makes it checks: isWord = True?
        # If true we save the word to a list.
        # Once every node is visited the lists is fully built and 
        # ready to return.
        def helper(root: TrieNode, seq: str):
            
            if root.isWord == True:
                allWords.append(seq)
                
            
            for ch in sorted(root.children.keys()):
                helper(root.children[ch], seq + ch)

        curr = self.root
        
        seq = ""
        helper(curr, seq)

        return allWords