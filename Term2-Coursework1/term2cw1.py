import os as os


def isWordCharacter(ch) :
  
      return (ch >= "A" and ch <= "Z" or ch >= "a" and ch <= "z") 


def countFullLineComments(filename) :
   myFile = open(filename, 'r')
   myLine = myFile.readline()
   myOutput = 0
   myListChecker = []
   while myLine :
      if(myLine.find('#') >= 0) :
         myString = list(myLine[0:myLine.index('#') + 1])
         print(myString)

      myLine = myFile.readline()
   myFile.close()
   return myOutput


# print(countFullLineComments('pythoncode.py'))



def readInRealWords(filename):
   myInputFile = open(filename, 'r')
   myLoopCounter = 0
   myOutputSet = set()
   myCurrentLine = myInputFile.readline()

   while myCurrentLine != '':
      myLoopCounter = myLoopCounter + 1
      myOutputSet.add(myCurrentLine[7 + len(str(myLoopCounter)) : ].strip().lower())
      myCurrentLine = myInputFile.readline()

   return myOutputSet


print(len(readInRealWords('linenumberwords.txt')))

def spellCheckComments(filename,correctlySpelledWords) :
   return()

      
def getWord(s):
   #To Complete
   return()
      
   

def RobustSpellCheck(filenamePy,filenameWords):
   #To Complete
   return()




def ExtractComment(s):
   #To Complete
   return()
     
def ExtractCommentAdvanced(s):
   #To Complete
   return()

