from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *

class ASTGeneration(MCVisitor):
     
    #program: decls+ EOF;
    def visitProgram(self,ctx:MCParser.ProgramContext):
        declist=[]
        for dec in ctx.decls():
            if dec.funcdecl():
                declist.append(self.visit(dec))
            
            # case var
            else:
                vardeclist=self.visit(dec)
                declist=declist+vardeclist
        return Program(declist)

    #decls : vardecl|funcdecl;
    def visitDecl(self,ctx:MCParser.DeclsContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl())
        else:
            return self.visit(ctx.funcdecl())

    
    #funcdecl : fultype ID LB plist? RB block_s;
    #plist   : para (CM para)*;
    def visitFuncdecl(self,ctx:MCParser.FuncdeclContext):
        name = ctx.ID().getText()
        param= ([self.visit(x) for x in ctx.plist().para()] if ctx.plist() else [])
        rett = self.visit(ctx.fultype())
        body = self.visit(ctx.block_s())
        return FuncDecl(Id(name),param,rett,body)
   
    
    #block_s : LP vardecl* stmt* RP;
    def visitBlock_s(self,ctx:MCParser.Block_sContext):
        vd = []
        if ctx.vardecl():
            for x in ctx.vardecl():
                vd = vd + self.visit(x)
        st = ([self.visit(x) for x in ctx.stmt()] if ctx.stmt() else [])
        return Block(vd,st)
        
    
    #stmt : if_s|dowhl_s|for_s|break_s|cont_s|ret_s|expr_s|block_s;
    def visitStmt(self,ctx:MCParser.StmtContext):
        if ctx.if_s():
            return self.visit(ctx.if_s())
        elif ctx.dowhl_s():
            return self.visit(ctx.dowhl_s())
        elif ctx.for_s():
            return self.visit(ctx.for_s())
        elif ctx.break_s():
            return Break()
        elif ctx.cont_s():
            return Continue()
        elif ctx.ret_s():
            return self.visit(ctx.ret_s())
        elif ctx.expr_s():
            return self.visit(ctx.expr_s())
        else:
            return self.visit(ctx.block_s())

    #if_s : IF LB expr RB stmt (ELSE stmt)?; 
    def visitIf_s(self,ctx:MCParser.If_sContext):
        ex = self.visit(ctx.expr())
        st1= self.visit(ctx.stmt(0))
        st2= None
        if ctx.stmt(1):
            st2=self.visit(ctx.stmt(1))
        return If(ex,st1,st2)

    #dowhl_s : DO stmt+ WHILE expr SEMI;
    def visitDowhl_s(self,ctx:MCParser.Dowhl_sContext):
        lst=[self.visit(x) for x in ctx.stmt()]
        exp=self.visit(ctx.expr())
        return Dowhile(lst,exp)

    #for_s : FOR LB expr SEMI expr SEMI expr RB stmt;
    def visitFor_s(self,ctx:MCParser.For_sContext):
        e1=self.visit(ctx.expr(0))
        e2=self.visit(ctx.expr(1))
        e3=self.visit(ctx.expr(2))
        st=self.visit(ctx.stmt())
        return For(e1,e2,e3,st)

    #ret_s : RETURN expr? SEMI;
    def visitRet_s(self,ctx:MCParser.Ret_sContext):
        if ctx.expr():
            return Return(self.visit(ctx.expr()))
        else:
            return Return()
        

    #expr_s : expr SEMI;
    def visitExpr_s(self,ctx:MCParser.Expr_sContext):
        return self.visit(ctx.expr())

    #para : vartype ID (LSB RSB)?;
    def visitPara(self,ctx:MCParser.ParaContext):
        if ctx.LSB():
            return VarDecl(Id(ctx.ID().getText()),ArrayPointerType(self.visit(ctx.vartype())))
        else:
            return VarDecl(Id(ctx.ID().getText()),self.visit(ctx.vartype()))
    
            
    #fultype : vartype LSB RSB |vartype|VOIDTYPE;
    def visitFultype(self,ctx:MCParser.FultypeContext):
        if ctx.VOIDTYPE():
            return VoidType()
        elif ctx.LSB():
            return ArrayPointerType(self.visit(ctx.vartype()))
        else:
            return self.visit(ctx.vartype())

    
    # vardecl  :vartype varid (CM varid)* SEMI;
    # varid   : ID (LSB INTLIT RSB)?;
    def visitVardecl(self,ctx:MCParser.VardeclContext):
        ans=[]
        for vid in ctx.varid():
            # int a[5]
            if vid.INTLIT():
                ans.append(VarDecl(Id(vid.ID().getText()), ArrayType(IntLiteral(int(vid.INTLIT().getText())), self.visit(ctx.vartype()))))
            # int a
            else:
                ans.append(VarDecl(Id(vid.ID().getText()), self.visit(ctx.vartype())))
        return ans


    # vartype : INTTYPE|BOOLEAN|FLOATTYPE|STRING;
    def visitVartype(self,ctx:MCParser.VartypeContext):
        if ctx.INTTYPE():
            return IntType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.FLOATTYPE():
            return FloatType()
        else:
            return StringType()
        

    # funcall : ID LB (expr (CM expr)*)? RB;	
    def visitFuncall(self,ctx:MCParser.FuncallContext):
        return CallExpr(Id(ctx.ID().getText()),[self.visit(x) for x in ctx.expr()] if ctx.expr() else [])
    
    #expr : expr2 ASS_OP expr | expr2;
    def visitExpr(self,ctx:MCParser.ExprContext):
        if ctx.ASS_OP():
            return BinaryOp("=",self.visit(ctx.expr2()),self.visit(ctx.expr()))
        else:   
            return self.visit(ctx.expr2())

    #expr2 : expr2 OR_OP  expr3 | expr3;
    def visitExpr2(self,ctx:MCParser.Expr2Context):
        if ctx.OR_OP():
            return BinaryOp("||",self.visit(ctx.expr2()),self.visit(ctx.expr3()))
        else:
            return self.visit(ctx.expr3())

    #expr3 : expr3 AND_OP expr4 | expr4;
    def visitExpr3(self,ctx:MCParser.Expr3Context):
        if ctx.AND_OP():
            return BinaryOp("&&",self.visit(ctx.expr3()),self.visit(ctx.expr4()))
        else:
            return self.visit(ctx.expr4())

    #expr4 : expr5 (EQUAL_OP|NOT_EQ_OP) expr5 | expr5;
    def visitExpr4(self,ctx:MCParser.Expr4Context):
        if ctx.EQUAL_OP():
            return BinaryOp("==",self.visit(ctx.expr5(0)),self.visit(ctx.expr5(1)))
        elif ctx.NOT_EQ_OP():
            return BinaryOp("!=",self.visit(ctx.expr5(0)),self.visit(ctx.expr5(1)))
        else:
            return self.visit(ctx.expr5(0))

    #expr5 : expr6 (LT_OP|LE_OP|GT_OP|GE_OP) expr6 | expr6;
    def visitExpr5(self,ctx:MCParser.Expr5Context):
        if ctx.LT_OP():
            return BinaryOp("<",self.visit(ctx.expr6(0)),self.visit(ctx.expr6(1)))
        elif ctx.LE_OP():
            return BinaryOp("<=",self.visit(ctx.expr6(0)),self.visit(ctx.expr6(1)))
        elif ctx.GT_OP():
            return BinaryOp(">",self.visit(ctx.expr6(0)),self.visit(ctx.expr6(1)))
        elif ctx.GE_OP():
            return BinaryOp(">=",self.visit(ctx.expr6(0)),self.visit(ctx.expr6(1)))
        else:
            return self.visit(ctx.expr6(0))

    #expr6 : expr6 (ADD_OP|SUB_OP) expr7 | expr7;
    def visitExpr6(self,ctx:MCParser.Expr6Context):
        if ctx.ADD_OP():
            return BinaryOp("+",self.visit(ctx.expr6()),self.visit(ctx.expr7()))
        elif ctx.SUB_OP():
            return BinaryOp("-",self.visit(ctx.expr6()),self.visit(ctx.expr7()))
        else:
            return self.visit(ctx.expr7())

    #expr7 : expr7 (MUL_OP|MOD_OP|DIV_OP) expr8 | expr8;
    def visitExpr7(self,ctx:MCParser.Expr7Context):
        if ctx.MUL_OP():
            return BinaryOp("*",self.visit(ctx.expr7()),self.visit(ctx.expr8()))
        elif ctx.MOD_OP():
            return BinaryOp("%",self.visit(ctx.expr7()),self.visit(ctx.expr8()))
        elif ctx.DIV_OP():
            return BinaryOp("/",self.visit(ctx.expr7()),self.visit(ctx.expr8()))
        else:
            return self.visit(ctx.expr8())

    #expr8 : (SUB_OP|NOT_OP) expr8 | expr9;
    def visitExpr8(self,ctx:MCParser.Expr8Context):
        if ctx.SUB_OP():
            return UnaryOp("-",self.visit(ctx.expr8()))
        elif ctx.NOT_OP():
            return UnaryOp("!",self.visit(ctx.expr8()))
        else:
            return self.visit(ctx.expr9())

    #expr9 : term LSB expr RSB | term;
    def visitExpr9(self,ctx:MCParser.Expr9Context):
        if ctx.expr():
            arr=self.visit(ctx.term())
            idx=self.visit(ctx.expr())
            return ArrayCell(arr,idx)
        else:
            return self.visit(ctx.term())

    #term : ID | INTLIT | FLOATLIT | BOOLLIT | STRINGLIT | LB expr RB | funcall;
    def visitTerm(self,ctx:MCParser.TermContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.BOOLLIT():
            return BooleanLiteral(True if ctx.BOOLLIT().getText()=="true" else False)
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.expr():
            return self.visit(ctx.expr())
        else:
            return self.visit(ctx.funcall())











