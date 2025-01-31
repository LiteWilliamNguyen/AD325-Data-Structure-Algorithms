import unittest
def duplicate_zeros(inventory):
    n = len(inventory)
    i = 0
    #loop
    while i < n:
        if inventory[i] == 0:
            inventory.insert(i,0) #duplicate zero and insert zero
            inventory.pop() #remove the last element in the array to maintain length
            i += 1 #skip to next zero
        i += 1
        

class Testduplicate_zero(unittest.TestCase):
    #Test Case
    #1st normal case
    def test_normal1(self) :
        inventory1 = [4,0,1,3,0,2,5,0]
        duplicate_zeros(inventory1)
        self.assertEqual(inventory1, [4,0,0,1,3,0,0,2])

    #2nd normal case
    def test_normal2(self):
        inventory2 = [3,2,1]
        duplicate_zeros(inventory2)
        self.assertEqual(inventory2, [3,2,1])
    #duplicate number
    def test_normal3(self):
        inventory3 = [1,1,3,4,4,0,1]
        duplicate_zeros(inventory3)
        self.assertEqual(inventory3,[1,1,3,4,4,0,0])


    #Edge case
    #all zero
    def test_edge1(self):
        inventory4 = [0,0,0,0,0]
        duplicate_zeros(inventory4)
        self.assertEqual(inventory4,[0,0,0,0,0])

    #1 zero
    def test_edge2(self):
        inventory5= [0]
        duplicate_zeros(inventory5)
        self.assertEqual(inventory5,[0])

    #large set 
    def test_edge3(self):
        inventory6 = [101,5,4,3,0,0,46,0,1320,150,94,0,0,5,1,20,65]
        duplicate_zeros(inventory6)
        self.assertEqual(inventory6,[101,5,4,3,0,0,0,0,46,0,0,1320,150,94,0,0,0])

if __name__ == "__main__":
    unittest.main()