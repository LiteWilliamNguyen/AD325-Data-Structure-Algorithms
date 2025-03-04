
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    
class BinarySearchTree:
    def __init__(self):
        
        self.root = None

    """Insert a new node"""
    def insert(self,value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self.insert_rec(self.root, value)

    def insert_rec(self,node,value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self.insert_rec(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else: 
                self.insert_rec(node.right, value)

        elif value == node.value:
            # Do nothing
            pass
    """Search for value in BST, return true if found, if not then false"""
    def search(self,value):
        return self.search_rec(self.root, value)

    def search_rec(self,node,value):
        if node is None:
            return False
        elif node.value == value:
            return True
        elif value < node.value:
            return self.search_rec(node.left, value)
        else:
            return self.search_rec(node.right, value)

    """Delete a node"""
    def delete(self,value):
        self.delete_rec(self.root, value)

    def delete_rec(self,node,value):
        if node is None:
            return None
        elif value < node.value:
            node.left = self.delete_rec(node.left, value)
        elif value > node.value:
            node.right = self.delete_rec(node.right, value)
        else: 
            #Node with no children
            if node.left is None and node.right is None:
                return None
            #Node has one child: return that child
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                #Node has two children: find the minimum value in the right subtree, replace the node's value with it, 
                #and recursively delete that minimum value from the right subtree
                min_node = self.find_min(node.right)
                node.value = min_node.value 
                node.right = self.delete_rec(node.right, min_node.value)    
        return node
    
    #Finds the node with the minimum value
    def find_min(self,node):
        if node.left is None:
            return node
        else:
            return self.find_min(node.left)
        
    """Inorder traversal"""
    def inorder(self):
        return self.inorder_traversal(self.root, [])
    
    def inorder_traversal_rec(self,node,result):
        """Returns a list of values representing the in-order traversal of the tree"""
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.value)
            self.inorder_traversal(node.right, result)
        return result