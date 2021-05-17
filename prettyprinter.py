from Visitor import visitor
import Node

class Prettyprinter(visitor) :  

    REL_OP = ['EQ', 'DIFF', 'INF', 'SUP']

    def __init__(self, verbosity) : 
        visitor.__init__(self,verbosity)
        self.prettyprinter = ""
        self.prettyprinter += "# Prettyprinter \n"
    
    def visitStatement(self, StatementNode) :
        if self.verbosity : 
            print("visitStatement")
        for i in StatementNode.children : 
            i.accept(self)
        self.prettyprinter += "\n"

    def visitNode(self, Node) : 
        if self.verbosity : 
            print("visit Node :" + Node.token.valeur)
        if (Node.token.type in self.REL_OP and self.prettyprinter[-1] in ('=', '<','>', '!')) or (self.prettyprinter[-1] == '\n'): 
            # no space for condition operator and first item of line
            self.prettyprinter += Node.token.valeur
        else : 
            self.prettyprinter += " " + Node.token.valeur
        if Node.token.type == 'TAB' : 
            self.prettyprinter +="\n    "
        

    def compile(self, file) : 
        PPfile = open(file, 'w')
        PPfile.write(self.prettyprinter)
        PPfile.close()