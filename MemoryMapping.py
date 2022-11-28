import json

class MemoryMapping:
    def __init__(self,destination,result,ALUOPkey):
        self.destination=destination
        self.result=result
        self.ALUOPkey =ALUOPkey

    def MemoryMapping(self):
        
        if(self.ALUOPkey == "lw" or self.ALUOPkey == "sw" ):
          dictonary ={self.destination:self.result}
          json_obj = json.dumps(dictonary,indent=1)
          with open ("DataMemory.json","w") as outputfile:
            outputfile.write(json_obj)
  
        else:
            print("data writting  to json file")
            dictonary ={self.destination:self.result}
            json_obj = json.dumps(dictonary,indent=1)
            with open ("registers.json","w") as outputfile:
               outputfile.write(json_obj)
               print("data written to json file")

    