import unittest

def bubble_sort(arr):
    #implement sort an array of integer in ascending order
    #parameter arr: List of integer
    #return Sorted List
    n = len(arr)
    for i in range(n-1): #Loop of each element
        for j in range(n-1-i): #Compare adjacent element
            if arr[j] > arr[j+1]: #swap the left element
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def Optimized_bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False # there is flag swap is occur
        for j in range(n-1-i):
            if arr[j] > arr[j+i]:
                arr[j],arr[j+1] = arr[j+1], arr[j]
                swapped = True #set flag if swap happen
        if not swapped: 
            break #Stop
    return arr

class Test_bubble_sort(unittest.TestCase):

    #A randomly generated array of integers.
    def test_random(self):
        self.assertEqual(bubble_sort([21,12,31,15,16,50]),[12,15,16,21,31,50])
    #An array that is already sorted in ascending order, 
    #to test the best-case scenario.
    def test_best_case(self):
        self.assertEqual(bubble_sort([12,15,16,21,31,50]),[12,15,16,21,31,50])
        self.assertEqual(Optimized_bubble_sort([12,15,16,21,31,50]),[12,15,16,21,31,50])
    
    #An array sorted in descending order, to assess the worst-case scenario.
    def test_worst_case(self):
        self.assertEqual(bubble_sort([9,8,7,6,3,1]),[1,3,6,7,8,9])
    #An array where all elements are identical, to examine the algorithm's behavior with uniform input.
    def test_identical_element(self):
        self.assertEqual(bubble_sort([5,5,5,5,5,5,5]),[5,5,5,5,5,5,5])
    #Edge cases, such as an empty array and a single-element array.
    def test_empty(self):
        self.assertEqual(bubble_sort([]),[])

    def test_single(self):
        self.assertEqual(bubble_sort([1]),[1])

if __name__ == "__main__":
    unittest.main()

#Optimization
"""
Time Complexity: Worst Case: O(n*n), Best Case O(n)
Space Complexity: O(1)
Stable: Yes, it doesn't need to swap element that is equal
"""