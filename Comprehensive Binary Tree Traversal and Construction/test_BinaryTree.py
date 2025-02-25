import unittest
from tree_node import TreeNode
from binary_tree import BinaryTree
from tree_builder import BinaryTreeBuilder

class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        """Set up a sample binary tree for testing."""
        self.root = TreeNode(1)
        self.root.left = TreeNode(2)
        self.root.right = TreeNode(3)
        self.root.left.left = TreeNode(4)
        self.root.left.right = TreeNode(5)
        self.root.right.left = TreeNode(6)
        self.root.right.right = TreeNode(7)

        self.tree = BinaryTree(self.root)

    def test_preorder_traversal(self):
        self.assertEqual(self.tree.preorder_traversal(), [1, 2, 4, 5, 3, 6, 7])

    def test_inorder_traversal(self):
        self.assertEqual(self.tree.inorder_traversal(), [4, 2, 5, 1, 6, 3, 7])

    def test_postorder_traversal(self):
        self.assertEqual(self.tree.postorder_traversal(), [4, 5, 2, 6, 7, 3, 1])

    def test_level_order_traversal(self):
        self.assertEqual(self.tree.level_order_traversal(), [1, 2, 3, 4, 5, 6, 7])


class TestBinaryTreeConstruction(unittest.TestCase):
    def setUp(self):
        """Set up the traversal orders for testing."""
        self.preorder = [1, 2, 4, 5, 3, 6, 7]
        self.inorder = [4, 2, 5, 1, 6, 3, 7]
        self.postorder = [4, 5, 2, 6, 7, 3, 1]

        self.builder = BinaryTreeBuilder()

    def test_build_from_pre_in(self):
        root = self.builder.build_from_pre_in(self.preorder, self.inorder)
        tree = BinaryTree(root)
        self.assertEqual(tree.preorder_traversal(), self.preorder)

    def test_build_from_post_in(self):
        root = self.builder.build_from_post_in(self.postorder, self.inorder)
        tree = BinaryTree(root)
        self.assertEqual(tree.inorder_traversal(), self.inorder)


if __name__ == "__main__":
    unittest.main()

