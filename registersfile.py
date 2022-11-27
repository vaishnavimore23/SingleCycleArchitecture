class RegisterFile:

    def __init__(self,instructionType,sourceRegister1,sourceRegister2,destinationRegister,instruction,immediateData):
        self.instructionType =instructionType
        self.sourceRegister1 =sourceRegister1
        self.sourceRegister2 =sourceRegister2
        self.destinationRegister =destinationRegister
        self.instruction =instruction
        self.immediateData =immediateData

    def checkRegistersforExceution(instructionType,sourceRegister1,sourceRegister2,destinationRegister,instruction,immediateData):
        if instructionType == "R-type Instruction":
            sourceRegister1=instruction[6:11]
            sourceRegister2 =instruction[11:16]
            destinationRegister = instruction[16:21]


        else:
            sourceRegister1=instruction[6:11]
            #sourceRegister2 =instruction[11:16]
            destinationRegister = instruction[11:16]
            immediateData = instruction[16:]

        return sourceRegister1,sourceRegister2,destinationRegister,instruction,immediateData

