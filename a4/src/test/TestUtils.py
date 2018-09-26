import sys,os
from antlr4 import *
from antlr4.error.ErrorListener import ConsoleErrorListener,ErrorListener
if not './main/mc/parser/' in sys.path:
    sys.path.append('./main/mc/parser/')
if os.path.isdir('../target/main/mc/parser') and not '../target/main/mc/parser/' in sys.path:
    sys.path.append('../target/main/mc/parser/')
from MCLexer import MCLexer
from MCParser import MCParser
from lexererr import *
from ASTGeneration import ASTGeneration
from StaticCheck import StaticChecker
from StaticError import *
from CodeGenerator import CodeGenerator
import subprocess

JASMIN_JAR = "./external/jasmin.jar"

class TestUtil:
    @staticmethod
    def makeSource(inputStr,num):
        filename = "./test/testcases/" + str(num) + ".txt"
        file = open(filename,"w")
        file.write(inputStr)
        file.close()
        return FileStream(filename)


class TestLexer:
    @staticmethod
    def checkLexeme(input,expect,num):
        inputfile = TestUtil.makeSource(input,num)
        dest = open("./test/solutions/" + str(num) + ".txt","w")
        lexer = MCLexer(inputfile)
        try:
            TestLexer.printLexeme(dest,lexer)
        except (ErrorToken,UncloseString,IllegalEscape) as err:
            dest.write(err.message)
        finally:
            dest.close() 
        dest = open("./test/solutions/" + str(num) + ".txt","r")
        line = dest.read()
        return line == expect

    @staticmethod    
    def printLexeme(dest,lexer):
        tok = lexer.nextToken()
        if tok.type != Token.EOF:
            dest.write(tok.text+",")
            TestLexer.printLexeme(dest,lexer)
        else:
            dest.write("<EOF>")
class NewErrorListener(ConsoleErrorListener):
    INSTANCE = None
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxException("Error on line "+ str(line) + " col " + str(column)+ ": " + offendingSymbol.text)
NewErrorListener.INSTANCE = NewErrorListener()

class SyntaxException(Exception):
    def __init__(self,msg):
        self.message = msg

class TestParser:
    @staticmethod
    def createErrorListener():
         return NewErrorListener.INSTANCE

    @staticmethod
    def checkParser(input,expect,num):
        inputfile = TestUtil.makeSource(input,num)
        dest = open("./test/solutions/" + str(num) + ".txt","w")
        lexer = MCLexer(inputfile)
        listener = TestParser.createErrorListener()

        tokens = CommonTokenStream(lexer)

        parser = MCParser(tokens)
        parser.removeErrorListeners()
        parser.addErrorListener(listener)
        try:
            parser.program()
            dest.write("successful")
        except SyntaxException as f:
            dest.write(f.message)
        except Exception as e:
            dest.write(str(e))
        finally:
            dest.close()
        dest = open("./test/solutions/" + str(num) + ".txt","r")
        line = dest.read()
        return line == expect

class TestAST:
    @staticmethod
    def checkASTGen(input,expect,num):
        inputfile = TestUtil.makeSource(input,num)
        dest = open("./test/solutions/" + str(num) + ".txt","w")
        lexer = MCLexer(inputfile)
        tokens = CommonTokenStream(lexer)
        parser = MCParser(tokens)
        tree = parser.program()
        asttree = ASTGeneration().visit(tree)
        dest.write(str(asttree))
        dest.close()
        dest = open("./test/solutions/" + str(num) + ".txt","r")
        line = dest.read()
        return line == expect

    @staticmethod
    def test(testdir,soldir,num):
        test = "./test/" + testdir + "/" + str(num) + ".txt"
        sol = open("./test/" + soldir + "/" + str(num) + ".txt","r")
        expect = sol.read().replace('\n', '')
        
        inputfile = FileStream(test)
        lexer = MCLexer(inputfile)
        tokens = CommonTokenStream(lexer)
        parser = MCParser(tokens)
        tree = parser.program()
        asttree = ASTGeneration().visit(tree)

        
        
        checker = StaticChecker(asttree)
        try:
            res = checker.check()
            line = str(list(res))
            #print(str(list(res)))
        except StaticError as e:
            line = str(e)
            #print(str(e))
        finally:
            sol.close()
        if(line != expect):
            print("test:", num)
            print("Line  :", line,"EOF")
            print("Expect:", expect,"EOF")
        return line == expect



class TestChecker:
    @staticmethod
    def test(input,expect,num):
        dest = open("./test/solutions/" + str(num) + ".txt","w")
        
        if type(input) is str:
            inputfile = TestUtil.makeSource(input,num)
            lexer = MCLexer(inputfile)
            tokens = CommonTokenStream(lexer)
            parser = MCParser(tokens)
            tree = parser.program()
            asttree = ASTGeneration().visit(tree)
        else:
            inputfile = TestUtil.makeSource(str(input),num)
            asttree = input
        
        
        checker = StaticChecker(asttree)
        try:
            res = checker.check()
            dest.write(str(list(res)))
        except StaticError as e:
            dest.write(str(e))
        finally:
            dest.close()
        dest = open("./test/solutions/" + str(num) + ".txt","r")
        line = dest.read()
        return line == expect

class TestCodeGen():
    @staticmethod
    def test(input, expect, num):
        global JASMIN_JAR
        solpath = "./test/solutions/"
        dest = open(solpath + str(num) + ".txt","w")
        
        if type(input) is str:
            inputfile = TestUtil.makeSource(input,num)
            lexer = MCLexer(inputfile)
            tokens = CommonTokenStream(lexer)
            parser = MCParser(tokens)
            tree = parser.program()
            asttree = ASTGeneration().visit(tree)
        else:
            inputfile = TestUtil.makeSource(str(input),num)
            asttree = input
        
        
        codeGen = CodeGenerator()
        
        path = solpath + str(num)
        if not os.path.isdir(path):
            os.mkdir(path)
        try:
            codeGen.gen(asttree, path)
            
            subprocess.call("java  -jar "+ JASMIN_JAR + " " + path + "/MCClass.j",shell=True,stderr=subprocess.STDOUT)
            

            f = open(solpath + str(num) + ".txt","w")
            subprocess.call("java -cp ./lib:. MCClass",shell=True, stdout = f)
            f.close()
        except StaticError as e:
            dest.write(str(e))
        except subprocess.CalledProcessError as e:
            raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
        finally:
            dest.close()
        dest = open(solpath + str(num) + ".txt","r")
        line = dest.read()
        return line == expect
