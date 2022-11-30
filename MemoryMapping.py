import json
import BinaryToDecimal

class MemoryMapping:
    def __init__(self,destination,result,ALUOPkey):
        self.destination=destination
        self.result=result
        self.ALUOPkey =ALUOPkey

    def MemoryMapping(self):

        if(self.ALUOPkey == "Sw" ):
          
          with open('registers.json', 'r') as openfile:
             registerFile_data = json.load(openfile)
             
             destination_reg_data = registerFile_data[str(self.destination)]
             print("Data in Register Rt",destination_reg_data)
          with open('DataMemory.json', 'r') as datamemory:
             Data_in_Memory = json.load(datamemory)
             MemoryLocation_in_DataMemory = BinaryToDecimal.BinaryToDecimal(self.result).BinaryToDecimal()
             Data_in_Memory[MemoryLocation_in_DataMemory]=destination_reg_data
          json_obj1 = json.dumps(Data_in_Memory,indent=1)
          with open ("DataMemory.json","w") as outputfile:
            outputfile.write(json_obj1)
          print("Writing  to Data Memory File.........")
          print("Check DataMemory.json")
  
        else:
            print("Writing  to Register File.........")
           
            with open('registers.json', 'r') as openfile:
             registerFile_data = json.load(openfile)
             
           
            registerFile_data[self.destination]=self.result

            json_obj = json.dumps(registerFile_data,indent=1)
            with open ("registers.json","w") as outputfile:
               outputfile.write(json_obj)
              # print("data written to Register File.........")

    