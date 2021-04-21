import Node

class Visitor :  

    def __init__(self) : 
        self.prettyprinter = ""

    def visitRoot(self, RootNode) :
        print("visitRoot " + RootNode.token.valeur)
        for i in RootNode.children : 
            i.accept(self)    
    def visitStatement(self, StatementNode) :
        print("visitStatement")
        for i in StatementNode.children : 
            i.accept(self)
        self.prettyprinter += "\n"

    def visitExpression(self, ExpressionNode) :
        print("visitExpression")
        for i in ExpressionNode.children : 
            i.accept(self)

    def visitCondition(self, ConditionNode) :
        print("visitCondition") 
        for i in ConditionNode.children : 
            i.accept(self)
    
    def visitFactor(self, FactorNode) :
        print("visitFactor" + FactorNode.token.valeur)
        for i in FactorNode.children : 
            i.accept(self)

    def visitTerm(self, TermNode) :
        print("visitTerm " + TermNode.token.valeur) 
        for i in TermNode.children : 
            i.accept(self)

    def visitNode(self, Node) : 
        print("visit Node :" + Node.token.valeur)
        self.prettyprinter += Node.token.valeur + " "

    def prettyprint(self) : 
        PPfile = open("pretty-print-test.py", 'w')
        PPfile.write(self.prettyprinter)
        PPfile.close()