import re
import sys


from operator import itemgetter, attrgetter

class Token() :
    def __init__(self, type, valeur, ligne, position):
        self.type = type
        self.valeur = valeur
        self.ligne = ligne
        self.position_debut = position[0]
        self.position_fin = position[1]

    def __str__(self):
        return "\nTOKEN FOUND \n type:" + str(self.type) + "\n valeur:" + str(self.valeur) + "\n position: ligne " + str(self.ligne) + " position " + str(self.position_debut)
>>>>>>> Stashed changes

regexExpressions = [
    
    (r"\b(for)\b", 'FOR'),
    (r"\b(if)\b", 'IF'),
    (r"\b(else)\b", 'ELSE'),
    (r"\b(while)\b", 'WHILE'),
    (r"\b(return)\b", 'RETURN'),
    (r"\b(in)\b", 'IN'),
    (r"\b(range)\b", 'RANGE'),
    (r"\b(\w+)\b", 'STRING'),
    (r"\#", 'COMMENT'),
    (r"\=", 'EQ'),
    (r"\+", 'ADD'),
    (r"\-", 'SUB'),
    (r"\*", 'MUL'),
    (r"\/", 'DIV'),
    (r"\!", 'DIFF'),
    (r"\|", 'BAR'),
    (r"\<", 'INF'),
    (r"\>", 'SUP'),
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
    (r"\n", 'EOL')
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
                match = re.search(kind, line)
                if match :
                    token = Token(description, match.group(),lineNumber, match.span())
                    if match.span() not in positions : 
                        Tokens.append(token)
                        positions.append(match.span())
                        

        lineNumber +=1
    # then we sort the tokens by begining position using sorted()
    tsorted = sorted(Tokens, key=attrgetter('ligne','position_debut'))
    return tsorted

def FileReWritting(file) : 
    """
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
FileReWritting(inputText)

