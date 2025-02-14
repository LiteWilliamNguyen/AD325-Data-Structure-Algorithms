import unittest

class ListNode:
    def __init__(self,value =0, next = None):
        self.value = value
        self.next = next
def isHealthRecordSymmetric(head:ListNode) -> bool:
    if not head or not head.next:
        return True
        
    #finding the middle
    front, back = head, head
    while back and back.next:
        front = front.next
        back = back.next.next
        
    #reverse the second half
    prev = None
    current = front
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    #compare the half
    first = head
    second = prev
    while second:
        if first.value!= second.value:
            return False
        first = first.next
        second = second.next
    return True
    
#Test Case

class TestHealthRecordSymmetric(unittest.TestCase):
    #Test odd length symmetric list [1,2,3,2,1]
    def test_symmetric_odd(self):
        head = ListNode(1,ListNode(2,ListNode(3,ListNode(2,ListNode(1)))))
        self.assertTrue(isHealthRecordSymmetric(head))

    #Test even length symmetric list [1,2,3,3,2,1]
    def test_symmetric_even(self):
        head = ListNode(1,ListNode(2,ListNode(3,ListNode(3,ListNode(2,ListNode(1))))))
        self.assertTrue(isHealthRecordSymmetric(head))

    #Test non symmetric list [1,2,3,4,5]
    def test_nonsymmetric_list(self):
        head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
        self.assertFalse(isHealthRecordSymmetric(head))

    #Test on single element list
    def test_single_element(self):
        head = ListNode(1)
        self.assertTrue(isHealthRecordSymmetric(head))

    #test on 2 non symmetric list
    def test_two_nonsymmetric(self):
        head = ListNode(1,ListNode(2))
        self.assertFalse(isHealthRecordSymmetric(head))

    #test on empty list
    def test_empty_list(self):
        head = None
        self.assertTrue(isHealthRecordSymmetric(None))

if __name__ == "__main__":
    unittest.main()