class Node:
    def __init__(self, token=None):
        self.token = token
        self.children = []  # a list of my children
    
    def add(self, token):
        """
        make a node out of a token and add it to self.children
        """
        self.addNode(  Node(token) )
        
    def addNode(self, node):
        """
        add a children to self.children
        """
        self.children.append(node)
        
    def toString(self, node):
        """
        displaying node tree (ast if the node is root)
        """

    def __str__(self) : 
        
        print("node")
        print(len(self.children))
        