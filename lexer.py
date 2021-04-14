import re
import sys
from operator import itemgetter, attrgetter

class Token() :
    def __init__(self, type, valeur, ligne = 0, position = (0,0)):
        self.type = type
        self.valeur = valeur
        self.ligne = ligne
        self.position_debut = position[0]
        self.position_fin = position[1]

    def __str__(self):
        return "\n type:" + str(self.type) + "\n valeur:" + str(self.valeur) + "\n position: ligne " + str(self.ligne) + " position " + str(self.position_debut)


regexExpressions = [
    #(r"\s\s\s\s", 'TAB'),
    (r"\b(for)\b", 'FOR'),
    (r"\b(if)\b", 'IF'),
    (r"\b(else)\b", 'ELSE'),
    (r"\b(while)\b", 'WHILE'),
    (r"\b(return)\b", 'RETURN'),
    (r"\b(in)\b", 'IN'),
    (r"\b(range)\b", 'RANGE'),
    (r"\b(\w)+\b", 'IDENTIFIER'),
    (r"\#", 'COMMENT'),
    (r"\=", 'EQ'),
    (r"\=", 'ASSIGN'),
    (r"\+", 'ADD'),
    (r"\-", 'SUB'),
    (r"\*", 'MUL'),
    (r"\/", 'DIV'),
    (r"\!", 'DIFF'),
    (r"\!\=", 'NEQ'),
    (r"\|", 'BAR'),
    (r"\<", 'INF'),
    (r"\<\=", 'INFEQ'),
    (r"\>", 'SUP'),
    (r"\>\=", 'SUPEQ'),
    (r"\(", 'LPAREN'),
    (r"\)", 'RPAREN'),
    (r"\{", 'LBRACE'),
    (r"\}", 'RBRACE'),
    (r"\[", 'LBRACKET'),
    (r"\]", 'RBRACKET'),
    (r"\;", 'SEMICOLON'),
    (r"\:", 'COLON'),
    (r"\,", 'COMMA'),
    (r"[+-]?[0-9]+(.[0-9]+)", 'FLOAT'),
    (r"[+-]?[0-9]+", 'INT'),
    # (r"\n", 'EOL')
    ]


def Lexer(file) :
    """
    Lexing python source file and extracting tokens from it
    :param file: file string stream from readlines()
    :return: list of Tokens found in file
    """

    Tokens = []
    lineNumber = 1
    for line in file:
        positions = []
        for regex in regexExpressions:
                kind, description = regex
                matchlist = re.finditer(kind, line)
                for match in matchlist : 
                    if match and (match.span() not in positions) :
                        token = Token(description, match.group(),lineNumber, match.span())
                        Tokens.append(token)

                        positions.append(match.span())
                
        lineNumber +=1
    # then we sort the tokens by begining position using sorted()
    tsorted = sorted(Tokens, key=attrgetter('ligne','position_debut'))
    return tsorted



def FileReWritting(file) : 
    """
    For it to work , you need to add the regex for EOL (commented)
    copies initial file then ret-writes it using tokens 
    :param file: file string stream from readlines 
    """
    Tokens  = Lexer(file)
    copyText = '' 
    for token in Tokens : 

        copyText += str(token.valeur)

    copyFile = open("test-copy.py", 'w')
    copyFile.write(copyText)
    copyFile.close()
    
def tokenPrint(Tokens) : 
    for token in Tokens : 
        print(token)

        

inputText = open("test.py").readlines()
Tokens  = Lexer(inputText)
tokenPrint(Tokens)
# FileReWritting(inputText)

