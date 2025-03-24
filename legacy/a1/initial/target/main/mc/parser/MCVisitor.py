# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MCParser import MCParser
else:
    from MCParser import MCParser

# This class defines a complete generic visitor for a parse tree produced by MCParser.

class MCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MCParser#program.
    def visitProgram(self, ctx:MCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#vardec.
    def visitVardec(self, ctx:MCParser.VardecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#vartype.
    def visitVartype(self, ctx:MCParser.VartypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#arrtype.
    def visitArrtype(self, ctx:MCParser.ArrtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#arptype.
    def visitArptype(self, ctx:MCParser.ArptypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#fultype.
    def visitFultype(self, ctx:MCParser.FultypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#varid.
    def visitVarid(self, ctx:MCParser.VaridContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#funcdec.
    def visitFuncdec(self, ctx:MCParser.FuncdecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#plist.
    def visitPlist(self, ctx:MCParser.PlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#para.
    def visitPara(self, ctx:MCParser.ParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr.
    def visitExpr(self, ctx:MCParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr2.
    def visitExpr2(self, ctx:MCParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr3.
    def visitExpr3(self, ctx:MCParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr4.
    def visitExpr4(self, ctx:MCParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr5.
    def visitExpr5(self, ctx:MCParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr6.
    def visitExpr6(self, ctx:MCParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr7.
    def visitExpr7(self, ctx:MCParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr8.
    def visitExpr8(self, ctx:MCParser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr9.
    def visitExpr9(self, ctx:MCParser.Expr9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#term.
    def visitTerm(self, ctx:MCParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#stmt.
    def visitStmt(self, ctx:MCParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#if_s.
    def visitIf_s(self, ctx:MCParser.If_sContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#dowhl_s.
    def visitDowhl_s(self, ctx:MCParser.Dowhl_sContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#for_s.
    def visitFor_s(self, ctx:MCParser.For_sContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#break_s.
    def visitBreak_s(self, ctx:MCParser.Break_sContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#cont_s.
    def visitCont_s(self, ctx:MCParser.Cont_sContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#ret_s.
    def visitRet_s(self, ctx:MCParser.Ret_sContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr_s.
    def visitExpr_s(self, ctx:MCParser.Expr_sContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#funcall.
    def visitFuncall(self, ctx:MCParser.FuncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#block_s.
    def visitBlock_s(self, ctx:MCParser.Block_sContext):
        return self.visitChildren(ctx)



del MCParser