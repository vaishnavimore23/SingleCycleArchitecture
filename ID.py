class ID:
    def __init__(self,instruction):
        self.instruction =instruction
    

    def decodeInstruction(self):
        controlSignal = ""
      
        if "".join(map(str, self.instruction[:6])) == "000000":
            
            instructionType = "R-type Instruction"
            
 
            if "".join(map(str,  self.instruction[26:]))==  "100000":   #ADD instruction
                controlSignal = "000001"
                opcode = "100000"

                return controlSignal,instructionType,opcode
            if "".join(map(str, self.instruction[26:]) )==  "100100":    #AND instruction
                controlSignal = "000010"
                opcode = "100100"
                return controlSignal,instructionType,opcode
            if "".join(map(str, self.instruction[26:]) )==  "100101":     #OR
                controlSignal = "000011"
                opcode ="100101"
                return controlSignal,instructionType,opcode
            if "".join(map(str, self.instruction[26:]) )==  "101010":     #slt
                controlSignal = "000100"
                opcode="101010"
                return controlSignal,instructionType,opcode
            if "".join(map(str, self.instruction[26:]) )==  "100010":     #sub
                controlSignal = "000101"
                opcode ="100010"
                return controlSignal,instructionType,opcode
            
        else:
            instructionType = "I-type Instruction"
           

            if "".join(map(str, self.instruction[:6]))==  "001000":   #ADDi instruction
                controlSignal = "000001"
                opcode ="001000"
                return controlSignal,instructionType,opcode
            if "".join(map(str, self.instruction[:6]) )==  "001100":    #ANDi instruction
                controlSignal = "000010"
                opcode=  "001100"
                return controlSignal,instructionType,opcode
            if "".join(map(str, self.instruction[:6]) )==  "001101":     #ORi
                controlSignal = "000011"
                opcode= "001101"
                return controlSignal,instructionType,opcode
            if "".join(map(str, self.instruction[:6]) )==  "001010":     #slti
                controlSignal = "000100"
                opcode ="001010"
                return controlSignal,instructionType,opcode
            if "".join(map(str, self.instruction[:6]) )==  "101011":     #sw
                controlSignal = "001000"
                opcode= "101011"
                return controlSignal,instructionType,opcode
            if "".join(map(str, self.instruction[:6]) )==  "100011":     #lw
                controlSignal = "000111"
                opcode =  "100011"
                return controlSignal,instructionType,opcode
            
            
        
       

       