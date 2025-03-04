import unittest
from BinarySearchTree import BinarySearchTree, TreeNode

class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_insert(self):
        self.bst.insert(5)
        self.bst.insert(3)
        self.bst.insert(7)
        self.bst.insert(2)
        self.assertEqual(self.bst.inorder(), [2, 3, 5, 7])

    def test_search(self):
        self.bst.insert(5)
        self.bst.insert(3)
        self.bst.insert(7)
        self.bst.insert(2)
        self.assertTrue(self.bst.search(3))
        self.assertFalse(self.bst.search(4))

    def test_deletion_leaf_node(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.bst.delete(5)
        self.assertFalse(self.bst.search(5))

    def test_deletion_node_with_one_child(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(3)
        self.bst.delete(5)
        self.assertFalse(self.bst.search(5))
        self.assertTrue(self.bst.search(3))

    def test_deletion_node_with_two_children(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.bst.delete(10)
        self.assertFalse(self.bst.search(10))
        self.assertTrue(self.bst.search(5))
        self.assertTrue(self.bst.search(15))

    def test_inorder_traversal(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.bst.insert(2)
        self.bst.insert(7)
        self.assertEqual(self.bst.inorder(), [2, 5, 7, 10, 15])

if __name__ == '__main__':
    unittest.main()