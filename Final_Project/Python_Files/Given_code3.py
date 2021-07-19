from typing import Counter


class BST:
    class Node:
        def __init__(self, data):
            self.data = data
            self.right = None
            self.left = None
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root == None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  

    def _insert(self, data, node):
        if data == node.data:
            return
        if data < node.data:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                node.left = BST.Node(data)
            else:
                self._insert(data, node.left)
        else:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(data, node.right)

    def get_lowest_value(self, node):
        current = node
        if current.left == None:
            return current
        elif current.left != None:
            self.get_lowest_value(current.left)

    def delete_node(self, root, data):
    
        # Base Case
        if root is None:
            return root

        # Checks if the data you want to delete
        # is on the left side of the root
        if data < root.data:
            root.left = self.delete_node(root.left, data)
    
        # Checks if the data you want to delete
        # is on the right side of the root
        elif data > root.data:
            root.right = self.delete_Node(root.right, data)


        # this is where you will start writing code to delete a node
        # with 1 or 2 child nodes
        pass

    def __iter__(self):
        """
        Perform a forward traversal (in order traversal) starting from 
	    the root of the BST.  This is called a generator function.
        This function is called when a loop	is performed:
        """
        yield from self._traverse_forward(self.root) 

    def _traverse_forward(self, node):
        """
        Does a forward traversal (in-order traversal) through the 
        BST.  If the node that we are given (which is the current
        sub-tree) exists, then we will keep traversing on the left
        side (thus getting the smaller numbers first), then we will 
        provide the data in the current node, and finally we will 
        traverse on the right side (thus getting the larger numbers last).


        This function is intended to be called the first time by 
        the __iter__ function.
        """
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)

tree = BST()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(1)
tree.insert(10)
tree.insert(9)
tree.insert(4)
tree.delete_node(tree.root, 7)
tree.delete_node(tree.root, 3)
for node in tree:
    print(node) # 1, 4, 5, 9, 10