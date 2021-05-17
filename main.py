import sys
import argparse
import lexer
from lexer import Lexer, tokenPrint
from parser_AST import Parser
from Visitor import Visitor




if __name__ == '__main__':

    # adding test file name as command line argument
    """argParser = argparse.ArgumentParser()
    argParser.add_argument('testFileName')
    args = argParser.parse_args()

    testFileName = args.testFileName

    try:
        with open(testFilename) as testFile:
            testFileData = testFile.readlines()
    except FileNotFoundError:
        print('Error: test file {} does not exist'.format(testFileName))
        sys.exit()

    inputText = open(testFilename).readlines()
    Tokens  = Lexer(inputText)
    

    verbose = True
    parser = Parser(verbose)
    parser.parse(tokens)
    """

    inputText = open("test.py").readlines()
    Tokens  = Lexer(inputText)
    tokenPrint(Tokens)
    parser = Parser(Tokens)
    AST = parser.parse()
    AST.printTree()
    visiteur = Visitor()
    visiteur.visitRoot(AST)
    visiteur.prettyprint()
