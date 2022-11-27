import DecimalToBinary

class ProgramCounter:

    def __init__(self,currentAddress):
        self.currentAddress = currentAddress

    def addByFour(self):
        self.currentAddress =  self.currentAddress+ DecimalToBinary.DecimalToBinary(4)
        print(self.currentAddress)
        return self.currentAddress
    
    