
class ControlUnit:
    def __init__(self,opcode):
        self.opcode=opcode
    def getALUOpKey(self):
        add_operation_opcode="000001"
        and_operation_opcode="000010"
        or_operation_opcode="000011"
        slt_operation_opcode="000100"
        sub_operation_opcode="000101"
       
        load_word_operation_opcode="000111"
        store_word_operation_opcode="001000"
        
        none_operating="000000"
        if (self.opcode==add_operation_opcode):
            return "Add"
        if (self.opcode==sub_operation_opcode):
            return "Sub"
        if (self.opcode==and_operation_opcode):
            return "And"
        if (self.opcode==or_operation_opcode):
            return "Or"
        if (self.opcode==slt_operation_opcode):
            return "Slt"
        
        if (self.opcode==load_word_operation_opcode):
            return "Lw"
        if (self.opcode==store_word_operation_opcode):
            return "Sw"
       
        if(self.opcode==none_operating):
            return "None"
        else:
            return "Undefined opcode"
