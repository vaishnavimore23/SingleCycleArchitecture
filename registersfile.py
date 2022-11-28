class RegisterFile:

    def __init__(self,instructionType,sourceRegister1,sourceRegister2,destinationRegister,instruction,immediateData):
        self.instructionType =instructionType
        self.sourceRegister1 =sourceRegister1
        self.sourceRegister2 =sourceRegister2
        self.destinationRegister =destinationRegister
        self.instruction =instruction
        self.immediateData =immediateData

    def checkRegistersforExceution(self):
        if self.instructionType == "R-type Instruction":
            sourceRegister1=self.instruction[6:11]
            sourceRegister2 =self.instruction[11:16]
            destinationRegister = self.instruction[16:21]


        else:
            sourceRegister1=self.instruction[6:11]
            #sourceRegister2 =instruction[11:16]
            destinationRegister = self.instruction[11:16]
            immediateData = self.instruction[16:]

        return sourceRegister1,sourceRegister2,destinationRegister,self.instruction,immediateData

