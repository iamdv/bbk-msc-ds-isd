import os as os

#================================================================
def isWordCharacter(ch) :
  
      return (ch >= "A" and ch <= "Z" or ch >= "a" and ch <= "z")
#================================================================

#================================================================
def getFullLineComments(filename) :
   myLineCounter = 0
   myFile = open(filename, 'r')
   myOutputDictionary = {}

   for myLine in myFile :
      myLineCounter = myLineCounter + 1
      if (myLine.find('#') >= 0) :
         if (myLine.lstrip()[0] == '#') :
            myOutputDictionary[myLineCounter] = myLine.strip()

   myFile.close()
   return myOutputDictionary
# print(getFullLineComments('pythoncode.py'))
#================================================================

#================================================================
def countFullLineComments(filename) :
   return len(getFullLineComments(filename))
# print(countFullLineComments('pythoncode.py'))
#================================================================

#================================================================
def readInRealWords(filename):
   myInputFile = open(filename, 'r')
   myLoopCounter = 0
   myOutputSet = set()
   myCurrentLine = myInputFile.readline()

   while myCurrentLine != '':
      myLoopCounter = myLoopCounter + 1
      myOutputSet.add(myCurrentLine[7 + len(str(myLoopCounter)) : ].strip().lower())
      myCurrentLine = myInputFile.readline()

   myInputFile.close()
   return myOutputSet
# print(len(readInRealWords('linenumberwords.txt')))
#================================================================

#================================================================
def getWord(s):
   myInputString = str(s).rstrip()
   myStringIndexList = []
   myLoopCounter = 0

   for myChar in myInputString:
      myLoopCounter = myLoopCounter + 1
      if (isWordCharacter(myChar)):
         myStringIndexList.append(myLoopCounter)

   if len(myStringIndexList) == 0:
      return ' '
   else:
      return myInputString[min(myStringIndexList) - 1: max(myStringIndexList) ]

# print(getWord(" !,Word’s** "))
# print(getWord(" !,Word’** "))
# print(getWord(" !,’** "))
# print(getWord(" !,’** dog'"" \\'''"))
#================================================================

#================================================================
def convertLineToWordHelper(inputDictionary, outputFormat) :
   myOutputSet = set()
   myValueKeyPair = {}

   for myKey, myValue in inputDictionary.items():
      for eachWord in myValue.split():
         myOutputSet.add(getWord(eachWord).lower())
         myValueKeyPair[getWord(eachWord).lower()] = myKey

   myOutputSet.remove(' ')

   if outputFormat == 'set' :
      return myOutputSet
   elif outputFormat == 'dict' :
      return myValueKeyPair
#================================================================

#================================================================
def spellCheckComments(filename,correctlySpelledWords) :
   # readInRealWords() function is created as part of question 3 and
   # it returns set of correctly spelled words
   myCorrectlySpelledWordSet = readInRealWords(correctlySpelledWords)

   # getFullLineComments is a helper function which returns only commented
   # lines front the code
   myCommentWordsDictionary = getFullLineComments(filename)

   # Converts dictionary values into Set
   myCommentWordSet = convertLineToWordHelper(myCommentWordsDictionary, 'set')

   # Checking if all comment words are part of correctly spelled words
   # and returns a set of incorrect words
   myIncorrectWords = myCommentWordSet - myCorrectlySpelledWordSet

   # convertLineToWordHelper() function returns a dictionary where words are keys
   # and the line numbers of the words are the Values
   myValueKeyPairDict = convertLineToWordHelper(myCommentWordsDictionary, 'dict')

   # Removing empty set element
   myOutput = {}

   # Looping through each incorrect word and also checking if the
   # key (line number) already exist in the output dictionary.
   # If the key (line number) exists then we append the value to the existing list
   # If the key (line number) doesn't exist then we create a dictionary element
   for eachWord in myIncorrectWords :
      if(myValueKeyPairDict[eachWord] in myOutput) :
         myOutput[myValueKeyPairDict[eachWord]].append(eachWord)
      else :
         myOutput[myValueKeyPairDict[eachWord]] = [eachWord]

   return myOutput
# print(spellCheckComments('pythoncode.py', 'linenumberwords.txt'))
#================================================================


#================================================================

def RobustSpellCheck(filenamePy,filenameWords):
   #To Complete
   return()


def ExtractComment(s):
   #To Complete
   return()
     
def ExtractCommentAdvanced(s):
   #To Complete
   return()

