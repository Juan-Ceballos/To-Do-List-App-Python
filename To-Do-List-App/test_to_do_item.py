import unittest
import to_do_item

class TestToDoItem(unittest.TestCase):
    def test_initialization(self):
        to_do_tc1 = to_do_item.ToDoItem("Laundry", "3 loads", "9/23/2024", "1")
        self.assertEqual(to_do_tc1.title, "Laundry")

if __name__ == '__main__':
    unittest.main()