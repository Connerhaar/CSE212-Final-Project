class BST:
    class Node:
        def __init__(self, value):
            self.root == value
            self.bigger == None
            self.smaller == None
    def __init__(self):
        self.root == None
    
    def add_node(self, data):
        if self.node == None:
            self.node = BST.Node(data)
        else:
            if data > self.root:
                