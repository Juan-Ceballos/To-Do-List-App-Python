import unittest
import to_do_list
import to_do_item

class TestToDoList(unittest.TestCase):

    def test_initialize(self):
        to_do_list_tc1 = to_do_list.ToDoList()
        self.assertEqual(len(to_do_list_tc1.to_do_items), 0)

    def test_add_item(self):
        to_do_list_tc2 = to_do_list.ToDoList()
        to_do_sample = to_do_item.ToDoItem("Code", "Testing", "10/15/2024", "2")
        to_do_list_tc2.add_to_do(to_do_sample)
        self.assertEqual(len(to_do_list_tc2.to_do_items), 1)

if __name__ == '__main__':
    unittest.main()
