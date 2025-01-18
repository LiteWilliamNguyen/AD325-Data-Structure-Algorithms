import unittest


#customerData1,m
#customerData2,n
#final: customerData1, m+n



def merge_customer_data(customerData1,m,customerData2,n):
    #index
    i = m - 1 # reading last element in customerData1
    j = n - 1 # reading last element in customerData2
    k = m + n - 1 # reading the last element in final customerData1 
    

    while i >= 0 and j >= 0:
        if customerData1[i] > customerData2[j]:
            customerData1[k] = customerData1[i]
            i -= 1

        else: 
            customerData1[k] = customerData2[j]
            j -= 1
        k -= 1


    #copy the remaining element from customerData2 if there is any left
    while j >= 0:
        customerData1[k] = customerData2[j]
        j -= 1
        k -= 1



class TestMergeCustomerData(unittest.TestCase):
    def test_normal(self):
        customerData1 = [101,104,107,0,0,0]
        customerData2 = [102,105,108]
        m = 3
        n = 3
        merge_customer_data(customerData1,m,customerData2,n)
        self.assertEqual(customerData1,[101,102,104,105,107,108])

    def test_edge_case_empty_second_array(self):
        customerData1 = [103]
        m = 1
        customerData2 = []
        n = 0
        merge_customer_data(customerData1, m, customerData2, n)
        self.assertEqual(customerData1, [103])

    def test_edge_case_empty_first_array(self):
        customerData1 = [0]
        m = 0
        customerData2 = [101]
        n = 1
        merge_customer_data(customerData1,m,customerData2,n)
        self.assertEqual(customerData1, [101])

    def test_edge_case_empty_arrays(self):
        customerData1 = []
        m = 0
        customerData2 = []
        n = 0
        merge_customer_data(customerData1,m,customerData2,n)
        self.assertEqual(customerData1, [])

    def test_same_number_array(self):
        customerData1 = [101,102,0,0]
        m = 2
        customerData2 = [101,102]
        n = 2
        merge_customer_data(customerData1,m,customerData2,n)
        self.assertEqual(customerData1, [101,101,102,102])

    
#Time Complexity: O(m+n), customerData1 and customerData1 processed at once
#Space complexity: O(1)
    


if __name__ == "__main__":
    unittest.main()