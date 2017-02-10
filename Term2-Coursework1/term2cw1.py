import os as os


def isWordCharacter(ch) :
  
      return (ch >= "A" and ch <= "Z" or ch >= "a" and ch <= "z") 


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

print(getFullLineComments('pythoncode.py'))

def countFullLineComments(filename) :
   return len(getFullLineComments(filename))


print(countFullLineComments('pythoncode.py'))



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

print(len(readInRealWords('linenumberwords.txt')))

def spellCheckComments(filename,correctlySpelledWords) :
   correctlySpelledWords = readInRealWords(filename)


   return()

      
def getWord(s):
   myInputString = str(s).rstrip()
   myStringIndexList = []
   myLoopCounter = 0

   for myChar in myInputString :
      myLoopCounter = myLoopCounter + 1
      if(isWordCharacter(myChar)) :
         myStringIndexList.append(myLoopCounter)

   if len(myStringIndexList) == 0 :
      return ' '
   else :
      return myInputString[ min(myStringIndexList) - 1 : max(myStringIndexList) ]

# print(getWord(" !,Word’s** "))
# print(getWord(" !,Word’** "))
# print(getWord(" !,’** "))
# print(getWord(" !,’** dog'"" \\'''"))
   

def RobustSpellCheck(filenamePy,filenameWords):
   #To Complete
   return()


def ExtractComment(s):
   #To Complete
   return()
     
def ExtractCommentAdvanced(s):
   #To Complete
   return()

