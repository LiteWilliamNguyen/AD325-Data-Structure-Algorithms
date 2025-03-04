import unittest
from main import AVLTree, AVLNode

class TestAVLTree(unittest.TestCase):
    def setUp(self):
        self.avl = AVLTree()
        self.root = None

    def test_insert_without_rotation(self):
        self.root = self.avl.insert(self.root, 20)
        self.root = self.avl.insert(self.root, 10)
        self.root = self.avl.insert(self.root, 30)
        self.assertEqual(self.avl.inOrderTraversal(self.root), [10, 20, 30])

    def test_insert_with_left_rotation(self):
        self.root = self.avl.insert(self.root, 10)
        self.root = self.avl.insert(self.root, 20)
        self.root = self.avl.insert(self.root, 30)  #left rotation
        self.assertEqual(self.avl.inOrderTraversal(self.root), [10, 20, 30])

    def test_insert_with_right_rotation(self):
        self.root = self.avl.insert(self.root, 30)
        self.root = self.avl.insert(self.root, 20)
        self.root = self.avl.insert(self.root, 10)  #right rotation
        self.assertEqual(self.avl.inOrderTraversal(self.root), [10, 20, 30])

    def test_delete_node(self):
        self.root = self.avl.insert(self.root, 40)
        self.root = self.avl.insert(self.root, 20)
        self.root = self.avl.insert(self.root, 10)
        self.root = self.avl.insert(self.root, 30)
        self.root = self.avl.insert(self.root, 50)
        self.root = self.avl.insert(self.root, 60)

        self.root = self.avl.delete(self.root, 50)  # Deletion causing imbalance
        self.assertEqual(self.avl.inOrderTraversal(self.root), [10, 20, 30, 40, 60])
    
    def test_delete_non_existing_node(self):
        self.root = self.avl.insert(self.root, 40)
        self.root = self.avl.delete(self.root, 20)
        self.assertEqual(self.avl.inOrderTraversal(self.root), [40])
        
    def test_search(self):
        self.root = self.avl.insert(self.root, 15)
        self.root = self.avl.insert(self.root, 25)
        self.assertTrue(self.avl.search(self.root, 15))
        self.assertFalse(self.avl.search(self.root, 100))

    def test_insert_duplicate(self):
        self.root = self.avl.insert(self.root, 15)
        self.root = self.avl.insert(self.root, 15)
        self.assertEqual(self.avl.inOrderTraversal(self.root), [15])


if __name__ == '__main__':
    unittest.main()