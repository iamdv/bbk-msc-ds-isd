def isWordCharacter(ch) :
  
      return (ch >= "A" and ch <= "Z" or ch >= "a" and ch <= "z") 
  

def countFullLineComments(filename) :
   myEachLine = ''
   myHashCounter = 0
   
   # Open the file and extract only lines with comments ('#')
   # Get the len 
   myFile = open(filename, 'r')
   for myLine in myFile:
      if(myLine.find('#') >= 0) :         
         if (myLine.lstrip()[0] == '#') :
            myHashCounter = myHashCounter + 1
   myFile.close()
   return myHashCounter

print(countFullLineComments('pythoncode.py'))

def readInRealWords(filename):
   #To Complete
   return()

def spellCheckComments(filename,correctlySpelledWords) :
   #To Complete
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

