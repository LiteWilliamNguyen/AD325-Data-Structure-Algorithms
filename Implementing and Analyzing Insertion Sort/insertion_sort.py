#Part 1: Implementation
import unittest
import time
import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

#Test Your Implementation
class TestInsertionSort(unittest.TestCase):
#Create a set of test arrays with varying characteristics: 
#a small array, a large array, a nearly sorted array, and a reversed array.
    def test_small_array(self):
        small_array = [5, 3, 8]
        self.assertEqual(insertion_sort(small_array), [3, 5, 8])

    def test_large_array(self):
        large_array = random.sample(range(1, 10001), 1000)  # Random array of 1000 elements
        start_time = time.time()
        sorted_large_array = insertion_sort(large_array.copy())
        end_time = time.time()
        # Here, we are not asserting the exact time, just printing it
        print("Large Array (Time Taken):", end_time - start_time)
        self.assertTrue(sorted_large_array == sorted(large_array))  # Ensure it is sorted correctly

    def test_nearly_sorted_array(self):
        nearly_sorted_array = [1, 2, 3, 4, 5]
        self.assertEqual(insertion_sort(nearly_sorted_array), [1, 2, 3, 4, 5])

    def test_reversed_array(self):
        reversed_array = [5, 4, 3, 2, 1]
        self.assertEqual(insertion_sort(reversed_array), [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()

"""
Part 2: Analysis
Best-Case Analysis: Time Complexity O(n). The array is already sorted
Worst-Case Analysis: Time Complexity O(n*n). The array is completely reversed
Average-Case Analysis: Time Complexity O(n*n). 
Space Complexity Discussion: O(1) Insertion sort is still within the array
Stability Analysis: nsertion Sort is stable, meaning if there are equal elements, their relative order remains unchanged.

Part 3: Reflection
Insertion Sort is efficient for small arrays because of its simplicity, but becomes inefficient for large arrays.
Bubble Sort, which also has O(n*n)complexity
Practical Applications: Insertion Sort is useful for small datasets, nearly sorted data, and situations where memory usage is critical because it sorts in-place.

"""
