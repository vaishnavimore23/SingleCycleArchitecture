import DecimalToBinary
import BinaryToDecimal

class ProgramCounter:

    def __init__(self,currentAddress):
        self.currentAddress = currentAddress

    def addByFour(self):
        self.currentAddress = BinaryToDecimal.BinaryToDecimal(self.currentAddress).BinaryToDecimal()  + 4
       # print( DecimalToBinary.DecimalToBinary( self.currentAddress).DecimalToBinary())
        return DecimalToBinary.DecimalToBinary( self.currentAddress).DecimalToBinary()
    
    