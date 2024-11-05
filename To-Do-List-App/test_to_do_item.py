import unittest
import to_do_item

class TestToDoItem(unittest.TestCase):
    def test_initialization(self):
        to_do_tc1 = to_do_item.ToDoItem("Laundry")
        self.assertEqual(to_do_tc1.description, "Laundry")

if __name__ == '__main__':
    unittest.main()