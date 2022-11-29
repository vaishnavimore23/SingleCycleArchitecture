import json
import BinaryToDecimal

class DataMemory:
    def __init__(self,ALUOpKey,result):
        self.ALUOpKey =ALUOpKey
        self.result= result
    
    def LoadAndStoreData(self):
        if self.ALUOpKey == "Lw":
          MemoryLocation = BinaryToDecimal.BinaryToDecimal(self.result).BinaryToDecimal()
         # print(type(MemoryLocation))
          print("Loading Memory .......")
          print("Memory Location to load:",MemoryLocation)
          with open('DataMemory.json', 'r') as openfile:
             Data_in_Memory = json.load(openfile)
             MemoryLocation =str(MemoryLocation)
             data_to_load_from_memory =  Data_in_Memory[MemoryLocation]
        return data_to_load_from_memory


        