import sys
import lexer
from lexer import Token
from Node import Node

# TODO : expect Indent for if while statements 
# TODO : add indent to AST representation 
# TODO : In range and Is smthg 
# TODO : Display AST 
class Parser:

    ADD_OP = ['ADD', 'SUB']
    REL_OP = ['EQ', 'NEQ', 'INF', 'INFEQ', 'SUP', 'SUPEQ']
    TERM_OP = ['MULT', 'DIV']
    FACTOR_TYPE = ['INT', 'FLOAT']


    def __init__(self, tokens):  
        self.tokens = tokens[:]
        self.errors = 0

    def show_next(self, n=1):
        """
        Permet d'acceder à un token dans la liste des tokens à consommer
        
        Args:
            n (int, optional): numero du token recherché Defaults to 1.

        Returns:
            token : le token demandé
        """
        try:
            return self.tokens[n - 1]
        except IndexError:
            #print('no more tokens left!')
            return 
            

    def expect(self, kind):
        """
        Cherche la présence d'un token conformément à la syntaxe python 
        
        Args:
            kind : type de token attendu 

        Returns:
            retourne et consomme le token si conforme
            syntaxe error sinon 
        """
        actualToken = self.show_next()
        actualKind = actualToken.type
        actualPosition = (actualToken.ligne, actualToken.position_debut,actualToken.position_fin)
        if isinstance(kind, str) : 
            if actualKind == kind:
                return self.accept_it()
            else:
                print("syntax error")
                print('Error at {}: expected {}, got {} instead'.format(str(actualPosition), kind, actualKind))
                sys.exit(1)
        else : 
            if actualKind in kind : 
                 return self.accept_it()
            else:
                print("syntax error")
                print('Error at {}: expected {}, got {} instead'.format(str(actualPosition), kind, actualKind))
                sys.exit(1)

    def accept_it(self) :
        """
        Consomme un token et le retourne 

        Returns:
            token: token consommé 
        """
        return self.tokens.pop(0)

    
#  définitions des fonctions de parsing permettant la création de l'AST.   
        
    def factor(self):
        """
        Permet de parser les facteurs
        factor = IDENTIFIER | NUMBER | "(" expression ")"
        
        Returns:
            n : Noeud de l'AST représentant le facteur 
        """
        #print("factor")
        retour = []

        if self.show_next().type == 'IDENTIFIER' : 
            retour.append(Node(self.accept_it()))
            return 
            
        if self.show_next().type in Parser.FACTOR_TYPE :
            retour.append(Node(self.accept_it()))
            return 
        
        elif self.show_next().type == 'LPAREN':
            retour.append(Node(self.accept_it()))
            retour.append(self.expression())
            retour.append(Node(self.expect('RPAREN')))
        else:
            print("syntax error")
            actualPosition = (self.show_next().ligne, self.show_next().position_debut,self.show_next().position_fin)
            print('Error at {}: expected {}, got {} instead'.format(str(actualPosition),"Identifier | number | (expression)", self.show_next().type))
            sys.exit(1)
        
        n = Node(Token("factor","factor"))
        for e in retour:
            n.addNode(e)
        return n

    #--------------------------------------------------
    def term(self):
        """
        Permet de parser les termes (combinaison de facteurs)
        term = factor {("*"|"/") factor}
        
        Returns:
            n : Noeud de l'AST représentant le terme
        """
        #print("term") 
        retour = []
        
        retour.append(self.factor())
        if self.show_next() is not None :
            while self.show_next().type in Parser.TERM_OP:
                retour.append(Node(self.accept_it()))
                retour.append(self.factor())
        
        n = Node(Token("term","term"))
        for e in retour:
            if e is not None : 
                n.addNode(e)

        return n

    #--------------------------------------------------
    def expression(self):
        """
        Permet de parser les expressions (combinaison linéaire de termes)
        expression = ["+"|"-"] term {("+"|"-") term}
        
        Returns:
            n : Noeud de l'AST représentant le terme
        """
        #print("expression")
        retour = []
        if self.show_next().type in Parser.ADD_OP:
            retour.append(Node(self.accept_it()))
        retour.append(self.term())
        if self.show_next() is not None :
            while self.show_next().type in Parser.ADD_OP:
                retour.append(Node(self.accept_it()))
                retour.append(self.term())

        n = Node(Token("expression","expression"))
        for e in retour:
            n.addNode(e)
        return n

    #--------------------------------------------------
    def condition(self):
        """
        Permet de parser une condition (relation entre 2 expression)

        condition =
            "odd" expression
            | expression ("="|"#"|"<"|"<="|">"|">=") expression
            | in range () 
            | in ... 
        
        Returns:
            n : Noeud de l'AST représentant le terme
        """
        #print("condition")
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
        
        n = Node(Token("condition","condition"))
        for e in retour:
            n.addNode(e)
        return n


    #--------------------------------------------------
    def statement(self):
        """
        Permet de parser les statements 
        
        statement =
            [IDENTIFIER "=" expression
            | "if" condition "then" statement
            | "while" condition "do" statement
            ]

        Returns:
            n : Noeud de l'AST représentant le terme
        """
        #print("statement")
        retour = []
        
        if self.show_next().type == 'IDENTIFIER':
            retour.append(Node(self.accept_it()))
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

        
        n = Node(Token("statement","statement"))
        for e in retour:
            n.addNode(e)
        return n
        


    #--------------------------------------------------
    def parse(self):
        """
        Permet le parsing du programme en entier (pas d'entrée vers main)
        
        Returns:
            n : Noeud de l'AST représentant le programme (root)
        """
        AST = Node(Token("root", "root"))
        while len(self.tokens) > 0 : 
            AST.addNode(self.statement())
            
        print("success : program is compiled")
        return AST

