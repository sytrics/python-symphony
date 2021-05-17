import Node

class visitor  :  

    REL_OP = ['EQ', 'DIFF', 'INF', 'SUP']

    def __init__(self, verbosity) : 
        self.verbosity = verbosity
        

    def visitRoot(self, RootNode) :
        if self.verbosity : 
            print("visitRoot " + RootNode.token.valeur)
        for i in RootNode.children : 
            i.accept(self)    
    def visitStatement(self, StatementNode) :
        if self.verbosity : 
            print("visitStatement")
        for i in StatementNode.children : 
            i.accept(self)

    def visitExpression(self, ExpressionNode) :
        if self.verbosity : 
            print("visitExpression")
        for i in ExpressionNode.children : 
            i.accept(self)

    def visitCondition(self, ConditionNode) :
        if self.verbosity : 
            print("visitCondition") 
        for i in ConditionNode.children : 
            i.accept(self)
        
    def visitFactor(self, FactorNode) :
        if self.verbosity : 
            print("visitFactor" + FactorNode.token.valeur)
        for i in FactorNode.children : 
            i.accept(self)
        
    def visitTerm(self, TermNode) :
        if self.verbosity : 
            print("visitTerm " + TermNode.token.valeur) 
        for i in TermNode.children : 
            i.accept(self)
        
    def visitNode(self, Node) : 
        if self.verbosity : 
            print("visit Node :" + Node.token.valeur)
        