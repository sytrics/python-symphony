import Node

class Visitor :  

    REL_OP = ['EQ', 'DIFF', 'INF', 'SUP']

    def __init__(self) : 
        self.prettyprinter = ""
        self.prettyprinter += "# Prettyprinter \n"
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
        if (Node.token.type in self.REL_OP and self.prettyprinter[-1] in ('=', '<','>', '!')) or (self.prettyprinter[-1] == '\n'): 
            # no space for condition operator and first item of line
            self.prettyprinter += Node.token.valeur
        else : 
            self.prettyprinter += " " + Node.token.valeur
        if Node.token.type == 'TAB' : 
            self.prettyprinter +="\n    "
        

    def prettyprint(self) : 
        PPfile = open("pretty-print-test.py", 'w')
        PPfile.write(self.prettyprinter)
        PPfile.close()