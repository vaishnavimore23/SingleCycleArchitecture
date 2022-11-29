import json

class MemoryMapping:
    def __init__(self,destination,result,ALUOPkey):
        self.destination=destination
        self.result=result
        self.ALUOPkey =ALUOPkey

    def MemoryMapping(self):

        if(self.ALUOPkey == "Sw" ):
          dictonary ={self.destination:self.result}
          json_obj = json.dumps(dictonary,indent=1)
          with open ("DataMemory.json","w") as outputfile:
            outputfile.write(json_obj)
  
        else:
            print("data writting  to Register File.........")
            with open('registers.json', 'r') as openfile:
             registerFile_data = json.load(openfile)
             
           
            registerFile_data[self.destination]=self.result

            json_obj = json.dumps(registerFile_data,indent=1)
            with open ("registers.json","w") as outputfile:
               outputfile.write(json_obj)
              # print("data written to Register File.........")

    