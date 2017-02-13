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
   myLowerUpperWordsDict = {}

   for myKey, myValue in inputDictionary.items():
      for eachWord in myValue.split():
         myOutputSet.add(getWord(eachWord).lower())
         myValueKeyPair[getWord(eachWord).lower()] = myKey
         myLowerUpperWordsDict[getWord(eachWord)] = getWord(eachWord)

   myOutputSet.remove(' ')

   if outputFormat == 'set' :
      return myOutputSet
   elif outputFormat == 'valueKey' :
      return myValueKeyPair
   elif outputFormat == 'lowerUpper' :
      return myLowerUpperWordsDict
#================================================================

#================================================================
def spellCheckComments(filename,correctlySpelledWords) :
   myCorrectlySpelledWordSet = correctlySpelledWords

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
   myValueKeyPairDict = convertLineToWordHelper(myCommentWordsDictionary, 'valueKey')
   # myLowerUpperWords = convertLineToWordHelper(myCommentWordsDictionary, 'lowerUpper')

   myOutput = {}

   # Looping through each incorrect word and also checking if the
   # key (line number) already exist in the output dictionary.
   # If the key (line number) exists then we append the value to the existing list
   # If the key (line number) doesn't exist then we create a dictionary element
   for eachWord in myIncorrectWords :
      print(eachWord)
      print(type(eachWord))
      if(myValueKeyPairDict[(eachWord)] in myOutput) :
         myOutput[myValueKeyPairDict[eachWord]].append([myValueKeyPairDict[eachWord]])
      else :
         myOutput[myValueKeyPairDict[eachWord]] = [eachWord]

   return  myOutput
# print(spellCheckComments('pythoncode.py', readInRealWords('linenumberwords.txt')))
#================================================================


#================================================================

def RobustSpellCheck(filenamePy,filenameWords):
   #To Complete
   return()


def getCommentsHelper(inputString, quoteType) :
   myInputString = inputString
   myQuoteType = quoteType
   myTotalIterations = int(myInputString.count(myQuoteType) / 2)

   for eachIteration in range(1, myTotalIterations + 1, 1) :
      myInputSubStringStartPos = myInputString.find(myQuoteType)
      myInputSubStringEndPos = myInputString.find(myQuoteType, myInputString.find(myQuoteType) + 1 ) + 1
      myInputStringLen = len(myInputString[myInputSubStringStartPos : myInputSubStringEndPos])
      myInputString = myInputString.replace(myInputString[myInputSubStringStartPos : myInputSubStringEndPos] , '|' * myInputStringLen, 1)
      
   if(myInputString.count('#') == 0) :
      return ''
   else :
      return inputString[myInputString.find('#') : ]

def ExtractComment(s):
   return getCommentsHelper(s, '"')

def ExtractCommentAdvanced(s):   
   if(s.count('"')) > 0 :
      myOutputString = getCommentsHelper(s, '"')
   elif(s.count("'")) > 0 :
      myOutputString = getCommentsHelper(s, "'")
   elif(s.count('"') + s.count("'")) == 0 and s.count('#') > 0 :
      return s
   elif(s.count('"') + s.count("'")) == 0 and s.count('#') == 0 :
      return ''   
   return myOutputString

# print(ExtractCommentAdvanced('         outf.write("/# " + str(number) + " #/ " + line) #lots of hash(#) symbols here'))
# print(ExtractCommentAdvanced("         outf.write('/# ' + str(number) + ' #/ ' + line) #lots of hash(#) symbols here"))
# print(ExtractCommentAdvanced("#lots of hash(#) symbols here"))
# print(ExtractCommentAdvanced('         outf.write(str(number) + line'))
