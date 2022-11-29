import SignExtender

class RegisterFile:

    def __init__(self,instructionType,instruction):
        self.instructionType =instructionType
        # self.sourceRegister1 =sourceRegister1
        # self.sourceRegister2 =sourceRegister2
        # self.destinationRegister =destinationRegister
        self.instruction =instruction
        # self.immediateData =immediateData

    def checkRegistersforExceution(self):
        immediateData=[]
        sourceRegister2=[]

        if self.instructionType == "R-type Instruction":
            sourceRegister1=self.instruction[6:11]
            sourceRegister2 =self.instruction[11:16]
            destination = self.instruction[16:21]


        else:
            sourceRegister1=self.instruction[6:11]
            #sourceRegister2 = []
            destination = self.instruction[11:16]
            immediateData = self.instruction[16:]
            immediateData = SignExtender.SignExtender(immediateData).BitSExtention()

        return sourceRegister1,sourceRegister2,immediateData,destination

