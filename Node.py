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

        print(_prefix, "`- " if _last else "|- ", self.token.type, sep="")
        _prefix += "   " if _last else "|  "
        
        N = len(self.children)
        for i, child in enumerate(self.children):
            _last = i == (N - 1)
            if child is not None:
                child.printTree(_prefix, _last)