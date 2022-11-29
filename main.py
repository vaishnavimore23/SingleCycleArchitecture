import ALU
import ALUInputData
import controlunit
import ID
import IF
import MemoryMapping
import PC
import registersfile
import BinaryToDecimal
import json
import DataMemory

def main():
    with open('instruction.json', 'r') as openfile:
             instruction_data = json.load(openfile)
    instruction_Addresses = list(instruction_data.keys())
    #print(instruction_data)
    for i in range(len(instruction_data)):
      currentaddress  = instruction_Addresses[i]
      print("currentaddress ",currentaddress)
     # currentaddress = "00000000000000000000000000000000"
      instruction = IF.IF(currentaddress).getinstruction()
      print("Binary form of instruction",instruction)
      opcode, instructiontype = ID.ID(instruction).decodeInstruction()
      print("Opcode: ",opcode)
      print("Instruction Type: ", instructiontype)
      ALUOPkey = controlunit.ControlUnit(opcode).getALUOpKey()
      print("ALU Operation: ",ALUOPkey)
      sourceRegister1,sourceRegister2,immediateData,destination =registersfile.RegisterFile(instructiontype,instruction).checkRegistersforExceution()
      register1=BinaryToDecimal.BinaryToDecimal(sourceRegister1).BinaryToDecimal()
      register2=BinaryToDecimal.BinaryToDecimal(sourceRegister2).BinaryToDecimal()
      destinationregister =BinaryToDecimal.BinaryToDecimal(destination).BinaryToDecimal()
      print("sourceRegister1",register1)
      print("sourceRegister2",register2)
   
      print("destination",destinationregister)
      inputdata1 , inputdata2 =ALUInputData.ALUInputData(register1,register2).ALUInputData()
      print("inputdata1",inputdata1)
      print("inputdata2",inputdata2)
      print("immediateData",immediateData)
      result = ALU.ALU(inputdata1,inputdata2,immediateData,ALUOPkey,instructiontype).operation()
      print("result",result)
      if ALUOPkey == "Lw":
        result = DataMemory.DataMemory(ALUOPkey,result).LoadAndStoreData()
      MemoryMapping.MemoryMapping(destinationregister,result,ALUOPkey).MemoryMapping()
      currentaddress = PC.ProgramCounter(currentaddress).addByFour()
    

if __name__ == "__main__":
    main()
