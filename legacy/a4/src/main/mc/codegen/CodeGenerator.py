'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
 *   @studentInfo
 *   @name  Luan Pham
 *   @id    1511899
 *  
'''
from AST import *
from Visitor import *
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod
from CodeGenError import *
import functools 

# NOTE: MC map sang 1 class cua Java
# 
#   global val  -> static field
#   local field -> index
#
#   val: index neu local
#   val: cname neu global
#
#   function -> static method 
#



class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"
        self.curFunc = Symbol("null", MType([],VoidType()), CName("MCClass"))

    def init(self):
        return [    Symbol("getInt", MType(list(), IntType()), CName(self.libName)),
                    Symbol("putInt", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("putIntLn", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("putFloatLn", MType([FloatType()], VoidType()), CName(self.libName)),
                    Symbol("getFloat", MType([], FloatType()), CName(self.libName)),
                    Symbol("putFloat", MType([FloatType()], VoidType()), CName(self.libName)),
                    Symbol("putFloatLn", MType([FloatType()], VoidType()), CName(self.libName)),
                    Symbol("putBool", MType([BoolType()], VoidType()), CName(self.libName)),
                    Symbol("putBoolLn", MType([BoolType()], VoidType()), CName(self.libName)),
                    Symbol("putString", MType([StringType()], VoidType()), CName(self.libName)),
                    Symbol("putStringLn", MType([StringType()], VoidType()), CName(self.libName)),
                    Symbol("putLn", MType([], VoidType()), CName(self.libName)),
                    ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)

class ClassType(Type):
    def __init__(self, cname):
        #cname: String
        self.cname = cname

    def __str__(self):
        return "ClassType"

    def accept(self, v, param):
        return v.visitClassType(self, param)

# use in Function Body
class SubBody():
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym

# use in Expression Body
class Access():
    def __init__(self, frame, sym, isLeft, isFirst, isDup=False):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean

        self.frame  = frame
        self.sym    = sym
        self.isLeft = isLeft
        self.isFirst = isFirst
        self.isDup  = isDup

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value):
        #value: String

        self.value = value

class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "MCClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")
        self.curFunc = Symbol("null", MType([],VoidType()), CName(self.className))

    def VarGlobal(self, ast, c):
        ctxt = c
        nameAtt = ast.variable.name
        typeAtt = ast.varType
        self.emit.printout(self.emit.emitATTRIBUTE(nameAtt, typeAtt, False, ""))
        symbol = Symbol(ast.variable.name, typeAtt, CName(self.className))
        c.append(symbol)
        return c
    
    def FuncGlobal(self,ast, c):
        ctxt = c
        nameFunc = ast.name.name
        typeFunc = MType([x.varType for x in ast.param], ast.returnType)
        symbol = Symbol(nameFunc, typeFunc, CName(self.className))
        c.append(symbol)
        return c


    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        
        lsVar       = list(filter(lambda x:type(x) is VarDecl, ast.decl))
        lsArrayVar  = list(filter(lambda x:type(x.varType) is ArrayType, lsVar))
        lsFun       = list(filter(lambda x:type(x) is FuncDecl, ast.decl))
        
        # printout static field and add them to self.env
        functools.reduce(lambda x,y: self.VarGlobal(y,x) if type(y) is VarDecl else self.FuncGlobal(y,x), \
                ast.decl, self.env if self.env else []) 
        
        # visit func decl
        functools.reduce(lambda a,b: self.visit(b,a), lsFun, SubBody(None, self.env))

        # generate default constructor
        self.genMETHOD(FuncDecl(Id("<init>"), [], None, Block([], [])), c, Frame("<init>", VoidType()))
        if lsArrayVar:
            self.emit.printout(self.emit.emitCLINIT(self.className, lsArrayVar, Frame("<clinit>", VoidType())))
        self.emit.emitEPILOG()
        return c
    
    def visitVarDecl(self,ast,c):
        #ast: VarDecl
        #c  : SubBody
        env  = c.sym if type(c) is SubBody else []
        indx = c.frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(indx, ast.variable.name, ast.varType, c.frame.getStartLabel(), c.frame.getEndLabel(), c.frame))
        return SubBody(c.frame, [Symbol(ast.variable.name, ast.varType, Index(indx))] + env)


    def arrayTypeDecl(self,ast,c):
        #ast : VarDecl
        #c   : any

        # coi lai
        index = (self.lookup(ast.variable.name,c.sym,lambda x:x.name)).value.value
        self.emit.printout(self.emit.emitNEWARRAY(ast.varType, c.frame))
        self.emit.printout(self.emit.emitWRITEVAR(ast.variable.name, ast.varType, index, c.frame))
        return SubBody(c.frame, c.sym)



    def genMETHOD(self, consdecl, o, frame):
        #consdecl: FuncDecl
        #o: Any
        #frame: Frame

        isInit = consdecl.returnType is None
        isMain = consdecl.name.name == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        returnType = VoidType() if isInit else consdecl.returnType
        methodName = "<init>" if isInit else consdecl.name.name
        intype = [ArrayPointerType(StringType())] if isMain else [x.varType for x in consdecl.param]
        mtype = MType(intype, returnType)
        
        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))

        frame.enterScope(True)

        glenv = o

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        
        glSubBody = SubBody(frame,glenv)
        if (isMain is False) and (intype != []):
            glSubBody = functools.reduce(lambda a,b: self.visit(b,a), consdecl.param, SubBody(frame,glenv)) 

        body   = consdecl.body
        curenv = functools.reduce(lambda a,b: self.visit(b,a), body.decl, glSubBody)
        
        lsArrVarDecl = list(filter(lambda x:type(x.varType) is ArrayType, body.decl))
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        
        for x in lsArrVarDecl:
            self.arrayTypeDecl(x,curenv)


        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        returnStmt = list(filter(lambda x:type(x) is Return, body.stmt))
        
        list(map(lambda x: self.printoutStmt(x, curenv), body.stmt))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if (type(returnType) is VoidType) or (not returnStmt):
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope();

    
    def printoutStmt(self,ast,env):
        #env    : SubBody
        frame  = env.frame
        newEnv = env.sym
        if type(ast) is BinaryOp:
            if ast.op == "=":
                self.emit.printout(self.visit(ast, Access(frame, newEnv, True, True, False))[0])
            else:
                self.emit.printout(self.visit(ast, Access(frame, newEnv, False, True, True))[0])
                self.emit.printout(self.emit.emitPOP(frame))

        elif type(ast) is CallExpr:
            self.emit.printout(self.visit(ast, Access(frame, newEnv, False, True, True))[0])
            sym = self.lookup(ast.method.name, newEnv, lambda x:x.name) 
            returnType = sym.mtype.rettype
        
            if type(returnType) != VoidType:
                self.emit.printout(self.emit.emitPOP(frame))

        elif (type(ast) is UnaryOp) or (type(ast) is Id) or (type(ast) is ArrayCell) or (type(ast) is IntLiteral) or \
                (type(ast) is FloatLiteral) or (type(ast) is StringLiteral) or (type(ast) is BooleanLiteral):
        
                self.emit.printout(self.visit(ast, Access(frame, newEnv, False, True, True))[0])
                self.emit.printout(self.emit.emitPOP(frame))

        elif (type(ast) is Block) or (type(ast) is If) or (type(ast) is For) or (type(ast) is Break) or \
                (type(ast) is Continue) or (type(ast) is Return) or (type(ast) is Dowhile):
                    # NOTE env hay new env vay cha noi 
                self.visit(ast, env)
        else:
            pass 


    def visitFuncDecl(self, ast, o):
        #ast: FuncDecl

        subctxt = o
        frame = Frame(ast.name.name, ast.returnType)
        self.curFunc = self.lookup(ast.name.name, subctxt.sym, lambda x: x.name)
        self.genMETHOD(ast, subctxt.sym, frame)
        
        return o
        #return SubBody(None, [Symbol(ast.name, MType(list(), ast.returnType), CName(self.className))] + subctxt.sym)


    def visitBlock(self,ast,c):
        #c  : SubBody
        ctxt = c
        frame = ctxt.frame
        newEnv = ctxt.sym

        frame.enterScope(False)
        #varEnv = ast.decl.foldLeft(SubBody(frame, newEnv))((x, e) => visit(e, x).asInstanceOf[SubBody])
        varEnv = functools.reduce(lambda a,b: self.visit(b,a), ast.decl,SubBody(frame, newEnv))

        # list Vardecl
        listVarDecl = ast.decl
        listArrayVarDecl = filter(lambda x:type(x) is ArrayType,listVarDecl) 

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        list(map(lambda x:self.arrayTypeDecl(x,varEnv), listArrayVarDecl))
        list(map(lambda x:self.printoutStmt(x,varEnv),ast.stmt))
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        frame.exitScope()
        return c

    def visitIf(self,ast,c):
        #c  : SubBody
        frame = c.frame
        env = c.sym
        (resExpr, typeExpr) = ast.expr.accept(self, Access(frame, env, False, True, True))
        falseLabel = frame.getNewLabel()
        
        self.emit.printout(resExpr + self.emit.emitIFFALSE(falseLabel, frame))
        self.printoutStmt(ast.thenStmt, c)
        if not ast.elseStmt:
            self.emit.printout(self.emit.emitLABEL(falseLabel, frame))
        else:
            trueLabel = frame.getNewLabel()
            self.emit.printout(self.emit.emitGOTO(trueLabel, frame) + self.emit.emitLABEL(falseLabel, frame)
                    )
            self.printoutStmt(ast.elseStmt, c)
            self.emit.printout(self.emit.emitLABEL(trueLabel, frame))


    def visitFor(self,ast,c):
        #c  : SubBody
        frame = c.frame
        env = c.sym
        beginLabel = frame.getNewLabel()
        frame.enterLoop()
        
        self.printoutStmt(ast.expr1, SubBody(frame, env))
        self.emit.printout(self.emit.emitLABEL(beginLabel, frame))
        (resExpr2, typeExpr2) = ast.expr2.accept(self,Access(frame, env, False, True, False))
        self.emit.printout(resExpr2)

        self.emit.printout(self.emit.emitIFTRUE(frame.getBreakLabel(), frame))
        self.printoutStmt(ast.loop, c)
        
        self.emit.printout(self.emit.emitLABEL(frame.getContinueLabel(), frame))
        self.printoutStmt(ast.expr3, SubBody(frame, env))
	
        self.emit.printout(self.emit.emitGOTO(beginLabel, frame))
        self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))
	
        frame.exitLoop()
    
    def visitDowhile(self,ast,c):
        #c  : SubBody
        frame = c.frame
        env = c.sym
        beginLabel = frame.getNewLabel()
        frame.enterLoop()
        
        self.emit.printout(self.emit.emitLABEL(beginLabel, frame))
        list(map(lambda x:self.printoutStmt(x,c) ,ast.sl))

        self.emit.printout(self.emit.emitLABEL(frame.getContinueLabel(), frame))

        (resExpr, typeExpr) = ast.exp.accept(self, Access(frame, env, False, True, True))
        self.emit.printout(resExpr)
        self.emit.printout(self.emit.emitIFTRUE(frame.getBreakLabel(), frame))
        self.emit.printout(self.emit.emitGOTO(beginLabel, frame))
        self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))
        frame.exitLoop()
    
    
    def visitBreak(self,ast,c):
        self.emit.printout(self.emit.emitGOTO(c.frame.getBreakLabel(), c.frame))
    
    def visitContinue(self,ast,c):
        self.emit.printout(self.emit.emitGOTO(c.frame.getContinueLabel(), c.frame))

    
    def visitReturn(self,ast,c):
        if ast.expr:
            (resExpr, resType) = self.visit(ast.expr, Access(c.frame, c.sym, False, True, True))
            typeFunc = self.curFunc.mtype.rettype
            if type(typeFunc) == FloatType and type(resType) == IntType:
                self.emit.printout(resExpr + self.emit.emitI2F(c.frame) + self.emit.emitRETURN(FloatType(), c.frame))
            else:
                self.emit.printout(resExpr + self.emit.emitRETURN(resType, c.frame))
        else:
            self.emit.printout(self.emit.emitRETURN(VoidType(), c.frame))
    

    def visitBinaryOp(self,ast,c):
        #c  : Access (co the la SubBody)
        ctxt = c
        frame = ctxt.frame
        env = ctxt.sym
        op = ast.op
        op_Str = ""
        str_Dup = "" 
        str_I2f = "" 
        resType = IntType()

        if op == "=":
            (resLeft1, typeLeft1) = self.visit(ast.left, Access(frame, env, True, True, False))
            (resRight, typeRight) = self.visit(ast.right,Access(frame, env, False, True, True))

            if type(typeLeft1) == FloatType and type(typeRight) == IntType:
                str_I2f = self.emit.emitI2F(frame)
            
            if ctxt.isDup == True:
                if type(ast.left) is Id:
                    str_Dup = self.emit.emitDUP(frame)
                else:
                    str_Dup = self.emit.emitDUP_X2(frame)
            
            (resLeft2, typeLeft2) = self.visit(ast.left, Access(frame, env, True, False, False))
            op_Str = resLeft1 + resRight + str_I2f + str_Dup  + resLeft2

            resType = typeLeft1

        else:
            (resLeft, typeLeft) = self.visit(ast.left, Access(frame, env, False, True, True))
            (resRight, typeRight) = self.visit(ast.right, Access(frame, env, False, True, True))

            if op == "+" or op == "-": 
                if type(typeLeft) is FloatType and type(typeRight) is IntType:
                    op_Str = resLeft + resRight + self.emit.emitI2F(frame) + self.emit.emitADDOP(op, FloatType(), frame)
                    resType = FloatType()
                elif type(typeLeft) is IntType and type(typeRight) is FloatType:
                    op_Str = resLeft + self.emit.emitI2F(frame) + resRight + self.emit.emitADDOP(op, FloatType(), frame)
                    resType = FloatType()
                else:
                    op_Str = resLeft + resRight + self.emit.emitADDOP(op, typeLeft, frame)
                    resType = typeLeft
            
            
            elif op == "*" or op == "/": 
                if type(typeLeft) is FloatType and type(typeRight) is IntType:
                    op_Str = resLeft + resRight + self.emit.emitI2F(frame) + self.emit.emitMULOP(op, FloatType(), frame)
                    resType = FloatType()
                elif type(typeLeft) is IntType and type(typeRight) is FloatType:
                    op_Str = resLeft + self.emit.emitI2F(frame) + resRight + self.emit.emitMULOP(op, FloatType(), frame)
                    resType = FloatType()
                else:
                    op_Str = resLeft + resRight + self.emit.emitMULOP(op, typeLeft, frame)
                    resType = typeLeft
            elif op == "%": 
                op_Str = resLeft + resRight + self.emit.emitMOD(frame)
                resType = IntType()
            elif (op == "<") or (op == "<=") or (op == ">") or (op == ">="): 
                if type(typeLeft) is FloatType and type(typeRight) is IntType:
                    op_Str = resLeft + resRight + self.emit.emitI2F(frame) + self.emit.emitREOP(op, FloatType(), frame)
                elif type(typeLeft) is IntType and type(typeRight) is FloatType:
                    op_Str = resLeft + self.emit.emitI2F(frame) + resRight + self.emit.emitREOP(op, FloatType(), frame)
                else:
                    op_Str = resLeft + resRight + self.emit.emitREOP(op, typeLeft, frame)
                resType = BoolType()
            elif (op == "==") or (op == "!="): 
                if type(typeLeft) is BoolType and type(typeRight) is BoolType:
                    op_Str = resLeft + resRight + self.emit.emitREOP(op, IntType(), frame)
                if type(typeLeft) is IntType and type(typeRight) is IntType:
                    op_Str = resLeft + resRight + self.emit.emitREOP(op, IntType(), frame)
                else:
                    resType = BoolType()
            elif (op == "&&") or (op == "||"): 
                op_Str = self.emit.emitAND_OR_SHORT_CIRCUIT(op, resLeft, resRight, frame)
                resType = BoolType()

        return (op_Str, resType)

    
    def visitUnaryOp(self,ast,c):
        ctxt = c
        frame = ctxt.frame
        env = ctxt.sym
        (resExpr, typeExpr) = self.visit(ast.body, Access(frame, env, False, True, True))
        if ast.op == "!":
            return (resExpr + self.emit.emitNOT(typeExpr, frame), typeExpr)
        elif ast.op == "-": 
            return (resExpr + self.emit.emitNEGOP(typeExpr, frame), typeExpr)


    def visitCallExpr(self, ast, o):
        #ast: CallExpr

        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.method.name, nenv, lambda x: x.name)
        cname = sym.value.value
        ctype = sym.mtype
        returnType = ctype.rettype 
        
        if ctxt.isLeft is True and ctxt.isFirst is False:
            return (self.emit.emitWRITEVAR2(ast.method.name, returnType, frame), returnType)
        else:
            listParamType = ctype.partype
            # zip
            checkList=[]
            for item in range(len(listParamType)):
                checkList.append((ast.param[item],listParamType[item]))
            
            in_ = ("",[])
            for x in checkList:
                (str1,typ1) = self.visit(x[0],Access(frame,nenv,False,True,True))
                if type(typ1) is IntType and type(x[1]) is FloatType:
                    in_ = (in_[0] + str1 + self.emit.emitI2F(frame), in_[1].append(typ1))
                else:
                    in_ = (in_[0] + str1, in_[1] + [typ1])
        
        return (in_[0] + self.emit.emitINVOKESTATIC(cname + "/" + ast.method.name, ctype, frame), returnType)

        #in_ = ("", list())
        #for x in ast.param:
        #    str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
        #    in_ = (in_[0] + str1, in_[1].append(typ1))
        #self.emit.printout(in_[0])
        #self.emit.printout(self.emit.emitINVOKESTATIC(cname + "/" + ast.method.name, ctype, frame))


    
    def visitId(self,ast,o,fl=False):
        # o : Access (co the la SubBody)
        if type(o) != SubBody: 
            sym  = self.lookup(ast.name, o.sym, lambda x: x.name)

            code = ""
            if o.isLeft is True and o.isFirst is True:
                pass
            elif o.isLeft is True and o.isFirst is False:
                if type(sym.mtype) is ArrayType or type(sym.mtype) is ArrayPointerType:
                    code = self.emit.emitWRITEVAR2(ast.name, sym.mtype, o.frame)
                else:
                    if type(sym.value) is CName:
                        code = self.emit.emitPUTSTATIC(sym.value.value + "." + ast.name, sym.mtype, o.frame)
                    elif type(sym.value) is Index:
                        code = self.emit.emitWRITEVAR(ast.name, sym.mtype, sym.value.value, o.frame) 

            elif o.isLeft is False:
                if type(sym.value) is CName:
                    code = self.emit.emitGETSTATIC(sym.value.value + "." + ast.name, sym.mtype, o.frame)
                elif type(sym.value) is Index:
                    code = self.emit.emitREADVAR(ast, sym.mtype, sym.value.value, o.frame)
                    
            return (code,sym.mtype)
        else:
            sym  = self.lookup(ast.name, o.sym, lambda x: x.name)
            return ("",sym.mtype)
             

    def visitArrayCell(self,ast,o):

        # if in body expression
        if type(o) != SubBody:
            frame = o.frame
            lsSym = o.sym
            if o.isLeft is True and o.isFirst is True:
                (resArr, typeArr) = self.visit(ast.arr, Access(frame, lsSym, False, True, False))
                (resIdx, typIdx)  = self.visit(ast.idx, Access(frame, lsSym, False, True, True))
                return (resArr + resIdx, typeArr.eleType)

            elif o.isLeft is True and o.isFirst is False:
                (resArr, typeArr) = self.visit(ast.arr, Access(frame, lsSym, True, False, False))
                return (resArr, typeArr)
            
            elif o.isLeft is False:
                (resArr, typeArr) = self.visit(ast.arr, Access(frame, lsSym, False, True, False))
                (resIdx, typIdx)  = self.visit(ast.idx, Access(frame, lsSym, False, True, True))
                if type(typeArr) is ArrayType:
                    arrayType = typeArr.eleType
                    aload = self.emit.emitALOAD(arrayType, frame)
                    return (resArr + resIdx + aload, arrayType)
                elif type(typeArr) is ArrayPointerType:
                    arrayPointerType = typeArr.eleType
                    aload = self.emit.emitALOAD(arrayPointerType, frame)
                    return (resArr + resIdx + aload, arrayPointerType)
        else:
            # ko o trong body expr thi o dau ta. o ngoai, vi du: a[6] = 4;
            frame = o.frame
            lsSym = o.sym
            (resArr, typeArr) = self.visit(ast.arr, Access(frame, lsSym, False, True, False))
            arrayType = typeArr.eleType
            return ("", arrayType) 


    def visitIntLiteral(self, ast, o):
        #ast: IntLiteral
        #o: Any

        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(ast.value, frame), IntType()

    def visitFloatLiteral(self, ast, o):
        #ast: FloatLiteral
        #o: Any
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHFCONST(str(ast.value), frame), FloatType()

    def visitStringLiteral(self, ast, o):
        #ast: StringLiteral
        #o: Any
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHCONST(ast.value, StringType(), frame), StringType()

    def visitBooleanLiteral(self,ast,o):
        ctxt = o
        frame = ctxt.frame
        return (self.emit.emitPUSHICONST(str(ast.value), frame), BoolType())

