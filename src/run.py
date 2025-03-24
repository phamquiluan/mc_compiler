import sys,os
sys.path.append('./test/')
sys.path.append('./main/mc/parser/')
sys.path.append('./main/mc/utils/')
sys.path.append('./main/mc/astgen/')
sys.path.append('./main/mc/checker/')
sys.path.append('./main/mc/codegen/')
import subprocess
import unittest
from antlr4 import *

ANTLR_JAR = '/usr/local/lib/antlr-4.7.1-complete.jar'
TARGET_DIR = '../target'
GENERATE_DIR = 'main/mc/parser'

def main(argv):
    global ANTLR_JAR, TARGET_DIR, GENERATE_DIR

    if len(argv) < 1:
        printUsage()
    elif argv[0] == 'gen':
        subprocess.run(["java","-jar",ANTLR_JAR,"-o","../target","-no-listener","-visitor","main/mc/parser/MC.g4"])
    elif argv[0] == 'clean':
        subprocess.run(["rm","-rf",TARGET_DIR + "/*"])
    elif argv[0] == '-assign1':
        from TestUtils import TestLexer,TestParser
        lexstart = int(argv[1])
        lexend = int(argv[2]) + 1
        lextestdir = argv[3]
        lexsoldir = argv[4]
        recstart = int(argv[5])
        recend = int(argv[6]) + 1
        rectestdir = argv[7]
        recsoldir = argv[8]
        for i in range(lexstart,lexend):
            TestLexer.test(lextestdir,lexsoldir,i)
        for i in range(recstart,recend):
            TestParser.test(rectestdir,recsoldir,i)
    elif argv[0] == '-assign2':
        from TestUtils import TestAST
        aststart = int(argv[1])
        astend = int(argv[2]) + 1
        asttestdir = argv[3]
        astsoldir = argv[4]
        print("asttestdir = "+asttestdir)
        print("astsoldir = "+astsoldir)
        for i in range(aststart,astend):
            TestAST.test(asttestdir,astsoldir,i)
    elif argv[0] == '-assign3':
        from TestUtils import TestAST
        aststart = 401
        astend = 410
        asttestdir = "testcases"
        astsoldir = "solutions"
        print("asttestdir = "+asttestdir)
        print("astsoldir = "+astsoldir)
        for i in range(aststart,astend):
            TestAST.test(asttestdir,astsoldir,i)
    elif argv[0] == 'test':     
        if not os.path.isdir(TARGET_DIR + "/" + GENERATE_DIR):
            subprocess.run(["java","-jar",ANTLR_JAR,"-o",GENERATE_DIR,"-no-listener","-visitor","main/mc/parser/MC.g4"])
        if not (TARGET_DIR + "/" + GENERATE_DIR) in sys.path:
            sys.path.append(TARGET_DIR + "/" + GENERATE_DIR)
        if len(argv) < 2:
            printUsage()
        elif argv[1] == 'LexerSuite':
            from LexerSuite import LexerSuite
            suite = unittest.makeSuite(LexerSuite)
            test(suite)
        elif argv[1] == 'ParserSuite':
            from ParserSuite import ParserSuite
            suite = unittest.makeSuite(ParserSuite)
            test(suite)
        elif argv[1] == 'ASTGenSuite':
            from ASTGenSuite import ASTGenSuite
            suite = unittest.makeSuite(ASTGenSuite)
            test(suite)
        elif argv[1] == 'CodeGenSuite':
            from CodeGenSuite import CheckCodeGenSuite
            suite = unittest.makeSuite(CheckCodeGenSuite)
            test(suite)
        else:
            printUsage()
    else:
        printUsage()
    

def test(suite):
    from pprint import pprint
    from io import StringIO
    stream = StringIO()
    runner = unittest.TextTestRunner(stream=stream)
    result = runner.run(suite)
    print('Tests run ', result.testsRun)
    print('Errors ', result.errors)
    pprint(result.failures)
    stream.seek(0)
    print('Test output\n', stream.read())

def printUsage():
    print("python3 run.py gen")
    print("python3 run.py test LexerSuite")
    print("python3 run.py test ParserSuite")
    print("python3 run.py test ASTGenSuite")

if __name__ == "__main__":
   main(sys.argv[1:])
