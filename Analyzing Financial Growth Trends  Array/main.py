import unittest

def sortedSquare(growthPercentages):
    n = len(growthPercentages)
    left,right = 0 , n-1
    final = n - 1
    result = [0] * n



    while left <= right:
        left_square = growthPercentages[left] ** 2
        right_square = growthPercentages[right] ** 2

        if left_square > right_square:
            result[final] = left_square
            left += 1

        else:
            result[final] = right_square
            right -= 1

        final -= 1

    return result

#Test Case
class TestsortedSquare(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(sortedSquare([-5, -2, 0, 3, 10]),[0, 4, 9, 25, 100])
        self.assertEqual(sortedSquare([-8, -3, 2, 4, 12]),[4, 9, 16, 64, 144])
        self.assertEqual(sortedSquare([-10,-5,-3,1,2]),[1,4,9,25,100])

    def test_edge(self):
        self.assertEqual(sortedSquare([-10,-5,-3]),[9,25,100])#all negative
        self.assertEqual(sortedSquare([0]),[0])#zero
        self.assertEqual(sortedSquare([-5,-5,-5,0,0,4,4]),[0,0,16,16,25,25,25])#multiple of same number




if __name__ == "__main__":
    unittest.main()