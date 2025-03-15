class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.rank = 0  # The rank helps maintain the leftist property

class LeftistTree:
    def __init__(self):
        self.root = None

    def merge(self, t1, t2):
        if not t1:
            return t2
        if not t2:
            return t1
        
        # Ensure t1 has the smaller root
        if t1.value > t2.value:
            t1, t2 = t2, t1
        
        # Merge the right subtree with t2
        t1.right = self.merge(t1.right, t2)
        
        # Ensure the leftist property
        if not t1.left or t1.left.rank < t1.right.rank:
            t1.left, t1.right = t1.right, t1.left
        
        # Update rank
        if not t1.right:
            t1.rank = 0
        else:
            t1.rank = t1.right.rank + 1
        
        return t1

    def insert(self, value):
        new_node = Node(value)
        self.root = self.merge(self.root, new_node)

    def delete_min(self):
        if not self.root:
            return None
        # Merge left and right children of the root to maintain the tree
        self.root = self.merge(self.root.left, self.root.right)

import unittest
class TestLeftistTree(unittest.TestCase):
    def test_insertion(self):
        tree = LeftistTree()
        tree.insert(15)
        tree.insert(10)
        tree.insert(20)
        tree.insert(8)
        tree.insert(12)
        tree.insert(17)
        tree.insert(25)
        
        # After inserting values, the root should be the minimum value (8 in this case)
        self.assertEqual(tree.root.value, 8)

    def test_deletion(self):
        tree = LeftistTree()
        values = [15, 10, 20, 8, 12, 17, 25]
        for value in values:
            tree.insert(value)

        # Delete the minimum value (root) and check the new root
        tree.delete_min()
        self.assertEqual(tree.root.value, 10)  # After deletion, 10 should be the new root

        # Delete the new minimum value and check the new root
        tree.delete_min()
        self.assertEqual(tree.root.value, 12)  # After another deletion, 12 should be the new root

        # Delete the new minimum value and check the new root
        tree.delete_min()
        self.assertEqual(tree.root.value, 15)  # After another deletion, 15 should be the new root 

    def test_merging(self):
        tree1 = LeftistTree()
        tree2 = LeftistTree()
        values1 = [15, 10, 20]
        values2 = [8, 12, 17, 25]
        
        for value in values1:
            tree1.insert(value)
        for value in values2:
            tree2.insert(value)

        merged_tree = LeftistTree()
        merged_tree.root = merged_tree.merge(tree1.root, tree2.root)
        
        # After merging, the root of the merged tree should be the minimum value (8)
        self.assertEqual(merged_tree.root.value, 8)

if __name__ == '__main__':
    unittest.main()

"""
Function       Complexity              Comparison
1) Get Min:       O(1)      [same as both Binary and Binomial]
2) Delete Min:    O(Log n)  [same as both Binary and Binomial]
3) Insert:        O(Log n)  [O(Log n) in Binary and O(1) in 
                            Binomial and O(Log n) for worst case]                                                                  
4) Merge:         O(Log n)  [O(Log n) in Binomial]
Got this from geeksforgeeks
"""