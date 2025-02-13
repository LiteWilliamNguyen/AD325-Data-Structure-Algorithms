import unittest

class PatientRecord:
    def __init__(self,ssn,age,full_name):
        self.ssn = ssn
        self.age = age
        self.full_name = full_name
        self.next = None

class PatientRecordMerger:
    def merged_sorted_list(list1, list2):
        list3 = PatientRecord(0,0,"") #default
        current = list3

        while list1 and list2:
            if list1.ssn <= list2.ssn:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        #append the remaining node
        current.next = list1 if list1 else list2
        return list3.next #return the merged list
    

#Test Case
class TestPatientRecordMerger(unittest.TestCase):
    def linked_list_from_list(self,records):
        if not records:
            return None
        head = PatientRecord(*records[0])
        current = head
        for rec in records[1:]:
            current.next = PatientRecord(*rec)
            current = current.next
        return head
    
    def list_from_linked_list(self,head):
        result =[]
        while head:
            result.append((head.ssn,head.age, head.full_name))
            head = head.next
        return result

    #default
    def test_normal_case(self):
        list1 = [(101,20,"Bob"),(103,19,"Mary")]
        list2 = [(102,24,"Caroline"),(104,30,"Jaco")]
        expected = [(101,20,"Bob"),(102,24,"Caroline"),(103,19,"Mary"),(104,30,"Jaco")]
        head1 = self.linked_list_from_list(list1)
        head2 = self.linked_list_from_list(list2)
        list3 = PatientRecordMerger.merged_sorted_list(head1,head2)
        self.assertEqual(self.list_from_linked_list(list3), expected)
        
    #both list are empty
    def test_two_empty_list(self):
        self.assertIsNone(PatientRecordMerger.merged_sorted_list(None,None))

    #list1 is empty
    def test_list1_empty(self):
        list2 = [(201,30,"Audrey")]
        head2 = self.linked_list_from_list(list2)
        list3 = PatientRecordMerger.merged_sorted_list(None,head2)
        expected = [(201,30,"Audrey")]
        self.assertEqual(self.list_from_linked_list(list3),expected)

    #identical SSN in both list
    def test_identical_ssn(self):
        list1 = [(101,20,"Bob"),(103,19,"Mary")]
        list2 = [(101,20,"Bob"),(104,30,"Jaco")]
        expected = [(101,20,"Bob"),(101,20,"Bob"),(103,19,"Mary"),(104,30,"Jaco")]
        head1 = self.linked_list_from_list(list1)
        head2 = self.linked_list_from_list(list2)
        list3 = PatientRecordMerger.merged_sorted_list(head1,head2)
        self.assertEqual(self.list_from_linked_list(list3), expected)

if __name__ == "__main__":
    unittest.main()