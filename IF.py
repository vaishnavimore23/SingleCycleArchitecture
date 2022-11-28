import json

class IF:
  def __init__(self,currentaddress):
    self.currentaddress =currentaddress

  def getinstruction(self):
   with open('instruction.json', 'r') as openfile:
 
    # Reading from json file
    instructionMemory = json.load(openfile)
    return instructionMemory[self.currentaddress]
    
    

  