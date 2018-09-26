from Utils import *
from StaticCheck import *
from StaticError import *
from MachineCode import JasminCode
from CodeGenError import *
import CodeGenerator as cgen
import functools

class Emitter():
    def __init__(self, filename):
        self.filename = filename
        self.buff = list()
        self.jvm = JasminCode()

    # Done
    def getJVMType(self, inType):
        typeIn = type(inType)
        if typeIn is IntType:
            return "I"
        elif typeIn is FloatType:
            return "F"
        elif typeIn is StringType:
            return "Ljava/lang/String;"
        elif typeIn is BoolType:
            return "Z"
        elif typeIn is VoidType:
            return "V"
        elif typeIn is ArrayType:
            return "[" + self.getJVMType(inType.eleType)
        elif typeIn is ArrayPointerType:
            return "[" + self.getJVMType(inType.eleType)
        elif typeIn is MType:
            return "(" + "".join(list(map(lambda x: self.getJVMType(x), inType.partype))) + ")" + self.getJVMType(inType.rettype)
        elif typeIn is cgen.ClassType:
            return "L" + inType.cname + ";"

    # Done
    def getFullType(self, inType):
        typeIn = type(inType)
        if typeIn is IntType:
            return "int"
        elif typeIn is FloatType:
            return "float"
        elif typeIn is BoolType:
            return "boolean"
        #elif typeIn is ClassType(i):
        #    return i
        elif typeIn is StringType:
            return "java/lang/String"
        elif typeIn is VoidType:
            return "void"

    # Done
    def emitPUSHICONST(self, in_, frame):
        #in: Int or Sring (this string must only contain integer characters)
        #frame: Frame
        
        frame.push();
        if type(in_) is int:
            i = in_
            if i >= -1 and i <=5:
                return self.jvm.emitICONST(i)
            elif i >= -128 and i <= 127:
                return self.jvm.emitBIPUSH(i)
            elif i >= -32768 and i <= 32767:
                return self.jvm.emitSIPUSH(i)
            else:
                return self.jvm.emitLDC(""+str(i)) 
        elif type(in_) is str:
            if in_ == "true":
                return self.emitPUSHICONST(1, frame)
            elif in_ == "false":
                return self.emitPUSHICONST(0, frame)
            else:
                return self.emitPUSHICONST(1 if in_ is "True" else 0, frame)

    # Done 
    def emitPUSHFCONST(self, in_, frame):
        #in_: String (this string must be only float format)
        #frame: Frame
        
        f = float(in_)
        frame.push()
        rst = "{0:.4f}".format(f)
        if rst == "0.0" or rst == "1.0" or rst == "2.0":
            return self.jvm.emitFCONST(rst)
        else:
            return self.jvm.emitLDC(in_)           

    ''' 
    *    generate code to push a constant onto the operand stack.
    *    @param in the lexeme of the constant
    *    @param typ the type of the constant
    '''
    
    def emitPUSHCONST(self, in_, typ, frame):
        #in_: String
        #typ: Type
        #frame: Frame
        
        if type(typ) is IntType:
            return self.emitPUSHICONST(in_, frame)
        elif type(typ) is FloatType:
            return self.emitPUSHFCONST(in_, frame)
        elif type(typ) is BoolType:
            return self.emitPUSHICONST(1 if in_ is True else 0, frame)
        elif type(typ) is StringType:
            frame.push()
            return self.jvm.emitLDC("\"" + in_ + "\"")
        else:
            raise IllegalOperandException(in_)

    ##############################################################

    # Done
    def emitALOAD(self, in_, frame):
        #in_: Type
        #frame: Frame
        #..., arrayref, index -> ..., value
        
        frame.pop()
        if type(in_) is IntType:
            return self.jvm.emitIALOAD()
        if type(in_) is FloatType:
            return self.jvm.emitFALOAD()
        if type(in_) is BoolType:
            return self.jvm.emitBALOAD()
        elif type(in_) is ArrayPointerType or type(in_) is cgen.ClassType or type(in_) is StringType:
            return self.jvm.emitAALOAD()
        else:
            raise IllegalOperandException(str(in_))

    # Done
    def emitASTORE(self, in_, frame):
        #in_: Type
        #frame: Frame
        #..., arrayref, index, value -> ...
        
        frame.pop()
        frame.pop()
        frame.pop()
        if type(in_) is IntType:
            return self.jvm.emitIASTORE()
        if type(in_) is BoolType:
            return self.jvm.emitBASTORE()
        if type(in_) is FloatType:
            return self.jvm.emitFASTORE()
        elif type(in_) is ArrayPointerType or type(in_) is cgen.ClassType or type(in_) is StringType or type(in_) is ArrayType:
            return self.jvm.emitAASTORE()
        else:
            raise IllegalOperandException(str(in_))


    '''    generate the var directive for a local variable.
    *   @param in       the index of the local variable.
    *   @param varName  the name of the local variable.
    *   @param inType   the type of the local variable.
    *   @param fromLabel the starting label of the scope where the variable is active.
    *   @param toLabel  the ending label  of the scope where the variable is active.
    '''

    # Done
    def emitVAR(self, in_, varName, inType, fromLabel, toLabel, frame):
        #in_: Int
        #varName: String
        #inType: Type
        #fromLabel: Int
        #toLabel: Int
        #frame: Frame
        
        return self.jvm.emitVAR(in_, varName, self.getJVMType(inType), fromLabel, toLabel)

    # Done
    def emitREADVAR(self, name, inType, index, frame):
        #name: String
        #inType: Type
        #index: Int
        #frame: Frame
        #... -> ..., value
        
        frame.push()
        if type(inType) is IntType:
            return self.jvm.emitILOAD(index)
        if type(inType) is FloatType:
            return self.jvm.emitFLOAD(index)
        if type(inType) is BoolType:
            return self.jvm.emitILOAD(index)
        elif type(inType) is ArrayPointerType or type(inType) is cgen.ClassType or type(inType) is StringType or type(inType) is ArrayType:
            return self.jvm.emitALOAD(index)
        else:
            raise IllegalOperandException(name)

    ''' generate the second instruction for array cell access
    *
    '''
    # Done
    def emitREADVAR2(self, name, typ, frame):
        #name: String
        #typ: Type
        #frame: Frame
        #... -> ..., value

        #frame.push()
        if type(typ) is ArrayType:
            emitALOAD(typ.eleType, frame)
        raise IllegalOperandException(name)

    '''
    *   generate code to pop a value on top of the operand stack and store it to a block-scoped variable.
    *   @param name the symbol entry of the variable.
    '''
    # Done
    def emitWRITEVAR(self, name, inType, index, frame):
        #name: String
        #inType: Type
        #index: Int
        #frame: Frame
        #..., value -> ...
        
        frame.pop()

        if type(inType) is IntType:
            return self.jvm.emitISTORE(index)
        if type(inType) is FloatType:
            return self.jvm.emitFSTORE(index)
        if type(inType) is BoolType:
            return self.jvm.emitISTORE(index)
        elif (type(inType) is ArrayPointerType) or (type(inType) is cgen.ClassType) or (type(inType) is StringType) or (type(inType) is ArrayType):
            return self.jvm.emitASTORE(index)
        else:
            raise IllegalOperandException(name)

    ''' generate the second instruction for array cell access
    *
    '''
    # Done 
    def emitWRITEVAR2(self, name, typ, frame):
        #name: String
        #typ: Type
        #frame: Frame
        #..., value -> ...

        #frame.push()
        if type(typ) is ArrayType or type(typ) is ArrayPointerType:
            return self.emitASTORE(typ.eleType,frame)
        raise IllegalOperandException(name)


    ''' generate the field (static) directive for a class mutable or immutable attribute.
    *   @param lexeme   the name of the attribute.
    *   @param in       the type of the attribute.
    *   @param isFinal  true in case of constant; false otherwise
    '''

    def emitATTRIBUTE(self, lexeme, in_, isFinal, value):
        #lexeme: String
        #in_: Type
        #isFinal: Boolean
        #value: String

        return self.jvm.emitSTATICFIELD(lexeme, self.getJVMType(in_), False)

    def emitGETSTATIC(self, lexeme, in_, frame):
        #lexeme: String
        #in_: Type
        #frame: Frame

        frame.push()
        return self.jvm.emitGETSTATIC(lexeme, self.getJVMType(in_))

    def emitPUTSTATIC(self, lexeme, in_, frame):
        #lexeme: String
        #in_: Type
        #frame: Frame
        
        frame.pop()
        return self.jvm.emitPUTSTATIC(lexeme, self.getJVMType(in_))

    def emitGETFIELD(self, lexeme, in_, frame):
        #lexeme: String
        #in_: Type
        #frame: Frame

        return self.jvm.emitGETFIELD(lexeme, self.getJVMType(in_))

    def emitPUTFIELD(self, lexeme, in_, frame):
        #lexeme: String
        #in_: Type
        #frame: Frame

        frame.pop()
        frame.pop()
        return self.jvm.emitPUTFIELD(lexeme, self.getJVMType(in_))

    ''' generate code to invoke a static method
    *   @param lexeme   the qualified name of the method(i.e., class-name/method-name)
    *   @param in       the type descriptor of the method.
    '''
    def emitINVOKESTATIC(self, lexeme, in_, frame):
        #lexeme: String
        #in_: Type
        #frame: Frame

        typ = in_
        list(map(lambda x: frame.pop(), typ.partype))
        if not type(typ.rettype) is VoidType:
            frame.push()
        return self.jvm.emitINVOKESTATIC(lexeme, self.getJVMType(in_))

    ''' generate code to invoke a special method
    *   @param lexeme   the qualified name of the method(i.e., class-name/method-name)
    *   @param in       the type descriptor of the method.
    '''
    def emitINVOKESPECIAL(self, frame, lexeme=None, in_=None):
        #lexeme: String
        #in_: Type
        #frame: Frame

        if not lexeme is None and not in_ is None:
            typ = in_
            list(map(lambda x: frame.pop(), typ.partype))
            frame.pop()
            if not type(typ.rettype) is VoidType:
                frame.push()
            return self.jvm.emitINVOKESPECIAL(lexeme, self.getJVMType(in_))
        elif lexeme is None and in_ is None:
            frame.pop()
            return self.jvm.emitINVOKESPECIAL()

    ''' generate code to invoke a virtual method
    * @param lexeme     the qualified name of the method(i.e., class-name/method-name)
    * @param in         the type descriptor of the method.
    '''
    def emitINVOKEVIRTUAL(self, lexeme, in_, frame):
        #lexeme: String
        #in_: Type
        #frame: Frame

        typ = in_
        list(map(lambda x: frame.pop(), typ.partype))
        frame.pop()
        if not type(typ) is VoidType:
            frame.push()
        return self.jvm.emitINVOKEVIRTUAL(lexeme, self.getJVMType(in_))

    '''
    *   generate ineg, fneg.
    *   @param in the type of the operands.
    '''
    def emitNEGOP(self, in_, frame):
        #in_: Type
        #frame: Frame
        #..., value -> ..., result

        if type(in_) is IntType:
            return self.jvm.emitINEG()
        else:
            return self.jvm.emitFNEG()

    def emitNOT(self, in_, frame):
        #in_: Type
        #frame: Frame

        label1 = frame.getNewLabel()
        label2 = frame.getNewLabel()
        result = list()
        result.append(self.emitIFTRUE2(label1, frame))
        result.append(self.emitPUSHCONST(True, in_, frame))
        result.append(self.emitGOTO(label2, frame))
        result.append(self.emitLABEL(label1, frame))
        result.append(self.emitPUSHCONST(False, in_, frame))
        result.append(self.emitLABEL(label2, frame))
        return ''.join(result)

    '''
    *   generate iadd, isub, fadd or fsub.
    *   @param lexeme the lexeme of the operator.
    *   @param in the type of the operands.
    '''
    def emitADDOP(self, lexeme, in_, frame):
        #lexeme: String
        #in_: Type
        #frame: Frame
        #..., value1, value2 -> ..., result

        frame.pop()
        if lexeme == "+":
            if type(in_) is IntType:
                return self.jvm.emitIADD()
            else:
                return self.jvm.emitFADD()
        else:
            if type(in_) is IntType:
                return self.jvm.emitISUB()
            else:
                return self.jvm.emitFSUB()

    '''
    *   generate imul, idiv, fmul or fdiv.
    *   @param lexeme the lexeme of the operator.
    *   @param in the type of the operands.
    '''

    def emitMULOP(self, lexeme, in_, frame):
        #lexeme: String
        #in_: Type
        #frame: Frame
        #..., value1, value2 -> ..., result

        frame.pop()
        if lexeme == "*":
            if type(in_) is IntType:
                return self.jvm.emitIMUL()
            else:
                return self.jvm.emitFMUL()
        else:
            if type(in_) is IntType:
                return self.jvm.emitIDIV()
            else:
                return self.jvm.emitFDIV()

    def emitDIV(self, frame):
        #frame: Frame

        frame.pop()
        return self.jvm.emitIDIV()

    def emitMOD(self, frame):
        #frame: Frame

        frame.pop()
        return self.jvm.emitIREM()

    '''
    *   generate iand
    '''

    def emitANDOP(self, frame):
        #frame: Frame

        frame.pop()
        return self.jvm.emitIAND()

    '''
    *   generate ior
    '''
    def emitOROP(self, frame):
        #frame: Frame

        frame.pop()
        return self.jvm.emitIOR()
    
    def emitAND_OR_SHORT_CIRCUIT(self,op,left,right,frame):
        #op:    String
        #left:  String
        #right: string
        #frame: Frame
        
        result = []
        labelX = frame.getNewLabel()
        labelY = frame.getNewLabel()
        
        if op == "||":
            result.append(left)
            result.append(self.jvm.emitIFGT(labelX))
            frame.pop()
            result.append(right)
            result.append(self.jvm.emitIFGT(labelX))
            frame.pop()
            result.append(self.emitPUSHCONST(0, IntType(), frame))
            frame.pop()
            result.append(self.emitGOTO(labelY,frame))
            result.append(self.emitLABEL(labelX,frame))
            result.append(self.emitPUSHCONST(1, IntType(), frame))
            result.append(self.emitLABEL(labelY,frame))
        elif op == "&&":
            result.append(left)
            result.append(self.jvm.emitIFLE(labelX))
            frame.pop()
            result.append(right)
            result.append(self.jvm.emitIFLE(labelX))
            frame.pop()
            result.append(self.emitPUSHCONST(1, IntType(), frame))
            frame.pop()
            result.append(self.emitGOTO(labelY,frame))
            result.append(self.emitLABEL(labelX,frame))
            result.append(self.emitPUSHCONST(0, IntType(), frame))
            result.append(self.emitLABEL(labelY,frame))

            
        return ''.j
    #    #in_: Type
    #    #frame: Frame
    #    #..., value1, value2 -> ..., result

    #    result = list()
    #    labelF = frame.getNewLabel()
    #    labelO = frame.getNewLabel()

    #    frame.pop()
    #    frame.pop()
    #    if op == ">":
    #        result.append(self.jvm.emitIFICMPLE(labelF))
    #    elif op == ">=":
    #        result.append(self.jvm.emitIFICMPLT(labelF))
    #    elif op == "<":
    #        result.append(self.jvm.emitIFICMPGE(labelF))
    #    elif op == "<=":
    #        result.append(self.jvm.emitIFICMPGT(labelF))
    #    elif op == "!=":
    #        result.append(self.jvm.emitIFICMPEQ(labelF))
    #    elif op == "==":
    #        result.append(self.jvm.emitIFICMPNE(labelF))
    #    result.append(self.emitPUSHCONST("1", IntType(), frame))
    #    frame.pop()
    #    result.append(self.emitGOTO(labelO, frame))
    #    result.append(self.emitLABEL(labelF, frame))
    #    result.append(self.emitPUSHCONST("0", IntType(), frame))
    #    result.append(self.emitLABEL(labelO, frame))
    #    return ''.join(result)



    def emitREOP(self, op, in_, frame):
        #op: String
        #in_: Type
        #frame: Frame
        #..., value1, value2 -> ..., result

        result = list()
        labelF = frame.getNewLabel()
        labelO = frame.getNewLabel()

        frame.pop()
        frame.pop()
        if op == ">":
            if type(in_) is FloatType:
                result.append(self.jvm.emitFCMPL())
                result.append(self.jvm.emitIFLE(labelF))
            else:
                result.append(self.jvm.emitIFICMPLE(labelF))
        elif op == ">=":
            if type(in_) is FloatType:
                result.append(self.jvm.emitFCMPL())
                result.append(self.jvm.emitIFLT(labelF))
            else:
                result.append(self.jvm.emitIFICMPLT(labelF))
        elif op == "<":
            if type(in_) is FloatType:
                result.append(self.jvm.emitFCMPL())
                result.append(self.jvm.emitIFGE(labelF))
            else:
                result.append(self.jvm.emitIFICMPGE(labelF))
        elif op == "<=":
            if type(in_) is FloatType:
                result.append(self.jvm.emitFCMPL())
                result.append(self.jvm.emitIFGT(labelF))
            else:
                result.append(self.jvm.emitIFICMPGT(labelF))
        elif op == "!=":
            if type(in_) is FloatType:
                result.append(self.jvm.emitFCMPL())
                result.append(self.jvm.emitIFEQ(labelF))
            elif (type(in_) is cgen.ClassType) or (type(in_) is ArrayType) or (type(in_) is StringType) or (type(in_) is ArrayPointerType):
                result.append(self.jvm.emitIFACMPEQ(labelF))
            else:
                result.append(self.jvm.emitIFICMPEQ(labelF))
        elif op == "==":
            if type(in_) is FloatType:
                result.append(self.jvm.emitFCMPL())
                result.append(self.jvm.emitIFNE(labelF))
            elif (type(in_) is cgen.ClassType) or (type(in_) is ArrayType) or (type(in_) is StringType) or (type(in_) is ArrayPointerType):
                result.append(self.jvm.emitIFACMPNE(labelF))
            else:
                result.append(self.jvm.emitIFICMPNE(labelF))

        result.append(self.emitPUSHCONST(1, IntType(), frame))
        frame.pop()
        result.append(self.emitGOTO(str(labelO), frame))
        result.append(self.emitLABEL(str(labelF), frame))
        result.append(self.emitPUSHCONST(0, IntType(), frame))
        result.append(self.emitLABEL(str(labelO), frame))
        return ''.join(result)



    #def emitRELOP(self, op, in_, trueLabel, falseLabel, frame):
    #    #op: String
    #    #in_: Type
    #    #trueLabel: Int
    #    #falseLabel: Int
    #    #frame: Frame
    #    #..., value1, value2 -> ..., result

    #    result = list()

    #    frame.pop()
    #    frame.pop()
    #    if op == ">":
    #        result.append(self.jvm.emitIFICMPLE(falseLabel))
    #        result.append(self.emitGOTO(trueLabel))
    #    elif op == ">=":
    #        result.append(self.jvm.emitIFICMPLT(falseLabel))
    #    elif op == "<":
    #        result.append(self.jvm.emitIFICMPGE(falseLabel))
    #    elif op == "<=":
    #        result.append(self.jvm.emitIFICMPGT(falseLabel))
    #    elif op == "!=":
    #        result.append(self.jvm.emitIFICMPEQ(falseLabel))
    #    elif op == "==":
    #        result.append(self.jvm.emitIFICMPNE(falseLabel))
    #    result.append(self.jvm.emitGOTO(trueLabel))
    #    return ''.join(result)

    def emitRELOP(self, op, in_, trueLabel, falseLabel, frame):
        #op: String
        #in_: Type
        #trueLabel: Int
        #falseLabel: Int
        #frame: Frame
        #..., value1, value2 -> ..., result

        result = [] 

        frame.pop()
        frame.pop()
        if op == ">":
            if type(in_) is FloatType:
                result.append(self.jvm.emitFCMPL())
                result.append(self.jvm.emitIFLE(falseLabel))
            else:
                result.append(self.jvm.emitIFICMPLE(falseLabel))
                result.append(self.jvm.emitGOTO(trueLabel))

        elif op == ">=":
            if type(in_) is FloatType:
                result.append(self.jvm.emitFCMPL())
                result.append(self.jvm.emitIFLT(falseLabel))
            else:
                result.append(self.jvm.emitIFICMPLT(falseLabel))

        elif op == "<":
            if type(in_) is FloatType:
                result.append(self.jvm.emitFCMPL())
                result.append(self.jvm.emitIFGE(falseLabel))
            else:
                result.append(self.jvm.emitIFICMPGE(falseLabel))

        elif op == "<=":
            if type(in_) is FloatType:
                result.append(self.jvm.emitFCMPL())
                result.append(self.jvm.emitIFGT(falseLabel))
            else:
                result.append(self.jvm.emitIFICMPGT(falseLabel))

        elif op == "!=":
            if (type(in_) is cgen.ClassType) or (type(in_) is ArrayType) or (type(in_) is StringType) or (type(in_) is ArrayPointerType):
                result.append(self.jvm.emitIFACMPEQ(falseLabel))
            elif type(in_) is FloatType:
                result.append(self.jvm.emitFCMPL())
                result.append(self.jvm.emitIFEQ(falseLabel))
            else:
                result.append(self.jvm.emitIFICMPEQ(falseLabel))

        elif op == "==":
            if (type(in_) is cgen.ClassType) or (type(in_) is ArrayType) or (type(in_) is StringType) or (type(in_) is ArrayPointerType):
                result.append(self.jvm.emitIFACMPNE(falseLabel))
            elif type(in_) is FloatType:
                result.append(self.jvm.emitFCMPL())
                result.append(self.jvm.emitIFNE(falseLabel))
            else:
                result.append(self.jvm.emitIFICMPNE(falseLabel))
    
        result.append(self.jvm.emitGOTO(trueLabel))
        return ''.join(result)

    '''   generate the method directive for a function.
    *   @param lexeme the qualified name of the method(i.e., class-name/method-name).
    *   @param in the type descriptor of the method.
    *   @param isStatic <code>true</code> if the method is static; <code>false</code> otherwise.
    '''

    def emitMETHOD(self, lexeme, in_, isStatic, frame):
        #lexeme: String
        #in_: Type
        #isStatic: Boolean
        #frame: Frame

        return self.jvm.emitMETHOD(lexeme, self.getJVMType(in_), isStatic)

    '''   generate the end directive for a function.
    '''
    def emitENDMETHOD(self, frame):
        #frame: Frame

        buffer = list()
        buffer.append(self.jvm.emitLIMITSTACK(frame.getMaxOpStackSize()))
        buffer.append(self.jvm.emitLIMITLOCAL(frame.getMaxIndex()))
        buffer.append(self.jvm.emitENDMETHOD())
        return ''.join(buffer)
    
    def emitNEWARRAY(self,in_,frame):
        #in_ :  ArrayType
        buffer = []
        buffer.append(self.emitPUSHICONST(in_.dimen.value, frame))
        if type(in_.eleType) is StringType:
            buffer.append(self.jvm.emitANEWARRAY(self.getFullType(in_.eleType)))
        elif (type(in_.eleType) is IntType) or (type(in_.eleType) is FloatType) or (type(in_.eleType) is BoolType):
            buffer.append(self.jvm.emitNEWARRAY(self.getFullType(in_.eleType)))
        
        return ''.join(buffer)

    def emitNEW(self,in_,frame):
        #in: ClassType
        buffer = []
        buffer.append(self.jvm.emitNEW(in_.cname))
        frame.push()
        buffer.append(self.jvm.emitDUP)
        frame.push()
        return ''.join(buffer)

    def emitINITGLOBALARRAY(self,lexeme,in_,frame):
        #lexeme : String    
        #in_    : ArrayType 
        
        buffer = []
        buffer.append(self.emitNEWARRAY(in_, frame))
        frame.pop()
        buffer.append(self.jvm.emitPUTSTATIC(lexeme, self.getJVMType(in_)))
        return ''.join(buffer)

    def emitCLINIT(self,classname,in_,frame):
        #in         : list[VarDecl]
        #classname  : String
        result          = []
        initGlobalArray = []
        tmp = MType([],VoidType())
        
        frame.enterScope(True)
        result.append(self.emitMETHOD("<clinit>", tmp, True, frame))
        
        for x in in_:
            initGlobalArray.append(self.emitINITGLOBALARRAY(classname+"."+x.variable.name,x.varType,frame))

        result.append(self.jvm.emitLIMITSTACK(frame.getMaxOpStackSize()))
        result.append(self.jvm.emitLIMITLOCAL(frame.getMaxIndex()))
        result.append(''.join(initGlobalArray))
        result.append(self.emitRETURN(VoidType(), frame))
        result.append(self.jvm.emitENDMETHOD())
        frame.exitScope()
        return ''.join(result)


    def getConst(self, ast):
        #ast: Literal
        if type(ast) is IntLiteral:
            return (str(ast.value), IntType())
        elif type(ast) is BooleanLiteral:
            return (str(ast.value), BoolType())
        elif type(ast) is FloatLiteral:
            return (str(ast.value), FloatType())
        elif type(ast) is StringLiteral:
            return (str(ast.value), StringType())


    '''   generate code to initialize a local array variable.<p>
    *   @param index the index of the local variable.
    *   @param in the type of the local array variable.
    '''

    '''   generate code to initialize local array variables.
    *   @param in the list of symbol entries corresponding to local array variable.    
    '''

    '''   generate code to jump to label if the value on top of operand stack is true.<p>
    *   ifgt label
    *   @param label the label where the execution continues if the value on top of stack is true.
    '''
    def emitIFTRUE(self, label, frame):
        #label: Int
        #frame: Frame

        frame.pop()
        return self.jvm.emitIFEQ(label)
    
    def emitIFTRUE2(self,label,frame):
        frame.pop()
        #jvm.emitIFGT(label);
        return self.jvm.emitIFNE(label)


    '''
    *   generate code to jump to label if the value on top of operand stack is false.<p>
    *   ifle label
    *   @param label the label where the execution continues if the value on top of stack is false.
    '''
    def emitIFFALSE(self, label, frame):
        #label: Int
        #frame: Frame

        frame.pop()
        return self.jvm.emitIFLE(label)

    def emitIFICMPGT(self, label, frame):
        #label: Int
        #frame: Frame

        frame.pop()
        return self.jvm.emitIFICMPGT(label)

    def emitIFICMPLT(self, label, frame):
        #label: Int
        #frame: Frame

        frame.pop()
        return self.jvm.emitIFICMPLT(label)    

    '''   generate code to duplicate the value on the top of the operand stack.<p>
    *   Stack:<p>
    *   Before: ...,value1<p>
    *   After:  ...,value1,value1<p>
    '''
    def emitDUP(self, frame):
        #frame: Frame

        frame.push()
        return self.jvm.emitDUP()

    def emitDUP_X2(self,frame):
        frame.push()
        return self.jvm.emitDUPX2()


    def emitPOP(self, frame):
        #frame: Frame

        frame.pop()
        return self.jvm.emitPOP()

    '''   generate code to exchange an integer on top of stack to a floating-point number.
    '''
    def emitI2F(self, frame):
        #frame: Frame

        return self.jvm.emitI2F()

    ''' generate code to return.
    *   <ul>
    *   <li>ireturn if the type is IntegerType or BooleanType
    *   <li>freturn if the type is RealType
    *   <li>return if the type is null
    *   </ul>
    *   @param in the type of the returned expression.
    '''

    def emitRETURN(self, in_, frame):
        #in_: Type
        #frame: Frame

        if type(in_) is IntType:
            frame.pop()
            return self.jvm.emitIRETURN()
        elif type(in_) is FloatType:
            frame.pop()
            return self.jvm.emitFRETURN()
        elif type(in_) is BoolType:
            frame.pop()
            return self.jvm.emitIRETURN()
        elif (type(in_) is StringType) or (type(in_) is ArrayType) or (type(in_) is ArrayPointerType):
            frame.pop()
            return self.jvm.emitARETURN()
        elif type(in_) is VoidType:
            return self.jvm.emitRETURN()
        elif type(in_) is cgen.ClassType:
            frame.pop()
            return self.jvm.emitARETURN()
        else:
            pass

    ''' generate code that represents a label	
    *   @param label the label
    *   @return code Label<label>:
    '''
    def emitLABEL(self, label, frame):
        #label: Int
        #frame: Frame

        return self.jvm.emitLABEL(label)

    ''' generate code to jump to a label	
    *   @param label the label
    *   @return code goto Label<label>
    '''
    def emitGOTO(self, label, frame):
        #label: Int
        #frame: Frame

        return self.jvm.emitGOTO(str(label))

    ''' generate some starting directives for a class.<p>
    *   .source MPC.CLASSNAME.java<p>
    *   .class public MPC.CLASSNAME<p>
    *   .super java/lang/Object<p>
    '''
    def emitPROLOG(self, name, parent):
        #name: String
        #parent: String

        result = list()
        result.append(self.jvm.emitSOURCE(name + ".java"))
        result.append(self.jvm.emitCLASS("public " + name))
        result.append(self.jvm.emitSUPER("java/land/Object" if parent == "" else parent))
        return ''.join(result)

    def emitLIMITSTACK(self, num):
        #num: Int

        return self.jvm.emitLIMITSTACK(num)

    def emitLIMITLOCAL(self, num):
        #num: Int

        return self.jvm.emitLIMITLOCAL(num)

    def emitEPILOG(self):
        file = open(self.filename, "w")
        file.write(''.join(self.buff))
        file.close()

    ''' print out the code to screen
    *   @param in the code to be printed out
    '''
    def printout(self, in_ ,fl=False):
        #in_: String
        
        self.buff.append(in_)

    def clearBuff(self):
        self.buff.clear()





        
