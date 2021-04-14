import sys
import lexer
from Node import Node

# TODO : expect Indent for if while statements 
# TODO : In range and Is smthg 
# TODO : Display AST 
class Parser:

    ADD_OP = ['ADD', 'SUB']
    REL_OP = ['EQ', 'NEQ', 'INF', 'INFEQ', 'SUP', 'SUPEQ']
    TERM_OP = ['MULT', 'DIV']
    FACTOR_TYPE = ['INT', 'FLOAT']


    def __init__(self, tokens):  
        self.tokens = tokens
        self.errors = 0
        self.indent = []
        
        

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
        if isinstance(kind, str) : 
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

    
   

    
        
    def factor(self):
        """
        factor = IDENTIFIER | NUMBER | "(" expression ")"
        .
        """
        retour = []
        if self.show_next().type in Parser.FACTOR_TYPE :
            retour.append(Node(self.accept_it()))
            pass
       
        elif self.show_next().type == 'LPAREN':
            retour.append(Node(self.accept_it()))
            retour.append(self.expression())
            retour.append(Node(self.expect('RPAREN')))
        else:
            print("factor: syntax error")
            

    #--------------------------------------------------
    def term(self):
        """
        term = factor {("*"|"/") factor}
        
        """
        retour = []
        retour.append(self.factor())
        while self.show_next().type in Parser.TERM_OP:
            retour.append(Node(self.accept_it()))
            retour.append(self.factor())
        
        n = Node()
        for e in retour:
            n.addNode(e)
        return n

    #--------------------------------------------------
    def expression(self):
        """
        expression = ["+"|"-"] term {("+"|"-") term}
        
        """
        retour = []
        if self.show_next().type in Parser.ADD_OP:
            retour.append(Node(self.accept_it()))
        retour.append(self.term())
        while self.show_next().type in Parser.ADD_OP:
            retour.append(Node(self.accept_it()))
            retour.append(self.term())

        n = Node()
        for e in retour:
            n.addNode(e)
        return n

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
            retour.append(Node(self.accept_it()))
            retour.append(self.expression())
        elif self.show_next().type == 'IN' : 
            pass 
            #TODO : in smthg 
        elif self.show_next().type == 'IS' : 
            pass 
            #TODO : is smthg 
        else :
            print("condition: found invalid operator ")
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
        """
        retour = []
        if self.show_next().type == 'IDENTIFIER':
            retour.append(Node(self.accept_it))
            retour.append(Node(self.expect('EQ')))
            retour.append(self.expression())


        elif self.show_next().type == 'IF':
            retour.append(self.condition())
            retour.append(Node(self.expect('COLON')))
        
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
        print("success : program is compiled")
        return AST

