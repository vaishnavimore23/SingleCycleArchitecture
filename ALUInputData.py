
import json

class ALUInputData:
    def __init__(self,input1,input2):
        self.input1 = input1
        self.input2 =input2

    def ALUInputData(inputdata1,inputdata2,sourceregister1,sourceregister2,immediateField):
         with open('registers.json', 'r') as openfile:
 
    # Reading from json file
          registers = json.load(openfile)
          inputdata1 = registers[sourceregister1]
          inputdata2 = registers[sourceregister2]
          
          return inputdata1,inputdata2,immediateField

        