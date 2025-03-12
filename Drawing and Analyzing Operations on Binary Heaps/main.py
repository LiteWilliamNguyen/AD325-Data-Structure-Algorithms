import heapq

class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    """Insertion into a Binary Heap"""
    def insert(self, value):
        heapq.heappush(self.heap, value)
        print(f"Inserted {value}: {self.heap}")
        self.size += 1

    """Deletion from a Binary Heap"""
    def delete(self):
        if self.size == 0:
            print("Heap is empty")
            return None
        else:
            removed = heapq.heappop(self.heap)
            print(f"Deleted {removed}: {self.heap}")
            self.size -= 1
            return removed
        
    def display(self):
        """Display the heap as a list"""
        print("Heap:", self.heap)
"""Initialize MinHeap"""
heap = MinHeap()

"""Insert elements into the heap: 15, 10, 20, 8, 12, 17, 25"""
elements = [15, 10, 20, 8, 12, 17, 25]
for element in elements:
    heap.insert(element)

"""Delete the root node (the minimum or maximum element, 
depending on the heap type) three times."""
for _ in range(3):
    heap.delete()


import unittest
from heapq import heappop

class TestMinHeap(unittest.TestCase):
    def setUp(self):
        self.heap = MinHeap()

    def test_single_insertion(self):
        """Test inserting a single element into an empty heap."""
        self.heap.insert(10)
        self.assertEqual(self.heap.heap, [10])

    def test_multiple_insertions(self):
        """Test inserting multiple elements and maintaining heap property."""
        elements = [15, 10, 20, 8, 12, 17, 25]
        for elem in elements:
            self.heap.insert(elem)
        
        expected_heap = sorted(elements)  # Heapq maintains min-heap order
        actual_heap = [heappop(self.heap.heap) for _ in range(len(elements))]
        self.assertEqual(actual_heap, expected_heap)

    def test_insert_duplicate_values(self):
        """Test inserting duplicate values and ensuring correct heap structure."""
        elements = [10, 5, 10, 5, 15, 5]
        for elem in elements:
            self.heap.insert(elem)

        expected_heap = sorted(elements)
        actual_heap = [heappop(self.heap.heap) for _ in range(len(elements))]
        self.assertEqual(actual_heap, expected_heap)

    def test_insert_negative_numbers(self):
        """Test inserting negative numbers into the heap."""
        elements = [-5, -15, -10, 0, 5, -20]
        for elem in elements:
            self.heap.insert(elem)

        expected_heap = sorted(elements)
        actual_heap = [heappop(self.heap.heap) for _ in range(len(elements))]
        self.assertEqual(actual_heap, expected_heap)

if __name__ == "__main__":
    unittest.main()

"""
Structure of a Binary Heap(Min Heap):
maintain all level are fully filled except last level may be partially filled
Structure of BInary Search Tree:
follows a specific order where left child is less than parent and right child is greater than parent
Structure of AVL Tree:
ensuring height balance of the tree between subtrees is at most 1

Time Complexity:
Binary Heap:
Insertion: O(log n)
Deletion: O(log n)
Search: O(n)
Binary Search Tree:
Worst case: O(n)
Insertion: O(log n)
Deletion: O(log n)
Search: O(log n)
AVL Tree:
Insertion: O(log n)
Deletion: O(log n)
Search: O(log n)

"""