import re
import sys

class Token() :
    def __init__(self, type, valeur, ligne, position):
        self.type = type
        self.valeur = valeur
        self.ligne = ligne
        self.position = position

    def __str__(self):
        return "\nTOKEN FOUND \n type:" + str(self.type) + "\n valeur:" + str(self.valeur) + "\n position: ligne " + str(self.ligne) + " position " + str(self.position[0])

regexExpressions = [

    (r"\b(for)\b", 'FOR'),
    (r"\b(if)\b", 'IF'),
    (r"\b(else)\b", 'ELSE'),
    (r"\b(while)\b", 'WHILE'),
    (r"\b(return)\b", 'RETURN'),
    (r"\#", 'COMMENT'),
    (r"\w+", 'STRING'),
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
    (r"[+-]?[0-9]+(.[0-9]+)?", 'INT'),
    (r"\n", 'EOL')
    ]


def Lexer(file) :
    """
    Lexing python source file and extracting tokens from it
    :param file: file stream from readlines()
    :return: list of Tokens found in file
    """

    Tokens = []
    lineNumber = 1
    for line in file:
        for regex in regexExpressions:
                kind, description = regex
                match = re.search(kind, line)
                if match :
                    token = Token(description, match.group(),lineNumber, match.span())
                    Tokens.append(token)
                    print(token)

        lineNumber +=1

    return Tokens

inputText = open("test.py").readlines()
Tokens  = Lexer(inputText)
