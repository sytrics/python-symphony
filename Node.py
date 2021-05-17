from lexer import Token

class Node:
    def __init__(self, token=None):
        self.token = token
        self.children = []  # a list of my children
    
        
    def addNode(self, node):
        """
        add a children to self.children
        """
        self.children.append(node)
        
    def printTree(self, _prefix="", _last=True):
        bitstream = self.token.type 
        if self.token.type in ('IDENTIFIER','INT','FLOAT') : 
            bitstream += " => " + self.token.valeur
        print(_prefix, "`- " if _last else "|- ",bitstream, sep="")
        _prefix += "   " if _last else "|  "
        
        N = len(self.children)
        for i, child in enumerate(self.children):
            _last = i == (N - 1)
            if child is not None:
                child.printTree(_prefix, _last)

    def accept(self, visitor) :
        visitor.visitNode(self)

class RootNode(Node) : 
    def __init__(self) : 
        super().__init__(Token("root", "root"))
    
    def accept(self, visitor) :
        visitor.visitRoot(self)
class StatementNode(Node) : 
    def __init__(self) : 
        super().__init__(Token("statement", "statement"))
    
    def accept(self, visitor) :
        visitor.visitStatement(self)

class ExpressionNode(Node) :
    def __init__(self) : 
        super().__init__(Token("expression", "expression"))

    def accept(self, visitor) :
        visitor.visitExpression(self)
class ConditionNode(Node) : 
    def __init__(self) : 
        super().__init__(Token("condition", "condition"))

    def accept(self, visitor) :
        visitor.visitCondition(self)

class FactorNode(Node) :
    def __init__(self) : 
        super().__init__(Token("factor", "factor"))
    
    def accept(self, visitor) :
        visitor.visitFactor(self)

class TermNode(Node) :
    def __init__(self) : 
        super().__init__(Token("term", "term"))

    def accept(self, visitor) :
        visitor.visitTerm(self)

