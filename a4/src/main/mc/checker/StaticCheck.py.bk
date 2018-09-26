
"""
 * @author nhphung
 * @student     luanpham
 * @studendID   1511899
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
import functools

class FuncType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,functype,value = None):
        self.name       = name
        self.functype   = functype
        self.value      = value


def checkIfExist(listDecl, decl, kind):
    if kind == "Variable":
        if any(de.name==decl.variable.name for de in listDecl):
            raise Redeclared(Variable(),decl.variable.name)    
        return Symbol(decl.variable.name, decl.varType)
    elif kind == "Parameter":
        if any(de.name==decl.variable.name for de in listDecl):
            raise Redeclared(Parameter(),decl.variable.name)
        return Symbol(decl.variable.name, decl.varType)
    else:
        if any(de.name==decl.name.name for de in listDecl):
            raise Redeclared(Function(),decl.name.name)    
        return Symbol(decl.name.name, FuncType([x.varType for x in decl.param],decl.returnType))
    return decl


def BinOpType(l,r):
    if (type(l),type(r)) == (IntType,IntType):
        return IntType()
    elif ((type(l),type(r)) == (FloatType,FloatType)) or\
         ((type(l),type(r)) == (FloatType,IntType)) or\
         ((type(l),type(r)) == (IntType,FloatType)): 
        return FloatType()
    return None


def AssignmentRule(l,r):
    if type(l) == VoidType or type(l) == ArrayType:
        return False
    elif ((type(l) == ArrayPointerType and type(r) == ArrayType)) or\
         ((type(l) == ArrayPointerType and type(r) == ArrayPointerType)):
        return assE(l.eleType,r.eleType)
    elif (type(l), type(r)) == (FloatType,IntType):
        return True 
    else:
        return type(l)==type(r)


def assE(l,r):
    if ((type(l),type(r)) == (BoolType,BoolType)) or\
       ((type(l),type(r)) == (StringType,StringType)) or\
       ((type(l),type(r)) == (FloatType,FloatType)) or\
       ((type(l),type(r)) == (IntType,IntType)):
        return True
    else:
        return False


def assignExplicitType(l,r):
    if ((type(l),type(r)) == (BoolType,BoolType)) or\
       ((type(l),type(r)) == (StringType,StringType)) or\
       ((type(l),type(r)) == (FloatType,FloatType)) or\
       ((type(l),type(r)) == (IntType,IntType)) or\
       ((type(l),type(r)) == (FloatType,IntType)):
        return True
    else: 
        return False


def findandkillit(env,rmId):
    [env.remove(it) for it in env if it.name == rmId]


class StaticChecker(BaseVisitor,Utils):

    global_envi = [\
            Symbol("getInt",FuncType([],IntType())),\
            Symbol("putInt",FuncType([IntType()],VoidType())),\
            Symbol("putIntLn",FuncType([IntType()],VoidType())),\
            Symbol("getFloat",FuncType([],FloatType())),\
            Symbol("putFloat",FuncType([FloatType()],VoidType())),\
            Symbol("putFloatLn",FuncType([FloatType()],VoidType())),\
            Symbol("putBool",FuncType([BoolType()],VoidType())),\
            Symbol("putBoolLn",FuncType([BoolType()],VoidType())),\
            Symbol("putString",FuncType([StringType()],VoidType())),\
            Symbol("putStringLn",FuncType([StringType()],VoidType())),\
            Symbol("putLn",FuncType([StringType()],VoidType()))\
            ]
            
    def __init__(self,ast):
        self.ast = ast
    

    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)


    def visitProgram(self,ast, c):
        env         = c.copy()
        mainast     = None 
        reachfunc   = {}
        
        for decl in ast.decl:
            env.append(checkIfExist(env,decl,"Variable" if type(decl) is VarDecl else "Function"))
            if type(decl) is FuncDecl:
                mainast = decl if decl.name.name == "main" else mainast
                reachfunc[decl.name.name] = 0 if decl.name.name != "main" else 1

        if mainast is None:
            raise NoEntryPoint()

        list(map(lambda x: self.visit(x,(env,None,False,None,reachfunc,None)),ast.decl))

        # check reachfunc
        for k in reachfunc:
            if reachfunc[k] == 0:
                raise UnreachableFunction(k)

        return []


    def visitVarDecl(self,ast,c):
        pass


    def visitFuncDecl(self,ast, c): 
        # env: list global_envi
        # par: list param
        env = c[0].copy()
        par = []
        
        for p in ast.param:
            par.append(checkIfExist(par,p,"Parameter"))
        
        isReturn = self.visit(ast.body, (env, ast.returnType, False, par,c[4],ast.name.name))
        if isReturn is False and type(ast.returnType) is not VoidType:
            raise FunctionNotReturn(ast.name.name)


    def visitBlock(self,ast,c):
        
        env = c[0].copy()
        # c[3]: list param
        lsP = c[3] if c[3] else []
        isRet = []
        isEnd = False 

        # find and override all vardecl
        for vd in ast.decl:
            lsP.append(checkIfExist(lsP,vd,"Variable"))
            findandkillit(env,vd.variable.name)
        env += lsP

        # visit each stmt (env,reT,B/C)
        for st in ast.stmt:
            if isEnd is True or isEnd is "BC":
                raise UnreachableStatement(st)
            isEnd = self.visit(st,(env,c[1],c[2],[],c[4],c[5]))
            isRet.append(isEnd)
        
        return isEnd if isEnd is True or isEnd is "BC" else False


    def visitIf(self,ast,c):
        """
        #expr:Expr
        #thenStmt:Stmt
        #elseStmt:Stmt
        """
        env = c[0].copy()

        if type(self.visit(ast.expr,(env,c[1],c[2],None,c[4],c[5]))) != BoolType:
            raise TypeMismatchInStatement(ast)

        ts = self.visit(ast.thenStmt,(env,c[1],c[2],[],c[4],c[5]))
        es = self.visit(ast.elseStmt,(env,c[1],c[2],[],c[4],c[5])) if ast.elseStmt else None
        
        if ts is True and es is True:
            return True
        elif ts is "BC" and es is "BC" or\
             ts is "BC" and es is True or\
             ts is True and es is "BC":
            return "BC"

    def visitFor(self,ast,c):
        """
        expr1,expr2,expr3: Expr
        loop: Stmt
        """
        env = c[0].copy()

        ex1 = self.visit(ast.expr1,(env,c[1],False,[],c[4],c[5]))
        ex2 = self.visit(ast.expr2,(env,c[1],False,[],c[4],c[5]))
        ex3 = self.visit(ast.expr3,(env,c[1],False,[],c[4],c[5]))
        if type(ex1) is not IntType or\
           type(ex2) is not BoolType or\
           type(ex3) is not IntType:
            raise TypeMismatchInStatement(ast)
        # visit all block 
        self.visit(ast.loop,(env,c[1],True,[],c[4],c[5]))
        

    def visitDowhile(self,ast,c):
        """
        sl:  list(Stmt)
        exp: Expr
        """
        env = c[0].copy()
        isEnd = False 
        for st in ast.sl:
            if isEnd is True or isEnd is "BC":
                raise UnreachableStatement(st)
            isEnd = self.visit(st,(env,c[1],True,[],c[4],c[5]))
        if type(self.visit(ast.exp,(env,c[1],False,[],c[4],c[5]))) is not BoolType:
            raise TypeMismatchInStatement(ast)
        return True if isEnd is True else None


    def visitBinaryOp(self,ast,c):
        """
        #op:string
        #left:Expr
        #right:Expr
        """
        env = c[0].copy() if c[0] is not None else []
        le  = self.visit(ast.left,(env,c[1],c[2],[],c[4],c[5]))
        ri  = self.visit(ast.right,(env,c[1],c[2],[],c[4],c[5]))
        op  = ast.op

        if op == "+" or op == "-" or op == "*" or op == "/":
            rtype = BinOpType(le,ri)
            if rtype is not None:
                return rtype
            raise TypeMismatchInExpression(ast)
        elif op == "<" or op == "<=" or op == ">" or op ==">=":
            rtype = BinOpType(le,ri)
            if rtype is not None:
                return BoolType()
            raise TypeMismatchInExpression(ast)
        elif op == "==" or op == "!=":
            if (type(le),type(ri)) == (IntType,IntType):
                return BoolType()
            elif (type(le),type(ri)) == (BoolType,BoolType):
                return BoolType()
            raise TypeMismatchInExpression(ast)
        elif op == "%":
            if (type(le),type(ri)) == (IntType,IntType):
                return IntType()
            raise TypeMismatchInExpression(ast)
        elif op == "&&" or op == "||":
            if (type(le),type(ri)) == (BoolType,BoolType):
                return BoolType()
            raise TypeMismatchInExpression(ast)
        elif op == "=":
            if assignExplicitType(le,ri): 
                return le
            raise TypeMismatchInExpression(ast)
        raise TypeMismatchInExpression(ast)

    def visitUnaryOp(self,ast,c):
        """
        op: String
        body: Expr
        """
        env = c[0].copy()
        rtype  = self.visit(ast.body,(env,c[1],c[2],[],c[4],c[5]))
        if ast.op is "!":
            if type(rtype) is not BoolType:
                raise TypeMismatchInExpression(ast) 
            return BoolType()
        if (type(rtype) is not IntType) and (type(rtype) is not FloatType):
            raise TypeMismatchInExpression(ast) 
        return rtype


    def visitId(self,ast,c):
        """ 
        name:string 
        """
        env = c[0].copy() if c[0] is not None else []
        res = self.lookup(ast.name, env, lambda x:x.name)
        if res is None or type(res.functype) is FuncType :
            raise Undeclared(Identifier(),ast.name) 
        elif type(res) is Symbol:
            return res.functype 
        else:
            raise Undeclared(Identifier(),ast.name) 


    def visitCallExpr(self, ast, c): 
        """
        method: Id
        param: list(Expr)
        """
        env = c[0].copy() 
        res = self.lookup(ast.method.name,env, lambda x: x.name)
        lsp = [self.visit(x,(env,c[1],c[2],[],c[4],c[5])) for x in ast.param]
      
        if res is None or not type(res.functype) is FuncType:
            raise Undeclared(Function(),ast.method.name)
        elif len(res.functype.partype) != len(lsp):
            raise TypeMismatchInExpression(ast)
        else:
            for i in range(len(lsp)):
                if AssignmentRule(res.functype.partype[i],lsp[i]) is False:
                    raise TypeMismatchInExpression(ast)
            # some magic here :v 
            if ast.method.name != c[5]:
                c[4][ast.method.name] += 1

            return res.functype.rettype


    def visitArrayCell(self,ast,c):
        """
        arr: Expr
        idx: Expr
        """
        env = c[0].copy()
        if type(self.visit(ast.idx,(env,c[1],c[2],[],c[4],c[5]))) is not IntType:
            raise TypeMismatchInExpression(ast)
        else:
            arr = self.visit(ast.arr,(env,c[1],c[2],[],c[4],c[5]))
            if type(arr) is (ArrayType or ArrayPointerType):
                return arr.eleType
            else:
                raise TypeMismatchInExpression(ast)


    def visitBreak(self,ast,c):
        if c[2] == False:
            raise BreakNotInLoop()
        return "BC"

    def visitContinue(self,ast,c):
        if c[2] == False:
            raise ContinueNotInLoop()
        return "BC"

    def visitReturn(self,ast,c):
        """
        expr: Expr
        """
        env   = c[0].copy()
        rtype = c[1]
        if ast.expr is None and type(rtype) is not VoidType:
            raise TypeMismatchInStatement(ast)
        elif ast.expr is None and type(rtype) is VoidType:
            return True
        elif AssignmentRule(rtype,self.visit(ast.expr,(env,None, False,[],c[4],c[5]))) is False:
            raise TypeMismatchInStatement(ast)

        return True 

    def visitIntType(self,ast,c):
        return IntType()

    def visitFloatType(self,ast,c):
        return FloatType()

    def visitBoolType(self,ast,c):
        return BoolType()

    def visitStringType(self,ast,c):
        return StringType()

    def visitVoidType(self,ast,c):
        return VoidType()

    def visitArrayType(self,ast,c):
        return ast.eleType 

    def visitArrayPointerType(self,ast,c):
        return ast.eleType

    def visitIntLiteral(self,ast, c): 
        return IntType()
    
    def visitFloatLiteral(self,ast, c): 
        return FloatType()

    def visitStringLiteral(self,ast, c): 
        return StringType()

    def visitBooleanLiteral(self,ast, c): 
        return BoolType()
   
