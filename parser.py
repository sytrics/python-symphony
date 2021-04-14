import sys
import lexer
from Node import Node


class Parser:

    ADD_OP = ['ADD', 'SUB']
    REL_OP = ['EQ', 'NEQ', 'INF', 'INFEQ', 'SUP', 'SUPEQ']
    TERM_OP = ['MULT', 'DIV']


    def __init__(self):  
        self.tokens = []
        self.errors = 0
        self.indent = []
        self.AST = [] #list of nodes to build AST 
        

    def show_next(self, n=1):
        try:
            return self.tokens[n - 1]
        except IndexError:
            print('ERROR: no more tokens left!')
            sys.exit(1)

    def expect(self, kind):
        actualToken = self.show_next()
        actualKind = actualToken.kind
        actualPosition = actualToken.position
        if isinstance(kind, 'STRING') : 
            if actualKind == kind:
                return self.accept_it()
            else:
                print('Error at {}: expected {}, got {} instead'.format(str(actualPosition), kind, actualKind))
                sys.exit(1)
        else : 
            if actualKind in kind : 
                 return self.accept_it()
            else:
                print('Error at {}: expected {}, got {} instead'.format(str(actualPosition), kind, actualKind))
                sys.exit(1)

    def accept_it(self):
        # token = self.show_next()
        # output = str(token.kind) + ' ' + token.value
        return self.tokens.pop(0)

    def parse_program(self):
        for token in self.tokens :
            if token.type == 'TAB' :
                self.indent[token.ligne()-1] += 1
                self.expect('TAB') #pop out of tokens 
                continue
            if token.type == 'IDENTIFIER' : 
                self.expect("IDENTIFIER")
                if self.show_next().type == 'EOL' : 
                    #new line
                    pass
            

        self.expect('RBRACE')
        if (self.errors == 1):
            print('WARNING: 1 error found!')
        elif (self.errors > 1):
            print('WARNING: ' + str(self.errors) + ' errors found!')
        else:
            print('parser: syntax analysis successful!')

    
        
    def factor(self):
        """
        factor = IDENTIFIER | NUMBER | "(" expression ")"
        .
        """
        if self.show_next().type == 'IDENTIFIER' :
            self.expect('IDENTIFIER')
            pass
        elif self.show_next().type == 'INT':
            self.expect('INT')
            pass
        elif self.show_next().type == 'LPAREN':
            self.expect('LPAREN')
            self.expression()
            self.expect('RPAREN')
        else:
            print("factor: syntax error")
            

    #--------------------------------------------------
    def term(self):
        """
        term = factor {("*"|"/") factor}
        .
        """
        retour = []
        self.factor()
        while self.show_next().type in Parser.TERM_OP:
            retour.append(Node(self.accept_it()))
            self.factor()

    #--------------------------------------------------
    def expression(self):
        """
        expression = ["+"|"-"] term {("+"|"-") term}
        .
        """
        retour = []
        if self.show_next().type in Parser.ADD_OP:
            retour.append(Node(self.expect(Parser.ADD_OP)))
        self.term()
        while self.show_next().type in Parser.ADD_OP:
            self.term()

    #--------------------------------------------------
    def condition(self):
        """
        condition =
            "odd" expression
            | expression ("="|"#"|"<"|"<="|">"|">=") expression
            | in range () 
            | in ... 
        .
        """
        retour = []
        self.expression()
        if (self.show_next().type in Parser.REL_OP):
            retour.append(Node(self.expect(Parser.REL_OP)))
            retour.append(self.expression())
        elif self.show_next().type == 'IN' : 
            pass 
            #TODO : in smthg 
        elif self.show_next().type == 'IS' : 
            pass 
            #TODO : is smthg 
        else :
            print("condition: found invalid operator line" + str(self.show_next().ligne))
            sys.exit(1) 
        
        n = Node()
        for e in retour:
            n.addNode(e)
        return n


    #--------------------------------------------------
    def statement(self):
        """
        statement =
            [IDENTIFIER "=" expression
            | "if" condition "then" statement
            | "while" condition "do" statement
            ]
        .
        """
        retour = []
        if self.show_next().type == 'IDENTIFIER':
            retour.append(Node(self.expect('IDENTIFIER')))
            retour.append(Node(self.expect('EQ')))
            retour.append(self.expression())


        elif self.show_next().type == 'IF':
            retour.append(self.condition())
            retour.append(Node(self.expect('COLON')))
            # tant qu'on est au meme niveau d'indent
            retour.append(self.statement())
            #ajouter else elseif

        elif self.show_next().type == 'WHILE':
            retour.append(self.condition())
            retour.append(Node(self.expect('COLON')))
            retour.append(self.statement())

        n = Node()
        for e in retour:
            n.addNode(e)
        return n
        


    #--------------------------------------------------
    def parse(self):
        
        AST = Node()
        while len(self.tokens) > 0 : 
            AST.addNode(self.statement())
        return AST

