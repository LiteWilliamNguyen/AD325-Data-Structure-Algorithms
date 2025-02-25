from collections import deque
from tree_node import TreeNode

class BinaryTree:
    def __init__(self, root=None):
        #Initialize the binary tree with an optional root node.
        self.root = root

    def preorder_traversal(self):
        #Preorder traversal (Root → Left → Right).
        result = []
        def dfs(node):
            if node:
                result.append(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(self.root)
        return result

    def inorder_traversal(self):
        #Inorder traversal (Left → Root → Right).
        result = []
        def dfs(node):
            if node:
                dfs(node.left)
                result.append(node.val)
                dfs(node.right)
        dfs(self.root)
        return result

    def postorder_traversal(self):
        #Postorder traversal (Left → Right → Root).
        result = []
        def dfs(node):
            if node:
                dfs(node.left)
                dfs(node.right)
                result.append(node.val)
        dfs(self.root)
        return result

    def level_order_traversal(self):
        #Level Order (using a queue for iterative approach)
        if not self.root:
            return []
        result, queue = [], deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result