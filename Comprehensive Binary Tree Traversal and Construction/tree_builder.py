from tree_node import TreeNode

class BinaryTreeBuilder:
    def __init__(self):
        pass

    def build_from_pre_in(self, preorder, inorder):
        #Constructs a binary tree from preorder and inorder traversal lists.
        if not preorder or not inorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)
        root_index = inorder.index(root_val)
        # extract the index of root element to the left subtree in preorder traversal
        root.left = self.build_from_pre_in(preorder[1:root_index+1], inorder[:root_index])
        # extract the index of root element to the right subtree in preorder traversal
        root.right = self.build_from_pre_in(preorder[root_index+1:], inorder[root_index+1:])

        return root

    def build_from_post_in(self, postorder, inorder):
        #Constructs a binary tree from postorder and inorder traversal lists.
        if not postorder or not inorder:
            return None

        root_val = postorder[-1]
        root = TreeNode(root_val)
        root_index = inorder.index(root_val)
        # extract the index of root element to the left subtree in postorder traversal
        root.left = self.build_from_post_in(postorder[:root_index], inorder[:root_index])
        # extract the index of root element to the right subtree in postorder traversal
        root.right = self.build_from_post_in(postorder[root_index:-1], inorder[root_index+1:])

        return root
