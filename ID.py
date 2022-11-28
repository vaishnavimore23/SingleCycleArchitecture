class ID:
    def __init__(self,instruction):
        self.instruction =instruction
    

    def decodeInstruction(self):
        opcode = ""
      
        if "".join(map(str, self.instruction[:6])) == "000000":
            
            instructionType = "R-type Instruction"
            
 
            if "".join(map(str,  self.instruction[26:]))==  "100000":   #ADD instruction
                opcode = "000001"
                return opcode,instructionType
            if "".join(map(str, self.instruction[26:]) )==  "100100":    #AND instruction
                opcode = "000010"
                return opcode,instructionType
            if "".join(map(str, self.instruction[26:]) )==  "100101":     #OR
                opcode = "000011"
                return opcode,instructionType
            if "".join(map(str, self.instruction[26:]) )==  "101010":     #slt
                opcode = "000100"
                return opcode,instructionType
            if "".join(map(str, self.instruction[26:]) )==  "100010":     #sub
                opcode = "000101"
                return opcode,instructionType
            
        else:
            instructionType = "I-type Instruction"
           

            if "".join(map(str, self.instruction[26:]))==  "001000":   #ADD instruction
                opcode = "000001"
                return opcode,instructionType
            if "".join(map(str, self.instruction[26:]) )==  "001100":    #AND instruction
                opcode = "000010"
                return opcode,instructionType
            if "".join(map(str, self.instruction[26:]) )==  "001101":     #OR
                opcode = "000011"
                return opcode,instructionType
            if "".join(map(str, self.instruction[26:]) )==  "001010":     #slt
                opcode = "000100"
                return opcode,instructionType
            if "".join(map(str, self.instruction[26:]) )==  "101011":     #sw
                opcode = "000011"
                return opcode,instructionType
            if "".join(map(str, self.instruction[26:]) )==  "00100011":     #lw
                opcode = "000111"
                return opcode,instructionType
            
            
        
       

       