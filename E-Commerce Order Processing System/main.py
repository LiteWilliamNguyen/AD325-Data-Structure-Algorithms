import unittest

class Order :
    def __init__(self, order_id,customer_id,order_detail):
        self.order_id = order_id
        self.customer_id = customer_id
        self.order_detail = order_detail
        self.next = None
    
    def __repr__(self):
        return f"Order({self.order_id},{self.customer_id},{self.order_detail})"
    
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self,order):
        if not self.head:
            self.head = order
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = order

    def display(self):
        current = self.head
        while current:
            print(current)
            current = current.next

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

#Unit Test
class TestSinglyLinkedList(unittest.TestCase):
    def setUp(self):
        self.orders = SinglyLinkedList()
        self.orders.append(Order(1,"Bob", "Laptop"))
        self.orders.append(Order(2,"Michelle", "Iphone"))
        self.orders.append(Order(3,"Mary", "Keyboard"))

    #append and display
    def test_append_and_display(self):
        expected = [(1,"Bob", "Laptop"),(2,"Michelle", "Iphone"),(3,"Mary", "Keyboard")]
        current = self.orders.head
        result = []
        while current:
            result.append((current.order_id, current.customer_id, current.order_detail))
            current = current.next
        self.assertEqual(result,expected)

    #reverse
    def test_reverse(self):
        self.orders.reverse()
        expected = [(3,"Mary"),(2,"Michelle"),(1,"Bob")]
        result = []
        current = self.orders.head
        while current:
            result.append((current.order_id, current.customer_id))
            current = current.next
        self.assertEqual(result,expected)

    #Reverse an empty list
    def test_reverse_empty_list(self):
        empty_list =  SinglyLinkedList()
        empty_list.reverse()
        self.assertIsNone(empty_list.head)

    #reverse a single element
    def test_reverse_single_order(self):
        single_order = SinglyLinkedList()
        single_order.append(Order(4,"Khanh","Desktop"))
        single_order.reverse()
        self.assertEqual(single_order.head.order_id,4)
        self.assertEqual(single_order.head.customer_id,"Khanh")

    #reverse 2 element
    def test_reverse_two_order(self):
        two_order = SinglyLinkedList()
        two_order.append(Order(1,"Bob", "Laptop"))
        two_order.append(Order(2,"Michelle", "Iphone"))
        two_order.reverse()
        self.assertEqual(two_order.head.order_id,2)
        self.assertEqual(two_order.head.next.order_id,1)


if __name__ == "__main__":
    unittest.main()