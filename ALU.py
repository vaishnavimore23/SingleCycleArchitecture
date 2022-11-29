import BinaryToDecimal


class ALU:
    def __init__(self,firstInput,secondInput,immediatefield,ALUopKey,instructionType) :
        self.firstInput=firstInput
        self.secondInput=secondInput
        self.immediatefield =immediatefield
       # self.destination = destination
        self.ALUopKey =ALUopKey
        self.instructionType=instructionType


    def operation(self):
         if self.instructionType =="I-type Instruction":
            self.secondInput= self.immediatefield

         if(self.ALUopKey=="Add" or self.ALUopKey=="Lw" or self.ALUopKey=="Sw"):
            result=[]
            carry=0
            for i in range(32):
                if(self.firstInput[32-i-1]==0 and self.secondInput[32-i-1]== 0 and carry==0):
                    result.append(0)
                    carry=0
                elif(self.firstInput[32-i-1]==0 and self.secondInput[32-i-1]==0 and carry==1):
                    result.append(1)
                    carry=0
                elif(self.firstInput[32-i-1]==1 and self.secondInput[32-i-1]==0 and carry==0):
                    result.append(1)
                    carry=0
                elif(self.firstInput[32-i-1]==1 and self.secondInput[32-i-1]==0 and carry==1):
                    result.append(0)
                    carry=1
                elif(self.firstInput[32-i-1]==0 and self.secondInput[32-i-1]==1 and carry==0):
                    result.append(1)
                    carry=0
                elif(self.firstInput[32-i-1]==0 and self.secondInput[32-i-1]==1 and carry==1):
                    result.append(0)
                    carry=1
                elif(self.firstInput[32-i-1]==1 and self.secondInput[32-i-1]== 1 and carry==0):
                    result.append(0)
                    carry=1
                elif(self.firstInput[32-i-1]==1 and self.secondInput[32-i-1]==1 and carry==1):
                    result.append(1)
                    carry=1
            
            return list(reversed(result))
                    

         if(self.ALUopKey=="Sub"):
            result=[]
            for i in range(32):
                if(self.secondInput[32-i-1]==1):
                    result.append(self.secondInput[32-i-1])
                    for j in range(32-i-1):
                        if(self.secondInput[32-i-j-2]==0):
                            result.append(1)
                        else:
                            result.append(0)
                    break
                else:
                    result.append(self.secondInput[32-i-1])
            
            result_sub=[]
            carry=0
            for i in range(32):
                if(self.firstInput[32-i-1]==0 and result[32-i-1]==0 and carry==0):
                    result_sub.append(0)
                    carry=0
                elif(self.firstInput[32-i-1]==0 and result[32-i-1]==0 and carry==1):
                    result_sub.append(1)
                    carry=0
                elif(self.firstInput[32-i-1]==1 and result[32-i-1]==0 and carry==0):
                    result_sub.append(1)
                    carry=0
                elif(self.firstInput[32-i-1]==1 and result[32-i-1]==0 and carry==1):
                    result_sub.append(0)
                    carry=1
                elif(self.firstInput[32-i-1]==0 and result[32-i-1]==1 and carry==0):
                    result_sub.append(1)
                    carry=0
                elif(self.firstInput[32-i-1]==0 and result[32-i-1]==1 and carry==1):
                    result_sub.append(0)
                    carry=1
                elif(self.firstInput[32-i-1]==1 and result[32-i-1]==1  and carry==0):
                    result_sub.append(0)
                    carry=1
                elif(self.firstInput[32-i-1]==1 and result[32-i-1]==1 and carry==1):
                    result_sub.append(1)
                    carry=1
            return result_sub

         if(self.ALUopKey=="And"):
            result=[]
            for i in range (32):
                if(self.firstInput[32-i-1]==1 and self.secondInput[32-i-1]==1):
                    result.append(1)
                else:
                   result.append(0)
            return result
         if(self.ALUopKey=="Or"):
            result=[]
            for i in range(32):
                if(self.firstInput[32-i-1]==0 and self.secondInput[32-i-1]==0):
                    result.append(0)
                else:
                    result.append(1)
            return result

         if(self.ALUopKey=="Slt"):
            result=[]
            if(BinaryToDecimal.BinaryToDecimal(self.firstInput).BinaryToDecimal()<BinaryToDecimal.BinaryToDecimal(self.secondInput).BinaryToDecimal()):
                result=[0,0,0,0,0,0,0,0,00,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
            else:
                result=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            return result