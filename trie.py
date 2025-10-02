# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 15:22:23 2025

@author: troy
"""

class Trie:
    """ A class for the Trie """
    def __init__ (self):
        self.insertDataMember = 0
        
    def getFromFile(fname: str) -> bool:
        

        try:
            with open(fname, "r", encoding="utf-8") as f:
                for line in f.readline():
                    break
        except FileNotFoundError:
            print(f"File was not found: {fname}")
        pass
    
    def insert():
        pass
    
    def remove():
        pass
    
    def clear():
        pass
    
    def wordCount():
        pass
    
    def words():
        pass