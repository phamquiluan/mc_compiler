import sys,os
sys.path.append('./test/')
sys.path.append('./main/mc/parser/')
sys.path.append('./main/mc/utils/')
sys.path.append('./main/mc/astgen/')
sys.path.append('./main/mc/checker')
import platform
import subprocess
import unittest
from antlr4 import *
import shutil

ANTLR_JAR = '/usr/local/lib/antlr-4.7.1-complete.jar'
TARGET_DIR = '../target'
GENERATE_DIR = '' if platform.system() == 'Windows' else '/main/mc/parser'

def main(argv):
    global ANTLR_JAR, TARGET_DIR, GENERATE_DIR

    if len(argv) < 1:
        printUsage()
    elif argv[0] == 'gen':
        subprocess.run(["java","-jar",ANTLR_JAR,"-o","../target","-no-listener","-visitor","main/mc/parser/MC.g4"])
    elif argv[0] == 'clean':
        for dir in os.listdir(TARGET_DIR):
            shutil.rmtree(os.path.join(TARGET_DIR,dir))
    elif argv[0] == 'test':     
        if not os.path.isdir(TARGET_DIR  + GENERATE_DIR):
            subprocess.run(["java","-jar",ANTLR_JAR,"-o",GENERATE_DIR,"-no-listener","-visitor","main/mc/parser/MC.g4"])
        if not (TARGET_DIR + GENERATE_DIR) in sys.path:
            sys.path.append(TARGET_DIR  + GENERATE_DIR)
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
        elif argv[1] == 'CheckSuite':
            from CheckSuite import CheckSuite
            suite = unittest.makeSuite(CheckSuite)
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
