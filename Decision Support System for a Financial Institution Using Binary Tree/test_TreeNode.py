import unittest
from main import *

class TreeNode:
    def __init__(self,question):
        self.question = question
        self.left = None
        self.right = None

class TestMaxDepth(unittest.TestCase):

    #calculate max depth of the binary tree
    def test_max_depth(self):
        root = TreeNode(1)
        root.left= TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(max_depth(root),2)
    #test if both side are equal
    def test_equal_side(self):
        root = TreeNode(1)
        root.left= TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        self.assertEqual(max_depth(root), 3)

    #test if one side is deeper
    def test_one_side_deeper(self):
        root = TreeNode(1)
        root.left= TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        self.assertEqual(max_depth(root),3)

    #test if different path have different depth
    def test_dif_path_dif_depth(self):
        root = TreeNode(1)
        root.left= TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        root.left.left.right = TreeNode(8)
        root.right.right.left = TreeNode(9)
        self.assertEqual(max_depth(root),4)
    #test empty
    def test_empty(self):
        self.assertEqual(max_depth(None),0)
    #test 1 node
    def test_root_node(self):
        root = TreeNode(1)
        self.assertEqual(max_depth(root),1)
    
if __name__ == "__main__":
    unittest.main()