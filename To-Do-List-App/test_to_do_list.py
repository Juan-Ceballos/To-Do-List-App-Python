import unittest
from datetime import datetime

import to_do_list
import to_do_item

class TestToDoList(unittest.TestCase):

    def test_initialize(self):
        to_do_list_tc = to_do_list.ToDoList({}, "Work")
        self.assertEqual(len(to_do_list_tc.to_do_items), 0)

    def test_add_item(self):
        to_do_list_tc = to_do_list.ToDoList({}, "Gym")
        to_do_sample = to_do_item.ToDoItem("Pushups")
        to_do_list_tc.add_to_do(to_do_sample, to_do_sample.to_do_id)
        self.assertEqual(len(to_do_list_tc.to_do_items), 1)

    def test_delete_item(self):
        to_do_list_tc = to_do_list.ToDoList({}, "School")
        to_do_sample = to_do_item.ToDoItem("Math")

if __name__ == '__main__':
    unittest.main()
