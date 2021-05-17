import sys
import argparse
import lexer
from lexer import Lexer, tokenPrint
from parser_AST import Parser
from prettyprinter import Prettyprinter
from MIDIcompiler import MIDIcompiler




if __name__ == '__main__':

    parser=argparse.ArgumentParser(
    description='''
    Le script permet de compiler un programme écrit en python (plus ou moins, voir doc) en utilisant le pattern Visiteur
    ''',
    epilog="""made by @sytrics for ENSTA Bretagne\n""")
    parser.add_argument('input', type=str , help='the name of the file to be compiled')
    parser.add_argument('output', type=str , help='the name of the file where we will print using Pretty-printer')
    parser.add_argument('--compiler',default="PP", type=str, help='choose the compiler PP: prettyprinter / MIDI: MIDI-Compiler')
    parser.add_argument('--verbose',default=0, type=bool, help='BOOL : if verbose set to 1, displays every visit method for debug purposes')
    args=parser.parse_args()

    inputText = open(args.input).readlines()
    print("\n======Start lexing======\n")
    Tokens  = Lexer(inputText)
    print("\n======Lexing Done======\n")
    print("\n======Start parsing======\n")
    parser = Parser(Tokens)
    AST = parser.parse()
    print("\n======Print AST======\n")
    AST.printTree()
    if args.compiler == 'PP' : 
        visiteur = Prettyprinter(args.verbose)
    elif args.compiler == 'MIDI' : 
        visiteur = MIDIcompiler(args.verbose)
    print("\n======compiler :" + args.compiler + " compiling to "+ args.output + "======\n")
    print('Verbosity set to ' + str(args.verbose))
    visiteur.visitRoot(AST)
    visiteur.compile(args.output)
    print('\n======Done======\n')
