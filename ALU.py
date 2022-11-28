import BinaryToDecimal


class ALU:
    def __init__(self,firstInput,secondInput,immediatefield,destination,ALUopKey,instructionType) :
        self.firstInput=firstInput
        self.secondInput=secondInput
        self.immediatefield =immediatefield
        self.destination = destination
        self.ALUopKey =ALUopKey
        self.instructionType=instructionType


        def operation(self):
         if self.instructionType =="I-type Instruction":
           self.secondInput= immediatefield

         if(self.ALUopKey=="Add" or self.ALUopKey=="Lw" or self.ALUopKey=="Sw"):
            result=""
            carry=0
            for i in range(32):
                if(self.firstInput[32-i-1]=='0' and self.secondInput[32-i-1]=='0' and carry==0):
                    result='0'+result
                    carry=0
                elif(self.firstInput[32-i-1]=='0' and self.secondInput[32-i-1]=='0' and carry==1):
                    result='1'+result
                    carry=0
                elif(self.firstInput[32-i-1]=='1' and self.secondInput[32-i-1]=='0' and carry==0):
                    result='1'+result
                    carry=0
                elif(self.firstInput[32-i-1]=='1' and self.secondInput[32-i-1]=='0' and carry==1):
                    result='0'+result
                    carry=1
                elif(self.firstInput[32-i-1]=='0' and self.secondInput[32-i-1]=='1' and carry==0):
                    result='1'+result
                    carry=0
                elif(self.firstInput[32-i-1]=='0' and self.secondInput[32-i-1]=='1' and carry==1):
                    result='0'+result
                    carry=1
                elif(self.firstInput[32-i-1]=='1' and self.secondInput[32-i-1]=='1' and carry==0):
                    result='0'+result
                    carry=1
                elif(self.firstInput[32-i-1]=='1' and self.secondInput[32-i-1]=='1' and carry==1):
                    result='1'+result
                    carry=1
            return result,destination
                    

         if(self.ALUopKey=="Sub"):
            result=""
            for i in range(32):
                if(self.secondInput[32-i-1]=='1'):
                    result=self.secondInput[32-i-1]+result
                    for j in range(32-i-1):
                        if(self.secondInput[32-i-j-2]=='0'):
                            result='1'+result
                        else:
                            result='0'+result
                    break
                else:
                    result=self.secondInput[32-i-1]+result
            result_sub=""
            carry=0
            for i in range(32):
                if(self.firstInput[32-i-1]=='0' and result[32-i-1]=='0' and carry==0):
                    result_sub='0'+result_sub
                    carry=0
                elif(self.firstInput[32-i-1]=='0' and result[32-i-1]=='0' and carry==1):
                    result_sub='1'+result_sub
                    carry=0
                elif(self.firstInput[32-i-1]=='1' and result[32-i-1]=='0' and carry==0):
                    result_sub='1'+result_sub
                    carry=0
                elif(self.firstInput[32-i-1]=='1' and result[32-i-1]=='0' and carry==1):
                    result_sub='0'+result_sub
                    carry=1
                elif(self.firstInput[32-i-1]=='0' and result[32-i-1]=='1' and carry==0):
                    result_sub='1'+result_sub
                    carry=0
                elif(self.firstInput[32-i-1]=='0' and result[32-i-1]=='1' and carry==1):
                    result_sub='0'+result_sub
                    carry=1
                elif(self.firstInput[32-i-1]=='1' and result[32-i-1]=='1' and carry==0):
                    result_sub='0'+result_sub
                    carry=1
                elif(self.firstInput[32-i-1]=='1' and result[32-i-1]=='1' and carry==1):
                    result_sub='1'+result_sub
                    carry=1
            return result,destination

         if(self.ALUopKey=="And"):
            result=""
            for i in range (32):
                if(self.firstInput[32-i-1]=='1' and self.secondInput[32-i-1]=='1'):
                    result='1'+result
                else:
                    result='0'+result
            return result,destination
         if(self.ALUopKey=="Or"):
            result=""
            for i in range(32):
                if(self.firstInput[32-i-1]=='0' and self.secondInput[32-i-1]=='0'):
                    result='0'+result
                else:
                    result='1'+result
            return result,destination

         if(self.ALUopKey=="Slt"):
            result=""
            if(BinaryToDecimal.BinaryToDecimal(self.firstInput).BinaryToDecimal()<BinaryToDecimal.BinaryToDecimal(self.secondInput).BinaryToDecimal()):
                result="00000000000000000000000000000001"
            else:
                result="00000000000000000000000000000000"
            return result,destination