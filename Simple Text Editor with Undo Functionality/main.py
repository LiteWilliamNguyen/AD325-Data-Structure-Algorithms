import unittest

class TextOperation:
    def __init__(self,operation,char = None):
        self.operation = operation
        self.char = char

class TextEditor:
    def __init__(self):
        self.text = []
        self.stack = [] #stack to store operation

    # Add Text
    def add_text(self,char):
        self.text.append(char)
        self.stack.append(TextOperation("add", char))
        self.display()

    # Delete Text
    def delete_text(self):
        if self.text:
            char = self.text.pop()
            self.stack.append(TextOperation("delete",char))
        self.display()


    # Undo operation
    def undo_operation(self):
        if self.stack:
            last_operation = self.stack.pop()
            if last_operation.operation == "add":
                self.text.pop() # reverse and remove added character
            elif last_operation.operation == "delete":
                self.text.append(last_operation.char)
        self.display()


    # Disply
    def display(self):
        print("Current Text: " + "".join(self.text))

        
class TestTextEditor(unittest.TestCase):
    def setUp(self):
        self.editor = TextEditor()

    #normal
    #adding character
    def test_add_text(self):
        self.editor.add_text('H')
        self.editor.add_text('i')
        self.assertEqual("".join(self.editor.text), "Hi")
        

    #delete character
    def test_delete_text(self):
        self.editor.add_text("H")
        self.editor.add_text("e")
        self.editor.add_text("l")
        self.editor.add_text("l")
        self.editor.add_text("o")
        self.editor.delete_text()
        self.editor.delete_text()
        self.assertEqual("".join(self.editor.text), "Hel")

    #undoing operation add
    def test_undo_operation_add(self):
        self.editor.add_text("H")
        self.editor.add_text("i")
        self.editor.undo_operation()
        self.assertEqual("".join(self.editor.text),"H")

    #undoing operation delete
    def test_undo_operation_delete(self):
        self.editor.add_text("H")
        self.editor.delete_text()
        self.editor.undo_operation()
        self.assertEqual("".join(self.editor.text), "H")

    #deleting an empty array
    def test_delete_empty(self):
        self.editor.delete_text()
        self.assertEqual("".join(self.editor.text),"")

    #multiple undo 
    def test_mulitple_undo(self):
        self.editor.add_text("H")
        self.editor.add_text("e")
        self.editor.add_text("l")
        self.editor.add_text("l")
        self.editor.add_text("o")
        self.editor.delete_text()
        self.editor.undo_operation()
        self.editor.undo_operation()
        self.editor.undo_operation()
        self.assertEqual("".join(self.editor.text),"Hel")

if __name__ == "__main__":
    unittest.main()



