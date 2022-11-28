
import json

class ALUInputData:
    def __init__(self,sourceregister1,sourceregister2):
        self.sourceregister1 = sourceregister1
        self.sourceregister2 =sourceregister2

    def ALUInputData(self):
         with open('registers.json', 'r') as openfile:
 
    # Reading from json file
          registers = json.load(openfile)
          inputdata1 = registers[str(self.sourceregister1)]
          inputdata2 = registers[str(self.sourceregister2)]
          
          return inputdata1,inputdata2

        