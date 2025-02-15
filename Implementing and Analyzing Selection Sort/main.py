import unittest

def selection_sort(arr):
    """
    implementation sorts an array (or list) of integers in ascending order

    """
    #Finds the minimum element in the unsorted part. 
    #Array Loop x2 so Time Complexity: O(n*n), Space Complexity:O(1) in set array
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        #Swaps it with the first unsorted element.
        arr[i], arr[min_index] = arr[min_index], arr[i]
         
    return arr
    
    #Repeats until the entire list is sorted.

class TestSelectionSort(unittest.TestCase):
    #A randomly generated array of integers.
    def test_random_list(self):
        self.assertEqual(selection_sort([64, 25, 12, 22, 11]), [11, 12, 22, 25, 64])
    #An array already sorted in ascending order.
    def test_already_sorted(self):
        self.assertEqual(selection_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
    #An array sorted in descending order.
    def test_reverse_sorted(self):
        self.assertEqual(selection_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
    #An array with all elements being the same.
    def test_all_same_elements(self):
        self.assertEqual(selection_sort([7, 7, 7, 7, 7]), [7, 7, 7, 7, 7])
    #An empty array
    def test_empty_list(self):
        self.assertEqual(selection_sort([]), [])
    #An array with one element (edge cases).    
    def test_single_element(self):
        self.assertEqual(selection_sort([42]), [42])

# Run the tests
if __name__ == '__main__':
    unittest.main()