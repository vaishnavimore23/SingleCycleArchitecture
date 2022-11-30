
import json

class ALUInputData:
    def __init__(self,sourceregister1,sourceregister2,instructiontype):
        self.sourceregister1 = sourceregister1
        self.sourceregister2 =sourceregister2
        self.instructiontype =instructiontype

    def ALUInputData(self):
         inputdata2 =[]
         with open('registers.json', 'r') as openfile:
   
    # Reading from json file
          registers = json.load(openfile)
          if self.instructiontype == "R-type Instruction":
            inputdata1 = registers[str(self.sourceregister1)]
            inputdata2 = registers[str(self.sourceregister2)]
          else:
              inputdata1 = registers[str(self.sourceregister1)]
          return inputdata1,inputdata2

        