class ID:
    def __init__(self,instruction):
        self.instruction =instruction
    

    def decodeInstruction(instruction):
        if instruction[:6] == "000000":
            instructionType = "R-type Instruction"
 
            if "".join(instruction[26:] )==  "00100000":   #ADD instruction
                opcode = "000001"
            if "".join(instruction[26:] )==  "00100100":    #AND instruction
                opcode = "000010"
            if "".join(instruction[26:] )==  "00100101":     #OR
                opcode = "000011"
            if "".join(instruction[26:] )==  "00101010":     #slt
                opcode = "000100"
            if "".join(instruction[26:] )==  "00100010":     #sub
                opcode = "000101"
           
        else:
            instructionType = "I-type Instruction"

            if "".join(instruction[26:] )==  "00001000":   #ADD instruction
                opcode = "000001"
            if "".join(instruction[26:] )==  "00001100":    #AND instruction
                opcode = "000010"
            if "".join(instruction[26:] )==  "00001101":     #OR
                opcode = "000011"
            if "".join(instruction[26:] )==  "00001010":     #slt
                opcode = "000100"
            if "".join(instruction[26:] )==  "00101011":     #sw
                opcode = "000011"
            if "".join(instruction[26:] )==  "00100011":     #lw
                opcode = "000111"
            
        
        print("Type of Instruction", instructionType)

        return opcode,instructionType