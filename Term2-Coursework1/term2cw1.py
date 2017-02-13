## Name: Deepak Vadithala
## Course: MSc Data Science
## Submission Date: 13-Feb-2017

## Please note: Inline comments explains the reasoning and the logic
## Also, I have written test cases within each function. 
## You can uncomment to test these cases. And I have used two helper
## function instead of repeating the code.

##================================================================
import os as os


##================================================================
def isWordCharacter(ch) :
  
      return (ch >= "A" and ch <= "Z" or ch >= "a" and ch <= "z")
##================================================================


##================================================================
def getFullLineComments(filename) :
# Please note: This is a helper function which used as an input 
# into other functions. This function returns ONLY full comment lines 
   myLineCounter = 0
   myFile = open(filename, 'r')
   myOutputDictionary = {}

# Loops through each line in the file and looks for only the commented
# lines. And stored the commented lines along with the line number in 
# the dictionary
   for myLine in myFile :
      myLineCounter = myLineCounter + 1
      if (myLine.find('#') >= 0) :
         if (myLine.lstrip()[0] == '#') :
            myOutputDictionary[myLineCounter] = myLine.strip()

   myFile.close()

   return myOutputDictionary
# print(getFullLineComments('pythoncode.py'))
##================================================================


##================================================================
def countFullLineComments(filename) :
# Using getFullLineComments() which is define above
   return len(getFullLineComments(filename))
# print(countFullLineComments('pythoncode.py'))
##================================================================


##================================================================
def readInRealWords(filename):
   myInputFile = open(filename, 'r')
   myLoopCounter = 0
   myOutputSet = set()
   myCurrentLine = myInputFile.readline()

# Looping through each line and storing iteration number in
# the myLoopCounter variable. And myLoopCounter variable's length 
# is used to determine the index of the words.
   while myCurrentLine != '':
      myLoopCounter = myLoopCounter + 1
      myOutputSet.add(myCurrentLine[7 + len(str(myLoopCounter)) : ].strip().lower())
      myCurrentLine = myInputFile.readline()

   myInputFile.close()
   
   return myOutputSet
# print(len(readInRealWords('linenumberwords.txt')))
##================================================================


##================================================================
def getWord(s):
   myInputString = str(s).rstrip()
   myStringIndexList = []
   myLoopCounter = 0

# Using isWordCharacter() to evaluate each character in the input string 
# and isWordCharacter() returns True or False. Storing the index position
# of each character in myStringIndexList and then using min and max
# to get the index position.

   for myChar in myInputString:
      myLoopCounter = myLoopCounter + 1
      if (isWordCharacter(myChar)):
         myStringIndexList.append(myLoopCounter)

   if len(myStringIndexList) == 0:
      return ' '
   else:
      return myInputString[min(myStringIndexList) - 1: max(myStringIndexList) ]

# Some unit test cases. Please uncomment the print statements to test.

# print(getWord(" !,Word’s** "))
# print(getWord(" !,Word’** "))
# print(getWord(" !,’** "))
# print(getWord(" !,’** dog'"" \\'''"))
##================================================================


##================================================================
def convertLineToWordHelper(inputDictionary, outputFormat) :

# Helper function which returns dictionary/set based on the outputFormat
# This function is used in Q4 or spellCheckComments()

   myOutputSet = set()
   myValueKeyPair = {}
   myLowerUpperWordsDict = {}

   for myKey, myValue in inputDictionary.items():
      for eachWord in myValue.split():
         myOutputSet.add(getWord(eachWord).lower())
         myValueKeyPair[getWord(eachWord).lower()] = myKey
         myLowerUpperWordsDict[getWord(eachWord).lower()] = getWord(eachWord)
   # print(myLowerUpperWordsDict)

   myOutputSet.remove(' ')

   if outputFormat == 'set' :
      return myOutputSet
   elif outputFormat == 'valueKey' :
      return myValueKeyPair
   elif outputFormat == 'lowerUpper' :
      return myLowerUpperWordsDict
##================================================================


##================================================================
def spellCheckComments(filename,correctlySpelledWords) :
   # Notes: Instead of repeating the code. I have used functions
   # 1, 2 and 3 along with the helper functions. T

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
   myLowerUpperWordsDict = convertLineToWordHelper(myCommentWordsDictionary, 'lowerUpper')

   # myTempDict returns the line number and the incorrect words as key value pairs
   # myOutput will sort the list elements in ascending order and returns 
   myTempDict = {}
   myOutput = {}

   # Looping through each incorrect word and also checking if the
   # key (line number) already exist in the output dictionary.
   # If the key (line number) exists then we append the value to the existing list
   # If the key (line number) doesn't exist then we create a dictionary element
   for eachWord in myIncorrectWords :
      if(myValueKeyPairDict[(eachWord)] in myTempDict) :
         myTempDict[myValueKeyPairDict[eachWord]].append(myLowerUpperWordsDict[eachWord])
      else :
         myTempDict[myValueKeyPairDict[eachWord]] = sorted([myLowerUpperWordsDict[eachWord]])

   for myKey, myValue in myTempDict.items():
      myOutput[myKey] = sorted(myValue)
      # print(sorted(myValue))

   return myOutput
# print(spellCheckComments('pythoncode.py', readInRealWords('linenumberwords.txt')))

##================================================================


##================================================================
def RobustSpellCheck(filenamePy,filenameWords):
   if(os.path.isfile(filenamePy) and os.path.isfile(filenameWords)) :
      return [0, spellCheckComments(filenamePy, readInRealWords(filenameWords))]
   elif(os.path.isfile(filenamePy)) :
      print('Could not successfully read in word list')
      return [1, {}]
   elif(os.path.isfile(filenameWords)) :
      print('Could not successfully spell check the selected file')
      return [2, {}]
   elif(not os.path.isfile(filenameWords and not os.path.isfile(filenameWords)) ) :
      print('Could not successfully check both the files')
      return [3, {}]

##  Unit test cases covering all the scenarios
# print(RobustSpellCheck('pythoncode.py','linenumberwords.txt')) # Both the files are available
# print(RobustSpellCheck('pythoncode.py','linenumber----.txt')) # World file is missing
# print(RobustSpellCheck('pythons.pys','linenumberwords.txt')) # Python file is missing
# print(RobustSpellCheck(' ','li nusdfsdfs.txts')) # Both the files are missing
##================================================================


##================================================================
def getCommentsHelper(inputString, quoteType) :
# This function accepts but single and double quotes as second paramter
# Logic: Function finds the single/double quote pairs and 
# then replaces the quotes with (|) characters. 
# This way we will find the real comment's start position.

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
##================================================================     


##================================================================
def ExtractComment(s):
   return getCommentsHelper(s, '"')
##================================================================  


##================================================================
def ExtractCommentAdvanced(s):   
   if(s.count('"')) > 0 :
      myOutputString = getCommentsHelper(s, '"')
   elif(s.count("'")) > 0 :
      myOutputString = getCommentsHelper(s, "'")
   elif(s.count('"') + s.count("'")) == 0 and s.count('#') > 0 :
      return s.strip()
   elif(s.count('"') + s.count("'")) == 0 and s.count('#') == 0 :
      return ''   
   return myOutputString

# Some unit test cases with single, double and no quotes. 
# These test cases also includes where we have some extra spaces.
# Please uncomment below print statements to execute the test cases.

# print(ExtractCommentAdvanced('         outf.write("/# " + str(number) + " #/ " + line) #lots of hash(#) symbols here'))
# print(ExtractCommentAdvanced("         outf.write('/# ' + str(number) + ' #/ ' + line) #lots of hash(#) symbols here"))
# print(ExtractCommentAdvanced("    #lots of hash(#) symbols here"))
# print(ExtractCommentAdvanced("  ''  '' #lots of hash(#) symbols here"))
# print(ExtractCommentAdvanced('  #lots of hash(#) symbols here'))
# print(ExtractCommentAdvanced('         outf.write(str(number) + line'))
##================================================================
