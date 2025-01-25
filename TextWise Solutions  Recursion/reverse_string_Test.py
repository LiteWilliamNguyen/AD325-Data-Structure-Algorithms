import unittest
from main import reverse_string

class reverse_string_Test(unittest.TestCase):
#Will the code work with number in it?
#Will the code work with special case
#with nothing in it
#Does it matter if it is a sentence or a word
    #normal case and edge case
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"),"olleh")

    def test_reverse_string_with_sentence(self):
        self.assertEqual(reverse_string("hello world"),"dlrow olleh")

    def test_reverse_string_with_number(self):
        self.assertEqual(reverse_string("Hello 12345"),"54321 olleH")

    def test_reverse_string_with_special_letter(self):
        self.assertEqual(reverse_string("add!@#"),"#@!dda")

    def test_reverse_string_with_different_case(self):
        self.assertEqual(reverse_string("Hello"),"olleH")

    def test_reverse_string_with_null(self):
        self.assertEqual(reverse_string(""),"")


if __name__ == "__main__":
    unittest.main()