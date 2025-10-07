# -*- coding: utf-8 -*-
"""
Due: Tuesday, October 7th, 2025 @ 11:59PM

Main File of Project 2 Spelling Bee
  This file is the entry point of the program. It contains all the commands
  a user can input to play the spelling bee game. The options are in display command.
  To play the game the user enters a file to read from. The file must contain valid 
  words. After the file has been read the user has to input 7 latters the first of 
  which is the central letter that all words should have in common.
  Once the file and the 7 letters have been chosen by the user they can start playing.
  They must use command 5 leave a space and enter a word that may contain those laters.
  Scoring:
        - 1 points for words of length 4
        - any word with more than 4 letters gets a score of that length (IE puzzle = 6 points)
        - Pangram, meaning the word has all 7 letters that were chosen initially by the user
          gets points based on the word size + 7 points bonus.
        - bingo can be score by getting a word for every single latter chosen initially by the user.


@author: Hristian Tountchev
"""
from sbtrie import SBTrie 


# This function builds the initial Trie.
# Anytime it is called it is cleared before 
# building a new one.
def getNewDictionary(sbt, filename):
  '''
  Command 1
  '''
  sbt.clear()
  sbt.getFromFile(filename)

# This function is used to input more words into the trie.
# If the words are split between multiple files the trie is updated
# with this function.
def updateDictionary(sbt, filename):
  '''
  Command 2
  '''
  sbt.getFromFile(filename)


# This function is used to choose the 7 playable letters.
# The first letter being the central letter that every word
# must contain.
def setupLetters(sbt, letters):
  '''
  Command 3
  '''

  filteredLetters = ""

  # Loops through the user input "letters".
  # If the input is a alphabet character accepted it.
  for ch in letters:
     if ch.isalpha():
      filteredLetters += ch.lower()
  
  # Check if the user inputed the correct length of letters.
  if len(filteredLetters) != 7 or len(set(filteredLetters)) != 7:
    return False
  
  # If the letters are accepted the code bellow clears the "game".
  # IE all variable and lists from previous games are deleted.
  sbt.central = filteredLetters[0]
  sbt.others = sorted(filteredLetters[1:])

  sbt.found.clear()
  sbt.score = 0
  sbt.pangramFound = False
  sbt.bingoFound = False
  sbt.seenFirstLetter.clear()

  return True

# Display the chosen letters that the play may use
# to spell a word.
def showLetters(sbt):
  '''
  Command 4
  '''
  letters = sbt.getLetters()
  
  if len(letters) != 7:
     return

  centralLetter = letters[0]
  otherLetters = letters[1:]

  print(f"Central Letter: {centralLetter}")
  print(f"6 Other Letters: {','.join(otherLetters)}")


def attemptWord(sbt, word):
  '''
  Command 5
  '''

  # The function isNewSBWord in the SBTrie class handles errors and see
  # if a word is valid. If that word is valid than the word
  # is accepted. If the word was accepted than the isNewSBWord returns the
  # points that word is worth.
  points = sbt.isNewSBWord(word)
  if points < 0:
    message = {
        -1: "word is too short",
        -2: "word is missing central letter",
        -3: "word contains invalid letter",
        -4: "word is not in the dictionary",
        -5: "word has already been found"
    }
    print(message[points]) 
    return
  
  wrd = word.lower()

  # Error checked insert the word into found trie.
  sbt.found.insert(wrd)
  # Incrament the score
  sbt.score += points


  # Check if the word is a pangram.
  pang = sbt.isPangram(wrd)
  if pang:
    sbt.pangramFound = True
  
  # Check if the user gets a bingo.
  bingoAgain = False
  if wrd:
    sbt.seenFirstLetter.add(wrd[0])
    if not sbt.bingoFound and len(sbt.seenFirstLetter) == 7:
      sbt.bingFound = True
      bingoAgain = True

  # Build out the report message to tell the user their score and
  # if the user has gotten a pangram word or scored a bingo.
  report = ""
  unit = "point" if points == 1 else "points"
  total_unit = "point" if sbt.score == 1 else "points"

  report += f"found {wrd} {points} {unit}, total {sbt.score} {total_unit}"
  if pang:
    report += f", Pangram found"
    
  if bingoAgain:
    report += f", Bingo scored"
    
  print(report)
  
  

# Function is used to show the user what their game's 
# statistics are.
def showFoundWords(sbt):
  '''
  Command 6
  '''
  allFoundWords = sbt.getFoundWord()
  allFoundWords.sort()

  # Prints all the found words.
  for word in allFoundWords:
    print(word)
  
  # Build the report for the user.
  n = len(allFoundWords)
  wrdUnit = "word" if n == 1 else "words"
  ptsUnit = "point" if sbt.score == 1 else "points"

  extra = []
  if sbt.pangramFound:
    extra.append("Pangram found")
  if sbt.bingoFound:
     extra.append("Bingo scored")
  
  report = (", " + ", ".join(extra)) if extra else ""

  # Print the score for the
  # Example: 10 words found, total 54 points, Pangram found, 
  # Bingo scored
  print(f"{n} {wrdUnit} found, total {sbt.score} {ptsUnit}{report}")


# Function that displays ALL the words that we have from
# the imported file.
def showAllWords(sbt):
  '''
  Command 7
  '''
  toPrint = sbt.words()
  for word in toPrint:
     print(word)


# The command menu
def displayCommands():
  '''
  Command 8
  '''

  print( "\nCommands are given by digits 1 through 9\n")
  print( "  1 <filename> - read in a new dictionary from a file")
  print( "  2 <filename> - update the existing dictionary with words from a file")
  print( "  3 <7letters> - enter a new central letter and 6 other letters")
  print( "  4            - display current central letter and other letters")
  print( "  5 <word>     - enter a potential word")
  print( "  6            - display found words and other stats")
  print( "  7            - list all possible Spelling Bee words from the dictionary")
  print( "  8            - display this list of commands")
  print( "  9            - quit the program")
  print()


# Main loop of the game.
def spellingBee():
  print("Welcome to Spelling Bee Game")
  
  
  sbt = SBTrie()


  displayCommands()

  while (True):
    try:
      line = input ("cmd> ")
    except EOFError:
       break
    
    command = line[0]
    
    
    # clear input from any previous value
    args = ""


    if(command == '1'):
        args = line[1:].strip()

        getNewDictionary(sbt, args)

    if(command == '2'):
        args = line[1:].strip()

        updateDictionary(sbt, args)
        
    if(command == '3'):
        args = line[1:].strip()
 
        if setupLetters(sbt, args) == False:
          print("Invalid letter set")
          continue
        

    if(command == '4'):
        showLetters(sbt)

    if(command == '5'):
        args = line[1:].strip()
      
        attemptWord(sbt, args)

    if(command == '6'):
        showFoundWords(sbt)

    if(command == '7'):

        showAllWords(sbt)

    
    if(command == '8' or command == '?'):
        displayCommands()
    
    if(command == '9' or command == 'q'):
        break
    

  return
  
if __name__ == "__main__":
  spellingBee()