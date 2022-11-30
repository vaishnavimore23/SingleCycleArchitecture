class SignExtender:
    def __init__(self,ImmedidateField):
        self.ImmedidateField =ImmedidateField

    def BitSExtention(self):
        extensionBits= []
        for i in range(16):
           extensionBits.append(0)
           
        for i in range(len(self.ImmedidateField)):
            extensionBits.append(self.ImmedidateField[i])
        
        #print("signed extended data: ",extensionBits)
        return extensionBits

        