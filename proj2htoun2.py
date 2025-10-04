# -*- coding: utf-8 -*-
"""
Due: Tuesday, October 7th, 2025 @ 11:59PM

@author: Hristian Tountchev
"""
from sbtrie import SBTrie 


# the following functions are to exist with the parameters as written
# the autograder may call these functions


def getNewDictionary(sbt, filename):
  sbt.clear()
  sbt.getFromFile(filename)
#   pass

def updateDictionary(sbt, filename):
  sbt.getFromFile(filename)
  # enter needed code here for command 2
  # pass

# TODO Check if it is correct
def setupLetters(sbt, letters):
  # enter needed code here for command 3

  filteredLetters = ""

  for ch in letters:
     if ch.isalpha():
      filteredLetters += ch.lower()
  
  if len(filteredLetters) != 7 or len(set(filteredLetters)) != 7:
    return False
  
  sbt.central = filteredLetters[0]
  sbt.others = sorted(filteredLetters[1:])

  sbt.found.clear()
  sbt.score = 0
  sbt.pangramFound = False
  sbt.bingoFound = False
  sbt.seenFirstLetter.clear()

  return True


def showLetters(sbt):
  # enter needed code here for command 4
  letters = sbt.getLetters()
  
  if len(letters) != 7:
     return

  centralLetter = letters[0]
  otherLetters = letters[1:]

  print(f"Central Letter: {centralLetter}")
  print(f"6 Other Letters: {','.join(otherLetters)}")


def attemptWord(sbt, word):
  # enter needed code here for command 5
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

  # Err checked insert the word into found trie.
  sbt.found.insert(wrd)
  # Incrament the score
  sbt.score += points


  pang = sbt.isPangram(wrd)
  if pang:
    sbt.pangramFound = True
  
  bingoAgain = False
  if wrd:
    sbt.seenFirstLetter.add(wrd[0])
    if not sbt.bingoFound and len(sbt.seenFirstLetter) == 7:
      sbt.bingFound = True
      bingoAgain = True

  report = ""
  unit = "point" if points == 1 else "points"
  total_unit = "point" if sbt.score == 1 else "points"

  report += f"found {wrd} {points} {unit}, total {sbt.score} {total_unit}"
  if pang:
    report += f", Pangram found"
    
  if bingoAgain:
    report += f", Bingo scored"
    
  print(report)
  
  


def showFoundWords(sbt):
  # enter needed code here for command 6
  pass

def showAllWords(sbt):
  
  toPrint = sbt.words()
  for word in toPrint:
     print(word)
  # enter needed code here for command 7
  pass

# def showAllWords(sbt):
  
#   # enter needed code here for command 7
#   pass

def displayCommands():
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
    #print ("Debug 0:" + line + "***" + command + "***")
    
    # clear input from any previous value
    args = ""


    if(command == '1'):
        args = line[1:].strip()
        #print ("Debug 1:" + args + "***")
        # getNewDictionary(sbt, args)
        getNewDictionary(sbt, args)

    if(command == '2'):
        args = line[1:].strip()
        #print( "Debug 2:" + args + "***")
        updateDictionary(sbt, args)
        
    if(command == '3'):
        args = line[1:].strip()
        #print( "Debug 3:" + args + "***")
        if setupLetters(sbt, args) == False:
          print("Invalid letter set")
          continue
        

    if(command == '4'):
        showLetters(sbt)

    if(command == '5'):
        args = line[1:].strip()
        #print ( "Debug 5:" + args + "***")
        attemptWord(sbt, args)

    if(command == '6'):
        showFoundWords(sbt)

    if(command == '7'):
        # showAllWords(sbt)
        showAllWords(sbt)

    
    if(command == '8' or command == '?'):
        displayCommands()
    
    if(command == '9' or command == 'q'):
        break
    

  return
  
if __name__ == "__main__":
  spellingBee()