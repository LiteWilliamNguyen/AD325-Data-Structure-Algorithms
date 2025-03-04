class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insert(self, root, key):
        if not root:
            return AVLNode(key)
        # method recursive call itself on the left subtree
        elif key < root.key:
            root.left = self.insert(root.left, key)
        # method recursive call itself on the right subtree
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root
        
        # Balance the tree
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)

        # Left-Left case
        if balance > 1 and key < root.left.key:
            return self.rightRotate(root)

        # Left-Right case
        if balance > 1 and key > root.left.key:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Right-Right case
        if balance < -1 and key > root.right.key:
            return self.leftRotate(root)

        # Right-Left case
        if balance < -1 and key < root.right.key:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root
    
    #This method is used to get the height of a node, which is necessary for calculating the balance factor
    def getHeight(self, node):
        return node.height if node else 0
    #Returns the balance factor of the given node
    def getBalance(self, node):
        return self.getHeight(node.left) - self.getHeight(node.right) if node else 0
    #Returns the node with the minimum value in the subtree rooted at node
    def getMinValueNode(self, node):
        if node.left is None:
            return node
        return self.getMinValueNode(node.left)


    def delete(self, root, key):
        if not root:
            return root
        # method recursive call itself on the left subtree
        elif key < root.key:
            root.left = self.delete(root.left, key)
        # method recursive call itself on the right subtree
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # If the node has no left child, it returns the right child
            if root.left is None:
                temp = root.right
                root = None
                return temp
            # If the node has no right child, it returns the left child
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            #If the node has both left and right children, 
            #it finds the node with the minimum value in the right subtree
            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            #recursively deletes the node with the minimum value from the right subtree
            root.right = self.delete(root.right, temp.key)

        if root is None:
            return root
        
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)
        
        #Rotation
        ##Left - Left Case
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)
        #Left - Right Case
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        #Right - Right Case
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)

        #Right - Left Case
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        
        #balance
        return root
    #Searches for a key in the tree and returns a boolean indicating whether the key exists.
    def search(self, root, key):
        if not root:
            return False
        if key == root.key:
            return True
        elif key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)
    
    #Returns the in-order traversal of the tree
    def inOrderTraversal(self, root):
        return self.inOrderTraversal(root.left) + [root.key] + self.inOrderTraversal(root.right) if root else []
    
    #Testing other traversals
    def preOrderTraversal(self, root):
        return [root.key] + self.preOrderTraversal(root.left) + self.preOrderTraversal(root.right)
    
    def postOrderTraversal(self, root):
        return self.postOrderTraversal(root.left) + self.postOrderTraversal(root.right) + [root.key]
    
    #Rotation
    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y
    
    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y